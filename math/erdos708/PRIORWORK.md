# Prior work on Erdős problem #708: Haoyu Chen

Research snapshot: 15 October 2026. Sources: the shallow clone at `priorwork/chy4pro/` (HEAD `dc150fd723184cc4e6f367aac6e7a8c9c7890f34`), its TeX and Markdown files, the live [Erdős Problems page](https://www.erdosproblems.com/708), its [proof-claims page](https://www.erdosproblems.com/forum/thread/708/proof-claims), and the linked [Zenodo record](https://doi.org/10.5281/zenodo.22267395). The clone is untrusted. I read its `.tex`, `.md`, `.txt`, and plain-text `LICENSE` files only. I did not read source code or Lean files, or run builds or scripts.

## Repository and publication record

- **Author:** Haoyu Chen (`chy4pro` on GitHub). The paper title block names Haoyu Chen (`paper/main.tex:18-19`).
- **Commit dates:** first commit `6437f25f35cfdb9b96d58bc1283cb0f16fb5dc71`, 2026-09-03 04:30:02 UTC; last commit in this snapshot `dc150fd723184cc4e6f367aac6e7a8c9c7890f34`, 2026-10-12 00:25:13 UTC. The clone is shallow, so I obtained the first date from GitHub's commits API. The last commit updates the Lean CI log and README.
- **License:** CC0 1.0 Universal (`LICENSE:1-2`). Zenodo also lists Creative Commons Zero v1.0 Universal.
- **Paper:** *Explicit upper bounds for the Erdős–Surányi function g(n)*, version 14, dated 2026-09-08 (`paper/main.tex:18-19,43`). The stable DOI `10.5281/zenodo.22267395` resolves to version 14, DOI `10.5281/zenodo.22660853`. The proof-claim page's note says “currently v10”; that note is stale relative to the live DOI record and the repository's v14 manuscript.
- **Other linked material:** the site links the Zenodo paper and `github.com/chy4pro/erdos-708-explicit-upper-bounds/tree/main/lean`. I found no arXiv or blog link in these materials. The repo has a Lean 4 development and Markdown documentation. I did not inspect `.lean` files.

The manuscript's author-status note says the $g(n)\le12n$ proof is formalised and kernel-checked; it says the $g(n)\le11n$ refinement is refereed but not formalised. These are the author's claims, not a review by erdosproblems.com. The paper says the conjectured general $g(n)\le2n$ is not proved (`paper/main.tex:36-42`).

## Main statements, quoted from the paper

The following are the manuscript's principal proved upper bounds and its stated open target. Statements in quotation blocks retain the TeX wording and symbols. Proof-method notes follow each group.

### Bounds depending only on n

**Theorem 1.1 (logarithmic bound), verbatim** (`paper/main.tex:103-109`):

> For every \(n\ge 2\),
> \[
>  g(n)\;\le\;F(n):=n\bigl(\Lam(2n)+\Lam(\Lam(2n))+2\bigr)\;=\;n\log_2 n+n\log_2\log_2 n+O(n).
> \]
> In particular \(F(2)=10\), \(F(3)=21\), \(F(4)=28\), \(F(10)=100\), \(F(100)=1300\), \(F(1000)=17000\).

**Method.** For each input, split its prime-power factors into large atoms and small atoms using a threshold $T=m/H$, where $m=a_n$ and $H$ is the target budget. Place large atoms by a per-prime greedy rule. Pack the small atoms into bins whose products are at most $T$, then choose distinct interval multiples for the bins. A divisor-counting argument bounds the number of bins. The logarithmic estimate counts the bins by a next-fit argument (`paper/main.tex:195-230, 279-318`).

**Theorem 1.2 (square-root bound), verbatim** (`paper/main.tex:111-118`):

> For every \(n\ge 1\), with \(L=81+\ln n\),
> \[
>  g(n)\;\le\;\Bigl\lceil 48\,n\sqrt{L/\ln L}\,\Bigr\rceil ,
> \qquad\text{and}\qquad
>  g(n)\;\le\;(2+o(1))\,n\sqrt{\frac{\ln n}{\ln\ln n}}\quad(n\to\infty).
> \]

**Method.** It uses the same large-atom placement and small-atom bins. The bin count is bounded by separating the number and size of prime factors, with an elementary prime-sum estimate. The asymptotic proof splits according to whether $\ln(m/H)$ is large, then applies a bound on $\omega(a)$ in the other range (`paper/main.tex:231-390`). This is **not** the conjectured $g(n)\le(2+o(1))n$; the extra square-root logarithmic factor is present.

### Long intervals and size regimes

**Theorem 1.3 (long intervals), verbatim** (`paper/main.tex:124-129`):

> If \(a_n\ge 8n^3\), then for every \(x\ge 0\) some \(2n\) of the integers \(x+1,\dots,x+a_n\) have product divisible
> by \(a_1\cdots a_n\) (at most \(2n\) are needed, and since \(a_n\ge 2n\) the set may be padded); in fact
> Conjecture~\ref{conj:S} below holds for such \(A\). Consequently \(g(n)\le 8n^3\) as
> well, and the question whether \(g(n)\le 2n\) is equivalent to the same question restricted to \(a_n<8n^3\).

**Method.** Put $C=m/(2n)$. Every input has at most one prime-power atom above $C$; split each input into at most two coprime demands with size at most $C$, apart from the one allowed large atom. Large atoms are hosted by distinct multiples per prime. Each small demand has at least $2n$ interval multiples, so it can be assigned an unused one. The paper's two-bin product lemma supplies the split (`paper/main.tex:393-439`).

**Theorem 1.4 (general (k)-split regime), verbatim** (`paper/main.tex:133-140`):

> Let \(k\ge 2\) be an integer and suppose that \(a_n\le kn\) or \(a_n^{\,k-1}\ge(kn)^{k+1}\). Then for every \(x\ge 0\) some (at
> most) \(kn\) of the integers \(x+1,\dots,x+a_n\) have product divisible by \(a_1\cdots a_n\). In particular \(a_n\ge 9n^2\)
> gives \(3n\) and \(a_n\ge 1024^{1/3}n^{5/3}\) gives \(4n\); for every \(\delta>0\) and every integer \(k\) with
> \(\delta(k-1)>2\), \(a_n\ge n^{1+\delta}\) gives \(kn\) as soon as \(n^{\delta(k-1)-2}\ge k^{k+1}\). Taking for each \(n\) the
> smallest admissible \(k\) (and Theorem~\ref{thm:log} where none is admissible) gives, for every \(n\ge 1\): \(7n\) integers
> suffice whenever \(a_n\ge n^3\), \(12n\) whenever \(a_n\ge n^2\), and \(15n\) whenever \(a_n\ge n^{7/4}\).

This includes the $12n$ claim for the restricted range $a_n\ge n^2$, but the all-$n$ $12n$ result below is stronger.

### Hinge inequalities and linear bounds

The paper's conditional hinge theorem states (verbatim, `paper/main.tex:566-569`):

> If Conjecture~\ref{conj:TH} holds, then \(g(n)\le 18n\) for all \(n\ge1\). More precisely, it suffices that
> \eqref{eq:TH} holds for \(m=a_n\) and every weight supported on the primes dividing \(\prod A\).

This is conditional, since the cited hinge conjecture is not proved in full.

**The O(n ln ln n) corollary, verbatim** (`paper/main.tex:881-883`):

> \(g(n)\le\bigl(17+149e\ln(1+\ln(8n^3))\bigr)n\) for all \(n\ge1\); in particular \(g(n)=O(n\ln\ln n)\).

**Method.** Linear-programming duality turns an integral cover into a weighted prime-factor inequality on intervals. A weighted sieve proves the hinge inequality with a threshold growing like $1+149e\ln(1+\ln m)$; LP rounding then gives the displayed bound. The long-interval theorem handles $m\ge8n^3$ separately (`paper/main.tex:873-887`).

**Theorem 10.1 (variable threshold), verbatim** (`paper/main.tex:1017-1023`):

> For every weight \(z\), every \(m\ge3\) and every \(x\ge0\),
> \begin{equation}\label{eq:th20}
> \sum_{k\le m}\bigl(w_z(k)-20\ln\ln m\bigr)^+\le\sum_{b\in I}\bigl(w_z(b)-1\bigr)^+ ,
> \end{equation}
> and for \(m\le2\) the inequality holds with threshold \(2\). Consequently \(g(n)\le\bigl(16+20\ln\ln(8n^3)\bigr)n\) for all \(n\ge1\).

**Method.** A geometric sequence of levels with ratio close to 1 and a factorial inversion let the proof pay for all levels with one sieve budget instead of paying at each dyadic level (`paper/main.tex:1011-1015`).

**Theorem 14.11 (linear bound), verbatim** (`paper/sec_signed.tex:218-223`):

> For every weight $z$, every $m\ge1$ and every $x\ge0$ the hinge inequality \eqref{eq:th65} with threshold $65$ holds, and
> \[
> g(n)\le81\,n\qquad\text{for every }n\ge1 .
> \]

**Theorem 15.1 (threshold 17), verbatim** (`paper/sec_h17.tex:9-15`):

> For every atom system, every $m\ge1$ and every window $I$ of $m$ consecutive positive integers,
> \[
> \sum_{k\le m}\bigl(S(k)-17\bigr)^+\ \le\ \sum_{b\in I}\bigl(S(b)-1\bigr)^+ .
> \]
> Consequently $g(n)\le33\,n$ for every $n\ge1$.

**Method.** A signed divisor certificate handles the sparse-core case: dyadic rounding, prefix carriers, positive carrier moduli, and negative clipping terms control the excess. This proves the threshold-65 hinge inequality for all weights and yields $81n$. The tightened threshold-17 proof uses similar rounded atoms and carrier counting, with the $16n$ rounding cost, to yield $33n$ (`paper/sec_signed.tex:1-22,188-226`; `paper/sec_h17.tex:1-7,36-91,140-146`). The paper also proves the $81n$ hinge bound by arithmetic shadows for $m\le10^{2887}$, which yields $g(n)\le81n$ for $n\le10^{962}$ before the all-$m$ signed proof (`paper/main.tex:1366-1400`).

**Theorem 16.1, c+2 reduction, verbatim** (`paper/sec_chain19.tex:11-19`):

> Let \(c\ge1\) be real and suppose that for every atom system, every \(m\ge1\) and every window \(I\) of \(m\) consecutive
> positive integers
> \[
> \sum_{k\le m}\bigl(S(k)-c\bigr)^+\ \le\ \sum_{b\in I}\bigl(S(b)-1\bigr)^+ .
> \]
> Then \(g(A,x)\le\lceil cn\rceil+2n\) for every \(A\) with \(|A|=n\) and every \(x\ge0\); in particular \(g(n)\le(c+2)n+1\),
> and \(g(n)\le(c+2)n\) whenever \(cn\) is an integer.

**Method.** The proof bounds the fractional LP cover by $cn$, rounds a vertex with fewer than the number of supported primes in extra cost, and counts those primes by $n+\pi(\sqrt m)$. The $k=3$ split handles $m\ge9n^2$; in the other range, $\pi(3n)\le n+1$ gives a total integer cover of at most $\lceil cn\rceil+2n$ (`paper/sec_chain19.tex:28-70`).

Consequences stated in the paper:

> \(g(n)\le19n\) for every \(n\ge1\). (`paper/sec_chain19.tex:21-22`)

> \(g(n)\le18n+\pi\bigl((18n)^{19/34}\bigr)-1=18n+O\bigl(n^{19/34}/\ln n\bigr)\) for every \(n\ge1\). (`paper/sec_chain19.tex:73-75`)

**Theorem 17.1 and Corollary 17.2, verbatim** (`paper/sec_h97.tex:9-20`):

> For every atom system, every \(m\ge1\) and every window \(I\) of \(m\) consecutive positive integers,
> \[
> \sum_{k\le m}\bigl(S(k)-\tfrac{97}{10}\bigr)^+\ \le\ \sum_{b\in I}\bigl(S(b)-1\bigr)^+ .
> \]
> \(g(n)\le12n\) for every \(n\ge1\).

**Method.** The LP reduction above gives a bound of $\lceil(97/10)n\rceil+2n\le12n$. To prove the hinge inequality, the paper rounds each prime's cumulative atom mass to four mantissa levels per dyadic band, with ratio 5/4 and loss 47/16. It then groups excess points by a short carrier prefix, bounds each carrier's contribution with a mass-specific factorial-moment order, and verifies 29 finite coefficient scales plus an analytic tail. The paper states the carrier's cofactor is at least 210 and gives an overall 3.9% slack (`paper/sec_h97.tex:1-7,64-85,88-120,150-179`).

The author reports the $12n$ chain as complete and Lean-kernel verified: 108 modules, exact certificates for the 29 scales, and final dependencies only on `propext`, `Classical.choice`, and `Quot.sound` (`paper/sec_h97.tex:215-225`). The repo's CI log records a successful 2026-10-12 build with the `g_le_12n` chain and no `sorry` or `native_decide` in the checked build (`lean/CI_LOG.md:6-19`). This report did not read the `.lean` files or rerun that build.

**Theorem 18.1 and Corollary 18.2, verbatim** (`paper/sec_h883.tex:11-20`):

> For every atom system, every \(m\ge1\) and every window \(I\) of \(m\) consecutive positive integers,
> \(\sum_{k\le m}\bigl(S(k)-\tfrac{56501}{6400}\bigr)^+\le\sum_{b\in I}\bigl(S(b)-1\bigr)^+\).
> \(g(n)\le11n\) for every \(n\ge1\).

**Method and status.** Eight mantissas per band, a level-specific retention rule, prime-density bounds, and a carrier count that tracks cardinality lower the threshold to $56501/6400<9$; the same $(c+2)$ reduction gives $11n$. The paper calls this result refereed and exact-arithmetic checked, but not formalised (`paper/sec_h883.tex:1-9,23-27,71-90`; `README.md:108-114`).

### The 2n target and special cases

The paper states Erdős's target in the introduction as “$g(n)\le(2+o(1))n$, or even $g(n)\le2n$” (`paper/main.tex:51-53`). These are questions, not proved general bounds. The split-assignment conjecture implies $g(n)\le2n$, and the paper says it is proved for $a_n\ge8n^3$; it also says the assignment exists when every input has at most two distinct prime factors (`paper/main.tex:534-547`).

**Special case: at most two distinct prime factors.** This is not a separately numbered theorem in the manuscript. The proved sentence in the split-assignment discussion says:

> “the assignment always exists when every \(a\in A\) has at most two distinct prime factors (use the finest splitting and Lemma~\ref{lem:large}); a counterexample would need elements with three or more prime factors competing for composite multiples.” (`paper/main.tex:540-544`)

Thus its assignment gives $h(A,x)\le2n$ in this class. The manuscript's later collision-cycle theorem implies the sharper $h(A,x)\le2n-1$ for $n\ge1$ in this class; it implies $h(A,x)\le n$ when all elements are prime powers, since then the incidence graph has cycle rank zero (see below).

**Other 2n criteria.** The paper proves $g(A,x)\le2n$ when the input-prime incidence graph has cycle rank $\beta\le n$ (`paper/sec_remains.tex:295-329`). This applies at any $M=a_n$, including some instances with three or more distinct prime factors. It does not cover all such instances.

For the hinge route, the manuscript also proves threshold 2 if at most four primes carry positive atom weight, or if the truncated atom system has sufficiently large mean (`paper/sec_remains.tex:53-79,84-110`). These are inequalities for atom systems, not by themselves $2n$ cover theorems. The paper reduces the remaining hinge-threshold-2 case to systems with at least five active primes, small mean, and a positive left side (`paper/sec_remains.tex:116-137`).

## Site status and acknowledgment

The live proof-claim page gives this summary:

> “Summary: Partial result: explicit upper bounds for g(n), not a resolution of the (2+o(1))n question. Main result of the linked paper (v14): g(n) <= 12n for all n.”

It also says:

> “Appearing on this page is no guarantee of proof correctness, and does not mean that anyone associated with this site has examined any part of the proof.”

The claim is listed as submitted by Haoyu Chen on 2026-09-05. The site page therefore records an **author-submitted partial proof claim with no site review**. I found no acknowledgment or endorsement by Thomas Bloom on the problem page, proof-claims page, or discussion page. The page's “Additional thanks to: Wouter van Doorn” is unrelated. The DOI record is a versioned preprint record; it is not an arXiv preprint. The site links the repository's Lean directory as the formalisation.

## Is the 12n proof complete in the repository?

**Repository evidence says yes; this research pass did not independently rebuild it.** The v14 manuscript contains the full $97/10$ hinge proof and the $c+2$ reduction. The paper explicitly says the theorem and reduction are in the Lean development, lists their declarations and standard axioms, and says the development was recompiled from scratch (`paper/sec_h97.tex:215-225`). The latest CI log records success for the final `g_le_12n` chain (`lean/CI_LOG.md:14,19`). The corresponding Lean directories and files are present according to `lean/README.md:21-24`. I found no “TODO”, external missing proof, or placeholder reference in the TeX/Markdown statements for the $12n$ theorem. The author also identifies a separate planning file containing `sorry` as “imported by nothing” (`lean/README.md:23`); the CI log says no `sorry` is in the checked build closure. The $11n$ refinement is the exception: the paper says it is refereed but not formalised.

## Comparison with our results in `NOTES.md`

Here $M=\max A$. “Same” compares the mathematical conclusion, not the proof or notation; the Chen manuscript writes $g(A,x)$ for the instance minimum called $h(A,x)$ in our notes.

| Our result | Prior-work comparison | Evidence |
|---|---|---|
| **Theorem A:** if $\omega(a)\le2$ for all $a\in A$, then $h(A,x)\le2n-H\le2n-1$. | **Same conclusion.** The split-assignment passage gives $h\le2n$ for this class. More strongly, the collision-cycle bound $h\le n+\beta$ implies $h\le2n-1$ for $n\ge1$ when all left degrees are at most two; it gives $h\le n$ for prime-power inputs. The manuscript does not state our hub-count $H$ refinement in this form. | Our `NOTES.md:107-118`; paper `main.tex:534-544`; `sec_remains.tex:295-329`. |
| **Theorem B:** $h(A,x)\le\sum_{c\in C}(1+\sum_{a\in S_c}\omega(a)-|P(S_c)|)$. | **Same statement.** Under the paper's anchor fibres $C_b$, it proves $\delta_p(S)\le\sum_C(r_{C,p}(1)-1)^+$, sums this over primes, and obtains $h\le|S|+\sum_C(\sum_{a\in C}\omega(a)-|P(C)|)$, which is exactly the same group expression. The wording in our notes already records this as an independent rediscovery, not a new result. | Our `NOTES.md:88-112` and `NOTES.md:14`; paper `sec_remains.tex:304-323`. |
| **Theorem C:** if $M>(2n+1)^3$, then $h(A,x)\le2n$. | **Prior work is stronger on the threshold.** The paper proves the same cover size for $M\ge8n^3$. Since $8n^3<(2n+1)^3$, that result covers a larger range, including the boundary $M=8n^3$. Its construction uses the two-bin split and fresh multiples for each small demand. | Our `NOTES.md:122-158`; paper `main.tex:124-140,393-439`. |
| **Exact lower bound:** for $n=\ell(\ell+1)/2$, $h(A,x)=2n-2\ell+1$ under the stated prime condition. | **Weaker explicit statement in prior work.** The paper states the Erdős–Surányi construction and $g(n)\ge(2-\varepsilon)n$ asymptotically, but does not state our squares-included instance, exact count, or formula $2n-2\ell+1$. Its described family uses $p_ip_j$ with $i\ne j$, not our $i\le j$ family. | Our `NOTES.md:20-60`; paper `main.tex:85-95`. |

## Useful material for the dense regime

The most directly relevant result is the **collision-cycle bound**. The paper anchors each input $a$ at a multiple $b(a)\in I$, partitions the inputs into fibres $C_b$, then charges each missing prime-power slot to repeated primes inside a fibre. It bounds the total deficit by the cycle rank of the bipartite input/prime incidence graph:

> “\(g(A,x)\le n+\beta\) for every \(A\) and every \(x\ge0\), with no hypothesis on \(a_n\).” (`paper/sec_remains.tex:304-306`)

Here $\beta=\sum_{a\in A}\omega(a)-|\mathcal P(A)|+c-n$, where $c$ is the number of connected components. Its proof and the $\beta\le n\Rightarrow g(A,x)\le2n$ corollary are at `paper/sec_remains.tex:295-329`. This argument does not require a fresh multiple for every repair demand, so it is relevant precisely where the small-demand construction can collide. It handles some dense instances with elements of three or more prime factors when their incidence-cycle rank is at most $n$, but does not establish $2n$ for arbitrary dense instances. For prime-power inputs, $\beta=0$, so it gives $h\le n$.

The manuscript's **threshold-2 large-mean proposition** can also cover a dense branch of the *fractional hinge inequality*: after truncation at $p^j\le m/6$, it applies when the atom mean is at least $h_0=(18-\sqrt{30})/7\approx1.789$ (`paper/sec_remains.tex:84-110`). Its **at-most-four-active-primes proposition** proves the hinge inequality at threshold 2 for systems supported on four primes (`paper/sec_remains.tex:53-79`). Both feed the paper's LP/rounding framework; neither directly gives $h\le2n$ for arbitrary inputs. The manuscript itself isolates a nonempty remaining threshold-2 regime with at least five active primes and low mean (`paper/sec_remains.tex:116-137`).

So the paper offers an exact, potentially combinable $2n$ criterion based on incidence cycle rank, plus fractional hinge lemmas for restricted atom systems. It does **not** provide a lemma that closes the unrestricted dense regime $M\le(2n+1)^3$ at $2n$. Its global $12n$ theorem does cover that regime with the weaker $12n$ bound.
