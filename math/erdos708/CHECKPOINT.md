# Erdős #708 — resume checkpoint (written 16 Oct 2026)

Read this first when resuming. It is the state of the attack, what is settled, what is open, what has been ruled out, and where every artifact lives. Everything here is in this directory of https://github.com/dpreil-ydlp/open-problems (branch master, tag `erdos708-checkpoint-1`).

## 1. The problem, exactly

A = {a_1 < ... < a_n}, a_1 ≥ 2, M = a_n. For x ≥ 0, I_x = {x+1, ..., x+M}. h(A,x) = least |B|, B ⊆ I_x, with ∏A | ∏B. g(n) = sup over A, x of h(A,x). Known since 1959/1992: g(2)=2, g(3)=4, g(n) > (2−ε)n. Erdős's question: g(n) ≤ (2+o(1))n, or even g(n) ≤ 2n. Prize $100. Primary sources transcribed in SOURCES.md; statement reconciliation in STATEMENT.md. Use the "at most g(n) numbers" reading.

## 2. What is proved (with proofs and referee reports in this directory)

| Result | Where | Status | Prior art |
|---|---|---|---|
| Lower bound construction has exact value h = 2n − 2ℓ + 1 for n = ℓ(ℓ+1)/2 under 2p₁² > p_ℓ² + 2p_ℓ | NOTES.md §2, VERIFICATION-LOWER.md (ILP: 3, 7, 13 confirmed) | proved, machine-checked | Erdős–Surányi construction; the exact count is ours, Chen states only (2−o(1))n |
| Theorem A: ω(a) ≤ 2 ∀a ⇒ h ≤ 2n − H ≤ 2n − 1 | NOTES.md §3A, REVIEW-SOL-THEOREM-A.md | proved, refereed (no blockers); 300 random instances pass | rediscovery: Chen main.tex 534–544 and sec_remains.tex 290–323 |
| Theorem B: h ≤ Σ_c (1 + Σ_{a∈S_c} ω(a) − |P(S_c)|) (hub-and-fill) | NOTES.md §3A | proved, refereed | rediscovery: Chen's intermediate inequality |
| Theorem C: M > (2n+1)³ ⇒ h ≤ 2n | NOTES.md §3B, REVIEW-SOL-THEOREM-C.md (552 exact solves, 59,998 split cases pass) | proved, refereed (minor fixes applied) | weaker form of Chen Theorem 1.3 (M ≥ 8n³) |
| Slot criterion: B works if |B ∩ p^vℤ| ≥ D(p,v) := #{a : p^v | a} for all prime powers; supply always suffices per slot | NOTES.md §3A Lemma 3 | proved | standard |

## 3. Prior work (must cite; see PRIORWORK.md, LITERATURE.md)

Haoyu Chen, *Explicit upper bounds for the Erdős–Surányi function g(n)*, repo chy4pro/erdos-708-explicit-upper-bounds (local clone, untracked: priorwork/chy4pro/). Claims: g(n) ≤ 12n for all n (Lean 4 kernel-checked per author, CI log 12 Oct 2026); 11n refereed, not formalised; 2n for M ≥ 8n³ (Thm 1.3); 2n whenever the input–prime incidence graph has cycle rank β ≤ n (collision-cycle theorem, sec_remains.tex 295–329); hinge-inequality/LP framework giving (c+2)n from a hinge threshold c, with threshold 2 reduced to a remaining case (≥ 5 active primes, low atom mean). erdosproblems.com lists it as a pending partial claim, unreviewed by the site. The (2+o(1))n and 2n questions are open in Chen's own account.

## 4. The open gap, precisely

Dense regime M < 8n³, sets containing elements with ≥ 3 distinct prime factors, incidence cycle rank β > n. There, fresh multiples of two-component groups (product ≤ M/(2n+1)) are not guaranteed, so hosts must be shared across elements subject to "one token per prime per number".

## 5. What has been tried and proved NOT to work (do not retry as-is)

- Singles-only fill after hubs (Theorem B): costs Σω − |P| per group; fails 2n for ω ≥ 3 groups on few primes.
- Fixed "split off the largest prime" rule with distinct hosts: Sol proved an asymptotic Hall violator (A_M = even numbers ≤ M with ≥ 2 odd prime factors; exact certificate M = 3·10⁸, x = 2000000000000001416) that persists as M/n → ∞. SOL-UPPER-ATTEMPT.md §2.
- Two-number induction (remove largest/smallest element, add ≤ 2): Astra proved unbounded increases defeat it. ASTRA-UPPER-ATTEMPT.md.
- Forbidden-point induction: infeasible (forbidding the unique multiple of a prime element). NOTES.md §4.
- Complement-profile formulation using only the exponent profile of C = [1,M] \ A: too strong even for n = 1 (Sol §4).
- LP duality alone: LP ≈ n on Erdős's instance while OPT ≈ 2n; integrality gap 2. Any proof is combinatorial.
- Counterexample search: 85 structured families, 16,777 exact ILP solves, CRT hubs + residue hill-climb: nothing above 2n (search/RESULTS.md). Conjecture looks true.

## 6. Ideas NOT yet tried (start here next time)

1. **Combine Chen's cycle-rank theorem with pair-hosting.** When β > n, the incidence graph has many cycles ⇒ many elements share pairs of primes ⇒ by counting, numbers divisible by those prime pairs are forced to exist in I (≥ ⌊M/(pq)⌋ each). Quantify: can the excess cycles be "paid" by pair-hosts at rate ≥ 1 per excess cycle? Target: h ≤ n + β − (something) ≤ 2n.
2. **Adaptive split choice.** Sol's obstruction kills a fixed rule; the per-element choice of which component to separate is free. Formulate as a matching with element-chosen edges; try Aharoni–Haxell-type conditions or an alternating-path argument where the residual chosen for each element depends on current slot occupancy.
3. **Read Chen's hinge route (sec_h97.tex, sec_remains.tex 53–137)** and see whether his remaining threshold-2 case (≥ 5 active primes, low mean) can be attacked with Theorem C's splitting lemma, which handles exactly the low-mean (many small components) situation when M is large; the open part is M < 8n³.
4. **Uniform-scale dense case first.** Prove 2n for A = all triple products of ℓ primes near M^{1/3} (pair-multiples ≈ M^{1/3} each, demand per pair ℓ − 2); then mixed scales. A clean sub-theorem here would be new.
5. **Regime push for Theorem C.** The cube exponent comes only from Case (i) of Lemma C3; investigate whether hosting (not fresh) can replace Case (i) to get (2n+1)^{2+ε}, matching or beating Chen's 8n³ (small but new if it works).

## 7. Tools and how to rerun

- Exact evaluator (ILP, PuLP/CBC): `verify_lower.py` (functions reusable), `search/` runner and ledger `search.jsonl`, review scripts `review_sol_theorem_a_check.py`, `review_sol_theorem_c_check.py`. Venv: `.venv/` in this directory; run with `.venv/bin/python <script>`.
- Lower-bound CRT instances: VERIFICATION-LOWER.md lists x for (11,13), (17,19,23), (37,41,43,47).
- Model roles used: Claude Fable (proofs, direction), GPT-6.1 Sol (refereeing; ultra for research), GPT-6 Astra max (independent research), GPT-6 Luna (computation, literature). Each engine attempt ran ~90 min and is recorded; do not repeat them with the same brief.

## 8. Publication state

Nothing on #708 has been sent anywhere. The natural first external step is a short note to Thomas Bloom via the erdosproblems.com feedback link offering the exact lower-bound count 2n − 2ℓ + 1 (Theorem 1 in NOTES.md) for the entry's remarks, since Chen's manuscript states it only asymptotically. Hold until any new upper-bound progress is reviewed, or send now as a small standalone remark.
