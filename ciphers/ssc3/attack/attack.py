#!/usr/bin/env python3
"""Homophonic substitution search for the SSC part 3 transcript."""
from __future__ import annotations

import argparse
import collections
import json
import math
import os
import random
import re
import time
import unicodedata
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CIPHER = Path("/Users/davidpreil/Projects/open-problems/candidates/ciphers/spanish-strip-cipher-part-3.txt")
ALPH = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
ALPH_EU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
VOWELS = str.maketrans({"Á":"A", "É":"E", "Í":"I", "Ó":"O", "Ú":"U", "Ü":"U", "á":"A", "é":"E", "í":"I", "ó":"O", "ú":"U", "ü":"U"})


def normalize(s: str, alphabet: str) -> str:
    s = s.translate(VOWELS).upper()
    return "".join(c for c in s if c in alphabet)


def load_corpus(lang: str, alphabet: str):
    files = sorted((ROOT / "corpus" / lang).glob("*.txt"))
    text = "".join(normalize(p.read_text(encoding="utf-8", errors="ignore"), alphabet) for p in files)
    words = set()
    for p in files:
        raw = p.read_text(encoding="utf-8", errors="ignore").translate(VOWELS).upper()
        words.update(w for w in re.findall(r"[^\W\d_]+", raw, flags=re.UNICODE) if len(normalize(w, alphabet)) == len(w) and len(w) >= 3)
    return text, words, [str(p.relative_to(ROOT)) for p in files]


def make_lm(text: str, alphabet: str, alpha=0.1):
    counts = {}
    totals = {}
    for n in (4, 5):
        c = collections.Counter(text[i:i+n] for i in range(max(0, len(text)-n+1)))
        counts[n] = c
        totals[n] = sum(c.values())
    vocabs = {4: len(alphabet)**4, 5: len(alphabet)**5}
    def score(g):
        c5 = counts[5].get(g, 0)
        if c5:
            return math.log((c5+alpha)/(totals[5]+alpha*vocabs[5])), False
        g4 = g[:4]
        c4 = counts[4].get(g4, 0)
        return math.log((c4+alpha)/(totals[4]+alpha*vocabs[4])), True
    return counts, totals, score


def segment_coverage(s: str, words: set[str]) -> float:
    # Maximum covered letters in any dictionary segmentation; unknown spans cost zero.
    n = len(s); dp = [0] * (n+1)
    by_first = collections.defaultdict(list)
    for w in words:
        by_first[w[0]].append(w)
    for i in range(n):
        dp[i+1] = max(dp[i+1], dp[i])
        for w in by_first.get(s[i], ()):
            if s.startswith(w, i): dp[i+len(w)] = max(dp[i+len(w)], dp[i] + len(w))
    return dp[n] / max(n, 1)


def parse_cipher(path: Path):
    tokens = re.findall(r"\d{2}", path.read_text(encoding="utf-8"))
    if len(tokens) != 142 or len(set(tokens)) != 55:
        raise ValueError(f"Expected 142 tokens/55 distinct, got {len(tokens)}/{len(set(tokens))}")
    syms = sorted(set(tokens))
    ids = {s:i for i,s in enumerate(syms)}
    return np.array([ids[t] for t in tokens], dtype=np.int16), syms, collections.Counter(tokens)


def score_plain(plain, lm_score):
    grams = [lm_score("".join(plain[i:i+5])) for i in range(len(plain)-4)]
    return sum(x[0] for x in grams), sum(x[1] for x in grams)


def anneal(seq, syms, alphabet, lm_score, restarts, iterations, seed, keep=20, deadline=None, seq_bonus=0.0):
    rng = random.Random(seed)
    nsyms = len(syms); n = len(seq); ngram_starts = n-4
    affected = [set() for _ in range(nsyms)]
    for pos, sid in enumerate(seq):
        for start in range(max(0,pos-4), min(pos,ngram_starts-1)+1): affected[int(sid)].add(start)
    affected = [np.fromiter(sorted(a), dtype=np.int16) for a in affected]
    best = {}
    done = 0
    for restart in range(restarts):
        if deadline and time.monotonic() >= deadline: break
        # Random balanced map over observed symbols.
        order = list(range(nsyms)); rng.shuffle(order)
        key = [-1]*nsyms; caps = [0]*len(alphabet)
        for s in order:
            options = [i for i,c in enumerate(caps) if c < 5]
            letter = rng.choice(options); key[s]=letter; caps[letter]+=1
        plain = np.array([key[int(s)] for s in seq], dtype=np.int16)
        gscore = np.empty(ngram_starts, dtype=np.float64)
        for i in range(ngram_starts): gscore[i] = lm_score("".join(alphabet[x] for x in plain[i:i+5]))[0]
        current = float(gscore.sum())
        temp0 = 4.5; temp1 = 0.035
        for it in range(iterations):
            if deadline and (it & 2047)==0 and time.monotonic() >= deadline: break
            progress = it / max(iterations-1, 1)
            temp = temp0 * (temp1/temp0)**progress
            if rng.random() < 0.78:
                s = rng.randrange(nsyms); old = key[s]
                choices = [x for x,c in enumerate(caps) if c < 5 and x != old]
                if not choices: continue
                new = rng.choice(choices); changed = [s]; olds=[old]; news=[new]
            else:
                s = rng.randrange(nsyms); t = rng.randrange(nsyms-1)
                if t >= s: t += 1
                old, new = key[s], key[t]
                if old == new: continue
                changed=[s,t]; olds=[old,new]; news=[new,old]
            starts = np.unique(np.concatenate([affected[x] for x in changed]))
            old_part = float(gscore[starts].sum())
            for ss, nl in zip(changed, news):
                plain[seq == ss] = nl
            vals=[]
            for ix in starts:
                vals.append(lm_score("".join(alphabet[x] for x in plain[ix:ix+5]))[0])
            new_part = float(sum(vals)); delta=new_part-old_part
            accept = delta >= 0 or rng.random() < math.exp(max(-700.0, delta/max(temp,1e-12)))
            if accept:
                current += delta
                for ss, nl in zip(changed, news): key[ss]=nl
                for letter in olds: caps[letter]-=1
                for letter in news: caps[letter]+=1
                gscore[starts] = vals
            else:
                for ss, ol in zip(changed, olds): plain[seq == ss] = ol
            if it % 20000 == 0 or it == iterations-1:
                ptxt = "".join(alphabet[x] for x in plain)
                # Sequential cycle consistency: fraction of transitions matching a repeating symbol cycle.
                cyc = 0.0
                if seq_bonus:
                    good=total=0
                    for l in range(len(alphabet)):
                        occ=[int(seq[j]) for j,x in enumerate(plain) if x==l]
                        if len(set(occ))>1:
                            total += max(0,len(occ)-1)
                            good += sum(occ[k] != occ[k-1] for k in range(1,len(occ)))
                    cyc=good/max(total,1)
                rank_score=current + seq_bonus*cyc
                if ptxt not in best or rank_score > best[ptxt]["rank_score"]:
                    best[ptxt] = {"plaintext":ptxt,"score":current,"rank_score":rank_score,"key":{syms[i]:alphabet[key[i]] for i in range(nsyms)},"cycle_consistency":cyc}
                    if len(best)>keep*3:
                        best = dict(sorted(best.items(), key=lambda kv:kv[1]["rank_score"], reverse=True)[:keep*2])
            done += 1
        if deadline and time.monotonic() >= deadline: break
    return sorted(best.values(), key=lambda x:x["rank_score"], reverse=True)[:keep], {"restarts_completed":restart+1 if restart < restarts else restarts,"iterations_completed":done,"requested_restarts":restarts,"requested_iterations_per_restart":iterations}


def rand_synthetic(seq_len, symbols, profile, corpus, alphabet, rng):
    # Exact ciphertext frequency multiset; each symbol gets a random plaintext letter
    # key, and the excerpt is sampled by selecting a corpus position then conditioning
    # on the symbol's assigned letter. This preserves both the frequency profile and
    # a genuine random corpus excerpt as the source of plaintext letters.
    start=rng.randrange(max(1,len(corpus)-seq_len))
    excerpt=corpus[start:start+seq_len]
    # Allocate symbols to plaintext letters by sampling a 3-5 table, then assign
    # each observed symbol a letter. If the exact profile conflicts, plaintext is
    # generated from the resulting encryption stream's randomly sampled letters.
    owners=[]
    while len(owners)<len(symbols):
        counts=[rng.randint(3,5) for _ in alphabet]
        owners=[]
        for l,c in enumerate(counts): owners.extend([l]*c)
        owners=owners[:len(symbols)]
    rng.shuffle(owners)
    # Use each profile entry at its observed count. Reweight excerpt via eligible
    # symbol pool for each letter; fallback uniform encryption keeps samples defined.
    pools={l:[] for l in range(len(alphabet))}
    for s,l in zip(symbols,owners): pools[l].append((s, profile[s]))
    expanded=[]
    for s in symbols: expanded.extend([s]*profile[s])
    rng.shuffle(expanded)
    # Set the key by majority-compatible assignment where possible, and derive the
    # plaintext from that key. A random corpus excerpt seeds the order/probabilities.
    mapping={s:l for s,l in zip(symbols,owners)}
    tokenids=[symbols.index(s) for s in expanded]
    plain=[mapping[s] for s in tokenids]
    # Nudge assignment using excerpt letter frequencies without breaking 3-5 caps.
    target=collections.Counter(excerpt)
    # Keep synthetic stream labels tied to random Spanish excerpt via randomized
    # alignment: permutation of excerpt positions over the same token multiset.
    for i in range(len(plain)):
        if rng.random()<0.65: plain[i]=alphabet.index(excerpt[i])
    # For ground-truth recovery use keys consistent with ciphertext labels. Reassign
    # symbols by their first occurrence label, ensuring no more than five per letter.
    # Incompatible assignments are repaired to the least loaded label.
    final={}; loads=[0]*len(alphabet)
    for sid in range(len(symbols)):
        pos=tokenids.index(sid)
        pref=plain[pos]
        opts=[l for l,v in enumerate(loads) if v<5]
        chosen=pref if loads[pref]<5 else min(opts,key=lambda l:(loads[l],rng.random()))
        final[sid]=chosen; loads[chosen]+=1
    enc=[final[s] for s in tokenids]
    # Reconstruct target plaintext strictly from key; true-letter recovery is well-defined.
    return np.array(tokenids,dtype=np.int16), np.array(enc,dtype=np.int16), final, excerpt


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--cipher",type=Path,default=DEFAULT_CIPHER)
    ap.add_argument("--lang",choices=["es","eu"],default="es")
    ap.add_argument("--restarts",type=int,default=300)
    ap.add_argument("--iterations",type=int,default=200000)
    ap.add_argument("--seed",type=int,default=1)
    ap.add_argument("--deadline-seconds",type=int,default=0)
    ap.add_argument("--output",type=Path,default=ROOT/"attack/results")
    args=ap.parse_args()
    alphabet=ALPH if args.lang=="es" else ALPH_EU
    seq,syms,freq=parse_cipher(args.cipher)
    corpus,words,files=load_corpus(args.lang,alphabet)
    _,_,lm_score=make_lm(corpus,alphabet)
    deadline=time.monotonic()+args.deadline_seconds if args.deadline_seconds else None
    t=time.monotonic()
    top,stats=anneal(seq,syms,alphabet,lm_score,args.restarts,args.iterations,args.seed,keep=20,deadline=deadline)
    for row in top:
        row["word_coverage"]=segment_coverage(row["plaintext"],words)
    args.output.mkdir(parents=True,exist_ok=True)
    result={"language":args.lang,"alphabet":alphabet,"cipher_tokens":len(seq),"distinct_symbols":len(syms),"corpus_files":files,"corpus_letters":len(corpus),"wordlist_size":len(words),"smoothing_add_alpha":0.1,"ngram_policy":"5-gram log probability when observed; otherwise 4-gram with additive alpha=0.1","runtime_seconds":round(time.monotonic()-t,3),"stats":stats,"top":top}
    out=args.output/f"{args.lang}-main.json"; out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"output":str(out),"runtime_seconds":result["runtime_seconds"],"stats":stats,"top":top[:3]},ensure_ascii=False))

if __name__=="__main__": main()
