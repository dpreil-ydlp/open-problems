# A062887 computational verification

## Environment and commands

- macOS 26.6, Python 3.13.2.
- `verify.py` uses the Python standard library only. No additional packages were installed.
- Commands, run from `/Users/davidpreil/Projects/open-problems/math/A062887`:

```sh
python3 test_verify.py
python3 -u verify.py
```

The unit tests passed (4 tests). The verification command exited with an
assertion failure after printing its full report. This is the requested
`found == (125 does not divide m)` assertion: it fails for 85 non-divisible
values because no witness appeared within the 2,000-digit cap. The script
continues through the identity checks and the 125 scan before it asserts.

## OEIS source

The exact `%N` NAME line, full OEIS text record, verbatim conjecture comment,
source URLs, and access timestamps are in [OEIS-ENTRY.md](OEIS-ENTRY.md).
The b-file was saved verbatim in [b062887.txt](b062887.txt). Its 26 terms at
indices 0 through 25 match the brute-force results below. OEIS history shows
the conjecture comment was added and the status changed from `proposed` to
`approved`; the retrieved history contains no proof or claim that it was
already proved.

## Brute-force comparison

The search generates all five admissible values at each length, sorts them by
numeric value, and selects the first divisible by `m=2n+1`.

| n | m | computed a(n) | b-file a(n) | match |
|---:|---:|---:|---:|:---:|
| 0 | 1 | 1 | 1 | yes |
| 1 | 3 | 3 | 3 | yes |
| 2 | 5 | 5 | 5 | yes |
| 3 | 7 | 7 | 7 | yes |
| 4 | 9 | 9 | 9 | yes |
| 5 | 11 | 319 | 319 | yes |
| 6 | 13 | 975 | 975 | yes |
| 7 | 15 | 75 | 75 | yes |
| 8 | 17 | 7531 | 7531 | yes |
| 9 | 19 | 19 | 19 | yes |
| 10 | 21 | 197531975319 | 197531975319 | yes |
| 11 | 23 | 3197 | 3197 | yes |
| 12 | 25 | 75 | 75 | yes |
| 13 | 27 | 5319 | 5319 | yes |
| 14 | 29 | 319 | 319 | yes |
| 15 | 31 | 31 | 31 | yes |
| 16 | 33 | 3197531975319 | 3197531975319 | yes |
| 17 | 35 | 53197531975 | 53197531975 | yes |
| 18 | 37 | 1975319 | 1975319 | yes |
| 19 | 39 | 975 | 975 | yes |
| 20 | 41 | 531975 | 531975 | yes |
| 21 | 43 | 1975319753197 | 1975319753197 | yes |
| 22 | 45 | 19753197531975 | 19753197531975 | yes |
| 23 | 47 | 75319753197531 | 75319753197531 | yes |
| 24 | 49 | 319753197531975319 | 319753197531975319 | yes |
| 25 | 51 | 753197531975319753 | 753197531975319753 | yes |

All 26 terms match, so the alternate “two more” reading was not needed.

## Capped conjecture check

For `n=0..3000` with `--max-len 2000`:

- 2,892 of 3,001 inputs found a witness.
- 24 inputs have `125 | m`; none found a witness, as expected.
- 85 inputs have `125 ∤ m` but no witness was found within 2,000 digits. These
  are violations of the requested capped assertion, not evidence that no
  longer witness exists.
- The longest witness found had 1,998 digits, at `n=2419`.
- Every input, including `n`, `m`, found status, witness length, and
  `125_divides_m`, is recorded in [n3000-results.csv](n3000-results.csv).

The 85 violating `n` values are:

```text
1324, 1480, 1493, 1564, 1626, 1685, 1693, 1745, 1746, 1858, 1879, 1948,
1980, 2064, 2105, 2130, 2134, 2135, 2142, 2179, 2186, 2189, 2214, 2219,
2259, 2284, 2303, 2304, 2323, 2325, 2335, 2368, 2381, 2407, 2408, 2414,
2442, 2458, 2466, 2478, 2480, 2490, 2504, 2524, 2556, 2559, 2596, 2600,
2605, 2629, 2630, 2634, 2639, 2673, 2674, 2678, 2679, 2699, 2715, 2726,
2731, 2738, 2745, 2750, 2751, 2767, 2781, 2814, 2818, 2819, 2824, 2826,
2853, 2855, 2863, 2876, 2880, 2890, 2906, 2909, 2910, 2922, 2965, 2972,
2983
```

## Proof identities and 125 scan

- Exact integer comparison of `X_(5k)` with
  `31975*(10**(5k)-1)//99999` for `k=1..40`: **pass** (40 checks).
- Random sample: 200 odd `m'` values coprime to 10, at most 1,000,000,
  generated with seed 62887. With a simple multiplicative-order loop capped
  at 100,000, 98 orders were computed and checked; 102 exceeded the cap and
  were skipped. All 98 modular `X_(5k) % m'` checks passed. No SymPy was
  installed. Modular geometric sums were used, so no large `X_(5k)` integers
  were built.
- Direct scan of 80,000 positive multiples of 125 through 10,000,000 found
  no admissible number: **pass**.

## Runtimes and conclusion

The final verification run took 4.809 seconds in total: n-range search
3.449 s, formula and random modular checks 1.324 s, and 125 scan 0.034 s. The
five unit tests completed in under one second.

The OEIS data reading and all 26 b-file comparisons are verified. The 40
formula checks, 98 completed random modular checks, and finite 125 scan passed.
The full `n<=3000` assertion is **not verified within the required 2,000-digit
cap**: 85 cases remain unresolved at that bound. The 102 order samples skipped
by the loop cap were not verified. These computations do not independently
establish the general proof in `PROOF.md`.

## Task record

- Owner: verification sub-agent.
- Outcome: source capture, verifier, unit tests, and per-n CSV are complete.
- Proof: see the commands, outputs, and limitations in this report.
- Remaining work: 85 cases have no witness within the cap; 102 order samples
  were skipped at the configured order cap.
- Next action: the proof owner can increase the search bound for additional
  witnesses or address the uncapped claim from the written argument.
- Unresolved decision: none for this bounded verification task.

## Round 2: exact order bound from the proof

Round 1 remains above as the record of the capped check and its limitations.
This section replaces its unresolved conclusion using the explicit bound in
Remark 1 of [PROOF.md](PROOF.md). No change was made to `PROOF.md`.

### Method

The new standard-library-only script [verify2.py](verify2.py) factors integers
by trial division. For every `n=0..3000`, it sets `m=2n+1`, strips all factors
of 5 to obtain `m'`, computes `φ(99999*m')` from its exact prime factorization,
then reduces that value by its prime factors until it has the exact order
`k=ord_(99999*m')(10)`. There is no order or digit cap. The prime table covers
the square root of the largest modulus used, including the 200 random checks.

For each of the 2,977 values with `125 ∤ m`, digit-wise modular Horner
evaluation checks `X_(5k) mod m` without constructing `X_(5k)` as a large
integer. A separate incremental residue scan tracks all five admissible
families for every length from 1 through `5k`. It stops at the first length
with a multiple; among hits at that length, the chosen witness has the
smallest leading digit, which is the smallest numeric value. The reported
units digit identifies that family. For the 24 values with `125 | m`, the
same scan checks every length through its order bound and finds no hit.

All five families were also scanned modulo 125 for every length 1 through
3,000; none has zero residue. The deterministic round 1 random sample was
repeated for all 200 odd `m'` values coprime to 10. Each exact order was
obtained by factorization and reduction, with no cap, and every
`X_(5k) mod m'` check passed.

The full per-n record, including exact `k`, `5k`, shortest witness length,
and units digit, is in [n3000-round2-results.csv](n3000-round2-results.csv).
The 85 entries which had no witness within 2,000 digits in round 1 are:

| n | m | k | bound 5k | smallest length | units digit |
|---:|---:|---:|---:|---:|---:|
| 1324 | 2649 | 2205 | 11025 | 2205 | 3 |
| 1480 | 2961 | 2070 | 10350 | 2070 | 3 |
| 1493 | 2987 | 2380 | 11900 | 2380 | 3 |
| 1564 | 3129 | 2220 | 11100 | 2220 | 3 |
| 1626 | 3253 | 2710 | 13550 | 2710 | 3 |
| 1685 | 3371 | 3370 | 16850 | 3370 | 3 |
| 1693 | 3387 | 2820 | 14100 | 2820 | 3 |
| 1745 | 3491 | 3490 | 17450 | 3490 | 3 |
| 1746 | 3493 | 2490 | 12450 | 2490 | 3 |
| 1858 | 3717 | 2610 | 13050 | 2610 | 3 |
| 1879 | 3759 | 2670 | 13350 | 2670 | 3 |
| 1948 | 3897 | 2160 | 10800 | 2160 | 3 |
| 1980 | 3961 | 2320 | 11600 | 2320 | 3 |
| 2064 | 4129 | 10320 | 51600 | 2829 | 5 |
| 2105 | 4211 | 4210 | 21050 | 4210 | 3 |
| 2130 | 4261 | 4260 | 21300 | 4260 | 3 |
| 2134 | 4269 | 2370 | 11850 | 2370 | 3 |
| 2135 | 4271 | 2135 | 10675 | 2135 | 3 |
| 2142 | 4285 | 4280 | 21400 | 2174 | 5 |
| 2179 | 4359 | 3630 | 18150 | 3630 | 3 |
| 2186 | 4373 | 5465 | 27325 | 2288 | 3 |
| 2189 | 4379 | 2100 | 10500 | 2100 | 3 |
| 2214 | 4429 | 3570 | 17850 | 3570 | 3 |
| 2219 | 4439 | 10560 | 52800 | 2228 | 1 |
| 2259 | 4519 | 3765 | 18825 | 3765 | 3 |
| 2284 | 4569 | 11415 | 57075 | 2523 | 1 |
| 2303 | 4607 | 21680 | 108400 | 2522 | 7 |
| 2304 | 4609 | 2090 | 10450 | 2090 | 3 |
| 2323 | 4647 | 7740 | 38700 | 3468 | 5 |
| 2325 | 4651 | 4650 | 23250 | 2216 | 3 |
| 2335 | 4671 | 5805 | 29025 | 2574 | 7 |
| 2368 | 4737 | 7890 | 39450 | 3064 | 9 |
| 2381 | 4763 | 2160 | 10800 | 2160 | 3 |
| 2407 | 4815 | 2385 | 11925 | 2385 | 5 |
| 2408 | 4817 | 24080 | 120400 | 2812 | 7 |
| 2414 | 4829 | 2190 | 10950 | 2190 | 3 |
| 2442 | 4885 | 4880 | 24400 | 2231 | 5 |
| 2458 | 4917 | 2220 | 11100 | 2220 | 3 |
| 2466 | 4933 | 12330 | 61650 | 2177 | 3 |
| 2478 | 4957 | 2065 | 10325 | 2065 | 3 |
| 2480 | 4961 | 4510 | 22550 | 2127 | 5 |
| 2490 | 4981 | 5840 | 29200 | 2658 | 3 |
| 2504 | 5009 | 3130 | 15650 | 3130 | 3 |
| 2524 | 5049 | 2160 | 10800 | 2160 | 3 |
| 2556 | 5113 | 8520 | 42600 | 2042 | 1 |
| 2559 | 5119 | 4265 | 21325 | 4265 | 3 |
| 2596 | 5193 | 2880 | 14400 | 2880 | 3 |
| 2600 | 5201 | 11130 | 55650 | 3710 | 1 |
| 2605 | 5211 | 8640 | 43200 | 2848 | 9 |
| 2629 | 5259 | 8760 | 43800 | 2218 | 9 |
| 2630 | 5261 | 5260 | 26300 | 5260 | 3 |
| 2634 | 5269 | 2390 | 11950 | 2390 | 3 |
| 2639 | 5279 | 13195 | 65975 | 2063 | 3 |
| 2673 | 5347 | 13365 | 66825 | 2974 | 1 |
| 2674 | 5349 | 8910 | 44550 | 2641 | 9 |
| 2678 | 5357 | 2430 | 12150 | 2430 | 3 |
| 2679 | 5359 | 12760 | 63800 | 2122 | 1 |
| 2699 | 5399 | 13495 | 67475 | 2481 | 9 |
| 2715 | 5431 | 2715 | 13575 | 2715 | 3 |
| 2726 | 5453 | 3690 | 18450 | 3690 | 3 |
| 2731 | 5463 | 9090 | 45450 | 3352 | 3 |
| 2738 | 5477 | 6845 | 34225 | 3313 | 5 |
| 2745 | 5491 | 12240 | 61200 | 2046 | 5 |
| 2750 | 5501 | 5500 | 27500 | 2748 | 9 |
| 2751 | 5503 | 27510 | 137550 | 2637 | 9 |
| 2767 | 5535 | 5535 | 27675 | 3767 | 5 |
| 2781 | 5563 | 13905 | 69525 | 2258 | 1 |
| 2814 | 5629 | 2160 | 10800 | 2160 | 3 |
| 2818 | 5637 | 4695 | 23475 | 4695 | 3 |
| 2819 | 5639 | 14095 | 70475 | 3023 | 7 |
| 2824 | 5649 | 4020 | 20100 | 4020 | 3 |
| 2826 | 5653 | 14130 | 70650 | 3302 | 7 |
| 2853 | 5707 | 2190 | 10950 | 2190 | 3 |
| 2855 | 5711 | 2855 | 14275 | 2855 | 3 |
| 2863 | 5727 | 13530 | 67650 | 2806 | 3 |
| 2876 | 5753 | 2610 | 13050 | 2610 | 3 |
| 2880 | 5761 | 4110 | 20550 | 4110 | 3 |
| 2890 | 5781 | 28290 | 141450 | 2103 | 1 |
| 2906 | 5813 | 14530 | 72650 | 2293 | 5 |
| 2909 | 5819 | 2530 | 12650 | 2530 | 3 |
| 2910 | 5821 | 5820 | 29100 | 2149 | 9 |
| 2922 | 5845 | 2490 | 12450 | 2490 | 5 |
| 2965 | 5931 | 29610 | 148050 | 2318 | 7 |
| 2972 | 5945 | 5740 | 28700 | 2056 | 5 |
| 2983 | 5967 | 2160 | 10800 | 2160 | 3 |

### Results and runtimes

- All 2,977 cases with `125 ∤ m` found a smallest witness no later than `5k`;
  no failures. The maximum smallest-witness length is 5,260 digits, at `n=2630`.
- All 24 cases with `125 | m` had no witness throughout their full `5k`
  scans. The independent five-family scan modulo 125 found no divisible
  admissible number of length at most 3,000.
- The exact-order random check verified all 200 samples. No order was skipped,
  and every `X_(5k) mod m'` remainder was zero.
- `python3 -m unittest -v test_verify.py`: 9 tests passed.
- `python3 -u verify2.py`: 7.187 s for exact order calculation and the
  all-n residue/Horner checks; 0.011 s for the 200 random checks; 7.214 s
  total, on the environment used for this run.

**Updated conclusion:** the full `n<=3000` assertion passes under the explicit
bound from Remark 1: every odd `m=2n+1` not divisible by 125 has an admissible
multiple within `5·ord_(99999*m')(10)` digits, and every tested `m` divisible
by 125 has none. This is computational verification over the stated finite
range, alongside the written general proof; it does not replace that proof.

### Round 2 task record

- Owner: verification sub-agent.
- Outcome: exact-order verifier, tests, full per-n CSV, and this report are
  complete; `PROOF.md` was not edited.
- Proof: `verify2.py` reported no failures; all 9 unit tests passed.
- Remaining work: none in the requested finite verification.
- Next action: none.
- Unresolved decision: none.
