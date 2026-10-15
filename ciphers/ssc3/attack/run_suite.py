#!/usr/bin/env python3
"""Run the requested attack and bounded significance suite under one wall clock."""
import argparse, collections, json, random, time
from pathlib import Path
import numpy as np
import attack

ROOT=attack.ROOT

def synthetic_v1(seq, syms, profile, corpus, alphabet, seed):
    r=random.Random(seed); n=len(seq); m=len(syms)
    # Sample a corpus excerpt, then retain its order while changing the fewest
    # letters needed to match the exact target symbol-frequency profile.
    start=r.randrange(len(corpus)-n)
    plain=list(corpus[start:start+n])
    counts=collections.Counter(plain)
    # Generate a full 3-5 homophone table, then retain 55 randomly selected
    # entries as the observed symbols, matching the real ciphertext's exact counts.
    owners_full=[]
    for l in alphabet: owners_full.extend([l]*r.randint(3,5))
    r.shuffle(owners_full)
    selected=r.sample(range(len(owners_full)),m)
    owners={s:owners_full[selected[s]] for s in range(m)}
    loads=collections.Counter(owners.values()); masses=collections.Counter()
    for s,l in owners.items(): masses[l]+=profile[syms[s]]
    target=collections.Counter({letter:counts[letter] for letter in alphabet})
    # Condition the sampled excerpt on the letter totals implied by the key and profile.
    over={l:counts[l]-masses[l] for l in alphabet}; under={l:masses[l]-counts[l] for l in alphabet}
    for pos,l in enumerate(plain):
        if over[l]>0:
            choices=[x for x in alphabet if under[x]>0]
            if choices:
                x=max(choices,key=lambda z:under[z]); plain[pos]=x; over[l]-=1; under[x]-=1
    # Shuffle the exact symbol quotas within each letter over occurrences of that letter.
    stream=np.empty(n,dtype=np.int16)
    by_letter={l:[] for l in alphabet}
    for s,l in owners.items(): by_letter[l].extend([s]*profile[syms[s]])
    positions={l:[i for i,x in enumerate(plain) if x==l] for l in alphabet}
    for l in alphabet:
        r.shuffle(by_letter[l]); r.shuffle(positions[l])
        for i,s in zip(positions[l],by_letter[l]): stream[i]=s
    true_key={s:alphabet.index(l) for s,l in owners.items()}
    true_plain=''.join(alphabet[x] for x in [true_key[int(s)] for s in stream])
    return stream,true_key,true_plain,''.join(plain)

def synthetic(seq, syms, profile, corpus, alphabet, seed):
    """Create an exact-profile control while preserving a sampled corpus excerpt."""
    r=random.Random(seed); n=len(seq); m=len(syms)
    start=r.randrange(len(corpus)-n)
    source=list(corpus[start:start+n])
    source_counts=collections.Counter(source)
    owners={}; loads=collections.Counter(); masses=collections.Counter()
    # Assign high-frequency symbols first to the letter with the largest remaining
    # quota. The profile items sum to the excerpt length, so this often matches the
    # excerpt exactly and otherwise needs only a few substitutions.
    order=sorted(range(m),key=lambda s:(-profile[syms[s]],r.random()))
    for s in order:
        available=[letter for letter in alphabet if loads[letter]<5]
        letter=max(available,key=lambda x:(source_counts[x]-masses[x],-loads[x],r.random()))
        owners[s]=letter; loads[letter]+=1; masses[letter]+=profile[syms[s]]
    plain=source[:]
    over={letter:source_counts[letter]-masses[letter] for letter in alphabet}
    under={letter:masses[letter]-source_counts[letter] for letter in alphabet}
    for pos,letter in enumerate(plain):
        if over[letter]>0:
            choices=[x for x in alphabet if under[x]>0]
            if choices:
                replacement=max(choices,key=lambda x:under[x])
                plain[pos]=replacement; over[letter]-=1; under[replacement]-=1
    changed=sum(a!=b for a,b in zip(source,plain))
    if any(x>0 for x in over.values()) or any(x>0 for x in under.values()):
        raise ValueError('Could not balance the exact symbol profile to the excerpt letter counts')
    if changed>max(2,n//50):
        raise ValueError(f'Synthetic conditioning changed {changed}/{n} letters; reject this excerpt')
    # Complete a latent 3-5 symbol table for every letter. The 55 observed
    # symbols occupy a subset of these entries.
    full_counts={letter:max(3,loads[letter]) for letter in alphabet}
    left=99-sum(full_counts.values())
    if left<0:
        raise ValueError('Observed assignment cannot fit a 99-entry, 3-5 homophone table')
    eligible=[l for l in alphabet if full_counts[l]<5]
    while left:
        if not eligible: raise ValueError('Could not fill synthetic 99-entry homophone table')
        l=r.choice(eligible); full_counts[l]+=1; left-=1
        if full_counts[l]==5: eligible.remove(l)
    stream=np.empty(n,dtype=np.int16)
    by_letter={l:[] for l in alphabet}
    for s,l in owners.items(): by_letter[l].extend([s]*profile[syms[s]])
    positions={l:[i for i,x in enumerate(plain) if x==l] for l in alphabet}
    for l in alphabet:
        r.shuffle(by_letter[l]); r.shuffle(positions[l])
        if len(by_letter[l])!=len(positions[l]):
            raise ValueError('Internal quota mismatch in synthetic ciphertext')
        for pos,s in zip(positions[l],by_letter[l]): stream[pos]=s
    true_key={s:alphabet.index(l) for s,l in owners.items()}
    true_plain=''.join(alphabet[true_key[int(s)]] for s in stream)
    return stream,true_key,true_plain,''.join(plain),''.join(source),changed

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--cipher',type=Path,default=attack.DEFAULT_CIPHER)
    p.add_argument('--budget-seconds',type=int,default=7200)
    p.add_argument('--restarts',type=int,default=300)
    p.add_argument('--iterations',type=int,default=200000)
    p.add_argument('--seed',type=int,default=42)
    p.add_argument('--controls-only',action='store_true')
    a=p.parse_args(); deadline=time.monotonic()+a.budget_seconds
    seq,syms,profile=attack.parse_cipher(a.cipher)
    out=ROOT/'attack/results'; out.mkdir(parents=True,exist_ok=True)
    summary={'budget_seconds':a.budget_seconds,'requested_restarts':a.restarts,'requested_iterations_per_restart':a.iterations,'seed':a.seed,'runs':[]}
    for lang,alphabet in ([] if a.controls_only else [('es',attack.ALPH),('eu',attack.ALPH_EU)]):
        if time.monotonic()>=deadline: break
        corpus,words,files=attack.load_corpus(lang,alphabet); _,_,score=attack.make_lm(corpus,alphabet)
        start=time.monotonic()
        top,stats=attack.anneal(seq,syms,alphabet,score,a.restarts,a.iterations,a.seed+(0 if lang=='es' else 1000),20,deadline)
        for row in top: row['word_coverage']=attack.segment_coverage(row['plaintext'],words) if lang=='es' else None
        result={'language':lang,'alphabet':alphabet,'corpus_files':files,'corpus_letters':len(corpus),'wordlist_size':len(words),'runtime_seconds':round(time.monotonic()-start,3),'stats':stats,'top':top}
        (out/f'{lang}-main.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
        summary['runs'].append({'kind':'main','language':lang,'best_score':top[0]['score'] if top else None,**stats,'runtime_seconds':result['runtime_seconds']})
    # Spanish significance runs, alternating classes so both score distributions
    # receive comparable coverage within a finite wall-clock budget.
    if time.monotonic()<deadline:
        corpus,words,_=attack.load_corpus('es',attack.ALPH); _,_,score=attack.make_lm(corpus,attack.ALPH)
        rng=random.Random(a.seed+5000); synth=[]; shuffles=[]
        for i in range(30):
            if time.monotonic()>=deadline: break
            sseq,key,truth,excerpt,source,changed=synthetic(seq,syms,profile,corpus,attack.ALPH,rng.randrange(2**31))
            top,stats=attack.anneal(sseq,syms,attack.ALPH,score,a.restarts,a.iterations,a.seed+10000+i,1,deadline)
            got=top[0] if top else None
            correct=sum(got['key'].get(s)==attack.ALPH[key[j]] for j,s in enumerate(syms))/len(syms) if got else None
            row={'case':i,'generator_version':2,'best_score':got['score'] if got else None,'key_letter_accuracy':correct,'plaintext':got['plaintext'] if got else None,'true_plaintext':truth,'corpus_excerpt_original':source,'corpus_excerpt_adjusted':excerpt,'excerpt_character_changes':changed,'stats':stats}
            synth.append(row); (out/f'synthetic-{i:02d}.json').write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n')
            if time.monotonic()>=deadline: break
            i=len(shuffles)
            shuffled=np.array(seq,copy=True); rng.shuffle(shuffled)
            top,stats=attack.anneal(shuffled,syms,attack.ALPH,score,a.restarts,a.iterations,a.seed+20000+i,1,deadline)
            row={'case':i,'best_score':top[0]['score'] if top else None,'plaintext':top[0]['plaintext'] if top else None,'stats':stats}
            shuffles.append(row); (out/f'shuffled-{i:02d}.json').write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n')
        real=json.loads((out/'es-main.json').read_text()) if (out/'es-main.json').exists() else None
        summary.update({'synthetic':synth,'shuffled':shuffles,'real_best_score':real['top'][0]['score'] if real and real['top'] else None})
        (out/'significance.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    (out/'run-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'output':str(out),'elapsed_seconds':a.budget_seconds-(max(0,deadline-time.monotonic())),'main_runs':summary['runs'],'synthetic_completed':len(summary.get('synthetic',[])),'shuffled_completed':len(summary.get('shuffled',[]))},ensure_ascii=False))

if __name__=='__main__': main()
