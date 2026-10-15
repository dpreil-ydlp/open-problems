# Erdős problem 708: adversarial search results

**Conclusion:** No instance exceeded `2n`. The maximum ratio observed is `h/n = 1.333` at `A={77,91,143}`, `x=5934` (`h=4`, `n=3`). The maximum observed value of `h − (2n − 2√(2n))` is `2.898979` at the same validation case. The search-only maximum of that adjusted value is `1.898979` at n=3, h=3.

Owner: Codex research sub-agent. Search budget: 75 minutes, cutoff 2026-10-15 21:16:39 UTC. The final in-progress CBC solve returned at 21:16:52 UTC (13 seconds after cutoff); it used 69 unique ILP solves and its best result was saved. The runner started no new A after the cutoff. All completed per-A records, including four validation benchmarks, are in [`search.jsonl`](search.jsonl).

## Exact evaluator and adversary

For each A, factor `prod(A)` and keep the primes p with positive demand `e_p`. For every eligible `t` in `[x+1,x+M]` divisible by at least one such p, create binary `y_t`. The PuLP/CBC model minimizes `sum(y_t)` subject to `sum(y_t v_p(t)) >= e_p` for every p. This is the exact minimum h(A,x), with a single valuation constraint per relevant prime.

The x search used the period `N = product_p p^(floor(log_p M)+1)`, without enumerating x. CRT hubs place a number c near the interval center with exact prescribed p-adic valuations, either for all primes in `lcm(A)` or selected subsets. Coordinate hill-climbing then changed one residue `x mod p^(floor(log_p M)+1)` at a time, accepted nondecreasing h, and used restarts. Each A had a target budget of about 200 distinct ILP solves; small residue spaces used fewer unique solves, and the last A stopped at 69 because the wall-clock budget expired.

Environment: Python 3.13.2, PuLP 2.9.0, bundled CBC, one thread, one search process, launched with `nice -n 10`. The 85 search records used 16,777 distinct ILP solves and sum to 72.1 minutes of per-A runtime. This sum does not include Python setup or time between A records.

## Validation checks

All four exact checks passed. For `(77,91,143)` at `x=5934`, the evaluator returned h=4 and selected `[5978,6006,6039,6045]`, with exponent totals `{'7': 3, '11': 2, '13': 2}`. The three constructed lower-bound cases returned the expected h values 3, 7, and 13.

| Check | A | n | M | x | I=[x+1,x+M] | h | Selected exponent totals |
|---|---|---:|---:|---:|---|---:|---|
| exact_example_77_91_143 | `{77,91,143}` | 3 | 143 | 5934 | `[5935,6077]` | 4 | `{'7': 3, '11': 2, '13': 2}` |
| lower_l2 | `{121,143,169}` | 3 | 169 | 2107021 | `[2107022,2107190]` | 3 | `{'11': 3, '13': 3}` |
| lower_l3 | `{289,323,391,361,437,529}` | 6 | 529 | 339391420595 | `[339391420596,339391421124]` | 7 | `{'17': 4, '19': 4, '23': 4}` |
| lower_l4 | `{1369,1517,1591,1739,1681,1763,1927,1849,2021,2209}` | 10 | 2209 | 7854246017435040183 | `[7854246017435040184,7854246017435042392]` | 13 | `{'37': 5, '41': 5, '43': 5, '47': 5}` |

The selected sets and per-prime exponent totals are stored in the validation rows of `search.jsonl`. No candidate had `h>2n`, so no counterexample required a second independent verification.

## Search coverage

| Family | Completed A |
|---|---:|
| Pairwise products, ℓ=3/4, with/without squares | 16 |
| Triple products, 4/5 primes | 5 |
| Mixed 2- and 3-prime products | 7 |
| Divisors of L=360,720,840 (M≤400) | 42 |
| Prime-power sets | 3 |
| Random upper-half sets | 9 |
| Exhaustive A⊂[2,30], |A|=4 | 3 |

The n=4 exhaustive family contains `C(29,4)=23,751` sets; 3 were searched before the deadline. The requested random families had 30 generated samples per M, of which 3 (M=60), 3 (M=120), and 3 (M=240) completed. Structured families were interleaved. The ℓ=4 square-included family has n=10, as required by that construction; other generated cases were in n=3…8 or n=10 for the listed 10-element structures.

## Top 20 by h−2n

| # | Family | A | n | M | x | h | 2n | h−2n | h/n |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | validation / exact_example_77_91_143 | `{77,91,143}` | 3 | 143 | 5934 | 4 | 6 | -2 | 1.333 |
| 2 | pairwise_l3_nosq | `{6,10,15}` | 3 | 15 | 6123 | 3 | 6 | -3 | 1.000 |
| 3 | pairwise_l3_nosq | `{6,14,21}` | 3 | 21 | 6392 | 3 | 6 | -3 | 1.000 |
| 4 | random_M240_sample2 | `{136,176,206}` | 3 | 206 | 48871323817 | 3 | 6 | -3 | 1.000 |
| 5 | pairwise_l3_nosq | `{6,22,33}` | 3 | 33 | 16754 | 3 | 6 | -3 | 1.000 |
| 6 | random_M240_sample3 | `{186,195,209}` | 3 | 209 | 10030034891640917401 | 3 | 6 | -3 | 1.000 |
| 7 | pairwise_l3_nosq | `{6,26,39}` | 3 | 39 | 352614 | 3 | 6 | -3 | 1.000 |
| 8 | divisors_360_M90 | `{60,72,90}` | 3 | 90 | 47835 | 3 | 6 | -3 | 1.000 |
| 9 | divisors_360_M120 | `{72,90,120}` | 3 | 120 | 47820 | 3 | 6 | -3 | 1.000 |
| 10 | divisors_360_M180 | `{2,120,180}` | 3 | 180 | 8207806 | 3 | 6 | -3 | 1.000 |
| 11 | divisors_720_M180 | `{120,144,180}` | 3 | 180 | 5636790 | 3 | 6 | -3 | 1.000 |
| 12 | divisors_720_M240 | `{144,180,240}` | 3 | 240 | 5636760 | 3 | 6 | -3 | 1.000 |
| 13 | divisors_840_M280 | `{168,210,280}` | 3 | 280 | 4567631740 | 3 | 6 | -3 | 1.000 |
| 14 | divisors_360_M180 | `{3,120,180}` | 3 | 180 | 38820609 | 3 | 6 | -3 | 1.000 |
| 15 | validation / lower_l2 | `{121,143,169}` | 3 | 169 | 2107021 | 3 | 6 | -3 | 1.000 |
| 16 | triples_4p | `{30,42,70,105}` | 4 | 105 | 654405391 | 4 | 8 | -4 | 1.000 |
| 17 | exhaustive_[2,30]_n4 | `{2,3,4,5}` | 4 | 5 | 600 | 4 | 8 | -4 | 1.000 |
| 18 | triples_4p | `{30,66,110,165}` | 4 | 165 | 7902977070 | 4 | 8 | -4 | 1.000 |
| 19 | exhaustive_[2,30]_n4 | `{2,3,4,6}` | 4 | 6 | 9 | 4 | 8 | -4 | 1.000 |
| 20 | triples_4p | `{30,78,130,195}` | 4 | 195 | 52688589538 | 4 | 8 | -4 | 1.000 |

## Top 20 by h/n

| # | Family | A | n | M | x | h | 2n | h−2n | h/n |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | validation / exact_example_77_91_143 | `{77,91,143}` | 3 | 143 | 5934 | 4 | 6 | -2 | 1.333 |
| 2 | validation / lower_l4 | `{1369,1517,1591,1739,1681,1763,1927,1849,2021,2209}` | 10 | 2209 | 7854246017435040183 | 13 | 20 | -7 | 1.300 |
| 3 | validation / lower_l3 | `{289,323,391,361,437,529}` | 6 | 529 | 339391420595 | 7 | 12 | -5 | 1.167 |
| 4 | pairwise_l3_nosq | `{6,10,15}` | 3 | 15 | 6123 | 3 | 6 | -3 | 1.000 |
| 5 | pairwise_l3_nosq | `{6,14,21}` | 3 | 21 | 6392 | 3 | 6 | -3 | 1.000 |
| 6 | random_M240_sample2 | `{136,176,206}` | 3 | 206 | 48871323817 | 3 | 6 | -3 | 1.000 |
| 7 | pairwise_l3_nosq | `{6,22,33}` | 3 | 33 | 16754 | 3 | 6 | -3 | 1.000 |
| 8 | random_M240_sample3 | `{186,195,209}` | 3 | 209 | 10030034891640917401 | 3 | 6 | -3 | 1.000 |
| 9 | pairwise_l3_nosq | `{6,26,39}` | 3 | 39 | 352614 | 3 | 6 | -3 | 1.000 |
| 10 | divisors_360_M90 | `{60,72,90}` | 3 | 90 | 47835 | 3 | 6 | -3 | 1.000 |
| 11 | divisors_360_M120 | `{72,90,120}` | 3 | 120 | 47820 | 3 | 6 | -3 | 1.000 |
| 12 | divisors_360_M180 | `{2,120,180}` | 3 | 180 | 8207806 | 3 | 6 | -3 | 1.000 |
| 13 | divisors_720_M180 | `{120,144,180}` | 3 | 180 | 5636790 | 3 | 6 | -3 | 1.000 |
| 14 | divisors_720_M240 | `{144,180,240}` | 3 | 240 | 5636760 | 3 | 6 | -3 | 1.000 |
| 15 | divisors_840_M280 | `{168,210,280}` | 3 | 280 | 4567631740 | 3 | 6 | -3 | 1.000 |
| 16 | divisors_360_M180 | `{3,120,180}` | 3 | 180 | 38820609 | 3 | 6 | -3 | 1.000 |
| 17 | validation / lower_l2 | `{121,143,169}` | 3 | 169 | 2107021 | 3 | 6 | -3 | 1.000 |
| 18 | triples_4p | `{30,42,70,105}` | 4 | 105 | 654405391 | 4 | 8 | -4 | 1.000 |
| 19 | exhaustive_[2,30]_n4 | `{2,3,4,5}` | 4 | 5 | 600 | 4 | 8 | -4 | 1.000 |
| 20 | triples_4p | `{30,66,110,165}` | 4 | 165 | 7902977070 | 4 | 8 | -4 | 1.000 |

## Limits and next action

The result is a bounded search, not a proof of `g(n)≤2n`. In particular, the full n=4 exhaustive family and all 30 random samples per M were not completed. The exact next step is to resume the round-robin A stream with the saved ledger, then prioritize the remaining 23,748 n=4 sets and random samples. No claim is made that the best x was found for any A beyond the hill-climb budget.
