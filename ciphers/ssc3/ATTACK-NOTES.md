# Attack notes for part 3

## Evidence

The supplied ciphertext has 142 two-digit symbols and 55 distinct values. The challenge says likely SSC, Summer/Fall 1936, probably Spanish, but possibly Basque. It gives no key, crib, or homophone-selection mode.

Baseline: 27 letters (A–Z plus separate Ñ), numbers 01–99, 3 or 4 homophones per letter. Part 3 permits 3–5 and alphabet variants with CH/LL or without W. Its hint does not state the number range. See STRUCTURE.md.

## Key-space scale

A 27-letter, 99-number table with 3–5 numbers per letter has layouts counted by summing

27!/(a! b! c!) × 99!/(3!^a 4!^b 5!^c)

for nonnegative a,b,c where a+b+c=27 and 3a+4b+5c=99. Here a,b,c count columns with 3, 4, and 5 values. This is about 2^447 layouts (log2 count ≈ 446.98). For the 3/4-only parts 1/2 case, the count is 27!/(9!18!) × 99!/(3!^9 4!^18), about 2^434.5 layouts (log2 count ≈ 434.49).

These estimates assume each number is assigned once and each letter has 3–5 homophones. They count all table positions, including the 44 numbers absent from this ciphertext. The 55 observed numbers alone have at most 27^55 raw letter assignments (about 2^261) before the size limits and language constraints. The alphabet variant and 00–99 vs 01–99 range change these counts.

The keyword strip and offset add choices, but do not multiply a free 27! and a free 27-way shift onto the table estimate: keyword generation restricts the permutations, and some key descriptions may be equivalent. These are scale estimates, not a work-factor calculation after cryptanalysis.

## Constraints

1. Each ciphertext number maps to one plaintext letter for the message. Different homophones in one column decrypt to the same letter.
2. Each group has only 3–5 values in the part 3 variant.
3. Number values are randomly distributed. There is no source-supported arithmetic relation between homophones. Do not search for numeric runs or modular patterns.
4. Repeated ciphertext values are repeated plaintext letters.
5. If homophones were selected sequentially, each plaintext letter cycles through its assigned values. Part 1 used sequential choice; part 2 used random choice; part 3 does not say. Test both. Column order is also unknown.
6. If the table uses 01–99, 44 values are not observed. They are latent table entries.
7. Word patterns, language frequency, and n-grams constrain the plaintext. Context from 1936 can inform later hypotheses, but it is not a crib.

## Suggested attack order

1. Preserve the exact two-digit stream. Record frequencies, positions, and repetitions. Do not merge values.
2. Test the standard 27-symbol alphabet, the 29-symbol alphabet with CH/LL, and a variant without W. Keep Ñ separate in at least one Spanish model.
3. Group observed values into candidate plaintext-letter classes with capacities 3–5. Allow unobserved table numbers to fill remaining capacity.
4. Test both random choice and per-letter cycling. Under cycling, check whether candidate classes support repeating 3-, 4-, or 5-value sequences at the occurrences of each proposed letter. Do not assume part 1's rule transfers to part 3.
5. Score candidate plaintexts with Spanish letter frequencies, then Spanish bigrams/trigrams/quadgrams from the included corpus. Homophones split letter counts, so raw ciphertext frequencies alone are weak.
6. Repeat with Basque frequency and n-gram resources. Compare both language models.
7. Refine candidates with simulated annealing or another stochastic search over number groups and strip alignment. Combine n-gram score, dictionary/word segmentation, and cycling consistency when applicable.
8. Keep separate development and final scoring material. Do not tune all scoring choices against this one short ciphertext.

This is a research plan only. No part 3 plaintext or key was attempted.

## Spanish letter frequencies

Common Spanish letter frequencies in percent, from the Spanish column in the cited reference:

| Letter | % | Letter | % | Letter | % |
|---|---:|---|---:|---|---:|
| A | 11.525 | J | 0.493 | S | 7.977 |
| B | 2.215 | K | 0.026 | T | 4.632 |
| C | 4.019 | L | 4.967 | U | 3.927 |
| D | 5.010 | M | 3.157 | V | 1.138 |
| E | 13.702 | N | 6.712 | W | 0.027 |
| F | 0.692 | Ñ | 0.311 | X | 0.515 |
| G | 1.768 | O | 8.683 | Y | 1.433 |
| H | 1.973 | P | 2.510 | Z | 0.467 |
| I | 6.247 | Q | 0.877 | R | 6.871 |
The MysteryTwister PDF itself gives E ≈13.68% and N ≈6.71% (printed p. 3/10). The reference percentages sum to about 100%; renormalize them before use as probabilities. The broader table is from the Spanish column at https://en.wikipedia.org/wiki/Letter_frequency, which cites Fletcher Pratt, Secret and Urgent (1942), pp. 254–255.

For scoring, map accented vowels to their base letter (Á→A, É→E, Í→I, Ó→O, Ú→U; optionally Ü→U). Keep Ñ distinct for the 27-letter alphabet. If testing an alphabet without Ñ, also score a version with Ñ→N. Strip punctuation and spaces for n-gram scoring, but retain a word-level form for dictionary scoring. Historical telegrams may omit accents.
