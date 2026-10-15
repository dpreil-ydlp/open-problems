# Spanish Strip Cipher part 3: attack round 1

## Verdict

**PARTIAL, unconfirmed.** The highest Spanish candidates contain readable fragments, including forms resembling `DONA`, `CUANDO`, `ELLA LLAMA`, and `DECIA`. The real best score (−1418.03) is above the two full-budget shuffled scores. The first synthetic generator changed 45.8%–48.6% of sampled corpus excerpt letters (65–69 characters), so its recovery scores are invalid for Spanish-like plaintext. I corrected the generator and checked 30 constructions with the exact frequency profile and at most two changed letters, but the corrected controls did not receive solver runs within the two-hour cap. The real plaintext and key are not trustworthy. Only two shuffled controls completed. The requested 30+30 significance matrix remains incomplete. The 100th-percentile ranks from two shuffled samples are not reliable significance evidence.

## Task record

- **Owner:** implementation sub-agent.
- **Outcome:** implement and run a Spanish/Basque homophonic substitution search; retain candidate and control JSON.
- **Proof:** 300 restarts completed for both language baselines; two full v1 synthetic and two full shuffled runs completed; one more v1 synthetic run was partial. The corrected v2 generator passed 30 construction checks, with no solver runs. Details are in `results/*.json`.
- **Scope:** local research only. No MysteryTwister submission.
- **Remaining:** run the corrected v2 generator through the solver for 30 synthetic cases, and complete the 30 shuffled controls at the same solver budget. Do not claim a solution from this run.
- **Next action:** run the corrected synthetic protocol before interpreting the real candidate.

## Model and scoring

- Ciphertext: 142 two-digit tokens, 55 distinct symbols. Plaintext alphabet: `A-Z` plus `Ñ` for Spanish; `A-Z` for Basque. Accented vowels fold to base vowels. Each observed ciphertext symbol maps to one letter; no letter receives more than five observed symbols.
- Corpus language model: character 4-gram and 5-gram counts from all supplied files for that language, with additive smoothing `alpha=0.1` over the full alphabet vocabulary (`27^n` for Spanish, `26^n` for Basque). For each 5-character window, use its 5-gram log probability if its count is nonzero; otherwise use the first four characters’ 4-gram log probability. Scores are sums over 138 windows; higher (less negative) is better.
- Word score: maximum non-overlapping coverage by corpus dictionary words of length at least 3. Spanish candidates use the Spanish list; Basque candidates use the Basque text vocabulary. This is a rough coverage measure, not a language probability.
- Fallback counts below report how many windows used the 4-gram fallback. The Basque corpus has only 115,621 normalized letters, so its top candidate windows mostly fall back to 4-grams. Do not compare raw Spanish and Basque scores directly.
- Move set: reassign one symbol to a letter with remaining capacity, or swap two symbols’ letters. Geometric temperature schedule: 4.5 to 0.035. One process, `nice -n 10`.

## Commands and runtimes

Run from `/Users/davidpreil/Projects/open-problems/ciphers/ssc3`:

```sh
nice -n 10 python3 attack/run_suite.py --budget-seconds 6780 --restarts 300 --iterations 200000 --seed 42
nice -n 10 python3 attack/run_suite.py --controls-only --budget-seconds 4800 --restarts 300 --iterations 200000 --seed 42
python3 attack/finalize_results.py
python3 attack/validate_synthetic_generator.py
```

- The first 6,780-second suite run saved the Spanish and Basque baselines, then exited on a synthetic symbol-indexing bug. The control generator was corrected and checked for length, distinct-symbol count, exact frequency profile, key capacity, and plaintext/key consistency.
- Spanish baseline: 920.979 seconds, 300 restarts, 59,219,925 scored proposals.
- Basque baseline: 782.800 seconds, 300 restarts, 59,252,128 scored proposals.
- Control run (generator v1): 4,800 seconds. It completed two full-budget synthetic cases, two full-budget shuffled cases, and one partial synthetic case (33 restarts, 6,426,301 scored proposals). The v1 synthetic outputs are invalid recovery controls. The remaining requested controls did not run.
- Corrected generator (v2): `python3 attack/validate_synthetic_generator.py` checked 30 exact-profile constructions. Every sample retained the 142-character corpus excerpt with zero to two letter substitutions. This checked generation only; no annealing or recovery rate was measured on v2 samples.
- An earlier inefficient implementation was stopped after about seven minutes. It produced no saved results and is excluded from all reported scores.

## Top Spanish candidates

All scores use the Spanish model. Keys map ciphertext symbols to plaintext letters.

### 1. score -1418.028; word coverage 81.0%; 4-gram fallback 11/138

`ITOPORLARTESABAESUELDONADELASIENDOCUANTOSAELLAMADELASDESALATENIALACALDESTARESPEROSOCONLACASIONDOALPARADECIAESENTABOSCUANTADOSLOCUATADOSEALGUET`

Key: `02=P, 03=E, 04=D, 05=E, 06=I, 08=O, 10=L, 11=T, 14=T, 16=S, 17=S, 18=S, 19=A, 22=T, 23=I, 24=M, 28=T, 30=O, 31=O, 32=A, 34=R, 35=E, 38=L, 39=B, 40=S, 41=B, 43=C, 44=U, 45=D, 47=C, 48=S, 49=G, 50=L, 51=O, 55=R, 58=R, 60=L, 62=P, 63=C, 64=I, 65=R, 68=A, 69=C, 73=P, 74=D, 76=E, 77=D, 78=N, 81=A, 82=O, 83=N, 84=E, 90=A, 91=D, 98=L`

### 2. score -1418.318; word coverage 83.1%; 4-gram fallback 7/138

`ITOPORLARTESABAESUELDONADELASIENTOCUANTOSAELLAMADELASDESALATENIALACALDESTADESPEROSOCONLACASIONDOALPARADECIAESENTANOSCUANTADOSLOCUATADOSEALGUET`

Key: `02=P, 03=E, 04=D, 05=E, 06=I, 08=O, 10=L, 11=T, 14=T, 16=S, 17=S, 18=S, 19=A, 22=T, 23=I, 24=M, 28=T, 30=O, 31=O, 32=A, 34=D, 35=E, 38=L, 39=N, 40=S, 41=B, 43=C, 44=U, 45=D, 47=C, 48=S, 49=G, 50=L, 51=O, 55=R, 58=R, 60=L, 62=P, 63=C, 64=I, 65=R, 68=A, 69=C, 73=P, 74=D, 76=E, 77=T, 78=N, 81=A, 82=O, 83=N, 84=E, 90=A, 91=D, 98=L`

### 3. score -1420.238; word coverage 84.5%; 4-gram fallback 6/138

`MPOCONLARDESERAELUELDONADELASMANPOCUANDOLAELLAMADELASDESALATENIALACASDESPARESPEROSOCONSERASCONDOASPARECERIAASENTADOSCUENTADOSLOQUEDADOSEALGUAD`

Key: `02=C, 03=E, 04=D, 05=E, 06=C, 08=O, 10=L, 11=T, 14=D, 16=S, 17=L, 18=S, 19=A, 22=P, 23=M, 24=M, 28=T, 30=O, 31=O, 32=A, 34=R, 35=E, 38=L, 39=D, 40=S, 41=R, 43=Q, 44=U, 45=D, 47=C, 48=S, 49=G, 50=L, 51=O, 55=R, 58=N, 60=L, 62=P, 63=R, 64=I, 65=R, 68=A, 69=C, 73=P, 74=D, 76=E, 77=P, 78=N, 81=A, 82=O, 83=N, 84=A, 90=E, 91=C, 98=S`

### 4. score -1421.849; word coverage 83.8%; 4-gram fallback 7/138

`MPOCONLARDESERAELUELDONADELASMANPOCUANDOLAELLAMADELASDESALATENIALACASDESPARESPEROSOCONSERASCONDOASTARECERIAASENTADOSCUENTADOSLOQUEDADOSEALGUAD`

Key: `02=C, 03=E, 04=D, 05=E, 06=C, 08=O, 10=L, 11=T, 14=D, 16=S, 17=L, 18=S, 19=A, 22=P, 23=M, 24=M, 28=T, 30=O, 31=O, 32=A, 34=R, 35=E, 38=L, 39=D, 40=S, 41=R, 43=Q, 44=U, 45=D, 47=C, 48=S, 49=G, 50=L, 51=O, 55=R, 58=N, 60=L, 62=T, 63=R, 64=I, 65=R, 68=A, 69=C, 73=P, 74=D, 76=E, 77=P, 78=N, 81=A, 82=O, 83=N, 84=A, 90=E, 91=C, 98=S`

### 5. score -1422.008; word coverage 79.6%; 4-gram fallback 10/138

`TUACONLARDODELAAPUESTANARASESTANTOCUANDOPEELLAVERELEDTODELADONDEHABESTOQUESESPARADOCONSELASMANDOESTARENELDAADANDELASBUENTADOSLOQUEDADOSEESCUAD`

Key: `02=C, 03=O, 04=R, 05=A, 06=M, 08=O, 10=L, 11=T, 14=D, 16=D, 17=P, 18=S, 19=E, 22=U, 23=T, 24=V, 28=D, 30=O, 31=A, 32=E, 34=S, 35=E, 38=L, 39=L, 40=Q, 41=L, 43=Q, 44=U, 45=T, 47=C, 48=S, 49=C, 50=S, 51=O, 55=R, 58=N, 60=H, 62=T, 63=L, 64=D, 65=R, 68=A, 69=B, 73=P, 74=D, 76=E, 77=T, 78=N, 81=A, 82=O, 83=N, 84=A, 90=E, 91=N, 98=S`

### 6. score -1422.097; word coverage 79.6%; 4-gram fallback 11/138

`TUARONLARDODELAAPUESTANARASESTANTOCUANDOPEELLAVERELEDTODELADONDEHABESTOQUESESPARADOCONSELASMANDOESTARENELDAADANDELASBUENTADOSLOQUEDADOSEESCUAD`

Key: `02=R, 03=O, 04=R, 05=A, 06=M, 08=O, 10=L, 11=T, 14=D, 16=D, 17=P, 18=S, 19=E, 22=U, 23=T, 24=V, 28=D, 30=O, 31=A, 32=E, 34=S, 35=E, 38=L, 39=L, 40=Q, 41=L, 43=Q, 44=U, 45=T, 47=C, 48=S, 49=C, 50=S, 51=O, 55=R, 58=N, 60=H, 62=T, 63=L, 64=D, 65=R, 68=A, 69=B, 73=P, 74=D, 76=E, 77=T, 78=N, 81=A, 82=O, 83=N, 84=A, 90=E, 91=N, 98=S`

### 7. score -1422.621; word coverage 76.8%; 4-gram fallback 10/138

`TUACONLARDODELAAPUESTANARASESTANTOCUANDOPEELLACERELEDTODELADONDEHABESTOQUESESPARADOCONSELASMANDOESTARENELDAADANDELASBUENTADOSLOQUEDADOSEESCUAD`

Key: `02=C, 03=O, 04=R, 05=A, 06=M, 08=O, 10=L, 11=T, 14=D, 16=D, 17=P, 18=S, 19=E, 22=U, 23=T, 24=C, 28=D, 30=O, 31=A, 32=E, 34=S, 35=E, 38=L, 39=L, 40=Q, 41=L, 43=Q, 44=U, 45=T, 47=C, 48=S, 49=C, 50=S, 51=O, 55=R, 58=N, 60=H, 62=T, 63=L, 64=D, 65=R, 68=A, 69=B, 73=P, 74=D, 76=E, 77=T, 78=N, 81=A, 82=O, 83=N, 84=A, 90=E, 91=N, 98=S`

### 8. score -1424.288; word coverage 77.5%; 4-gram fallback 12/138

`TUARONLARDODELAAPUESTANARASESTANTOCUANDOPEELLACERELEDTODELADONDEHABESTOQUESESPARADOCONSELASMANDOESTASENELDAADANDELASBUENTADOSLOQUEDADOREESCUAD`

Key: `02=R, 03=O, 04=R, 05=A, 06=M, 08=O, 10=L, 11=T, 14=D, 16=D, 17=P, 18=R, 19=E, 22=U, 23=T, 24=C, 28=D, 30=O, 31=A, 32=E, 34=S, 35=E, 38=L, 39=L, 40=Q, 41=L, 43=Q, 44=U, 45=T, 47=C, 48=S, 49=C, 50=S, 51=O, 55=R, 58=N, 60=H, 62=T, 63=L, 64=D, 65=S, 68=A, 69=B, 73=P, 74=D, 76=E, 77=T, 78=N, 81=A, 82=O, 83=N, 84=A, 90=E, 91=N, 98=S`

### 9. score -1426.212; word coverage 80.3%; 4-gram fallback 12/138

`TUACONLARDODELAAPUESTANARASESTANTOCUANDOPEELLAVERELEDTODELADONDEHABESTOQUESESPARADOCONSELASMANDOESTASENELDAADANDELASBUENTADOSLOQUEDADOYEESCUAD`

Key: `02=C, 03=O, 04=R, 05=A, 06=M, 08=O, 10=L, 11=T, 14=D, 16=D, 17=P, 18=Y, 19=E, 22=U, 23=T, 24=V, 28=D, 30=O, 31=A, 32=E, 34=S, 35=E, 38=L, 39=L, 40=Q, 41=L, 43=Q, 44=U, 45=T, 47=C, 48=S, 49=C, 50=S, 51=O, 55=R, 58=N, 60=H, 62=T, 63=L, 64=D, 65=S, 68=A, 69=B, 73=P, 74=D, 76=E, 77=T, 78=N, 81=A, 82=O, 83=N, 84=A, 90=E, 91=N, 98=S`

### 10. score -1428.478; word coverage 78.2%; 4-gram fallback 16/138

`ARACIBLANDODECAOSUERIANADORESANNUECUANDOSEELLAMADELEDIODELADONLACABESIOPRESESIONADECONSELASMANDOESTASENELLANDONDELASBUENTADOSLOQUEDADETEEROUND`

Key: `02=C, 03=O, 04=D, 05=O, 06=M, 08=O, 10=L, 11=T, 14=D, 16=D, 17=S, 18=T, 19=A, 22=R, 23=A, 24=M, 28=D, 30=I, 31=A, 32=E, 34=S, 35=E, 38=L, 39=L, 40=P, 41=C, 43=Q, 44=U, 45=I, 47=C, 48=S, 49=O, 50=R, 51=E, 55=N, 58=B, 60=C, 62=T, 63=L, 64=L, 65=S, 68=A, 69=B, 73=I, 74=D, 76=E, 77=U, 78=N, 81=A, 82=O, 83=N, 84=N, 90=E, 91=N, 98=S`

## Top Basque candidates

All scores use the Basque model. Word coverage uses the supplied Basque vocabulary.

### 1. score -1435.659; word coverage 28.9%; 4-gram fallback 119/138

`RREGOTRAZKENITAIZAINHERADINAARINTEGAANKEZATORAKUDIOANHENARAKENMUTAKALHERRANIAGIZENEGERLIOAAMENDEALBALISTOMAININKANEAKAINKADEARELAIKADEZIANMAIK`

Key: `02=G, 03=E, 04=D, 05=I, 06=M, 08=E, 10=R, 11=K, 14=K, 16=N, 17=Z, 18=Z, 19=U, 22=R, 23=R, 24=K, 28=K, 30=O, 31=E, 32=A, 34=N, 35=I, 38=O, 39=N, 40=R, 41=T, 43=L, 44=A, 45=H, 47=G, 48=A, 49=M, 50=N, 51=E, 55=Z, 58=T, 60=T, 62=B, 63=O, 64=M, 65=L, 68=A, 69=K, 73=G, 74=D, 76=T, 77=T, 78=R, 81=A, 82=E, 83=N, 84=I, 90=I, 91=S, 98=L`

### 2. score -1436.494; word coverage 28.9%; 4-gram fallback 116/138

`RREGOTRAZKENITAIZAINHERADINAARINDESAANKEZATORAKUDIOANHENARAKENMUTAKALHERRANIAGIZENESERLIOAAMENDEALBALISTOMAININKANEAKAINDADEARELAIKADEZIANMAIK`

Key: `02=G, 03=E, 04=D, 05=I, 06=M, 08=E, 10=R, 11=D, 14=K, 16=N, 17=Z, 18=Z, 19=U, 22=R, 23=R, 24=K, 28=K, 30=O, 31=E, 32=A, 34=N, 35=I, 38=O, 39=N, 40=R, 41=T, 43=L, 44=A, 45=H, 47=S, 48=A, 49=M, 50=N, 51=E, 55=Z, 58=T, 60=T, 62=B, 63=O, 64=M, 65=L, 68=A, 69=K, 73=G, 74=D, 76=T, 77=D, 78=R, 81=A, 82=E, 83=N, 84=I, 90=I, 91=S, 98=L`

### 3. score -1438.397; word coverage 20.4%; 4-gram fallback 124/138

`DKOKOKRANZUNITAEZTELTORANELARDUAGAZTAAZIZAELRABENELANTUNARAKUALERAIAITUSKAIERMENONAZURIIZARROADIAITAKINEZLAUNEAKASORITIABADURRISTIZADATEALETUZ`

Key: `02=K, 03=U, 04=N, 05=E, 06=R, 08=I, 10=R, 11=B, 14=Z, 16=N, 17=Z, 18=T, 19=E, 22=K, 23=D, 24=B, 28=K, 30=O, 31=O, 32=A, 34=I, 35=E, 38=L, 39=S, 40=S, 41=T, 43=S, 44=T, 45=T, 47=Z, 48=R, 49=E, 50=L, 51=A, 55=N, 58=K, 60=R, 62=T, 63=Z, 64=L, 65=K, 68=A, 69=I, 73=M, 74=D, 76=E, 77=G, 78=R, 81=A, 82=U, 83=A, 84=U, 90=I, 91=N, 98=I`

### 4. score -1438.661; word coverage 20.4%; 4-gram fallback 126/138

`DKOKOKRANZUNITAEZTELTORANELARDUAGAZTAAZIZAELRABENELANTUNARAKUALERAIAITUSKAIERMENONAZURIIZARROADIAITAKINEZLAUNEAKASORITIABADURRISTIZADATEALUTUZ`

Key: `02=K, 03=U, 04=N, 05=E, 06=R, 08=I, 10=R, 11=B, 14=Z, 16=N, 17=Z, 18=T, 19=E, 22=K, 23=D, 24=B, 28=K, 30=O, 31=O, 32=A, 34=I, 35=E, 38=L, 39=S, 40=S, 41=T, 43=S, 44=T, 45=T, 47=Z, 48=R, 49=U, 50=L, 51=A, 55=N, 58=K, 60=R, 62=T, 63=Z, 64=L, 65=K, 68=A, 69=I, 73=M, 74=D, 76=E, 77=G, 78=R, 81=A, 82=U, 83=A, 84=U, 90=I, 91=N, 98=I`

### 5. score -1440.213; word coverage 27.5%; 4-gram fallback 116/138

`RREGOTRAZKENITAIZAINHERALINAARINTEGAANKEZATORAKULIOANHENARAKENMUTAKALHERRANIAGIZENEGERLIOAAMENDEALBALISTOMAININKANEAKAINOADEARELAIKADESIANIAIK`

Key: `02=G, 03=E, 04=L, 05=I, 06=M, 08=E, 10=R, 11=O, 14=K, 16=N, 17=Z, 18=S, 19=U, 22=R, 23=R, 24=K, 28=K, 30=O, 31=E, 32=A, 34=N, 35=I, 38=O, 39=N, 40=R, 41=T, 43=L, 44=A, 45=H, 47=G, 48=A, 49=I, 50=N, 51=E, 55=Z, 58=T, 60=T, 62=B, 63=O, 64=M, 65=L, 68=A, 69=K, 73=G, 74=D, 76=T, 77=T, 78=R, 81=A, 82=E, 83=N, 84=I, 90=I, 91=S, 98=L`

## Significance controls

Full-budget score lists (each full case used 300 restarts × 200,000 iterations):

- Synthetic known-key cases: -1497.749, -1507.930.
- Shuffled real-cipher cases: -1497.398, -1495.799.
- Real best Spanish score: -1418.028.
- Empirical rank: above all observed controls (100th percentile in both samples); each reference sample has only `n=2`. This is descriptive only.

Synthetic recovery uses the best key’s fraction of the 55 observed symbol mappings that match the known key. The two full cases recovered 5.45%, 0.00% (mean 2.73%); neither recovered 90% of the key. The partial third case recovered 1.82% after 33 restarts.

The v1 synthetic generator makes a random 3–5-entry-per-letter full table, samples 55 observed entries, and uses the real ciphertext’s exact symbol-frequency multiset. To fit its fixed key, it changes 65–69 of the 142 characters in each source excerpt. These texts are not valid Spanish-like samples. Their key accuracies are recorded for audit, but they do not establish the solver’s recovery rate on Spanish. The corrected v2 generator assigns high-frequency observed symbols to letters with matching excerpt quotas, completes a 99-entry table with 3–5 symbols per letter, and changes at most two excerpt letters. Thirty constructions passed checks for token length, distinct symbols, exact frequency profile, key capacity, and plaintext/key consistency. The v2 solver recovery rate is unknown because no annealing runs were made. The shuffled sample remains only two cases. The real score and fragments do not establish a trustworthy solution.

## Output files

- `attack.py`: language-model builder, word coverage, and annealing solver.
- `run_suite.py`: baseline and bounded synthetic/shuffled runs.
- `finalize_results.py`: attaches keys, fallback counts, dictionary coverage, and rank summaries.
- `validate_synthetic_generator.py`: validates 30 corrected synthetic constructions without running the solver.
- `results/es-main.json`, `results/eu-main.json`: top 20 plaintext/key candidates per language.
- `results/synthetic-*.json`, `results/shuffled-*.json`: per-case plaintexts, keys, scores, and run counts.
- `results/significance.json`: observed distributions, recovery rates, and limited-sample percentiles.

Sequential homophone cycling was not tested in this round.
