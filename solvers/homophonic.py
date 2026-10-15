#!/usr/bin/env python3
"""Anneal many-to-one symbol mappings for homophonic ciphers."""
import argparse, collections, json, math, random, time
from pathlib import Path
from cipherkit import LANGS, FREQ, load_table, score, json_result, read_cipher

def solve(text,lang='en',restarts=12,iters=24000,alphabet=None,checkpoint=None,checkpoint_seconds=30,seed=31):
 table=load_table(lang); symbols=list(alphabet if alphabet is not None else dict.fromkeys(c for c in text if c.isalpha()))
 if len(set(symbols))!=len(symbols):raise ValueError('symbol alphabet contains duplicates')
 unknown=[c for c in text if c.isalpha() and c not in symbols]
 if unknown:raise ValueError(f'cipher symbols missing from configured alphabet: {unknown[:5]}')
 freq=collections.Counter(c for c in text if c in symbols); rng=random.Random(seed); started=time.perf_counter(); last=started; best=(-math.inf,None,None)
 probs=[x/sum(FREQ[lang]) for x in FREQ[lang]]
 def objective(p):
  q=collections.Counter(c for c in p if 'A'<=c<='Z')
  n=sum(q.values())
  chi=sum((q.get(chr(i+65),0)-n*probs[i])**2/(n*probs[i]) for i in range(26)) if n else 0
  return score(p,table)-1.5*chi
 def render(key):return ''.join(chr(key[symbols.index(c)]+65) if c in symbols else c for c in text)
 def save():
  if checkpoint:
   d={'score':score(best[2],table),'objective':best[0],'key':{symbols[i]:chr(best[1][i]+65) for i in range(len(symbols))},'plaintext':best[2],'elapsed_seconds':time.perf_counter()-started}
   Path(checkpoint).parent.mkdir(parents=True,exist_ok=True);Path(checkpoint).write_text(json.dumps(d,indent=2)+'\n')
 one_to_one=len(symbols)<=26
 for run in range(restarts):
  if one_to_one:k=rng.sample(range(26),len(symbols))
  else:k=[rng.randrange(26) for _ in symbols]
  p=render(k); cur=objective(p); local=(cur,k[:],p)
  if local[0]>best[0]:best=(local[0],local[1][:],local[2])
  for step in range(iters):
   k2=local[1][:]
   if one_to_one:
    if len(k2)<2:break
    i,j=rng.sample(range(len(k2)),2);k2[i],k2[j]=k2[j],k2[i]
   else:
    i=rng.randrange(len(k2));k2[i]=rng.randrange(26)
   p2=render(k2); s=objective(p2); temp=max(2.0,110*(1-step/max(1,iters)))
   if s>local[0] or rng.random()<math.exp(max(-60,(s-local[0])/temp)):local=(s,k2,p2)
   if local[0]>best[0]:best=(local[0],local[1][:],local[2])
   now=time.perf_counter()
   if now-last>=checkpoint_seconds:save();last=now
 save()
 return {'score':score(best[2],table),'objective':best[0],'key':{symbols[i]:chr(best[1][i]+65) for i in range(len(symbols))},'plaintext':best[2],'runtime_seconds':time.perf_counter()-started}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('ciphertext',type=Path);p.add_argument('--lang',choices=LANGS,default='en');p.add_argument('--restarts',type=int,default=12);p.add_argument('--iters',type=int,default=24000);p.add_argument('--alphabet',help='ordered cipher-symbol alphabet; default uses distinct letters');p.add_argument('--checkpoint',type=Path,default=Path('homophonic-best.json'));p.add_argument('--checkpoint-seconds',type=float,default=30);p.add_argument('--output',type=Path);a=p.parse_args();r=solve(read_cipher(a.ciphertext),a.lang,a.restarts,a.iters,a.alphabet,a.checkpoint,a.checkpoint_seconds);print(r['plaintext']);print(f"score={r['score']:.2f} runtime={r['runtime_seconds']:.2f}s key={r['key']}");
 if a.output:json_result(a.output,r)
if __name__=='__main__':main()
