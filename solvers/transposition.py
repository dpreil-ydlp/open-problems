#!/usr/bin/env python3
"""Columnar and double-columnar transposition search plus alternating combo."""
import argparse, itertools, math, random, time
from pathlib import Path
from cipherkit import *
def decrypt_once(text,order):
 n=len(text);w=len(order);q,r=divmod(n,w);lens=[q+(i<r) for i in range(w)];cols=['']*w;pos=0
 for c in order:cols[c]=text[pos:pos+lens[c]];pos+=lens[c]
 return ''.join(cols[c][row] for row in range(q+1) for c in range(w) if row<len(cols[c]))
def decrypt(text,keys):
 for k in keys: text=decrypt_once(text,k)
 return text

def solve(text,lang='en',max_len=20,restarts=3,iters=1400,double=False,seed=53,post_key=None):
 clean=''.join(c for c in text.upper() if 'A'<=c<='Z');table=load_table(lang);rng=random.Random(seed);start=time.perf_counter();best=(-math.inf,None,None)
 def evaluate(stage):
  if post_key is None:return stage
  import subst
  return subst.decrypt(stage,[ord(c)-65 for c in post_key])
 lengths=range(2,min(max_len,len(clean))+1)
 pairs=[(n,None) for n in lengths] if not double else [(a,b) for a in lengths for b in lengths]
 for nkey,nsecond in pairs:
  if not double and nkey<=8:
   for key in itertools.permutations(range(nkey)):
    stage=decrypt_once(clean,key);p=evaluate(stage);s=score(p,table)
    if s>best[0]:best=(s,[list(key)],p)
   continue
  pair_restarts=max(1,restarts//2) if double else restarts
  pair_iters=max(100,iters//3) if double else iters
  for _ in range(pair_restarts):
   key=list(range(nkey));rng.shuffle(key)
   if double:
    k2=list(range(nsecond));rng.shuffle(k2);keys=[key,k2]
   else:keys=[key]
   stage=decrypt(clean,keys);p=evaluate(stage);local=(score(p,table),[k[:] for k in keys],p)
   for i in range(pair_iters):
    temp=max(1.0,180*(1-i/max(1,pair_iters))); cand=[k[:] for k in local[1]];k=cand[rng.randrange(len(cand))];x,y=rng.sample(range(len(k)),2);k[x],k[y]=k[y],k[x];plain=evaluate(decrypt(clean,cand));s=score(plain,table)
    if s>local[0] or rng.random()<math.exp(max(-60,(s-local[0])/temp)):local=(s,cand,plain)
    if local[0]>best[0]:best=(local[0],[k[:] for k in local[1]],local[2])
 return {'score':best[0],'key':best[1],'plaintext':best[2],'runtime_seconds':time.perf_counter()-start,'mode':'double-columnar' if double else 'columnar','post_key':post_key}
def combined(text,lang='en',max_len=12,restarts=4,iters=2500,seed=53):
 # Alternate a transposition search and monoalphabetic substitution search on the current order.
 import subst
 first=solve(text,lang,max_len,restarts,iters,False,seed)
 sub=subst.solve(first['plaintext'],lang,restarts=max(4,restarts),iters=iters)
 trans=solve(text,lang,max_len,restarts,iters,False,seed+1,post_key=sub['key'])
 return {'score':trans['score'],'key':{'transposition':trans['key'],'substitution':sub['key']},'plaintext':trans['plaintext'],'runtime_seconds':first['runtime_seconds']+sub['runtime_seconds']+trans['runtime_seconds'],'mode':'combined-substitution-transposition'}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('ciphertext',type=Path);p.add_argument('--lang',choices=LANGS,default='en');p.add_argument('--max-len',type=int,default=20);p.add_argument('--restarts',type=int,default=3);p.add_argument('--iters',type=int,default=1400);p.add_argument('--double',action='store_true');p.add_argument('--combined',action='store_true');p.add_argument('--output',type=Path);a=p.parse_args();r=combined(read_cipher(a.ciphertext),a.lang,a.max_len,a.restarts,a.iters) if a.combined else solve(read_cipher(a.ciphertext),a.lang,a.max_len,a.restarts,a.iters,a.double);print(r['plaintext']);print(f"score={r['score']:.2f} mode={r['mode']} key={r['key']} runtime={r['runtime_seconds']:.2f}s");
 if a.output:json_result(a.output,r)
if __name__=='__main__':main()
