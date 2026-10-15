# Proposed OEIS edit for A062887

Submit via https://oeis.org/edit?seq=A062887 (requires an OEIS account; edits are moderated by the OEIS editors).

## COMMENTS: replace the conjecture line

Current:

    Conjecture: The only numbers n for which a(n)=0 are those for which 2*n+1 is divisible by 125. - Sean A. Irvine, Apr 14 2023

Proposed:

    The only numbers n for which a(n)=0 are those for which 2*n+1 is divisible by 125 (conjectured by Sean A. Irvine, Apr 14 2023; proved by Dovid Preil and Claude, Oct 15 2026, see link). Proof sketch: an admissible number is determined by its length and its units digit; no admissible number ends in a multiple of 125 since the only all-odd ending among 000,125,...,875 is 375, which violates the digit rule; conversely for gcd(m,10)=1 the number 31975*(10^(5k)-1)/99999, whose digits from the right repeat 5,7,9,1,3, is divisible by m when 10^(5k) == 1 (mod 99999*m), and it is divisible by 25 since it ends in 75. - Dovid Preil, Oct 15 2026

## LINKS: add

    Dovid Preil and Claude, <a href="https://github.com/dpreil-ydlp/open-problems/blob/master/math/A062887/PROOF.md">Proof that a(n)=0 iff 125 | 2n+1</a>, with independent review and computational verification, Oct 2026.

## EXAMPLE: correct the indexing slip

The current EXAMPLE assigns 975 to a(7). The DATA and recomputation give a(6) = 975 (975 = 13*75, modulus 2*6+1 = 13) and a(7) = 75 (modulus 15). Propose changing "a(7) = 975" to "a(6) = 975".

## FORMULA: add

    a(n) = 0 iff n == 62 (mod 125).
    For 125 not dividing m = 2n+1, write m = 5^a*m' with gcd(m',10)=1; then a(n) <= 31975*(10^(5k)-1)/99999 where k is the multiplicative order of 10 modulo 99999*m', so the search for a(n) terminates.

## Notes for the submitter

- Keep the edit minimal; OEIS editors prefer a short comment plus a link over a long proof in the entry.
- Sign the comment with the OEIS account holder's name and date in OEIS format.
- The proof file and the review are in this repository; the repository must be public before the link is added.
