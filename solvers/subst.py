#!/usr/bin/env python3
"""Simulated annealing solver for monoalphabetic substitution."""
import argparse, random
from pathlib import Path
from cipherkit import *
def decrypt(text,key): return ''.join(ALPHABET[key[ord(c)-65]] if c in ALPHABET else c for c in text.upper())
def solve(text,lang='en',restarts=12,iters=18000,fix=None,seed=17):
 table=load_table(lang); fixed={}
 for pair in (fix or []):
  c,p=pair.upper().split(':'); fixed[ord(c)-65]=ord(p)-65
 if len(set(fixed.values()))!=len(fixed): raise ValueError('fixed plaintext letters must be unique')
 free_c=[i for i in range(26) if i not in fixed]; free_p=[i for i in range(26) if i not in fixed.values()]
 rng=random.Random(seed); best=(-1e99,None,None); start=time.perf_counter()
 counts={i:text.upper().count(ALPHABET[i]) for i in range(26)}
 ranked_c=sorted(free_c,key=lambda i:counts[i],reverse=True)
 ranked_p=sorted(free_p,key=lambda i:FREQ[lang][i],reverse=True)
 for run in range(restarts):
  rhs=free_p[:]
  if run==0:
   for c,p in zip(ranked_c,ranked_p):rhs[free_c.index(c)]=p
  else:rng.shuffle(rhs)
  key=list(range(26))
  for i,v in fixed.items():key[i]=v
  for i,v in zip(free_c,rhs):key[i]=v
  plain=decrypt(text,key); cur=score(plain,table); local=(cur,key[:],plain)
  for step in range(iters):
   if len(free_c)<2:break
   temp=max(1.5,100*(1-step/max(1,iters))); x,y=rng.sample(free_c,2); k=local[1][:];k[x],k[y]=k[y],k[x]
   p=decrypt(text,k);s=score(p,table)
   import math
   if s>local[0] or rng.random()<math.exp(max(-60,(s-local[0])/temp)):local=(s,k,p)
   if local[0]>best[0]:best=(local[0],local[1][:],local[2])
 return {'score':best[0],'key':''.join(ALPHABET[x] for x in best[1]),'plaintext':best[2],'runtime_seconds':time.perf_counter()-start}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('ciphertext',type=Path);p.add_argument('--lang',choices=LANGS,default='en');p.add_argument('--restarts',type=int,default=12);p.add_argument('--iters',type=int,default=18000);p.add_argument('--fix',action='append',default=[],metavar='C:P',help='known cipher:plain mapping; repeat for more');p.add_argument('--output',type=Path);a=p.parse_args();r=solve(read_cipher(a.ciphertext),a.lang,a.restarts,a.iters,a.fix);print(r['plaintext']);print(f"score={r['score']:.2f} runtime={r['runtime_seconds']:.2f}s key={r['key']}");
 if a.output:json_result(a.output,r)
if __name__=='__main__':main()
