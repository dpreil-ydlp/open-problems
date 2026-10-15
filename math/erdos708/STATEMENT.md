# Statement reconciliation: Erdős problem 708

## Primary-source statement

Erdős (1992, p. 34) states the problem as follows:

> Let \(g(n)\) be the smallest integer for which if \(1<a_1<a_2<\cdots<a_n\) is any sequence of \(n\) integers then for every \(x\geq0\) we can find \(g(n)\) integers among \(x+1,x+2,\ldots,x+a_n\) whose product is a multiple of \(\prod_{i=1}^n a_i\).

Thus the quantifiers are, in order:

1. For every increasing sequence \(A=(a_1<\cdots<a_n)\) of integers with \(a_1>1\);
2. for every \(x\geq0\), which specifies the interval \(I=\{x+1,\ldots,x+a_n\}\) of exactly \(a_n=\max(A)\) consecutive positive integers;
3. there is a subset \(B\subseteq I\) of exactly \(g(n)\) distinct integers for which \(\prod_{b\in B}b\) is divisible by \(\prod_{a\in A}a\).

The source defines a uniform guarantee over **all** such \(A\) and **all** positions of \(I\). Equivalently, the relevant obstruction for fixed \(A\) is its worst interval, not its easiest interval. The source says “smallest integer” and asks for exactly that many selected integers. It does not define \(g(n)\) as a constraint on the number of distinct multiples assigned to the elements of \(A\).

The 1959 paper gives the same problem in words: from as many consecutive integers as the largest given integer, how many must be selected so their product is divisible by the product of the given integers? It gives a positive answer for two inputs and a counterexample to “three suffice” for three inputs. Erdős’s 1992 text explicitly states \(g(3)=4\); its two-input statement implies \(g(2)=2\).

## Differences from erdosproblems.com

- **Interval positions:** The site says any set of \(\max(A)\) consecutive integers. The primary source says \(x+1,\ldots,x+a_n\) for every \(x\geq0\). For positive-integer intervals these are equivalent; the source makes the allowed positions explicit.
- **Set \(B\):** Both the site and the primary source require exactly \(g(n)\) selected integers. The source’s “smallest integer” is a uniform guarantee over every input and every interval. This is not a per-\(A\) bound obtained from one favorable interval.
- **Domain/order:** The site writes \(A\subseteq[2,\infty)\cap\mathbb N\) with \(|A|=n\); the primary source writes \(1<a_1<\cdots<a_n\). These are equivalent for integer sets.
- **Lower-bound construction:** The site’s remark says \(p_ip_j\) for \(i\ne j\). Erdős’s 1992 text says \(1\leq i\leq j\leq\ell\), includes the squares, and gives \(\binom{\ell+1}{2}\) elements and product \((\prod_i p_i)^{\ell+1}\). The 1959 text’s count and product formula also require the diagonal products. Omitting them changes the described construction.
- **Construction interval:** The site summary names the set \(A\), but does not name the interval used in the lower-bound example. The primary source chooses a particular interval of \(p_\ell^2\) consecutive integers by solving congruences. The 1992 proof sketch describes those congruences. The special interval \([M+1,2M]\), where \(M=\max(A)\), is not that interval in the source’s argument.
- **Other variants:** The primary source separately defines \(c_n\) by asking for \(n\) elements from an interval of length \(c_na_n\), and separately defines \(f(n)\) with distinct multiples assigned to distinct \(a_i\). Neither condition is part of \(g(n)\).

## The director’s multiples observation

The observation is valid for the stated interval. Let \(M=p_\ell^2\) and take the source construction with \(a=p_ip_j\) for \(1\leq i\leq j\leq\ell\). Since every \(a\geq p_1^2\), the condition \(2p_1^2>M\) puts every \(2a\) in \([M+1,2M]\). These values are distinct, and their product is divisible by \(\prod_{a\in A}a\). The same observation holds for the off-diagonal set, when that is the set being tested.

This does **not** contradict the primary-source lower bound. It supplies a small \(B\) for one interval position. A lower bound for \(g(n)\) needs a hard interval position for the same or another \(A\), because \(g(n)\) guarantees success for every interval. Erdős and Surányi choose a specific interval by congruences; the easy interval \([M+1,2M]\) does not replace or refute that construction.

The distinct-multiple matching idea is therefore a valid sufficient condition for a particular \((A,I)\), and it can give a global upper bound only if it works for every legal \((A,I)\). In the 1959 paper, the stronger assignment of distinct multiples is instead the separate \(f(n)\) variant.

## Precise question to attack

For every \(n\)-element set \(A\subset\{2,3,\ldots\}\) and every interval \(I\) of \(\max(A)\) consecutive positive integers, find a uniform bound on the least size of \(B\subseteq I\) such that

\[
\prod_{a\in A}a\mid\prod_{b\in B}b.
\]

The primary-source question is whether this uniform bound satisfies \(g(n)<(2+\epsilon)n\) for all sufficiently large \(n\), or perhaps \(g(n)\leq2n\). Any attack on the lower bound must inspect its CRT-selected interval. The single easy interval \([\max(A)+1,2\max(A)]\) does not settle the worst case.

## Inferences and limits

- The exact \(g(2)=2\) value is inferred from the primary text’s assertion that two selected numbers always suffice and the requirement to select a pair.
- The 1992 HRJ and 1959 Rényi scans were inspected directly. The requested Eureka item was not obtained; see [`SOURCES.md`](SOURCES.md). No conclusion here depends on an uninspected Eureka passage.
