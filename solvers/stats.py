#!/usr/bin/env python3
"""Ciphertext profile, coincidence periods, n-grams and repeats."""
import argparse, collections, math, re
from pathlib import Path
from cipherkit import read_cipher

def analyze(text):
 # Spaces and line breaks are formatting. Keep every other visible symbol so
 # digit- and punctuation-based homophones remain visible to the classifier.
 s=''.join(c for c in text if not c.isspace()); n=len(s); counts=collections.Counter(s); ic=sum(v*(v-1) for v in counts.values())/(n*(n-1)) if n>1 else 0.0
 periods=[]
 for p in range(1,31):
  cols=[s[i::p] for i in range(p)]; vals=[]
  for c in cols:
   q=collections.Counter(c); z=len(c); vals.append(sum(v*(v-1) for v in q.values())/(z*(z-1)) if z>1 else 0)
  periods.append((p,sum(vals)/len(vals)))
 repeats=collections.defaultdict(list)
 for size in range(3,min(7,n)+1):
  for i in range(n-size+1): repeats[s[i:i+size]].append(i)
 dup={k:v for k,v in repeats.items() if len(v)>1}
 # Non-overlap distance factors are Kasiski evidence.
 votes=collections.Counter()
 for pos in dup.values():
  for i in range(1,len(pos)):
   d=pos[i]-pos[i-1]
   for p in range(2,31):
    if d%p==0: votes[p]+=1
 top_period=sorted(periods,key=lambda x:x[1],reverse=True)[:3]
 poly_p=max(votes,key=votes.get) if votes else top_period[0][0]
 if len(counts)<8 and n>40: guess='transposition (few distinct symbols; inspect language IC)'
 elif len(counts)>26 and n>40 and ic<.065: guess='homophonic substitution'
 elif ic>.065: guess='monoalphabetic substitution'
 elif ic<.045: guess=f'polyalphabetic, likely period {poly_p}'
 elif votes and votes[poly_p]>=2: guess=f'polyalphabetic, likely period {poly_p}'
 elif len(counts)>20 and counts.most_common(1)[0][1]/max(1,n)<.04: guess='homophonic substitution'
 else: guess='transposition or monoalphabetic substitution'
 return {"symbols":n,"distinct_symbols":len(counts),"ic":ic,"periodic_ic":periods,"top_periods":top_period,"guess":guess,"unigrams":counts,"bigrams":collections.Counter(s[i:i+2] for i in range(n-1)),"repeats":dup}
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('ciphertext',type=Path);a=ap.parse_args();d=analyze(read_cipher(a.ciphertext))
 print(f"Symbols: {d['symbols']} | distinct: {d['distinct_symbols']} | IC: {d['ic']:.5f}")
 print('Periodic IC: '+' '.join(f"{p}:{v:.4f}" for p,v in d['periodic_ic']))
 print('Unigrams: '+' '.join(f'{k}:{v}' for k,v in d['unigrams'].most_common()))
 print('Bigrams: '+' '.join(f'{k}:{v}' for k,v in d['bigrams'].most_common(20)))
 print('Repeated substrings: '+'; '.join(f"{k}@{','.join(map(str,v))}" for k,v in sorted(d['repeats'].items(),key=lambda kv:(-len(kv[0]),kv[0]))[:30]) or 'none')
 print('Guess: '+d['guess'])
if __name__=='__main__':main()
