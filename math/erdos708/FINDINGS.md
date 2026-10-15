# Erdős 708: source and bounded-search findings

## What the primary sources say

Erdős’s 1992 Hardy–Ramanujan paper defines \(g(n)\) as the smallest uniform number of selected integers that works for **every** increasing \(n\)-element set \(A\) and **every** interval position \(I=\{x+1,\ldots,x+\max(A)\}\), with \(x\geq0\). It states \(g(3)=4\), derives \(g(2)=2\), and states that for every \(\epsilon>0\), all sufficiently large \(n\) satisfy \(g(n)>(2-\epsilon)n\). This agrees with the site’s asymptotic lower-bound summary.

The easy multiples in \([M+1,2M]\), with \(M=p_\ell^2\), give \(|B|=|A|\) for that **one interval**. They do not bound \(g(n)\), which is a worst-case guarantee over all interval positions. The lower-bound construction chooses a particular, different interval by congruences. Thus there is no contradiction in the primary statement. The matching condition belongs to the separate \(f(n)\) variant in the 1959 paper; it is not required by \(g(n)\). One actual paraphrase error is that the site says \(i\ne j\): the 1992 source includes \(p_i^2\) and uses \(1\leq i\leq j\leq\ell\).

The full 1959 Hungarian paper and the HRJ paper were obtained and saved under `sources/`. The requested Eureka 52 paper was not obtained: the current Archimedeans archive link returned 403, exact-title Internet Archive search found no matching item, CDX requests timed out, and guessed old-site PDF paths returned 404. See [`SOURCES.md`](SOURCES.md) for source URLs, attempts, verbatim extracts, and translations. The Eureka text remains an evidence gap.

## Bounded brute force

[`bruteforce.py`](bruteforce.py) enumerates all \(A\subseteq[2,M_{\max}]\) of size \(n\) and all intervals of length \(\max(A)\) with minimum in \(1,\ldots,200\). It uses exact prime-exponent vectors and bounded branch-and-bound to find the least \(|B|\), with a search cap of \(n+2\). These are finite-box maxima, **not** claims about unrestricted \(g(n)\). A full period for the exponent condition divides \(\prod_{a\in A}a\); the 200-start scan need not cover that period.

- \(n=2, M_{\max}=24\): maximum 2 over 50,600 \((A,I)\) cases. Example: \(A=(2,3), I=[1,3], B=(2,3)\).
- \(n=3, M_{\max}=24\): maximum 3 over 354,200 cases. Example: \(A=(2,3,4), I=[1,4], B=(2,3,4)\). The bounded scan does **not** reproduce 4 because it excludes the source’s larger example. Evaluating the 1959 example \(A=(77,91,143)\), \(I=[5935,6077]\), gives minimum 4; for the same \(A\), the easy interval \([144,286]\) has minimum 3. This directly shows why a single easy interval does not settle the worst case.
- \(n=4, M_{\max}=16\): maximum 4 over 273,000 cases. Example: \(A=(2,3,4,5), I=[1,5], B=(2,3,4,5)\). Other tied worst cases include \(A=(2,3,4,6), I=[1,6]\).

Construction checks for starts 1–200 and the specific interval \([M+1,2M]\) found minimum \(|B|=n\): \(A=(35)\) for primes \(5,7\); \(A=(77,91,143)\) for \(7,11,13\); and \(A=(323,391,437)\) for \(17,19,23\). The last triple meets \(2\cdot17^2>23^2\). Under the 1992 source’s diagonal-inclusive construction for the same triple, \(A=(289,323,361,391,437,529)\), \(n=6\), and the minimum on \([530,1058]\) is 6.

## Best exact statement to attack

For every \(n\)-element set \(A\subset\{2,3,\ldots\}\) and every interval \(I\) of \(\max(A)\) consecutive positive integers, bound the minimum size of \(B\subseteq I\) with \(\prod_{a\in A}a\mid\prod_{b\in B}b\). To test the cited lower bound, analyze its CRT-selected interval and its prime-exponent count; the interval \([M+1,2M]\) is only an easy test case.
