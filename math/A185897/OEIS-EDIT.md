# Proposed OEIS edit for A185897

Submit via https://oeis.org/edit?seq=A185897 (requires an OEIS account; moderated).

## COMMENTS: replace the conjecture line

Current (Paul D. Hanna, Oct 05 2025):

    Conjecture: for n > 1, a(n) is odd when n = 3*2^k through 4*2^k - 1 for k >= 0.

Proposed:

    For n > 1, a(n) is odd iff 3*2^k <= n <= 4*2^k - 1 for some k >= 0 (conjectured by Paul D. Hanna, Oct 05 2025; proved by Dovid Preil and Claude, Oct 15 2026, see link). Proof sketch: the defining equation determines A(x) uniquely over the integers, so it suffices to solve it mod 2. Over GF(2) put L(y) = Sum_{k>=0} y^(2^k), so that L(y)^2 + L(y) = y. Then B(x) = L(x + x^3)/(1 + x) satisfies B(x + B(x)^2) = x/(1 + x), because with u = x + B^2 one has u = L(x+x^3)/(1+x)^2 and L(u + u^3) = x(1+u)/(1+x), verified by the Artin-Schreier identity. Hence A(x) == L(x + x^3)/(1 + x) (mod 2), whose coefficients are 1 exactly for n = 1 and 3*2^k <= n <= 4*2^k - 1. - Dovid Preil, Oct 15 2026

## FORMULA: add

    A(x) == (x + x^2 + x^3 + x^4 + x^6 + x^8 + x^12 + x^16 + x^24 + ...)/(1 + x) (mod 2), where the numerator is Sum_{k>=0} (x^(2^k) + x^(3*2^k)).
    a(n) mod 2 = parity of #{m <= n : m = 2^k or m = 3*2^k for some k >= 0}.

## LINKS: add

    Dovid Preil and Claude, <a href="https://github.com/dpreil-ydlp/open-problems/blob/master/math/A185897/PROOF.md">Proof of the parity conjecture</a>, with independent review and computational verification to 400 terms, Oct 2026.

## Notes for the submitter

- Keep the comment short; the full proof lives at the link.
- Sign with the OEIS account holder's name and date in OEIS format.
