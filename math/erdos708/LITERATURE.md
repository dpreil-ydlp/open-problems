# Erdős problem 708: literature search

Search date: 2026-10-15. Scope: literature search only; no proof checking or proving was done. The target is the worst-case minimum number of selected integers, over every (n)-element set (A) and every interval position of length \(\max(A)\), as reconciled in [STATEMENT.md](STATEMENT.md).

## Verdict

**An upper-bound claim is known: \(g(n)\leq 12n\) for every \(n\), under the intended “at most this many selected integers” convention.** Haoyu Chen's proof claim, submitted 2026-09-05 on the current Erdős Problems page, says this bound is kernel-verified in Lean 4. The claim is marked **Claimed / Partial**, and the page says that its presence is no guarantee of correctness and that the site has not examined the proof. I have not checked the proof, its formalization, or the cited repository. Treat this as a recent, formally checked author claim, not as an independently reviewed or accepted published result.

The claim does **not** establish either open target \(g(n)\leq (2+o(1))n\) or \(g(n)\leq2n\). Thus an explicit linear upper bound has been found, but no literature source searched here settles the problem's stated asymptotic or sharp bound.

There is a wording issue to keep visible. The historical sources ask for how many integers must be selected, which defines the minimum required cardinality (equivalently, a guarantee of at most that many). Some web pages write \(|B|=g(n)\) literally. Their modern problem-page notes explain why that exact-size wording is inconsistent for large \(n\); see the original [statement reconciliation](STATEMENT.md). The \(12n\) claim is in the at-most convention. It is not a claim about a literal exact-size definition.

## Upper bounds and primary sources

| Source | What it says | Relevance |
|---|---|---|
| [Erdős and Surányi, “Megjegyzések egy versenyfeladathoz” (1959), *Matematikai Lapok* 10, 39–48](https://users.renyi.hu/~p_erdos/1959-07.pdf) | The paper states the problem, gives the two-input affirmative result and a three-input counterexample, and gives the asymptotic lower bound \(g(n)>(2-o(1))n\). It ends the lower-bound discussion by saying they do not know whether the ratio can be considerably worse. | No general upper bound appears in the inspected passages. Full scan and translation notes are in [SOURCES.md](SOURCES.md). |
| [Erdős, “Some of my forgotten problems in number theory” (1992), *Hardy–Ramanujan Journal* 15, 34–50](https://hrj.episciences.org/125) | Explicitly says \(g(3)=4\), repeats the asymptotic lower bound, and asks whether \(g(n)<(2+\epsilon)n\), or even \(g(n)\leq2n\). It states that the 1959 paper appeared only in Hungarian and outlines its lower-bound construction. | The author presents the upper bounds as open questions, not results. |
| [Erdős Problems #708, current page](https://erdosproblems.ai/problems/708) | The page reports a 2026-09-05 claim by Haoyu Chen: \(g(n)\leq12n\) for all \(n\), said by the author to be kernel-verified in Lean 4. It also reports \(g(n)\leq11n\) as “refereed, not formalised,” and the conjectured \(2n\) bound when \(\max(A)\geq8n^3\). | The page marks the submission “Claimed” and “Partial,” says the proof is unreviewed outside the author's pipeline, and says the displayed \((2+o(1))n\) and \(2n\) targets remain unresolved. The page links the [claim](https://erdosproblems.ai/problems/708#claims), a [Zenodo concept DOI](https://doi.org/10.5281/zenodo.22660853), and the [Lean/research repository](https://github.com/chy4pro/erdos-708-explicit-upper-bounds/tree/94a23325ec41d84b52d0ee89904bc0f2288c1ca1). I did not inspect or verify those artifacts. |

The older [legacy forum thread](https://www.erdosproblems.com/forum/thread/708/proof-claims#proof-claim-262) shows the history of this submission. A 2026-09-07 comment describes version 11 as claiming \(81n\) for all \(n\), with a Lean formalization still in progress at that point. The current page's 12n summary is newer. These are evolving, site-hosted claims, not separate published theorems. The separate interval-length quantity \(c_n\) in the 1992 paper is not \(g(n)\): the paper says \(c_2=1\), \(c_3=\sqrt2\), and reports no good general bounds.

## Citation chase

### Erdős 1992

Google Scholar search for the exact title returned a record with **15 citing results** ([cited-by page](https://scholar.google.com/scholar?cites=12102869334173157199&hl=en), inspected both pages). OpenAlex returned **3 records** ([OpenAlex citing-work query](https://api.openalex.org/works?filter=cites:W2611456884&per-page=20)). The records below are the Google Scholar results; duplicated preprint/journal or translated records are retained because Scholar presents them separately. “Adjacent” means the title/available description concerns distinct-multiple assignment or another neighboring Erdős problem, not this \(g(n)\). “No touch found” means no evidence of discussion of #708 was present in the indexed title/snippet; I did not read all full texts.

| Citing result (Google Scholar title) | Year | Assessment for #708 | Record |
|---|---:|---|---|
| “Primitive sets and von Mangoldt chains: Erdős Problem #1196 and beyond” | 2026 | No touch found; different Erdős problem. | [arXiv:2605.00301](https://arxiv.org/abs/2605.00301) |
| “Sarnak's Program for Erdős Sieves. Part I: Topological Dynamics and Light Tails” | 2026 | No touch found; unrelated sieve problem. | [arXiv:2602.24031](https://arxiv.org/abs/2602.24031) |
| “On the length of an interval that contains distinct multiples of the first positive integers” | 2026 | Adjacent distinct-multiple topic; not evidence for a bound on #708. | [arXiv:2601.16972](https://arxiv.org/abs/2601.16972) |
| “An improved lower bound for odd integers not of the form \(p+2^a+2^b\)” | 2026 | No touch found; unrelated additive problem. | [arXiv:2607.05357](https://arxiv.org/abs/2607.05357) |
| “Long Intervals Without Distinct Multiples of the First Positive Integers” | 2026 | Adjacent distinct-multiple topic; not evidence for a bound on #708. | [arXiv:2607.10431](https://arxiv.org/abs/2607.10431) |
| “Improved Bounds for Distinct Multiples in Intervals” | 2026 | Adjacent distinct-multiple topic; the 1959 paper's separate \(f(n)\) problem is relevant, but this is not a \(g(n)\) bound. | [arXiv:2607.26450](https://arxiv.org/abs/2607.26450) |
| “Sum-free Sets and Arithmetic Notions of Structure in Combinatorics” | 2025 | No touch found; dissertation on other combinatorics topics. | [ProQuest record](https://search.proquest.com/openview/bc7dd829e148c27852d3810c93a52f40/1?pq-origsite=gscholar&cbl=2026366&diss=y) |
| “Erdos Sieves and Dynamics” | 2026 | No touch found; sieve/dynamics topic. | [Paderborn repository](https://digital.ub.uni-paderborn.de/hs/content/titleinfo/8306542/full.pdf) |
| “On a problem of Erdős and Sárközy about sequences with no term dividing the sum of two larger terms” | 2023 | No touch found; different divisibility problem. | [arXiv:2301.07065](https://arxiv.org/abs/2301.07065) |
| “Conjuntos Sidon en Contextos Finitos” | 2023 | No touch found; Sidon sets. | [SciELO record](https://www.scielo.org.co/scielo.php?pid=S0370-39082023000401024&script=sci_arttext) |
| “Sidon Sets in Finite Contexts” | 2023 | English-indexed duplicate/translation of the preceding Sidon-set paper; no touch found. | [Google Scholar result](https://scholar.google.com/scholar?cites=12102869334173157199&hl=en&start=10) |
| Wouter van Doorn, “On the length of an interval that contains distinct multiples of the first positive integers” (published *Integers* version) | 2026 | Adjacent distinct-multiple topic; no #708 upper bound found. | [PDF](https://math.colgate.edu/~integers/aa7/aa7.pdf) |
| “On a problem of Erdős, Berend, and Freud concerning bounded sums and bounded differences” | n.d. (year not shown in Scholar record) | No touch found; unrelated additive problem. | [PDF](https://boonsuan.github.io/erdos863.pdf) |
| “Additive Number Theory” (Guy, *Unsolved Problems in Number Theory*) | 2004 | Broad additive-number-theory chapter; its citation of Erdős 1992 does not show that it treats #708. | [Springer chapter](https://link.springer.com/chapter/10.1007/978-0-387-26677-0_4) |
| “Quasi Sidon Sets” (Javier Cilleruelo) | n.d. (year not shown in Scholar record) | No touch found; Sidon-set topic. | [PDF](https://matematicas.uam.es/~franciscojavier.cilleruelo/Papers/quasi-Sidon%20-%20greedy%20-%20solo%20A-A.pdf) |

OpenAlex's three indexed citing records were “Additive Number Theory” (1994 edition), “Additive Number Theory” (2004 edition), and “Conjuntos Sidon en Contextos Finitos” (2023). These overlap with the broader Google Scholar results and do not provide an additional #708 upper bound.

### Erdős and Surányi 1959

Google Scholar exact-title queries for both the Hungarian title [“Megjegyzések egy versenyfeladathoz”](https://scholar.google.com/scholar?q=%22Megjegyz%C3%A9sek+egy+versenyfeladathoz%22) and German title [“Bemerkungen zu einer Aufgabe eines mathematischen Wettbewerbs”](https://scholar.google.com/scholar?q=%22Bemerkungen+zu+einer+Aufgabe+eines+mathematischen+Wettbewerbs%22) did not produce a reliable indexed record of the 1959 article with a cited-by list. The Hungarian query returned a 2026 preprint, [“Optimal bounds for an Erdős problem on matching integers to distinct multiples”](https://arxiv.org/abs/2603.28636), which concerns the separate distinct-multiple problem (#709 / the paper's \(f(n)\)), not #708. The German query returned Ruzsa's “Erdős and the integers” (1999); its cited-by count is for Ruzsa's survey and cannot be treated as the 1959 paper's citation count. I therefore do not claim an exhaustive list of works citing the 1959 article.

## Concept searches and related entries

Searches used Google web search, the two title variants above, and direct inspection of the relevant Erdős Problems pages. Exact searches included:

- English: “product of consecutive integers” with “product of given integers” and “divisible”; “a_n consecutive integers” with “a_1” and “product divisible”; and “Erdős-Surányi” with “consecutive integers” / “divisibility”.
- Hungarian: `"egymást követő egész számok" szorzat osztható Erdős Surányi`, plus a search for the opening wording of the two-part competition problem.
- German: `"aufeinanderfolgende Zahlen" Produkt teilbar Erdős Surányi` and `"aufeinanderfolgende ganze Zahlen" "Erdős" "Surányi" Produkt`.
- Contest: `Gallai Erdős Surányi competition 1959 Kürschák` and `Erdős Surányi 1959 Hungarian competition problem official solution Kürschák`.
- arXiv/web: `arxiv "selecting integers" interval product divisible consecutive integers`, with searches for product/divisibility wording and the author names.

The directly inspected [#708 page](https://erdosproblems.com/708) says Erdős and Surányi proved \(g(3)=4\) and a lower bound \(g(n)>(2-o(1))n\), and asks whether \(g(n)\leq(2+o(1))n\) or \(2n\). Its note describes the lower-bound set as \(p_ip_j\) for \(i\ne j\); the original 1992 paper explicitly has \(1\leq i\leq j\leq\ell\), including the squares, as documented in [SOURCES.md](SOURCES.md). The page links to [#709](https://erdosproblems.com/709), the distinct-multiples function \(f(n)\), which is related but is not #708.

The 1959 and 1992 texts say the special two- and three-number assertion appeared as a Hungarian competition problem and attribute the broader question to Tibor Gallai. The searches did not identify the contest year/series or an official solution in a Kürschák/Hungarian Problem Book volume. I found no source that ties it specifically to the Kürschák competition; that identification remains unresolved.

For Guy, Google Books/search results expose the table-of-contents entry **B25, “Equal sums of geometric progressions with prime ratios,” p. 124**. That entry is not #708. The search of candidate B25–B40 divisibility entries did not locate an Erdős–Surányi statement or a matching text, so I do not attribute an unverified B-series entry to this problem. The accessible [Guy 2004 chapter record](https://link.springer.com/chapter/10.1007/978-0-387-26677-0_4) surfaced as a citation of the 1992 paper, but did not provide a #708-specific statement.

OEIS searches for `Erdős Surányi`, `consecutive integers product divisibility`, and the small terms `2, 4` with those keywords found no sequence identified as \(g(n)\) or the paper's \(c_n\). A search hit worth excluding is [A002034](https://oeis.org/A002034), described as “Smallest k such that n divides product of k consecutive integers starting with n + 1.” It is a different one-parameter sequence and does not encode worst-case \(g(n)\). Other Erdős–Surányi hits concerned signed sums of powers, also unrelated.

No arXiv result from 2015–2026 found by these concept queries states a bound for #708. The 2026 distinct-multiple papers above concern neighboring functions. They must not be conflated with the Erdős–Selfridge theorem about products of consecutive integers not being perfect powers; that theorem did not yield an upper bound for this selection problem in the searches recorded here.

## Database and access limits

- **Google Scholar:** accessible. Exact-title search gave 15 citing results for the 1992 paper. For the 1959 item it did not provide a reliable article record/cited-by page; title searches returned mixed or adjacent works.
- **OpenAlex:** accessible. Returned 3 citing records for the 1992 DOI, listed above. No 1959 work record suitable for a citation chase was found.
- **zbMATH Open:** direct record query for MR 144847 returned HTTP 403 / Cloudflare challenge. No citing list could be checked there.
- **MathSciNet:** no accessible session or subscription interface in this search environment; citing list not checked.
- **Semantic Scholar:** its graph API returned HTTP 429 on both title searches, and the website search endpoint returned an empty response. No citing list could be checked there.
- **Firecrawl web search:** unavailable because its app returned `USER_NOT_LOGGED_IN`; Google web search through the collaborative browser was used instead.

These limits mean the citation chase is **not exhaustive**, especially for the 1959 article. No statement that “all citing papers” have been identified is justified. The strongest supported conclusion is the 12n site-hosted proof claim above, with its pending/unreviewed status, and no located source that resolves either conjectured sharp bound.
