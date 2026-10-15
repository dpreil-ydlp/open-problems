#!/usr/bin/env python3
"""Check exact-profile Spanish synthetic construction without running annealing."""
import collections, json, random
from pathlib import Path
import attack, run_suite

ROOT=Path(__file__).resolve().parents[1]

def main():
    seq,syms,profile=attack.parse_cipher(attack.DEFAULT_CIPHER)
    corpus,_,_=attack.load_corpus('es',attack.ALPH)
    seeds=random.Random(5042); changes=[]
    for _ in range(30):
        stream,key,plain,adjusted,source,changed=run_suite.synthetic(
            seq,syms,profile,corpus,attack.ALPH,seeds.randrange(2**31))
        assert len(stream)==142 and len(set(map(int,stream)))==55
        assert collections.Counter(syms[int(s)] for s in stream)==profile
        assert all(sum(v==l for v in key.values())<=5 for l in range(len(attack.ALPH)))
        assert ''.join(attack.ALPH[key[int(s)]] for s in stream)==plain
        assert plain==adjusted and changed<=2
        changes.append(changed)
    report={'cases_checked':len(changes),'length':142,'distinct_symbols':55,
            'exact_real_frequency_profile':True,'max_source_edits':max(changes),
            'source_edits_per_case':changes,
            'note':'This validates generation only. It does not measure solver recovery.'}
    out=ROOT/'attack/results/synthetic-generator-validation.json'
    out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))

if __name__=='__main__': main()
