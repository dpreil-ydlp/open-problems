#!/usr/bin/env python3
"""Profile ciphertext, run plausible solvers within a shared wall-clock budget, rank JSON results."""
import argparse, json, subprocess, sys, time
from pathlib import Path
from cipherkit import LANGS, read_cipher, slug, json_result
import stats
ROOT=Path(__file__).resolve().parent
SOLVERS={
 'subst':('subst.py',[]),
 'homophonic':('homophonic.py',['--checkpoint-seconds','5']),
 'vigenere':('vigenere.py',[]),
 'transposition':('transposition.py',[]),
 'playfair':('playfair.py',[]),
}
def choose(d):
 g=d['guess']; selected=['subst']
 if 'polyalphabetic' in g:selected+=['vigenere']
 if 'homophonic' in g or d['distinct_symbols']>26:selected+=['homophonic']
 if 'transposition' in g or d['ic']>.045:selected+=['transposition','playfair']
 return list(dict.fromkeys(selected))
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('ciphertext',type=Path);p.add_argument('--lang',choices=LANGS,default='en');p.add_argument('--time-budget',type=float,default=240,help='total seconds shared by sequential solvers');a=p.parse_args()
 raw=read_cipher(a.ciphertext);profile=stats.analyze(raw); names=choose(profile); outdir=ROOT/'results'/slug(a.ciphertext);outdir.mkdir(parents=True,exist_ok=True)
 (outdir/'stats.json').write_text(json.dumps({'symbols':profile['symbols'],'distinct_symbols':profile['distinct_symbols'],'ic':profile['ic'],'periodic_ic':profile['periodic_ic'],'guess':profile['guess']},indent=2)+'\n')
 print(f"Guess: {profile['guess']}; selected: {', '.join(names)}; budget: {a.time_budget:.0f}s")
 deadline=time.monotonic()+a.time_budget; completed=[]
 for idx,name in enumerate(names):
  remaining=deadline-time.monotonic()
  if remaining<=1:break
  script,extra=SOLVERS[name]; result_path=outdir/f'{name}.json'; slot=max(1,remaining/(len(names)-idx))
  # Derive safe iteration limits for short samples so one family does not consume the entire budget.
  its=max(200,min(18000,int(slot*55)));restarts=max(1,min(12,int(slot/2)))
  cmd=[sys.executable,str(ROOT/script),str(a.ciphertext),'--lang',a.lang,'--output',str(result_path),*extra]
  if name in ('subst','homophonic','playfair'):cmd += ['--iters',str(its),'--restarts',str(restarts)]
  elif name=='vigenere':cmd += ['--polish-iters',str(its)]
  else:cmd += ['--iters',str(max(100,its//5)),'--restarts',str(max(1,restarts//3))]
  try:
   proc=subprocess.run(cmd,capture_output=True,text=True,timeout=max(1,slot))
   if proc.returncode==0 and result_path.exists():
    data=json.loads(result_path.read_text());completed.append((data['score'],name,data));print(f"{name}: score {data['score']:.2f} ({data.get('runtime_seconds',0):.1f}s)")
   else:print(f"{name}: failed ({proc.stderr.strip()[-300:] or proc.stdout.strip()[-300:]})")
  except subprocess.TimeoutExpired:print(f"{name}: stopped at its {slot:.1f}s budget")
  except Exception as e:print(f"{name}: {e}")
 ranked=sorted(completed,reverse=True);print('\nRanked results:')
 for rank,(score_value,name,data) in enumerate(ranked,1):print(f"{rank}. {name} score={score_value:.2f} key={data['key']}\n   {data['plaintext'][:220]}")
 print(f"\nSaved results in {outdir}")
if __name__=='__main__':main()
