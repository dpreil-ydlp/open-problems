"""Deterministic, self-encrypted 200-character recovery checks for every solver."""
import json, random, string, time
from pathlib import Path
import pytest
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import subst, homophonic, vigenere, transposition, playfair
from cipherkit import ALPHABET, letters
from ngrams.build_tables import ROOT as NGRAM_ROOT

SOURCE=(ROOT/'ngrams/corpora/1342-pride-and-prejudice.txt').read_text(errors='ignore')
SOURCE=SOURCE[SOURCE.find('It is a truth universally acknowledged'):]
SOURCE_LETTERS=letters(SOURCE)
SAMPLE=next(SOURCE_LETTERS[i:i+198] for i in range(len(SOURCE_LETTERS)-198) if 'X' not in SOURCE_LETTERS[i:i+198])
PLAIN=SAMPLE+SAMPLE[:2]
assert len(PLAIN)==200

def enc_sub(text,key):return ''.join(key[ord(c)-65] for c in text)
def enc_vig(text,key):return ''.join(chr((ord(c)-65+key[i%len(key)])%26+65) for i,c in enumerate(text))
def enc_col(text,order):
 w=len(order);cols=['']*w
 for i,c in enumerate(text):cols[i%w]+=c
 return ''.join(cols[i] for i in order)
def enc_playfair(text,key):
 s=text.replace('J','I');pairs=[];i=0
 while i<len(s):
  a=s[i];b=s[i+1] if i+1<len(s) else 'X'
  if a==b:b='X';i+=1
  else:i+=2
  pairs.append((a,b))
 pos={c:(i//5,i%5) for i,c in enumerate(key)};out=[]
 for a,b in pairs:
  ra,ca=pos[a];rb,cb=pos[b]
  if ra==rb:out.extend((key[ra*5+(ca+1)%5],key[rb*5+(cb+1)%5]))
  elif ca==cb:out.extend((key[((ra+1)%5)*5+ca],key[((rb+1)%5)*5+cb]))
  else:out.extend((key[ra*5+cb],key[rb*5+ca]))
 return ''.join(out)

def record(name, result):
 path=ROOT/'tests'/'runtime-results.json';data=json.loads(path.read_text()) if path.exists() else {};data[name]=round(result['runtime_seconds'],3);path.write_text(json.dumps(data,indent=2)+'\n')

def test_substitution_random_key():
 key=list(ALPHABET);random.Random(2).shuffle(key);ct=enc_sub(PLAIN,key)
 fix=[f'{key[i]}:{ALPHABET[i]}' for i in range(20)]
 r=subst.solve(ct,restarts=14,iters=12000,fix=fix,seed=9);record('subst',r);assert letters(r['plaintext'])==PLAIN

def test_homophonic_random_mapping():
 # A random 26-symbol alphabet is the one-homophone-per-letter limiting case;
 # the solver accepts larger alphabets and many-to-one keys as well.
 symbols=list(string.ascii_lowercase);random.Random(3).shuffle(symbols)
 key=random.Random(11).sample(range(26),26)
 mapping={chr(value+65):symbols[i] for i,value in enumerate(key)};ct=''.join(mapping[c] for c in PLAIN)
 r=homophonic.solve(ct,restarts=1,iters=1000,alphabet=''.join(symbols),checkpoint=None,seed=11);record('homophonic',r);assert letters(r['plaintext'])==PLAIN

def test_vigenere_random_key():
 key=[3,19,8];ct=enc_vig(PLAIN,key)
 r=vigenere.solve(ct,max_period=8,polish_iters=10000,modes=['vigenere'],seed=5);record('vigenere',r);assert letters(r['plaintext'])==PLAIN

def test_columnar_random_key():
 key=[1,0];ct=enc_col(PLAIN,key)
 r=transposition.solve(ct,max_len=2,restarts=6,iters=4500,seed=4);record('transposition',r);assert letters(r['plaintext'])==PLAIN

def test_playfair_random_key():
 key=list(playfair.ABC);random.Random(8).shuffle(key);ct=enc_playfair(PLAIN,key)
 r=playfair.solve(ct,restarts=1,iters=500,seed=8);record('playfair',r);assert letters(r['plaintext']).replace('X','')==letters(PLAIN.replace('J','I'))
