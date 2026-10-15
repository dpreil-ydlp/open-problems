"""Shared, dependency-light primitives for classical cipher solvers."""
from __future__ import annotations
import json, math, random, re, time
from pathlib import Path
import numpy as np
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LANGS = ("en", "de", "fr", "it", "es", "la")
FREQ = {
"en": [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,.153,.772,4.025,2.406,6.749,7.507,1.929,.095,5.987,6.327,9.056,2.758,.978,2.360,.150,1.974,.074],
"de": [6.5,1.9,3.1,5.1,17.4,1.7,3.0,4.6,7.6,.3,1.2,3.4,2.5,9.8,2.5,0.8,.02,7.0,7.3,6.2,4.4,0.7,1.9,.03,0.04,1.1],
"fr": [7.6,.9,3.3,3.7,14.7,1.1,1.0,.7,7.5,.6,.05,5.5,2.7,7.1,5.8,3.0,.01,6.7,7.9,7.2,6.3,1.8,.04,.4,.1,.3],
"it": [11.7,.9,4.5,3.7,11.8,.9,1.6,1.5,11.3,.01,.01,6.5,2.5,6.9,9.8,3.0,.5,6.4,4.9,5.6,3.0,2.1,.01,.01,.01,.5],
"es": [12.5,1.4,4.7,5.9,13.7,.7,1.0,.9,6.2,.4,.01,4.9,3.2,6.7,8.7,2.5,.9,6.9,7.9,4.6,3.9,1.1,.02,.2,1.0,.5],
"la": [10.0,1.0,4.0,5.0,12.0,1.0,2.0,3.0,10.0,.1,.1,5.0,3.0,6.0,8.0,2.0,.1,6.0,6.0,5.0,4.0,1.0,.1,.1,.1,.1]}

def letters(text: str) -> str: return ''.join(c for c in text.upper() if 'A' <= c <= 'Z')
def indices(text: str) -> np.ndarray:
    raw=np.frombuffer(text.encode('ascii','ignore'),dtype=np.uint8)
    raw=raw[(raw>=65)&(raw<=90)]
    return (raw-65).astype(np.int16,copy=False)
def load_table(lang: str) -> np.ndarray:
    if lang not in LANGS: raise ValueError(f"unknown language {lang!r}; choose {', '.join(LANGS)}")
    path=Path(__file__).parent/'ngrams'/f'{lang}.quad.npy'
    if not path.exists(): raise FileNotFoundError(f"quadgram table missing: {path}; run `uv run python ngrams/build_tables.py`")
    return np.load(path,mmap_mode='r')
def score(text: str, table: np.ndarray) -> float:
    a=indices(text); n=len(a)
    if n<4: return float('-inf')
    ids=(((a[:-3]*26+a[1:-2])*26+a[2:-1])*26+a[3:]).astype(np.int64)
    return float(np.sum(table[ids],dtype=np.float64))
def anneal(text: str, decrypt, table: np.ndarray, *, iters=12000, restarts=8, seed=17, callback=None):
    rng=random.Random(seed); best=(-math.inf,None,None); started=time.perf_counter()
    for run in range(restarts):
        key0=init_key(rng)
        plain=decrypt(text,key0); value=score(plain,table); local=(value,key0[:],plain)
        for i in range(iters):
            t=max(.02, 18.0*(1-i/max(1,iters)))
            key=local[1][:]
            x,y=rng.sample(range(len(key)),2); key[x],key[y]=key[y],key[x]
            p=decrypt(text,key); s=score(p,table)
            if s>local[0] or rng.random()<math.exp(max(-60,(s-local[0])/t)): local=(s,key,p)
            if local[0]>best[0]: best=(local[0],local[1][:],local[2])
        if callback: callback(run+1,best,time.perf_counter()-started)
    return {"score":best[0],"key":best[1],"plaintext":best[2],"runtime_seconds":time.perf_counter()-started}
def init_key(rng):
    a=list(range(26)); rng.shuffle(a); return a
def json_result(path, result, **extra):
    d={"score":float(result["score"]),"key":result["key"],"plaintext":result["plaintext"],"runtime_seconds":result.get("runtime_seconds",0),**extra}
    Path(path).parent.mkdir(parents=True,exist_ok=True); Path(path).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
    return d
def slug(text): return re.sub(r'[^a-z0-9]+','-',Path(text).stem.lower()).strip('-') or 'ciphertext'
def read_cipher(path): return Path(path).read_text(errors='replace')
