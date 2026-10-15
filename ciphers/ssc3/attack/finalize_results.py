#!/usr/bin/env python3
"""Add reproducible key, fallback, and coverage fields to completed run JSON."""
import collections, json, random
from pathlib import Path
import numpy as np
import attack, run_suite

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'attack/results'
SEED=42

def key_from_plain(seq, syms, plain, alphabet):
    key={}
    for sid,ch in zip(seq,plain): key[syms[int(sid)]]=ch
    return key

def main():
    for lang,alphabet in [('es',attack.ALPH),('eu',attack.ALPH_EU)]:
        path=OUT/f'{lang}-main.json'
        if not path.exists(): continue
        data=json.loads(path.read_text())
        corpus,words,_=attack.load_corpus(lang,alphabet); _,_,score=attack.make_lm(corpus,alphabet)
        for row in data['top']:
            row['word_coverage']=attack.segment_coverage(row['plaintext'],words)
            fallbacks=sum(score(row['plaintext'][i:i+5])[1] for i in range(len(row['plaintext'])-4))
            row['fivegram_windows']=len(row['plaintext'])-4
            row['fourgram_fallback_windows']=fallbacks
        path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

    cipher,syms,profile=attack.parse_cipher(attack.DEFAULT_CIPHER)
    es_corpus,_,_=attack.load_corpus('es',attack.ALPH); _,_,score=attack.make_lm(es_corpus,attack.ALPH)
    rng=random.Random(SEED+5000)
    case_files=[p for p in list(OUT.glob('synthetic-*.json'))+list(OUT.glob('shuffled-*.json'))
                if p.stem.split('-')[1].isdigit()]
    maxidx=max([int(p.stem.split('-')[1]) for p in case_files],default=-1)
    versions={}
    for p in OUT.glob('synthetic-*.json'):
        if not p.stem.split('-')[1].isdigit(): continue
        r=json.loads(p.read_text()); versions[r['case']]=r.get('generator_version',1)
    generated={}
    shuffled={}
    for i in range(maxidx+1):
        case_seed=rng.randrange(2**31)
        if versions.get(i,1)>=2:
            sseq,true_key,true_plain,excerpt,raw_excerpt,changed=run_suite.synthetic(cipher,syms,profile,es_corpus,attack.ALPH,case_seed)
        else:
            sseq,true_key,true_plain,excerpt=run_suite.synthetic_v1(cipher,syms,profile,es_corpus,attack.ALPH,case_seed)
            local_rng=random.Random(case_seed)
            start=local_rng.randrange(len(es_corpus)-len(cipher))
            raw_excerpt=es_corpus[start:start+len(cipher)]
            changed=sum(a!=b for a,b in zip(raw_excerpt,excerpt))
        generated[i]=(sseq,true_key,true_plain,excerpt,raw_excerpt)
        x=np.array(cipher,copy=True); rng.shuffle(x); shuffled[i]=x
    synth=[]; shuffles=[]
    for path in sorted(OUT.glob('synthetic-*.json')):
        if not path.stem.split('-')[1].isdigit(): continue
        row=json.loads(path.read_text()); i=row['case']; sseq,true_key,true_plain,excerpt,raw_excerpt=generated[i]
        recovered=key_from_plain(sseq,syms,row['plaintext'],attack.ALPH) if row.get('plaintext') else {}
        row['ciphertext_tokens']=[syms[int(x)] for x in sseq]
        row['true_key']={syms[s]:attack.ALPH[l] for s,l in true_key.items()}
        row['recovered_key']=recovered
        row['true_plaintext']=true_plain
        row['corpus_excerpt_adjusted']=excerpt
        row['corpus_excerpt_original']=raw_excerpt
        row['generator_version']=versions.get(i,1)
        row['excerpt_character_changes']=sum(a!=b for a,b in zip(raw_excerpt,excerpt))
        row['excerpt_character_change_fraction']=row['excerpt_character_changes']/len(raw_excerpt)
        row['fourgram_fallback_windows']=sum(score(row['plaintext'][j:j+5])[1] for j in range(len(row['plaintext'])-4)) if row.get('plaintext') else None
        path.write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n'); synth.append(row)
    for path in sorted(OUT.glob('shuffled-*.json')):
        row=json.loads(path.read_text()); i=row['case']; x=shuffled[i]
        row['ciphertext_tokens']=[syms[int(v)] for v in x]
        row['recovered_key']=key_from_plain(x,syms,row['plaintext'],attack.ALPH) if row.get('plaintext') else {}
        row['fourgram_fallback_windows']=sum(score(row['plaintext'][j:j+5])[1] for j in range(len(row['plaintext'])-4)) if row.get('plaintext') else None
        path.write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n'); shuffles.append(row)
    real=json.loads((OUT/'es-main.json').read_text())['top'][0]['score']
    def percentile(values):
        if not values: return None
        return round(100*(sum(x<real for x in values)+0.5*sum(x==real for x in values))/len(values),2)
    is_full=lambda x:x['stats']['restarts_completed']==300 and x['stats']['iterations_completed']>=59000000
    scores_s=[x['best_score'] for x in synth if x.get('best_score') is not None]
    scores_h=[x['best_score'] for x in shuffles if x.get('best_score') is not None]
    scores_s_full=[x['best_score'] for x in synth if is_full(x) and x.get('best_score') is not None]
    scores_h_full=[x['best_score'] for x in shuffles if is_full(x) and x.get('best_score') is not None]
    acc=[x['key_letter_accuracy'] for x in synth if is_full(x) and x.get('key_letter_accuracy') is not None]
    dist={'requested_cases_per_class':30,'requested_restarts':300,'requested_iterations_per_restart':200000,'real_best_score':real,
          'synthetic_best_scores':scores_s,'shuffled_best_scores':scores_h,
          'synthetic_full_budget_scores':scores_s_full,'shuffled_full_budget_scores':scores_h_full,
          'real_percentile_vs_synthetic_full_budget':percentile(scores_s_full),'real_percentile_vs_shuffled_full_budget':percentile(scores_h_full),
          'real_percentile_vs_all_observed_synthetic':percentile(scores_s),'real_percentile_vs_all_observed_shuffled':percentile(scores_h),
          'synthetic_key_letter_accuracy':acc,'mean_synthetic_key_letter_accuracy':sum(acc)/len(acc) if acc else None,
          'synthetic_fraction_at_least_90pct_key_correct':sum(x>=0.9 for x in acc)/len(acc) if acc else None,
          'synthetic_completed':len(synth),'shuffled_completed':len(shuffles),
          'synthetic_full_budget_completed':sum(is_full(x) for x in synth),
          'shuffled_full_budget_completed':sum(is_full(x) for x in shuffles),
          'synthetic_control_generator_version':1,
          'synthetic_controls_valid_for_recovery':False,
          'corrected_generator_version':2,
          'corrected_generator_cases_validated':30,
          'corrected_generator_solver_runs':0,
          'note':'The v1 synthetic controls alter a large fraction of sampled excerpt letters and are invalid for Spanish-like solver recovery. The v2 generator preserves the exact profile and was checked on 30 constructions, but received no annealing runs. The significance experiment is inconclusive.'}
    (OUT/'significance.json').write_text(json.dumps(dist,ensure_ascii=False,indent=2)+'\n')
    summary_path=OUT/'run-summary.json'
    summary=json.loads(summary_path.read_text()) if summary_path.exists() else {}
    summary['baselines']={lang:{'runtime_seconds':json.loads((OUT/f'{lang}-main.json').read_text())['runtime_seconds'],
                                'stats':json.loads((OUT/f'{lang}-main.json').read_text())['stats']}
                          for lang in ('es','eu') if (OUT/f'{lang}-main.json').exists()}
    summary['controls']={'synthetic_completed':len(synth),'synthetic_full_budget':len(scores_s_full),
                         'shuffled_completed':len(shuffles),'shuffled_full_budget':len(scores_h_full),
                         'synthetic_excerpt_changes':[{ 'case':x['case'],'characters_changed':x.get('excerpt_character_changes'),
                                                        'fraction_changed':x.get('excerpt_character_change_fraction') } for x in synth],
                         'conclusion':'Synthetic outputs are not valid Spanish-like controls; significance experiment is inconclusive.'}
    summary_path.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__': main()
