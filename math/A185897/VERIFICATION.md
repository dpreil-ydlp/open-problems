# A185897 computational verification

## Environment and inputs

- Environment: macOS 26.6 (build 25G72), Python 3.13.2.
- Arithmetic: one Python process; integer coefficients use Python `int`; formal-series coefficients over F2 use Python integer bit-vectors.
- Source snapshot: `OEIS-ENTRY.md`, fetched from https://oeis.org/A185897 at 2026-10-15 22:18:04 +03:00. It contains the complete OEIS response, including the name, displayed data, all entry sections, Paul D. Hanna's dated conjecture, formulas, programs, and links.
- B-file: `b185897.txt`, fetched from https://oeis.org/A185897/b185897.txt. It contains 400 terms, indexed 1 through 400. The saved file matches the downloaded response byte for byte.
- Commands:

  ```sh
  python3 verify.py --degree 2000
  python3 -m unittest -v test_verify.py
  ```

## Results

| Check | Result |
|---|---|
| Exact integer recursion vs. b-file | 400/400 terms match; 0 mismatches. The first terms are 1, 2, 9, 64, 574, 5919. |
| Odd-index set vs. stated intervals | Both sets contain 145 indices in [1, 400]; symmetric difference is empty. Intervals present are {1}, [3,3], [6,7], [12,15], [24,31], [48,63], [96,127], [192,255], and [384,400]. |
| (i) `w^2 + w = x + x^3` | PASS through degree 2000. |
| (ii) Support of `B = w/(1+x)` | PASS through degree 2000; bits match exactly the stated index set. |
| (iii) `u = x + B^2 = w/(1+x)^2` | PASS through degree 2000. |
| (iv) `v^2 + v = u + u^3` | PASS through degree 2000. |
| (v) `B(x + B(x)^2) = x/(1+x)` | PASS coefficient by coefficient through degree 2000. |
| (vi) Integer sequence modulo 2 equals `B` | PASS through degree 400. |
| Mod-2 coefficient uniqueness | PASS for n=1..400. At each index, testing both candidate bits in the defining equation's coefficient recursion gave exactly one valid bit. |

The parity comparison used the recomputed integer terms. The mod-2 equations used F2 series truncated at degree 2000, with XOR addition, carry-less multiplication, bit-spreading squaring, Newton inversion, and Horner composition.

## Runtime

Measured by `verify.py` on this run:

| Operation | Runtime |
|---|---:|
| Read b-file | 0.000826 s |
| Exact integer recomputation, N=400 | 6.122554 s |
| F2 identities, D=2000 | 0.356122 s |
| Mod-2 uniqueness checks, n=1..400 | 1.395870 s |

The focused unittest command ran 4 tests and passed in 7.713 s.

## Scope

This independently verifies the first 400 integer coefficients against the saved OEIS b-file, the stated parity pattern on that range, and the listed F2 identities to the stated finite degrees. The computational checks do not prove the infinite formal-series claims; those remain the subject of `PROOF.md`. This run does not verify coefficients beyond the b-file range or residues modulo powers of 2 greater than 2.
