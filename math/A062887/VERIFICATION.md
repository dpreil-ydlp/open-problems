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
