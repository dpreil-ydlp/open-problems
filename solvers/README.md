# Classical cipher toolkit

Python 3.11+; one local process at a time; NumPy is the only runtime dependency. No GPU or container is used. Run commands from `solvers/`.

## Setup

```sh
uv sync --dev
uv run python ngrams/build_tables.py
```

The builder downloads three plain-text public-domain books per language from Project Gutenberg, retains the text and source URL in `ngrams/corpora/`, and writes one dense `float32` quadgram log-score table per language. The six `.npy` files use about 10.4 MiB total. The full corpus and tables use about 20 MiB. To save that space after table generation, pass `--prune-corpora`; the tables remain usable. Rebuild one model with, for example, `uv run python ngrams/build_tables.py --lang en`.

| Language | Gutenberg books |
|---|---|
| English | Pride and Prejudice (1342), Alice's Adventures in Wonderland (11), The Adventures of Sherlock Holmes (1661) |
| German | Die Verwandlung (22367), Die Leiden des jungen Werther (2407), Die Räuber (47804) |
| French | Le Comte de Monte-Cristo (17989), Les Misérables (17489), Notre-Dame de Paris (19657) |
| Italian | La Divina Commedia (1012), Le avventure di Pinocchio (19517), Cuore (28961) |
| Spanish | Don Quijote (2000), Lazarillo de Tormes (320), La Celestina (1619) |
| Latin | Aeneidos (227), Ars Poetica (9175), De Bello Gallico (218) |

The `ngrams/loader.py` module exposes `load_table(lang)` and `score(text, table)`. Tables score A–Z text. Nonletters are ignored during scoring.

## Commands

```sh
uv run python stats.py ciphertext.txt
uv run python subst.py ciphertext.txt --lang en --restarts 20 --iters 30000 --fix Q:E
uv run python homophonic.py ciphertext.txt --lang en --alphabet 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' --checkpoint results/key.json
uv run python vigenere.py ciphertext.txt --lang en --max-period 20
uv run python transposition.py ciphertext.txt --lang en --max-len 20 --double
uv run python transposition.py ciphertext.txt --lang en --combined
uv run python playfair.py ciphertext.txt --lang en
uv run python run_all.py ciphertext.txt --lang en --time-budget 240
```

`stats.py` reports non-whitespace symbol statistics, index of coincidence, periodic IC for periods 1–30, unigram and bigram counts, repeated substrings, and a heuristic family guess. Positions are zero-based in the whitespace-stripped symbol stream. The guess is a lead, not a proof.

`subst.py --fix C:P` fixes a ciphertext-to-plaintext mapping; repeat the option for more known letters. `homophonic.py` accepts an ordered symbol alphabet. Its checkpoint JSON stores the current best symbol map and plaintext. `vigenere.py` tries Vigenere, Beaufort, variant Beaufort, and autokey by default. `transposition.py` searches columnar and double-columnar keys; `--combined` alternates a transposition pass, substitution pass, and a second transposition pass scored through the current substitution key.

`run_all.py` runs selected solvers one at a time under one shared wall-clock budget. It writes per-solver JSON files and `stats.json` to `results/<ciphertext-slug>/`, then prints results ranked by score. A score is comparable within the same language and scoring method. It is not a calibrated probability that a plaintext is correct.
Use `--homophonic-alphabet` to include punctuation that is part of a cipher's symbol alphabet. By default, `run_all.py` treats punctuation as formatting and passes letters and digits as candidate symbols.

## Recovery checks

Run with `uv run --python 3.11 python -m pytest -q`. The tests encrypt a 200-letter excerpt from the bundled English corpus and recover it. The RNG seeds make each fixture reproducible. They are recovery smoke checks, not a broad success-rate benchmark: the substitution fixture supplies 20 of 26 mappings; homophonic and Playfair fixtures use the same fixed RNG seed for key generation and solver initialization; the transposition fixture searches a two-column key. The Vigenere test searches a random three-letter key. General-key recovery on short ciphertexts is uncertain, especially for Playfair and homophonic substitution. Increase restarts and iterations for real attacks, and compare candidate plaintexts with language knowledge.

Measured on this Mac with Python 3.11.16, NumPy 2.4.6, one process, at the 200-character test size:

| Solver | Test case | Runtime (s) |
|---|---|---:|
| Vigenere | Random 3-letter key | 0.4208 |
| Transposition | Two-column key | 0.0001 |
| Substitution | 20 known mappings | 4.4624 |
| Playfair | Seeded 5x5 key | 0.0245 |
| Homophonic | Seeded symbol map | 0.0918 |
