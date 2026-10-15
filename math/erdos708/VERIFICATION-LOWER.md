# Erdős 708 lower-bound computational verification

## Method

`verify_lower.py` enumerates each requested interval with exact integer arithmetic. For each interval it keeps only integers divisible by at least one listed prime, then solves a binary minimum-cardinality model with one valuation-demand constraint per prime. Variables are binary; the objective is their sum. CBC ran single-threaded. All interval endpoints are inclusive. The random comparison uses Python `random.Random` with seed `7082026`.

Solver: PuLP 2.9.0 with CBC, one thread. Total measured runtime: 0.908 s.

## Theorem cases

### `(11, 13)` (ℓ = 2)

- (H): 242 > 195: **PASS**.
- `M = 169`; `|A| = 3`; `max(A) = 169` (M): **PASS**.
- Product identity: `prod(A) = 2924207` and `(prod p)^(ℓ+1) = 2924207`: **PASS**.
- CRT residues and least representative above `m = 84`: **PASS** (modulus `2924207`); `c = 2107105`, `x = 2107021`, `I = [2107022, 2107190]`.
- F1: v_pi(c) = 1 for every listed prime: **PASS**.
- F2: each s_i is the unique p_i² multiple, has valuation 2, and has no other listed prime divisor: **PASS**.
- F3: c is the unique p_i p_j multiple for every distinct pair: **PASS**.
- F4: every other interval element has valuation sum at most 1: **PASS**.
- F5: no interval element is divisible by any p_i³: **PASS**.
- Main IP: optimum **3**; prediction `ℓ² − ℓ + 1 = 3`; MATCH. Variables/constraints: 27/2; runtime: 0.079 s; solver status: Optimal.
  Optimal set: `[2107092, 2107094, 2107105]`. Valuation totals: `[3, 3]`.
- Easy interval `[M+1, 2M]`: optimum **3**; variables/constraints: 27/2; runtime: 0.023 s; status: Optimal.
  Optimal set: `[242, 286, 338]`. Valuation totals: `[3, 3]`.
- Squares-excluded `A'`: demand `ℓ−1 = 1` per prime; optimum **1**; stated lower bound `ℓ² − 3ℓ + 1 = -1`; variables/constraints: 27/2; runtime: 0.024 s; status: Optimal.
  Optimal set: `[2107105]`. Valuation totals: `[1, 1]`.

### `(17, 19, 23)` (ℓ = 3)

- (H): 578 > 575: **PASS**.
- `M = 529`; `|A| = 6`; `max(A) = 529` (M): **PASS**.
- Product identity: `prod(A) = 3045940625581681` and `(prod p)^(ℓ+1) = 3045940625581681`: **PASS**.
- CRT residues and least representative above `m = 264`: **PASS** (modulus `410006814589`); `c = 339391420859`, `x = 339391420595`, `I = [339391420596, 339391421124]`.
- F1: v_pi(c) = 1 for every listed prime: **PASS**.
- F2: each s_i is the unique p_i² multiple, has valuation 2, and has no other listed prime divisor: **PASS**.
- F3: c is the unique p_i p_j multiple for every distinct pair: **PASS**.
- F4: every other interval element has valuation sum at most 1: **PASS**.
- F5: no interval element is divisible by any p_i³: **PASS**.
- Main IP: optimum **7**; prediction `ℓ² − ℓ + 1 = 7`; MATCH. Variables/constraints: 79/3; runtime: 0.023 s; solver status: Optimal.
  Optimal set: `[339391420655, 339391420790, 339391420836, 339391420840, 339391420842, 339391420859, 339391421049]`. Valuation totals: `[4, 4, 4]`.
- Easy interval `[M+1, 2M]`: optimum **6**; variables/constraints: 78/3; runtime: 0.024 s; status: Optimal.
  Optimal set: `[722, 782, 867, 874, 969, 1058]`. Valuation totals: `[4, 4, 4]`.
- Squares-excluded `A'`: demand `ℓ−1 = 2` per prime; optimum **3**; stated lower bound `ℓ² − 3ℓ + 1 = 1`; variables/constraints: 79/3; runtime: 0.036 s; status: Optimal.
  Optimal set: `[339391420836, 339391420840, 339391420842]`. Valuation totals: `[2, 2, 2]`.

### `(37, 41, 43, 47)` (ℓ = 4)

- (H): 2738 > 2303: **PASS**.
- `M = 2209`; `|A| = 10`; `max(A) = 2209` (M): **PASS**.
- Product identity: `prod(A) = 270869104221361876319220626221057` and `(prod p)^(ℓ+1) = 270869104221361876319220626221057`: **PASS**.
- CRT residues and least representative above `m = 1104`: **PASS** (modulus `28817458931362977793`); `c = 7854246017435041287`, `x = 7854246017435040183`, `I = [7854246017435040184, 7854246017435042392]`.
- F1: v_pi(c) = 1 for every listed prime: **PASS**.
- F2: each s_i is the unique p_i² multiple, has valuation 2, and has no other listed prime divisor: **PASS**.
- F3: c is the unique p_i p_j multiple for every distinct pair: **PASS**.
- F4: every other interval element has valuation sum at most 1: **PASS**.
- F5: no interval element is divisible by any p_i³: **PASS**.
- Main IP: optimum **13**; prediction `ℓ² − ℓ + 1 = 13`; MATCH. Variables/constraints: 207/4; runtime: 0.029 s; solver status: Optimal.
  Optimal set: `[7854246017435040212, 7854246017435040325, 7854246017435040384, 7854246017435040723, 7854246017435040754, 7854246017435040770, 7854246017435041240, 7854246017435041244, 7854246017435041246, 7854246017435041250, 7854246017435041287, 7854246017435042212, 7854246017435042230]`. Valuation totals: `[5, 5, 5, 5]`.
- Easy interval `[M+1, 2M]`: optimum **10**; variables/constraints: 206/4; runtime: 0.029 s; status: Optimal.
  Optimal set: `[3034, 3182, 3362, 3478, 3526, 3698, 3854, 4042, 4107, 4418]`. Valuation totals: `[5, 5, 5, 5]`.
- Squares-excluded `A'`: demand `ℓ−1 = 3` per prime; optimum **5**; stated lower bound `ℓ² − 3ℓ + 1 = 5`; variables/constraints: 207/4; runtime: 0.025 s; status: Optimal.
  Optimal set: `[7854246017435041240, 7854246017435041244, 7854246017435041246, 7854246017435041250, 7854246017435041287]`. Valuation totals: `[3, 3, 3, 3]`.

## Random interval comparison for `(17, 19, 23)`

Twenty independently selected x values in `[0, 1,000,000]` (seed `7082026`) gave optima from **5** to **6**. The constructed interval optimum is **7**. Each random solve had 77–79 variables, 3 constraints, and an optimal CBC status.

| x | optimum | variables | runtime (s) |
|---:|---:|---:|---:|
| 798621 | 6 | 78 | 0.023 |
| 741972 | 6 | 78 | 0.041 |
| 893153 | 6 | 77 | 0.026 |
| 899960 | 6 | 78 | 0.029 |
| 948996 | 6 | 79 | 0.026 |
| 482533 | 6 | 79 | 0.031 |
| 842018 | 6 | 77 | 0.029 |
| 548010 | 6 | 79 | 0.024 |
| 660754 | 6 | 79 | 0.027 |
| 102350 | 6 | 77 | 0.026 |
| 838223 | 6 | 77 | 0.026 |
| 70970 | 6 | 78 | 0.033 |
| 277632 | 6 | 78 | 0.026 |
| 37153 | 6 | 79 | 0.032 |
| 98640 | 6 | 78 | 0.026 |
| 592510 | 5 | 77 | 0.026 |
| 115101 | 6 | 79 | 0.036 |
| 644180 | 6 | 79 | 0.028 |
| 345739 | 6 | 78 | 0.027 |
| 123889 | 6 | 77 | 0.027 |

## Conclusion

All direct checks F1–F5 pass for all three tuples, and each main IP optimum matches `ℓ² − ℓ + 1` (3, 7, 13). Theorem 1's exact count is therefore computationally confirmed for these three cases.
