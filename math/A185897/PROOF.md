# The parity of OEIS A185897

**Claim settled.** OEIS A185897 is the sequence a(1), a(2), ... defined by the formal power series A(x) = Σ_{n≥1} a(n) xⁿ satisfying

    A(x − A(x)²) = x/(1 − x).                                   (★)

Paul D. Hanna conjectured (OEIS comment, 5 Oct 2025): for n > 1, a(n) is odd exactly when 3·2^k ≤ n ≤ 4·2^k − 1 for some k ≥ 0. We prove this, together with a(1) odd, i.e.

    a(n) is odd  ⇔  n = 1  or  n ∈ [3·2^k, 4·2^k − 1] for some k ≥ 0.

Author: Claude Fable 5.1, directed by Dovid Preil, 15 October 2026. Independent review: REVIEW-SOL.md. Computational check: verify.py and VERIFICATION.md.

## 1. The equation determines A uniquely over Z

Write A = Σ_{n≥1} a(n) xⁿ with integer coefficients (the OEIS entry gives a(1) = 1, a(2) = 2, a(3) = 9, ...). The series x − A(x)² has zero constant term and linear term x, so the composition in (★) is well defined and

    A(x − A²) = Σ_{j≥1} a(j) (x − A²)^j.

Fix n ≥ 1. The term j = n contributes a(n) xⁿ + (higher). For 1 ≤ j < n, expand (x − A²)^j = Σ_{i=0}^{j} C(j,i) x^{j−i} (−A²)^i. The piece with index i has lowest degree (j − i) + 2i = j + i, and its x^n coefficient involves coefficients of A^{2i} of degree n − j + i, which involve only a(k) with k ≤ n − j + i − (2i − 1) = n − j − i + 1 ≤ n − 1 when i ≥ 1; the piece i = 0 is x^j with j < n. Hence the coefficient of xⁿ on the left of (★) equals a(n) plus a polynomial in a(1), ..., a(n−1), and (★) determines a(n) recursively and uniquely. (Check: n = 1 gives a(1) = 1; n = 2 gives a(2) − a(1)³ = 1, so a(2) = 2.)

Consequently, reducing coefficients modulo 2, Ā(x) := A(x) mod 2 is the unique series in F₂[[x]] with zero constant term satisfying

    Ā(x + Ā(x)²) = x/(1 + x)   in F₂[[x]],                      (★₂)

because reduction mod 2 commutes with composition of formal power series, and the same recursion determines the solution of (★₂) uniquely over F₂.

So it suffices to exhibit a series B ∈ F₂[[x]] with zero constant term that satisfies (★₂) and whose coefficient of xⁿ is 1 exactly for n = 1 and n ∈ [3·2^k, 4·2^k − 1]. Then Ā = B, which is the theorem.

## 2. Tools over F₂[[x]]

All series below have zero constant term where substituted. Over F₂, (y + z)² = y² + z², hence for every k, (y + z)^{2^k} = y^{2^k} + z^{2^k}, and (1 + x)^{2^k} = 1 + x^{2^k}. Define the F₂-linear operator

    ℓ(y) = Σ_{k≥0} y^{2^k} = y + y² + y⁴ + y⁸ + ...   (y with zero constant term).

Then ℓ(y + z) = ℓ(y) + ℓ(z), and ℓ(y)² = Σ_{k≥0} y^{2^{k+1}} = ℓ(y) + y. Thus

    w = ℓ(y)   ⟹   w² + w = y.                                  (AS)

Conversely, in F₂[[x]] the equation z² + z = 0 has only the solutions z = 0 and z = 1: comparing coefficients, z_i = z_{i/2} for even i and z_i = 0 for odd i ≥ 1, so every z_i with i ≥ 1 reduces to z_m = 0 with m odd. Hence a series with zero constant term is determined by its Artin–Schreier image: if v, v' both have zero constant term and v² + v = v'² + v', then v = v'.

## 3. The candidate series B

Let

    B(x) = ℓ(x + x³) / (1 + x).

Lemma 1 (coefficients of B). The coefficient of xⁿ in B is 1 exactly for n = 1 and n ∈ [3·2^k, 4·2^k − 1], k ≥ 0.

Proof. ℓ(x + x³) = ℓ(x) + ℓ(x³) = Σ_k x^{2^k} + Σ_k x^{3·2^k}, a 0/1 series supported on E = {2^k : k ≥ 0} ∪ {3·2^k : k ≥ 0} = {1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, ...}. Dividing by 1 + x over F₂ takes partial sums: the xⁿ coefficient of B is #(E ∩ [1, n]) mod 2. The elements of E in increasing order alternate 2^{k+1}, 3·2^k: namely 1, 2, 3, 4, 6, 8, 12, 16, 24, .... The count #(E ∩ [1,n]) is odd exactly on the intervals between an odd-indexed element and the next element minus one: [1,1], [3,3], [6,7], [12,15], [24,31], ..., that is n = 1 and [3·2^k, 4·2^k − 1]. ∎

(Alternatively, directly: Σ_{j=3·2^k}^{4·2^k−1} x^j = x^{3·2^k}(1 + x^{2^k})/(1 + x), and summing over k and adding x gives x + (ℓ(x³) + ℓ(x) + x + x²)/(1 + x) = ℓ(x + x³)/(1 + x).)

Lemma 2 (B is given by the same formula at any argument). For every y ∈ F₂[[x]] with zero constant term,

    B(y) = ℓ(y + y³) / (1 + y).

Proof. This is the definition of B evaluated at y; composition of formal power series is a ring homomorphism, ℓ(y + y³) = Σ_k (y + y³)^{2^k} is the composition of ℓ(x + x³) with y, and 1/(1 + y) is the composition of 1/(1 + x) with y. ∎

## 4. B satisfies (★₂)

Put w = ℓ(x + x³), so B = w/(1 + x) and, by (AS),

    w² = w + x + x³.                                             (1)

Let u = x + B(x)². Using (1) and (1 + x)² = 1 + x²:

    u = x + w²/(1 + x)² = [x(1 + x)² + w + x + x³]/(1 + x)² = [x + x³ + w + x + x³]/(1 + x)² = w/(1 + x)².   (2)

Hence

    1 + u = [(1 + x)² + w]/(1 + x)² = (1 + x² + w)/(1 + x)².        (3)

By Lemma 2, B(u) = ℓ(u + u³)/(1 + u). We claim

    ℓ(u + u³) = v,  where  v := x(1 + u)/(1 + x) = x(1 + x² + w)/(1 + x)³.     (4)

Both sides of (4) have zero constant term (u has zero constant term by (2) since w does), so by Section 2 it suffices to check v² + v = u + u³, since ℓ(u + u³) satisfies that equation by (AS).

Right side. u + u³ = u(1 + u)², and by (2), (3), (1):

    u(1 + u)² = w (1 + x² + w)² / (1 + x)⁶ = w (1 + x⁴ + w²) / (1 + x)⁶
              = w (1 + x⁴ + w + x + x³) / (1 + x)⁶
              = [w(1 + x + x³ + x⁴) + w²] / (1 + x)⁶
              = [w(1 + x + x³ + x⁴) + w + x + x³] / (1 + x)⁶
              = [x + x³ + w(x + x³ + x⁴)] / (1 + x)⁶.

Left side. From (4) and (1):

    v² = x²(1 + x² + w)²/(1 + x)⁶ = x²(1 + x⁴ + w + x + x³)/(1 + x)⁶,
    v  = x(1 + x² + w)(1 + x)³/(1 + x)⁶ = x(1 + x² + w)(1 + x + x² + x³)/(1 + x)⁶.

Expand (1 + x² + w)(1 + x + x² + x³) = (1 + x + x² + x³) + (x² + x³ + x⁴ + x⁵) + w(1 + x)³ = 1 + x + x⁴ + x⁵ + w(1 + x + x² + x³). Therefore

    (1 + x)⁶ (v² + v) = x²(1 + x + x³ + x⁴ + w) + x(1 + x + x⁴ + x⁵) + x w (1 + x + x² + x³)
                      = (x² + x³ + x⁵ + x⁶ + x² w) + (x + x² + x⁵ + x⁶) + w(x + x² + x³ + x⁴)
                      = x + x³ + w(x² + x + x² + x³ + x⁴)
                      = x + x³ + w(x + x³ + x⁴).

This equals (1 + x)⁶ (u + u³) computed above. So v² + v = u + u³, hence (4) holds.

Finally, by Lemma 2 and (4),

    B(x + B(x)²) = B(u) = ℓ(u + u³)/(1 + u) = v/(1 + u) = x/(1 + x),

which is (★₂). ∎

## 5. Conclusion

B has zero constant term and satisfies (★₂); by Section 1 the solution of (★₂) with zero constant term is unique, so Ā = B. By Lemma 1, a(n) is odd exactly when n = 1 or 3·2^k ≤ n ≤ 4·2^k − 1 for some k ≥ 0. This is Hanna's conjecture (which excludes n = 1 only because it is stated for n > 1). ∎

## Remarks

1. The proof gives the closed form A(x) ≡ ℓ(x + x³)/(1 + x) (mod 2), equivalently A(x) ≡ (x + x² + x³ + x⁴ + x⁶ + x⁸ + x¹² + x¹⁶ + x²⁴ + ...)/(1 + x) (mod 2). In particular a(n) mod 2 is the parity of the number of elements of {2^k} ∪ {3·2^k} not exceeding n.
2. Nothing beyond characteristic-2 Frobenius linearity and the Artin–Schreier uniqueness in Section 2 is used. The same technique should decide the parity of other sequences defined by compositional equations of the form A(x − A(x)^{2^j}) = R(x) with R ∈ F₂(x).
3. The reduction mod 2 is legitimate because (★) has a unique solution over Z and its coefficients are integers (Section 1 and the OEIS data). No claim is made about a(n) modulo higher powers of 2.
