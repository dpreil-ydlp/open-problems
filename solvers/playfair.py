#!/usr/bin/env python3
"""Simulated annealing Playfair decryptor (I/J share a square cell)."""
import argparse, math, random, time
from pathlib import Path
from cipherkit import *
ABC='ABCDEFGHIKLMNOPQRSTUVWXYZ'
def decrypt(text,key):
 s=''.join(c for c in text.upper().replace('J','I') if c in ABC)
 if len(s)%2:s+='X'
 pos={c:(i//5,i%5) for i,c in enumerate(key)};out=[]
 for i in range(0,len(s),2):
  a,b=s[i:i+2];ra,ca=pos[a];rb,cb=pos[b]
  if ra==rb:out.extend((key[ra*5+(ca-1)%5],key[rb*5+(cb-1)%5]))
  elif ca==cb:out.extend((key[((ra-1)%5)*5+ca],key[((rb-1)%5)*5+cb]))
  else:out.extend((key[ra*5+cb],key[rb*5+ca]))
 return ''.join(out)
def solve(text,lang='en',restarts=16,iters=24000,seed=61):
 table=load_table(lang);rng=random.Random(seed);best=(-math.inf,None,None);started=time.perf_counter()
 for _ in range(restarts):
  key=list(ABC);rng.shuffle(key);p=decrypt(text,key);local=(score(p,table),key[:],p)
  if local[0]>best[0]:best=(local[0],local[1][:],local[2])
  for i in range(iters):
   temp=max(2.0,300*(1-i/max(1,iters)));k=local[1][:]
   x,y=rng.sample(range(25),2);k[x],k[y]=k[y],k[x]
   if rng.random()<.15:k.reverse()
   plain=decrypt(text,k);s=score(plain,table)
   if s>local[0] or rng.random()<math.exp(max(-60,(s-local[0])/temp)):local=(s,k,plain)
   if local[0]>best[0]:best=(local[0],local[1][:],local[2])
 return {'score':best[0],'key':''.join(best[1]),'plaintext':best[2],'runtime_seconds':time.perf_counter()-started}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('ciphertext',type=Path);p.add_argument('--lang',choices=LANGS,default='en');p.add_argument('--restarts',type=int,default=16);p.add_argument('--iters',type=int,default=24000);p.add_argument('--output',type=Path);a=p.parse_args();r=solve(read_cipher(a.ciphertext),a.lang,a.restarts,a.iters);print(r['plaintext']);print(f"score={r['score']:.2f} runtime={r['runtime_seconds']:.2f}s key={r['key']}");
 if a.output:json_result(a.output,r)
if __name__=='__main__':main()
