#!/usr/bin/env python3
"""Download the configured public-domain books and build dense quadgram tables."""
from collections import Counter
import unicodedata
from pathlib import Path
import argparse, subprocess
import numpy as np
ROOT=Path(__file__).parent; CORP=ROOT/'corpora'
TRANSLITERATION=str.maketrans({'ß':'SS','ẞ':'SS','æ':'AE','Æ':'AE','œ':'OE','Œ':'OE','ø':'O','Ø':'O','ł':'L','Ł':'L','đ':'D','Đ':'D','ð':'D','Ð':'D','þ':'TH','Þ':'TH'})
def normalize_letters(text):
 text=text.translate(TRANSLITERATION)
 text=''.join(c for c in unicodedata.normalize('NFKD',text.upper()) if not unicodedata.combining(c))
 return ''.join(c for c in text if 'A'<=c<='Z')
# Three Gutenberg plain-text books per language. The downloader records exact source URLs.
BOOKS={
'en':[(1342,'pride-and-prejudice'),(11,'alice-in-wonderland'),(1661,'sherlock-holmes')],
'fr':[(17989,'le-comte-de-monte-cristo'),(17489,'les-miserables'),(19657,'notre-dame-de-paris')],
'es':[(2000,'don-quijote'),(320,'lazarillo-de-tormes'),(1619,'la-celestina')],
'it':[(1012,'divina-commedia'),(19517,'le-avventure-di-pinocchio'),(28961,'cuore')],
'de':[(22367,'die-verwandlung'),(2407,'die-leiden-des-jungen-werther'),(47804,'die-raeuber')],
'la':[(227,'aeneidos'),(9175,'ars-poetica'),(218,'de-bello-gallico')]}
def fetch(book):
 ident,name=book; path=CORP/f'{ident}-{name}.txt'
 if path.exists() and path.stat().st_size>5000:return path
 urls=[f'https://www.gutenberg.org/cache/epub/{ident}/pg{ident}.txt',f'https://www.gutenberg.org/files/{ident}/{ident}-0.txt',f'https://www.gutenberg.org/files/{ident}/{ident}.txt']
 err=None
 for url in urls:
  try:
   # curl uses the system certificate store on macOS. urllib may stall while
   # trying to validate Gutenberg's certificate in some Python installations.
   result=subprocess.run(['curl','-fLsS','--max-time','45',url],capture_output=True,timeout=50)
   if result.returncode: raise RuntimeError(result.stderr.decode(errors='replace').strip())
   data=result.stdout
   if len(data)<5000:continue
   path.write_bytes(data); (CORP/f'{ident}-{name}.source.txt').write_text(url+'\n'); print(f'Fetched {path.name}: {len(data):,} bytes');return path
  except Exception as e:err=e
 raise RuntimeError(f'Could not download Gutenberg book {ident} ({name}): {err}')
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--lang',choices=BOOKS,action='append');ap.add_argument('--prune-corpora',action='store_true',help='remove downloaded raw texts after tables are built');a=ap.parse_args();CORP.mkdir(exist_ok=True);langs=a.lang or list(BOOKS)
 # Fetch serially to avoid disk/network bursts.
 for lang in langs:
  texts=[]
  for book in BOOKS[lang]:
   try:texts.append(fetch(book).read_text(errors='ignore'))
   except Exception as e:print(f'WARNING {lang}: {e}')
  if len(texts)<1:raise SystemExit(f'No usable books for {lang}')
  counts=Counter(); total=0
  for text in texts:
   s=normalize_letters(text)
   counts.update(s[i:i+4] for i in range(len(s)-3));total+=len(s)-3
  table=np.full(26**4,np.float32(-16.0)); floor=1/(total+26**4)
  # log probabilities, with a small additive floor for unseen sequences.
  table[:]=np.float32(np.log(floor))
  for gram,n in counts.items():
   idx=0
   for c in gram:idx=idx*26+ord(c)-65
   table[idx]=np.float32(np.log((n+.05)/(total+.05*26**4)))
  np.save(ROOT/f'{lang}.quad.npy',table); print(f'{lang}: {len(texts)} books, {total:,} letters, {len(counts):,} quadgrams, {(ROOT/f"{lang}.quad.npy").stat().st_size:,} bytes')
 if a.prune_corpora:
  for path in CORP.iterdir():
   if path.is_file():path.unlink()
  print('Removed raw corpus text and source URL files after table generation.')
 else:print('Raw corpora retained in ngrams/corpora/.')
if __name__=='__main__':main()
