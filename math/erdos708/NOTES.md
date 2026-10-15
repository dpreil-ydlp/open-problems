# Erdős problem #708: partial progress, 15 October 2026

**Status: OPEN. Nothing here resolves the problem in general.** Prior work (Section 1A): Haoyu Chen's 2026 manuscript claims g(n) ≤ 12n for all n; Section 3A rediscovers one of his intermediate inequalities. Proved here (both rediscoveries of results in Chen's manuscript): the bound 2n − 1 for all sets whose elements have at most two distinct prime factors (Theorem A) and the bound 2n for every set with max(A) > (2n+1)³ (Theorem C). Original text continued: the question has an affirmative answer, with the bound 2n − 1, for all sets whose elements have at most two distinct prime factors, which includes Erdős's extremal family (Theorem A), and for every set with max(A) > (2n+1)³ (Theorem C). A counterexample to g(n) ≤ 2n must have max(A) ≤ (2n+1)³ and an element with three or more distinct prime factors. This note (i) states the problem precisely from the primary sources, (ii) gives a complete proof, with the exact count, of the Erdős–Surányi lower bound whose details the 1992 paper leaves to the reader, (iii) records a reduction for the upper bound and the special cases it settles, and (iv) lists what was tried and failed. Author: Claude Fable 5.1, directed by Dovid Preil. Sources and brute force: SOURCES.md, STATEMENT.md, FINDINGS.md.

## 1. The problem

For a set A = {a_1 < ... < a_n} of integers with a_1 ≥ 2, write M = a_n. For x ≥ 0 let I_x = {x+1, ..., x+M}. Let h(A, x) be the least size of a set B ⊆ I_x with ∏_{a∈A} a | ∏_{b∈B} b, and g(n) = sup over all such A and all x ≥ 0 of h(A, x). (Erdős 1992, p. 34, and Erdős–Surányi 1959.) Known: g(2) = 2, g(3) = 4, and g(n) > (2−ε)n for n > n_0(ε). Asked: is g(n) < (2+ε)n for large n, or even g(n) ≤ 2n? Prize $100.

Remarks. (a) h(A, x) is finite: every a ≤ M has a multiple in I_x, so B = I_x works. (b) g is nondecreasing in n: if (A, x) is hard for n and M ≥ n+2, adjoin any a' ∈ [2, M] \ A (such a' exists since |[2,M]| = M−1 ≥ n+1 > n); covering A ∪ {a'} is at least as hard. (c) B = A shows h(A, 0) ≤ n; the difficulty is entirely in the adversary's choice of x.

## 1A. Prior work found on 15 October 2026 (after Sections 3A and 3B were written)

- Haoyu Chen, *Explicit upper bounds for the Erdős–Surányi function g(n)*, public manuscript and Lean 4 development, https://github.com/chy4pro/erdos-708-explicit-upper-bounds (commit 8b9c1c1, 8 Sep 2026; proof claim submitted to erdosproblems.com on 5 Sep 2026, listed there as "Claimed / Partial", unreviewed by the site). It claims g(n) ≤ 12n for all n (kernel-verified in Lean according to the author), an 11n bound "refereed, not formalised", and, per the site summary, the 2n bound for max(A) ≥ 8n³ as a conjecture.
- Chen's collision–cycle proof contains, as an intermediate inequality, exactly the group bound of Theorem B below (δ_p(S) ≤ Σ_C (r_{C,p}(1) − 1)^+ and Σ_p δ_p(S) ≤ Σ_C (Σ_{a∈C} ω(a) − |P(C)|), with h(A,x) ≤ |S| + Σ_p δ_p(S)), and his main.tex states the two-prime-factor case and the "a counterexample needs three prime factors" remark. **Sections 3A (Theorems A, B, Corollary 5) are therefore an independent rediscovery, not new results.** They were written on 15 Oct 2026 without knowledge of Chen's work and are kept here as a self-contained exposition.
- Chen's Theorem 1.3 (main.tex lines 124–129, proof in his Section 5, lines 393–439, commit dc150fd of 12 Oct 2026) proves h(A,x) ≤ 2n whenever max(A) ≥ 8n³, by the same method as Section 3B (split components, assign large prime powers by prime, fresh multiples for small groups). Since (2n+1)³ > 8n³, **Theorem C below is an independent proof of a weaker form of Chen's Theorem 1.3, not a new result.** The earlier statement in this file that the site lists this bound as a conjecture was wrong; it is a theorem with a written proof. Referee report: REVIEW-SOL-THEOREM-C.md (correct with minor fixes; 552 exact solves, 1,104 constructions, 59,998 splitting cases, no violation).
- Independent referee report on 3A: REVIEW-SOL-THEOREM-A.md (mathematics correct; 300 random instances, 3,517 exact ILP solves, no violation; blocked on novelty only).

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

## 3A. Upper bounds by hub-and-fill (independent rediscovery of an inequality in Chen's manuscript; see 1A)

Notation. For a prime p and v ≥ 1 put D(p,v) = #{a ∈ A : p^v | a} and N(p,v) = #{b ∈ I : p^v | b}. Since the elements of A divisible by p^v are distinct multiples of p^v in [1, M],

    D(p,v) ≤ ⌊M/p^v⌋ ≤ N(p,v)   for every prime power p^v.            (S)

ω(m) denotes the number of distinct primes dividing m, and for a set S of integers P(S) is the set of primes dividing at least one element of S.

**Lemma 3 (slot criterion).** If B ⊆ I satisfies |B ∩ p^vℤ| ≥ D(p,v) for every prime power p^v, then ∏A | ∏B.

Proof. For each prime p, Σ_{b∈B} v_p(b) = Σ_{v≥1} |B ∩ p^vℤ| ≥ Σ_{v≥1} D(p,v) = Σ_{a∈A} v_p(a). ∎

**Construction.** For each a ∈ A choose μ(a) ∈ I with a | μ(a) (exists since a ≤ M = |I|). Let C = μ(A) be the set of hubs, H = |C|, and for c ∈ C let S_c = μ^{-1}(c) (the group of c), so the S_c partition A. For a prime p and v ≥ 1 put K(p,v) = |C ∩ p^vℤ|.

For each prime p, let F_p ⊆ I \ C be a set of non-hub multiples of p with

    |F_p ∩ p^vℤ| ≥ (D(p,v) − K(p,v))^+   for every v ≥ 1,              (F)

of size f_p := max_{v≥1} (D(p,v) − K(p,v))^+. (Only primes dividing ∏A need be considered; for every other prime, and whenever f_p = 0, take F_p = ∅.) Such F_p exists. Put r(v) = max_{w≥v} (D(p,w) − K(p,w))^+, which is nonincreasing in v with r(1) = f_p and r(v) ≥ (D(p,v) − K(p,v))^+. Availability: for w ≥ v, N(p,v) − N(p,w) counts the multiples of p^v in I that are not multiples of p^w, and K(p,v) − K(p,w) counts the hubs among them, so N(p,v) − K(p,v) ≥ N(p,w) − K(p,w) ≥ D(p,w) − K(p,w) by (S); hence the number of non-hub multiples of p^v in I is at least r(v). Now build F_p from the top: let v_max be the largest v with r(v) > 0; choose r(v_max) non-hub multiples of p^{v_max}; then for v = v_max − 1, ..., 1 add non-hub multiples of p^v until F_p contains r(v) multiples of p^v (those chosen at higher levels already count, and enough non-hub multiples of p^v are available). The result satisfies |F_p ∩ p^vℤ| ≥ r(v) ≥ (D(p,v) − K(p,v))^+ for all v and |F_p| = r(1) = f_p.

Put B = C ∪ ⋃_p F_p. For every p^v, |B ∩ p^vℤ| ≥ K(p,v) + (D(p,v) − K(p,v))^+ ≥ D(p,v), so ∏A | ∏B by Lemma 3, and

    |B| ≤ H + Σ_p f_p.                                                    (1)

**Lemma 4.** For every prime p, f_p ≤ Σ_{c∈C} (n_c(p) − 1)^+, where n_c(p) = #{a ∈ S_c : p | a}.

Proof. Let G(p,v) = #{c ∈ C : some a ∈ S_c has p^v | a}. If a ∈ S_c and p^v | a then p^v | μ(a) = c, so G(p,v) ≤ K(p,v). Writing n_c(p,v) = #{a ∈ S_c : p^v | a},

    D(p,v) − K(p,v) ≤ D(p,v) − G(p,v) = Σ_c ( n_c(p,v) − [n_c(p,v) ≥ 1] ) = Σ_c (n_c(p,v) − 1)^+ ≤ Σ_c (n_c(p,1) − 1)^+,

the last step because n_c(p,v) is nonincreasing in v. Take the maximum over v. ∎

**Theorem B (general upper bound).** For every A and x,

    h(A, x) ≤ Σ_{c∈C} ( 1 + Σ_{a∈S_c} ω(a) − |P(S_c)| ).

Proof. By (1) and Lemma 4, |B| ≤ H + Σ_c Σ_p (n_c(p) − 1)^+. For fixed c, Σ_p n_c(p) = Σ_{a∈S_c} ω(a) and Σ_p [n_c(p) ≥ 1] = |P(S_c)|. ∎

**Theorem A (the case of at most two prime factors).** If ω(a) ≤ 2 for every a ∈ A, then h(A, x) ≤ 2n − H ≤ 2n − 1 for every x ≥ 0.

Proof. Fix a group S_c. If some a ∈ S_c has ω(a) = 2 then |P(S_c)| ≥ 2, so the group's term in Theorem B is at most 1 + 2|S_c| − 2 = 2|S_c| − 1. Otherwise every element of S_c is a prime power, Σ_{a∈S_c} ω(a) = |S_c| and |P(S_c)| ≥ 1, so the term is at most |S_c| ≤ 2|S_c| − 1. Summing over the H groups gives h(A,x) ≤ 2n − H. ∎

**Corollary 5.** (i) Erdős's question "g(n) ≤ 2n?" has an affirmative answer for all sets whose elements have at most two distinct prime factors; in that class the truth lies between 2n − 2ℓ + 1 (Theorem 1, n = ℓ(ℓ+1)/2) and 2n − 1. (ii) Any pair (A, x) with h(A, x) > 2n must contain an element with at least three distinct prime factors. (iii) For general A, h(A,x) ≤ Σ_a ω(a) − Σ_c (|P(S_c)| − 1), which improves the trivial bound Σ_a ω(a) by the number of "extra" primes absorbed by hubs.

Remark. The bound of Theorem B is tight for the Erdős instance up to the hub's own contribution: there every group term is 1 + 2|S_c| − ℓ_c. The method fails to give 2n once elements have three or more prime factors because the fill is done one prime at a time; a group of ω = 3 elements on few primes has Σ ω − |P| ≈ 3|S_c|. Reaching 2n in general requires fill numbers that carry two or more demanded primes at once; such numbers exist (for an element with components q_1 q_2 q_3 ⋯ there are at least q_3 ≥ 2 multiples of q_1 q_2 in I) but their availability after the hubs are removed is exactly the unresolved point.

## 3B. The sparse regime: Theorem C (independent proof of a weaker form of Chen's Theorem 1.3; see 1A)

Throughout this section put T = M/(2n+1) (a real number) and assume

    M > (2n+1)³,  equivalently  T > (2n+1)².                              (R)

Call a prime-power component q = p^v of an element a (meaning p^v ∥ a) *big* if q > T.

**Lemma C1.** Under (R) every element of A has at most one big component. Proof: two coprime components both > T would multiply to more than T² = M · M/(2n+1)² > M(2n+1) > M ≥ a. ∎

**Lemma C2 (fresh numbers).** If Q ≤ T then I contains at least 2n+1 multiples of Q, since ⌊M/Q⌋ ≥ ⌊2n+1⌋. In particular, whenever fewer than 2n+1 numbers have been selected, some multiple of Q in I is still unselected. ∎

**Lemma C3 (splitting).** Under (R), let a ≤ M have no big component and a > T. Then the prime-power components of a can be partitioned into two nonempty groups with products Q_1 ≤ T and Q_2 ≤ T.

Proof. Let q_1 ≤ q_2 ≤ ... ≤ q_r be the components (r ≥ 2 since a > T ≥ every component) and P^{(k)} = q_1 ⋯ q_k.

Case (i): some component q_j > T²/a. Then Q_1 = q_j ≤ T (not big) and Q_2 = a/q_j < a²/T² ≤ M²/T² = (2n+1)² < T by (R).

Case (ii): every component is ≤ T²/a. Since P^{(0)} = 1 < a/T (as a > T) and P^{(r)} = a ≥ a/T, let k ≥ 1 be minimal with P^{(k)} ≥ a/T. Then P^{(k)} = P^{(k−1)} q_k < (a/T)(T²/a) = T, so Q_1 = P^{(k)} ∈ [a/T, T) and Q_2 = a/Q_1 ≤ T. If k = r then Q_1 = a < T, contradicting a > T; so both groups are nonempty. ∎

(The hypothesis (R) is used only in Case (i). Some condition of the shape M ≥ (2n+1)² is necessary for any such splitting, since Q_1 Q_2 = a can be as large as M while Q_1, Q_2 ≤ T forces M ≤ T².)

**Theorem C.** If M > (2n+1)³ then h(A, x) ≤ 2n for every x ≥ 0.

Proof. We build B ⊆ I with |B| ≤ 2n satisfying the slot criterion of Lemma 3, i.e. |B ∩ p^vℤ| ≥ D(p,v) for all prime powers. We will in fact exhibit, for each prime p, an injective map a ↦ h(a,p) from {a ∈ A : p | a} into B with p^{v_p(a)} | h(a,p); this gives |B ∩ p^vℤ| ≥ #{a : v_p(a) ≥ v} = D(p,v).

Phase 1 (big components). For each element a with a big component p^v (at most one by Lemma C1) call (a, p, v) a big token. For each prime p, host the big tokens at p on pairwise distinct multiples of the respective p^v in I: process them in decreasing order of v; when a token with exponent v is processed, the number of tokens at p with exponent ≥ v already hosted is less than #{a : p^v | a} = D(p,v) ≤ N(p,v), so an unused multiple of p^v in I exists. Let B_1 be the set of all hosts so chosen (hosts for different primes may coincide). Set h(a,p) := the host of a's big token. |B_1| ≤ n_big := number of elements with a big component.

Phase 2 (fresh groups). For each element a let a* = a divided by its big component (a* = a if there is none). If a* = 1 there is nothing to do. If a* ≤ T, form the single group Q_1 = a*. Otherwise a* > T; a* has no big component and a* ≤ M, so Lemma C3 splits its components into two groups Q_1, Q_2 ≤ T. Note that if a has a big component q then a* = a/q < M/T = 2n+1 ≤ T, so this case always yields a single group. Now go through all groups of all elements in any order; for each group Q select a multiple of Q in I that has not been selected before (Phase 1 hosts count as selected). This is possible by Lemma C2 because at most 2n numbers are selected in total: elements with a big component contribute at most 1 + 1, elements without contribute at most 2. For every prime p dividing Q set h(a,p) := the selected multiple of Q.

Let B = B_1 ∪ {all selected group multiples}. Then |B| ≤ 2n.

Injectivity. Fix a prime p. If a has p in its big component, h(a,p) ∈ B_1 and the Phase 1 hosts at p are pairwise distinct. If p lies in a group of a, h(a,p) is a Phase 2 number, which was selected fresh, hence differs from every Phase 1 host and from every other Phase 2 number; and a Phase 2 number hosts components of a single element only. So a ↦ h(a,p) is injective on {a : p | a}, and p^{v_p(a)} | h(a,p) in both cases. By Lemma 3, ∏A | ∏B. ∎

**Corollary 6.** Erdős's question "g(n) ≤ 2n?" has an affirmative answer whenever max(A) > (2n+1)³. Combined with Theorem A, a counterexample to g(n) ≤ 2n, if one exists, must satisfy M ≤ (2n+1)³ and contain an element with at least three distinct prime factors.

Remark. The constant 3 in the exponent comes only from Case (i) of Lemma C3; the method cannot go below exponent 2 because of the trivial obstruction M ≤ T². The dense regime M ≤ (2n+1)³ is where Erdős's own construction lives (there n ≍ M/(log M)²), and it is exactly the regime where fresh multiples of two-component groups need not exist. Closing it requires hosting groups on numbers that already carry other elements' tokens, which is the unresolved point.

## 4. What was tried for the upper bound and why it failed

1. Charging one repair number per collision (Lemma 2) fails when a large gcd has a unique multiple in I, already used. Splitting the gcd into prime-power pieces costs up to Ω(d_j) numbers, and Σ_a Ω(a) is not O(n).
2. Grouping prime powers of the total deficit into blocks of size ≤ M (at most 2n+1 blocks, since ∏A ≤ M^n) bounds the cost by O(n) per "round", but a block may again have only a used multiple; splitting blocks to size ≤ √M guarantees ≥ √M multiples, which exceeds the budget only when M > (3n+1)², and a prime power above √M cannot be split at all.
3. Induction removing the largest element needs the unique multiple m of M to be available; when the inductive set already uses m, the hypothesis is too weak to recover. Strengthening to a forbidden-point version is impossible, since forbidding the unique multiple of a prime M makes the instance infeasible.
4. Induction removing the smallest element keeps I fixed but the deficit a_1 / gcd(a_1, spare) may be a_1 itself with every multiple used.

At the time these routes were tried I believed no linear bound was known. Section 1A records that Chen's 2026 manuscript claims g(n) ≤ 12n (and 11n refereed); those claims are not checked here. The open question is (2+o(1))n, equivalently the dense regime M < 8n³ with elements having three or more distinct prime factors.
