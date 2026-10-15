# Erdős problem #708: partial progress, 15 October 2026

**Status: OPEN. Nothing here resolves the problem.** This note (i) states the problem precisely from the primary sources, (ii) gives a complete proof, with the exact count, of the Erdős–Surányi lower bound whose details the 1992 paper leaves to the reader, (iii) records a reduction for the upper bound and the special cases it settles, and (iv) lists what was tried and failed. Author: Claude Fable 5.1, directed by Dovid Preil. Sources and brute force: SOURCES.md, STATEMENT.md, FINDINGS.md.

## 1. The problem

For a set A = {a_1 < ... < a_n} of integers with a_1 ≥ 2, write M = a_n. For x ≥ 0 let I_x = {x+1, ..., x+M}. Let h(A, x) be the least size of a set B ⊆ I_x with ∏_{a∈A} a | ∏_{b∈B} b, and g(n) = sup over all such A and all x ≥ 0 of h(A, x). (Erdős 1992, p. 34, and Erdős–Surányi 1959.) Known: g(2) = 2, g(3) = 4, and g(n) > (2−ε)n for n > n_0(ε). Asked: is g(n) < (2+ε)n for large n, or even g(n) ≤ 2n? Prize $100.

Remarks. (a) h(A, x) is finite: every a ≤ M has a multiple in I_x, so B = I_x works. (b) g is nondecreasing in n: if (A, x) is hard for n and M ≥ n+1, adjoin any a' ∈ [2, M] \ A; covering A ∪ {a'} is at least as hard. (c) B = A shows h(A, 0) ≤ n; the difficulty is entirely in the adversary's choice of x.

## 2. The lower bound, with the exact count

**Theorem 1.** Let p_1 < p_2 < ... < p_ℓ be primes with

    2 p_1² > p_ℓ² + 2 p_ℓ.                                            (H)

Put M = p_ℓ², A = {p_i p_j : 1 ≤ i ≤ j ≤ ℓ}, so n = |A| = ℓ(ℓ+1)/2 and max A = M. Then there is x ≥ 0 with

    h(A, x) = ℓ² − ℓ + 1 = 2n − 2ℓ + 1.

Consequently g(ℓ(ℓ+1)/2) ≥ ℓ² − ℓ + 1 whenever (H) is satisfiable for ℓ.

(H) is satisfiable for every ℓ ≥ 1: by the prime number theorem the number of primes in (y, 1.4y) tends to infinity, and 1.4² = 1.96 < 2 leaves room for the 2p_ℓ term. Explicit witnesses: ℓ = 2: (11, 13); ℓ = 3: (17, 19, 23); ℓ = 4: (37, 41, 43, 47). With monotonicity (Remark (b)) this gives g(n) ≥ 2n − 2√(2n) − O(1) for all n, hence g(n) > (2−ε)n for large n, which is (1) of Erdős 1992.

Proof. Each prime p_i divides exactly ℓ+1 elements of A counted with multiplicity (the ℓ−1 products p_i p_j with j ≠ i, and p_i² twice), so ∏A = (p_1 ⋯ p_ℓ)^{ℓ+1}. We must show: for a suitable x, every B ⊆ I_x with v_{p_i}(∏B) ≥ ℓ+1 for all i has |B| ≥ ℓ² − ℓ + 1, and some such B has exactly that size.

Choice of x. Let m = ⌊M/2⌋ and choose, by the Chinese remainder theorem (the moduli p_i³ are pairwise coprime), an integer c > m with

    c ≡ p_i + p_i²  (mod p_i³)   for every i = 1, ..., ℓ,

and put x = c − m ≥ 0, so c = x + m is the m-th element of I_x. Set s_i = c − p_i. Note s_i ≥ x + 1 since m > p_i.

Facts about I_x.

(F1) v_{p_i}(c) = 1 for every i: p_i | c and c ≡ p_i ≢ 0 (mod p_i²).

(F2) s_i is the unique multiple of p_i² in I_x, and v_{p_i}(s_i) = 2, and p_j ∤ s_i for j ≠ i. Indeed s_i = c − p_i ≡ p_i² (mod p_i³), so v_{p_i}(s_i) = 2. Any other multiple of p_i² in I_x would be s_i ± p_i²; s_i − p_i² < x + 1 because m − p_i − p_i² < 1 (as p_i² > m), and s_i + p_i² > x + M because m − p_i + p_i² > M, i.e. p_i² − p_i > M − m = ⌈M/2⌉, which follows from (H): p_i² − p_i ≥ p_1² − p_1 > (M + 2p_ℓ)/2 − p_1 ≥ ⌈M/2⌉. Finally p_j | c and p_j ∤ p_i give p_j ∤ s_i.

(F3) c is the unique element of I_x divisible by p_i p_j for any i < j. Any other would be c ± p_i p_j. Now p_i p_j ≥ p_1 p_2 ≥ p_1(p_1 + 2) = p_1² + 2p_1 > ⌈M/2⌉ + p_ℓ by (H), so c + p_i p_j > x + M, and c − p_i p_j < x + 1 since p_i p_j > m.

(F4) Every t ∈ I_x other than c and the s_i satisfies Σ_i v_{p_i}(t) ≤ 1: by (F3) t is divisible by at most one p_i, and by (F2) not by its square.

(F5) No element of I_x is divisible by p_i³, by (F2).

Counting. Let B ⊆ I_x satisfy v_{p_i}(∏B) ≥ ℓ+1 for all i. Write β = 1 if c ∈ B else 0, σ_i = 1 if s_i ∈ B else 0, and r_i = #{t ∈ B \ {c, s_1, ..., s_ℓ} : p_i | t}. By (F1), (F2), (F4), (F5), v_{p_i}(∏B) = β + 2σ_i + r_i, so r_i ≥ ℓ + 1 − β − 2σ_i. The sets counted by the r_i are pairwise disjoint by (F4), hence

    |B| ≥ β + Σ_i σ_i + Σ_i r_i ≥ β + Σ_i (σ_i + ℓ + 1 − β − 2σ_i) = β + ℓ(ℓ+1) − ℓβ − Σ_i σ_i ≥ ℓ(ℓ+1) − (ℓ−1)β − ℓ ≥ ℓ² − ℓ + 1,

using σ_i ≤ 1 and β ≤ 1. Equality is attained: take c, all s_i, and for each i a further ℓ − 2 multiples of p_i from I_x \ {c, s_i} (there are at least ⌊M/p_i⌋ − 2 ≥ p_ℓ − 2 ≥ ℓ − 2 of them, as ℓ ≤ π(p_ℓ) < p_ℓ). Then v_{p_i} = 1 + 2 + (ℓ−2) = ℓ+1 for every i and |B| = 1 + ℓ + ℓ(ℓ−2) = ℓ² − ℓ + 1. ∎

Predictions checked by exact integer programming (see VERIFICATION-LOWER.md when present): ℓ = 3 with (17, 19, 23) gives h = 7 at the constructed x; ℓ = 4 with (37, 41, 43, 47) gives h = 13.

Variant. Dropping the squares, A' = {p_i p_j : i < j}, n' = ℓ(ℓ−1)/2, the same interval gives h(A', x) ≥ ℓ² − 3ℓ + 1 = 2n' − 2ℓ + 1 by the identical count with ℓ−1 in place of ℓ+1. This recovers g(3) ≥ 4 from (7, 11, 13) only with a different interval (the 1959 one avoids a multiple of 13²); the point is that for n = 3 the squares-included construction yields only 3.

## 3. The upper bound: a reduction and what it settles

Fix A, x, and write I = I_x. For each a ∈ A choose a multiple m_a ∈ I (one exists since a ≤ M). Let B_1 = {m_a : a ∈ A} as a set, and for b ∈ B_1 let S_b = {a : m_a = b} (the elements that collided on b). Order each S_b as a_1, ..., a_k arbitrarily and set L_j = lcm(a_1, ..., a_j).

**Lemma 2 (telescoping deficit).** ∏_{a∈S_b} a = L_k · ∏_{j=2}^{k} gcd(a_j, L_{j−1}), and L_k | b. Hence ∏A divides ∏B_1 · ∏_{b∈B_1} ∏_{j=2}^{k_b} gcd(a_j^{(b)}, L_{j−1}^{(b)}).

Proof. L_j = L_{j−1} a_j / gcd(a_j, L_{j−1}); multiply out. L_k | b since each a_j | b. ∎

So after B_1 (at most n numbers) the remaining demand is a product of n − |B_1| gcds d_j = gcd(a_j, L_{j−1}), each a divisor of some a_j, and it suffices to find distinct new numbers in I \ B_1 whose product is divisible by every d_j.

**Corollary 3.** (i) If A is pairwise coprime, h(A, x) ≤ n. (ii) If the m_a can be chosen distinct, h(A, x) ≤ n. (iii) If every d_j has a multiple in I outside B_1 and these can be chosen distinct, h(A, x) ≤ 2n − |B_1| ≤ 2n − 1 when n ≥ 2. (iv) Any d_j ≤ M/(2n) has at least 2n multiples in I, so it never blocks.

Thus the whole difficulty is concentrated in gcds d_j > M/(2n) all of whose multiples in I have already been taken. Erdős's construction is exactly this: d = p_i p_j with the single multiple c.

## 4. What was tried for the upper bound and why it failed

1. Charging one repair number per collision (Lemma 2) fails when a large gcd has a unique multiple in I, already used. Splitting the gcd into prime-power pieces costs up to Ω(d_j) numbers, and Σ_a Ω(a) is not O(n).
2. Grouping prime powers of the total deficit into blocks of size ≤ M (at most 2n+1 blocks, since ∏A ≤ M^n) bounds the cost by O(n) per "round", but a block may again have only a used multiple; splitting blocks to size ≤ √M guarantees ≥ √M multiples, which exceeds the budget only when M > (3n+1)², and a prime power above √M cannot be split at all.
3. Induction removing the largest element needs the unique multiple m of M to be available; when the inductive set already uses m, the hypothesis is too weak to recover. Strengthening to a forbidden-point version is impossible, since forbidding the unique multiple of a prime M makes the instance infeasible.
4. Induction removing the smallest element keeps I fixed but the deficit a_1 / gcd(a_1, spare) may be a_1 itself with every multiple used.

A proof of g(n) ≤ Cn for any constant C would already be new; none is known to me and none is claimed here.
