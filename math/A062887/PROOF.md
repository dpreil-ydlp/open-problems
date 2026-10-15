# The zeros of OEIS A062887

**Claim settled.** OEIS A062887 is defined as: a(n) is the smallest positive multiple of 2n+1 whose decimal digits are all odd and each digit is two less (mod 10) than the previous digit; a(n) = 0 if no such number exists. Sean A. Irvine conjectured (OEIS comment, 14 Apr 2023) that a(n) = 0 exactly when 125 divides 2n+1. We prove this.

Author: Claude Fable 5.1, directed by Dovid Preil, 15 October 2026. Independent review: see REVIEW-SOL.md. Computational check: see verify.py and VERIFICATION.md.

## Definitions

Write a positive integer N in decimal as

    N = c_{L-1} 10^{L-1} + ... + c_1 10 + c_0,   c_{L-1} ≠ 0,

so c_0 is the units digit and c_i is the digit in the 10^i place. Reading left to right, "each digit is two less (mod 10) than the previous digit" means c_{i} ≡ c_{i+1} − 2 (mod 10) for 0 ≤ i ≤ L−2, equivalently

    c_{i+1} ≡ c_i + 2 (mod 10)   for 0 ≤ i ≤ L−2.        (1)

Call N **admissible** if all c_i are odd and (1) holds. Since adding 2 preserves parity, (1) together with c_0 odd already forces every digit odd, and the leading digit is odd hence nonzero.

By (1), an admissible number is completely determined by its length L and its units digit c_0: c_i ≡ c_0 + 2i (mod 10). In particular, for each L there are exactly five admissible numbers of length L.

Let X_L denote the admissible number of length L with units digit 5. Its digits from the right are c_i ≡ 5 + 2i (mod 10), i.e. the periodic sequence

    5, 7, 9, 1, 3, 5, 7, 9, 1, 3, ...   (period 5).

So X_1 = 5, X_2 = 75, X_3 = 975, X_4 = 1975, X_5 = 31975, X_6 = 531975, and so on.

## Lemma 1. No admissible number is divisible by 125.

Proof. Let N be admissible with 125 | N. Then N ≥ 125, so L ≥ 3, and N mod 1000 is one of 000, 125, 250, 375, 500, 625, 750, 875. The last three digits of N are odd, which leaves only 375, i.e. c_2 = 3, c_1 = 7, c_0 = 5. But (1) at i = 1 requires c_2 ≡ c_1 + 2, i.e. 3 ≡ 9 (mod 10), which is false. Contradiction. ∎

(Equivalently: the admissible three-digit endings are exactly 197, 319, 531, 753 and 975, and none of them is divisible by 125.)

## Lemma 2. For every k ≥ 1,

    X_{5k} = 31975 · (10^{5k} − 1) / 99999.

Proof. The digit sequence of X_{5k} from the right is k copies of the block 5,7,9,1,3. The block occupying places 10^{5j}, ..., 10^{5j+4} contributes

    10^{5j} (5 + 7·10 + 9·100 + 1·1000 + 3·10000) = 10^{5j} · 31975.

Summing over j = 0, ..., k−1 gives X_{5k} = 31975 · Σ_{j=0}^{k−1} 10^{5j} = 31975 · (10^{5k} − 1)/(10^5 − 1), and 10^5 − 1 = 99999. ∎

## Lemma 3. If gcd(m, 10) = 1, then m divides X_{5k} for some k ≥ 1. One may take k = φ(99999·m).

Proof. 99999 = 3^2 · 41 · 271, so gcd(10, 99999·m) = 1. By Euler's theorem, 10^{φ(99999 m)} ≡ 1 (mod 99999·m). With k = φ(99999 m) we get 99999·m | 10^{5k} − 1, hence 10^{5k}−1 = 99999·m·t for an integer t, hence (10^{5k} − 1)/99999 = m·t. By Lemma 2, X_{5k} = 31975·m·t, so m | X_{5k}. ∎

(Any positive multiple of the multiplicative order of 10 modulo 99999·m also works as k; the order itself gives the shortest witness of this form. Existence is all that is needed here.)

## Theorem. Let m be a positive odd integer. There exists an admissible multiple of m if and only if 125 does not divide m.

Proof.

(⇒) Lemma 1.

(⇐) Suppose 125 ∤ m. Since m is odd, write m = 5^a · m' with a ∈ {0, 1, 2} and gcd(m', 10) = 1. Choose k as in Lemma 3 for m', so m' | X_{5k}.

For L ≥ 2 the last two digits of X_L are 7, 5, so X_L ≡ 75 ≡ 0 (mod 25). Hence 5^a | X_{5k} for every a ≤ 2.

Now 5^a | X_{5k} and m' | X_{5k} with gcd(5^a, m') = 1, so m = 5^a m' divides X_{5k}. X_{5k} is admissible by construction and positive. ∎

## Corollary (the conjecture).

Put m = 2n+1. If 125 ∤ 2n+1, the Theorem provides an admissible multiple of 2n+1, so the set of admissible multiples is nonempty and has a least element; thus a(n) ≠ 0. If 125 | 2n+1, Lemma 1 shows no admissible multiple exists, so a(n) = 0 by definition. Therefore

    a(n) = 0  ⇔  125 | 2n + 1,

equivalently a(n) = 0 exactly for n ≡ 62 (mod 125). ∎

## Remarks

1. The proof is effective. Given m = 2n+1: if 125 | m, return a(n) = 0 by Lemma 1. Otherwise write m = 5^a m' with a ≤ 2 and gcd(m', 10) = 1; then X_L with L = 5·ord_{99999 m'}(10) is an admissible multiple of m, so a(n) is found by enumerating the five admissible numbers of each length 1, 2, ..., L in increasing numerical order and returning the first multiple of m. This turns the OEIS definition ("0 if no such number exists") into a terminating algorithm. (The qualification 125 ∤ m is necessary: for m = 125 the length bound would be 25, but X_25 ≡ 100 (mod 125).)
2. The same argument shows more: for every odd m with 125 ∤ m, there are infinitely many admissible multiples of m (take every positive multiple of the order as k), and the units digit of a witness can always be taken to be 5.
3. The method generalises to digit rules c_{i+1} ≡ c_i + s (mod 10) with s even, but each case needs its own periodic block and its own ending check. What the argument uses about the block is that k consecutive copies of it, including the joins between copies, form an admissible number, and that the block's divisibility by powers of 5 covers every power of 5 not excluded by the ending analysis. For s = 2 the units-5 block is 31975, divisible by 25, and the excluded power is 125. For s = 0, 4, 6, 8 the units-5 blocks are 5, 17395, 93715, 79135, each divisible by 5 but not 25, and in those cases no admissible number is divisible by 25 either, since an ending of 75 requires s = 2; so the excluded power is 25. (The direction-reversed sequence OEIS A062886, digits increasing by 2, records the 25-pattern empirically.)

## Review status

Independent adversarial review by GPT-6.1 Sol (REVIEW-SOL.md, 15 Oct 2026): VERDICT: CORRECT WITH MINOR FIXES, four minor wording objections, no blockers. All four are addressed in this revision: the digit relation in Lemma 1, the parenthetical after Lemma 3, and Remarks 1 and 3. The reviewer also noted an indexing slip in the OEIS entry's own EXAMPLE line, which assigns 975 to a(7); the data and recomputation give a(6) = 975 and a(7) = 75. That is an error in the entry's example, not in the sequence or this proof, and is reported alongside the proof.

## Verification of the reading of the definition

The b-file terms a(0..25) were recomputed by brute force from the definition above (see verify.py) and match OEIS exactly, which confirms that the "two less than the previous digit" convention used here is the one the sequence uses. For example a(5) = 319 = 11·29: reading left to right 3, 1, 9 satisfies 1 ≡ 3−2 and 9 ≡ 1−2 (mod 10).
