# Independent review of Section 3A

VERDICT: BLOCKED

The claim of a **new result** is blocked by prior public work. I found no mathematical counterexample. The argument for Theorems A and B is valid, subject to the minor empty-set convention below. All 300 requested random tests passed. This verdict distinguishes the novelty claim from mathematical validity.

Owner: Sol review sub-agent. The coordinating agent owns acceptance. Authority: the user's adversarial-referee request of 15 October 2026. Budget: 40 minutes; completed within that limit. No child tasks were created. I did not edit NOTES.md or another worker's record.

1. **BLOCKER — novelty: the general group bound already occurs in a public manuscript.** Haoyu Chen's manuscript *Explicit upper bounds for the Erdős–Surányi function g(n)* contains the same bound in the proof of its collision–cycle theorem, under “The incidence graph.” This is a direct mathematical match, not a similarity of terminology.

   The source chooses a multiple b(a) of each a, forms the distinct anchors S and their fibres C, defines prime-power counts, and proves

       δ_p(S) ≤ Σ_C (r_{C,p}(1) − 1)^+,
       Σ_p δ_p(S) ≤ Σ_C (Σ_{a∈C} ω(a) − |P(C)|).

   It then uses h(A,x) ≤ |S| + Σ_p δ_p(S). Adding |S| to the preceding displayed inequality gives exactly the proposed Theorem B. The substitutions are S ↔ the hub set C in NOTES.md, source fibre C ↔ S_c, and δ_p(S) ↔ f_p. The subsequent groupwise case split gives the proposed 2n − H ≤ 2n − 1 statement without an additional idea. The source also explicitly states the ≤2n result when each input has at most two distinct prime factors, and the need for at least three prime factors in a counterexample, in its earlier split-assignment discussion.

   Reproducible primary sources:

   - [Collision–cycle proof, source lines 290–323](https://github.com/chy4pro/erdos-708-explicit-upper-bounds/blob/8b9c1c1b0da9c9696b425d52b308d358213b77c5/paper/sec_remains.tex#L290).
   - [Two-prime special case, source lines 540–545](https://github.com/chy4pro/erdos-708-explicit-upper-bounds/blob/8b9c1c1b0da9c9696b425d52b308d358213b77c5/paper/main.tex#L540).
   - [Commit 8b9c1c1, dated 8 September 2026](https://github.com/chy4pro/erdos-708-explicit-upper-bounds/commit/8b9c1c1b0da9c9696b425d52b308d358213b77c5). I fetched both files at this exact commit. The GitHub API gives its committer date as `2026-09-08T20:42:24Z`, before this note's 15 October date.

   This establishes a prior public statement and derivation. It does not establish journal publication, peer acceptance, or priority before that source. I did not verify the manuscript's general 12n bound or its Lean development. The smallest correction is to cite this source, remove the unqualified novelty claim, and present Section 3A as an independent proof or exposition. The exact group bound is already present as an intermediate inequality, even though the source's named theorem proceeds to a graph-theoretic bound.

2. **MINOR — specify the zero-deficit case.** In the revised Construction, “let v_max be the largest v with r(v)>0” has no meaning when f_p=0. This occurs for every prime when n=1, for example. Add: “If f_p=0, take F_p=∅. Otherwise proceed as follows.” Also, it is enough to consider primes dividing ∏A; for every other prime take F_p=∅. This is an omitted convention, not a failure of the theorem.

The initial text also had a false suggestion that positive parts restore monotonicity. During this review another writer replaced that paragraph with the correct tail-maximum argument. That objection is resolved in the reviewed final snapshot. I made no change to NOTES.md.

Proof audit:

- **(a) Lemma 3 is correct.** For a positive integer b, v_p(b)=Σ_{v≥1}[p^v divides b]. Both B and I are finite and contain positive integers. For fixed p the sum vanishes above max_{b∈I} v_p(b). Thus the interchange of sums is finite and the displayed identity is exact. Summing the slot inequalities gives the required valuation inequality for each prime. The criterion is sufficient; the proof does not need its converse.

- **(b) Inequality (S) is correct.** Distinct inputs divisible by q=p^v belong to {q,2q,…,⌊M/q⌋q}, so D≤⌊M/q⌋. For integer x≥0,

      N(p,v)=⌊(x+M)/q⌋−⌊x/q⌋ ≥ ⌊M/q⌋.

  This holds at every interval position, including when q>M. The distinctness of A is essential for the first inequality and is part of the problem.

- **(c) Non-monotone deficits do not invalidate the descending construction.** Here is an example using the exact first-multiple hub rule used in the tests:

      A={4,5,12}, n=3, M=12, x=8, I={9,…,20}.
      μ(4)=12, μ(5)=10, μ(12)=12, C={10,12}.

  For p=2, at v=1,2,3 the respective counts are D=(2,2,0), K=(2,1,0), and (D−K)^+=(0,1,0). Taking positive parts has not made this sequence nonincreasing. Set F_2={16}. It meets the level-2 demand; at level 1 retain 16 even though the demand there is zero. Then |F_2|=1=max_v(D−K)^+. No other prime needs a fill. The constructed B={10,12,16} covers ∏A=240. The ILP minimum is 2, with B={12,20}; Theorem B gives 3.

  For a formal argument put T_v=(I\C)∩p^vℤ, d_v=(D(p,v)−K(p,v))^+, and r_v=max_{w≥v}d_w. The sets T_v are nested. For every w≥v,

      |T_v| ≥ |T_w| = N(p,w)−K(p,w) ≥ d_w,

  where the last step uses (S) and nonnegativity. Hence |T_v|≥r_v. When descending from v+1 to v, the current selected set lies in T_v and has r_{v+1} elements. Add r_v−r_{v+1} unused elements of T_v. There are enough, since |T_v|−r_{v+1}≥r_v−r_{v+1}. Later additions cannot remove earlier coverage. The final size is r_1=f_p. All d_v vanish for sufficiently large v because D does. With the zero case in objection 2, this proves existence completely. The revised NOTES.md gives this argument.

- **(d) Lemma 4 is correct.** A group counted by G(p,v) contains an a divisible by p^v, so its hub is divisible by p^v. This gives an injection into the distinct hubs counted by K(p,v); equality is not needed. The groups partition A, so D−G=Σ_c(n_c(p,v)−1)^+. Each n_c(p,v) decreases or stays constant with v. The right side at v=1 is nonnegative, so it also bounds (D−K)^+, and then f_p.

- **(e) Theorem B's summation and Theorem A's cases are correct.** For a nonempty group S_c, Σ_p n_c(p)=Σ_{a∈S_c}ω(a) and Σ_p[n_c(p)>0]=|P(S_c)|. These are finite sums. If the group contains an input with two prime factors, its contribution is at most 2|S_c|−1. Otherwise every input is a prime power because a≥2, and the contribution is |S_c|+1−|P(S_c)|≤|S_c|≤2|S_c|−1. This also covers groups of prime powers based on different primes. There are H nonempty groups, 1≤H≤n, so summation gives 2n−H≤2n−1. If n=1, H=1 and Theorem B gives exactly 1; a multiple of the sole input exists in I. No n≥2 assumption is used.

- **(f) The union count is correct.** C=μ(A) is a set of distinct numbers, although several inputs can have the same hub. Each F_p is a set in I\C. Different F_p may intersect; that helps the cardinality bound. Pairwise disjointness between different primes is unnecessary. For each fixed p, the hubs and F_p are disjoint, which justifies their addition in the slot count. Only finitely many primes have f_p>0. Thus |B|≤H+Σ_p f_p is a valid finite union bound.

- **(g) Corollary 5(ii) is correct.** If every input has ω≤2, then h≤2n−1, which contradicts h>2n. Thus a counterexample to the proposed universal bound must contain an input with ω≥3. In fact the same necessary condition follows already from h≥2n. This is a necessary condition, not a sufficient one. Corollary 5(iii) is Theorem B with H=Σ_c1. In part (i), the lower bound concerns the worst case in the restricted class at the stated triangular n, not every individual A or interval.

Literature check:

I ran searches for `"Erdős" "Surányi" "two prime factors"`, `"Erdos" "Suranyi" "two distinct prime"`, and variants with product/consecutive integers and problem 708. The broad search did not itself establish a matching theorem. Direct inspection of the proof-claim repository did, as detailed in objection 1.

I read the live [#708 page](https://www.erdosproblems.com/708), its [discussion](https://www.erdosproblems.com/forum/thread/708), its [proof claim](https://www.erdosproblems.com/forum/thread/708/proof-claims), and the [claim's comment endpoint](https://www.erdosproblems.com/forum/proof-claims/262/comments), on 15 October 2026. The ordinary #708 discussion addresses the distinction between “exactly g(n)” and “at most g(n).” NOTES.md uses the correct worst-case-minimum definition. The proof-claim page reports Chen's general 12n claim and expressly warns that site listing does not certify correctness. I used its linked repository as the primary source for the matching special-case argument.

I also read the live [#709 page](https://www.erdosproblems.com/709) and all three visible [discussion comments](https://www.erdosproblems.com/forum/thread/709). These discuss distinct-multiple assignment in longer intervals and bounds for its different function f(n). None states the present group bound. They must not be used as a proof of this #708 assertion. This was a bounded search, not an exhaustive historical priority review.

Firecrawl was unavailable: its tool returned `asdk_app_6a314a73f8ac819195b0d55e36b9c609 is not connected`. I completed the search with the available web-search tool and direct HTTP reads. Plain HTTP Google and DuckDuckGo searches returned challenge pages; these were not counted as negative search evidence.

Computational results:

The reproducible script is [review_sol_theorem_a_check.py](review_sol_theorem_a_check.py). Full inputs, interval positions, optimal sets, hub groups, fill sets, bounds, and summaries are in [REVIEW-SOL-THEOREM-A-RESULTS.json](REVIEW-SOL-THEOREM-A-RESULTS.json). Run it from this directory with:

    .venv/bin/python review_sol_theorem_a_check.py

It reuses `valuation` from `verify_lower.py` and uses PuLP 2.9.0 with the existing bundled CBC. For each prime p dividing ∏A, the integer model requires Σ_b z_b v_p(b)≥Σ_a v_p(a) and minimizes Σ_b z_b. Equal valuation vectors are grouped into one integer count bounded by the number of distinct available interval integers. This is exactly equivalent to one binary variable per integer: any allowed count can be expanded to that many distinct members of its group. Numbers whose valuations are all zero can be omitted. The script expands every selected count to actual integers and checks divisibility with exact integer arithmetic. It requires both PuLP status `Optimal` and `LpSolutionOptimal`; a merely feasible solution is rejected.

An initial ungrouped, time-limited run stopped without a proved optimum and was discarded. The completed run below used the grouped model. There was no unresolved solver failure and no theorem violation.

- Seed: `708150026`. Exactly **300 distinct random input sets**, all with ω(a)≤2, n≤7, and max(A)≤150. Observed M range: 4–149. There were 43 sets at each n=1,…,6 and 42 at n=7.
- Each initial x was uniform in [0,1,000,000]. Three greedy hill-climb rounds tested unit offsets and random offsets of size 2,…,2M. Ties could move across a plateau. The chosen position always had the largest optimum seen for that input set. This is a short local search, not a global maximization over all x.
- **3,517 distinct (A,x) evaluations** received exact optimal solutions. The hill-climb increased the optimum in **84 of 300** cases. Final optima ranged from 1 to 7. The random sample did not produce a case with optimum greater than n; it does not reproduce the known extremal lower-bound family.
- At **every evaluated position**, the script checked optimum≤|constructed B|≤H+Σ_p f_p≤Theorem B. It also checked Theorem B≤2n−H≤2n−1. There were **zero violations**. The smallest slack for each requested upper bound was zero.
- The script directly checked (S), G≤K, the tail-maximum capacity, fill cardinalities, fill/hub disjointness, slot coverage, Lemma 4, and exact divisibility of the constructed set. **85** random positions had a non-monotone positive deficit for at least one prime. Their constructions all passed.
- Six additional directed tests passed: the non-monotone example above; n=1 with a prime, a prime power, and a number with two distinct primes; a seven-element set of powers of 2; and a general set containing inputs with three distinct primes for Theorem B. In the last test, A={6,10,15,30,42,70,105}, x=100, the optimum was 5 and Theorem B gave 8. Theorem A was not asserted for that general test.
- Completed-run time, including the directed tests: **132.455 seconds**.

A nontrivial equality case for Theorem B in the random results is A={3,5,8,10,12,15,16}, M=16, x=207182. CBC proved optimum 7, Theorem B gave 7, H=6, and 2n−H=8. An optimal set is {207184,207185,207188,207189,207190,207192,207195}.

The tests support the argument; they do not replace the proof or quantify over all interval positions.

Snapshot and closeout:

The first read of NOTES.md had SHA-256 `a27b8e199f19900a8d69dacf821ef08ad3b3a4b559f7be9434b49f8899569d1d`. A concurrent writer corrected the Construction during this review. The final reviewed snapshot, also recorded by the completed test run, has SHA-256 `42e9618efb054dc3bc09aabfd439592e4aa682b8867522e2b3d538efb0984de6`. The verifier hash is `d304908998f33231a16b5cb0f3a15efda83fb26b33a9007177619be4f9f61492`.

The source file `paper/sec_remains.tex` at the cited prior commit has SHA-256 `fad2489c5e39a5ecdfd15ce6ed9c2f9daba18daaf7f58ea5813e2c8b3f38c4de`. Its matching argument is independent of the manuscript's unverified general linear-bound claim.

Review work is complete. Remaining owner actions: acknowledge the prior result and add the zero-deficit convention. Next action: the coordinating agent decides how to revise and accept the exposition. There is no unresolved mathematical counterexample, active test process, or child task. No milestone acceptance receipt is due from this review sub-agent; acceptance remains with the coordinator.
