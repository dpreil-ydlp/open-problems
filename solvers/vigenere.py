#!/usr/bin/env python3
"""Period detection and quadgram refinement for Vigenere-family ciphers."""
import argparse, collections, math, random, time
from pathlib import Path
import numpy as np
from cipherkit import *
MODES=('vigenere','beaufort','variant-beaufort','autokey')
def decrypt(text,key,mode='vigenere'):
 out=[]; j=0; plain=[]
 for c in text.upper():
  if not ('A'<=c<='Z'):out.append(c);continue
  x=ord(c)-65; k=key[j%len(key)] if mode!='autokey' or j<len(key) else plain[j-len(key)]
  y=(x-k)%26 if mode in ('vigenere','autokey') else ((k-x)%26 if mode=='beaufort' else (k+x)%26)
  plain.append(y);out.append(chr(y+65));j+=1
 return ''.join(out)
def periods(text,max_period=30):
 s=letters(text); n=len(s); ans=[]
 for p in range(1,min(max_period,n)+1):
  val=0
  for col in range(p):
   q=collections.Counter(s[col::p]);z=sum(q.values());val+=sum(v*(v-1) for v in q.values())/(z*(z-1)) if z>1 else 0
  ans.append((p,val/p))
 return sorted(ans,key=lambda x:x[1],reverse=True)
def fit_key(text,period,lang):
 s=indices(letters(text)); target=np.array(FREQ[lang],dtype=float);target/=target.sum();key=[]
 for col in range(period):
  vals=s[col::period]; best=(1e99,0)
  for k in range(26):
   shifted=np.bincount((vals-k)%26,minlength=26); n=max(1,len(vals)); chi=np.sum((shifted-n*target)**2/(n*target+1e-8))
   if chi<best[0]:best=(chi,k)
  key.append(best[1])
 return key
def solve(text,lang='en',max_period=20,polish_iters=18000,modes=None,seed=7):
 table=load_table(lang); choices=modes or MODES; started=time.perf_counter(); per=periods(text,max_period); candidates=per[:min(8,len(per))]; best=(-math.inf,None,None,None,None); rng=random.Random(seed)
 for mode in choices:
  for period,_ in candidates:
   base=fit_key(text,period,lang)
   # Autokey's feedback invalidates the ordinary column fit beyond the seed; still use the fit as its seed.
   plain=decrypt(text,base,mode); val=score(plain,table); local=(val,base,plain)
   for step in range(max(400,polish_iters//max(1,len(choices)*len(candidates)))):
    temp=max(.02,12*(1-step/max(1,polish_iters//max(1,len(choices)*len(candidates))))); k=local[1][:];i=rng.randrange(period);k[i]=(k[i]+rng.choice([-2,-1,1,2]))%26
    p=decrypt(text,k,mode);s=score(p,table)
    if s>local[0] or rng.random()<math.exp(max(-60,(s-local[0])/temp)):local=(s,k,p)
   if local[0]>best[0]:best=(local[0],local[1][:],local[2],mode,period)
 return {'score':best[0],'key':''.join(chr(x+65) for x in best[1]),'plaintext':best[2],'mode':best[3],'period':best[4],'period_candidates':per,'runtime_seconds':time.perf_counter()-started}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('ciphertext',type=Path);p.add_argument('--lang',choices=LANGS,default='en');p.add_argument('--max-period',type=int,default=20);p.add_argument('--polish-iters',type=int,default=18000);p.add_argument('--modes',nargs='+',choices=MODES,default=list(MODES));p.add_argument('--output',type=Path);a=p.parse_args();r=solve(read_cipher(a.ciphertext),a.lang,a.max_period,a.polish_iters,a.modes);print(r['plaintext']);print(f"score={r['score']:.2f} mode={r['mode']} period={r['period']} key={r['key']} runtime={r['runtime_seconds']:.2f}s");
 if a.output:json_result(a.output,r)
if __name__=='__main__':main()
