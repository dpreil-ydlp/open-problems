# Independent review of Theorem C

VERDICT: CORRECT WITH MINOR FIXES

The stated bound is correct: for a set of n distinct integers at least 2,
M = max(A) > (2n+1)^3 implies h(A,x) <= 2n for every integer x >= 0.
I found no mathematical BLOCKER in Lemmas C1–C3, Theorem C, or the stated
counterexample reduction. The sparse result is already in a public prior
preprint, with a better threshold. The introduction also states a stronger
bound than Theorem C proves.

Review date: 2026-10-15. Owner: Sol review sub-agent; the parent owns acceptance.
Authority: the user's referee request, with a 40-minute budget. Review scope:
Section 1, Section 3A Lemma 3, Section 3B, the requested tests, and prior art.
No child tasks were created. NOTES.md and other agents' files were not edited.

1. **MINOR — Theorem C is not new; a stronger prior sparse theorem exists.**
   Haoyu Chen's *Explicit upper bounds for the Erdős–Surányi function g(n)*
   states the bound 2n whenever M >= 8n^3. See
   [Theorem 1.3, source lines 124–129](https://github.com/chy4pro/erdos-708-explicit-upper-bounds/blob/dc150fd723184cc4e6f367aac6e7a8c9c7890f34/paper/main.tex#L124-L129)
   and its
   [proof in Section 5, lines 393–439](https://github.com/chy4pro/erdos-708-explicit-upper-bounds/blob/dc150fd723184cc4e6f367aac6e7a8c9c7890f34/paper/main.tex#L393-L439).
   The source is dated 8 September 2026; the inspected repository commit is
   `dc150fd723184cc4e6f367aac6e7a8c9c7890f34`, dated 12 October 2026.
   Since (2n+1)^3 > 8n^3, that theorem includes every instance of Theorem C.
   Its method also matches: split the components, assign large prime powers
   by prime, then use fresh multiples for the small groups. I checked those
   parts of the source proof, not only its abstract. They are valid. This is
   a prior public preprint/repository result; I did not establish journal
   acceptance or rebuild its Lean proofs. A concurrent edit added Section 1A
   during this review. It now treats novelty as unresolved and calls Chen's
   sparse bound a conjecture. That classification is incorrect: it is a
   theorem with the proof linked above. Cite that theorem and describe
   Theorem C as an independent proof of a weaker prior result. The last
   sentence still says that any general linear bound would be new; revise
   it to acknowledge the claims now listed in Section 1A. This review does
   not certify Chen's separate general linear bounds.

2. **MINOR — The introduction overstates the bound from Theorem C.**
   Its first paragraph assigns the bound 2n−1 to both special regimes.
   Theorem A proves 2n−1; Theorem C proves 2n. Change the introductory sparse
   bound to 2n. This is an unsupported strengthening in the summary, not a
   defect in the theorem being reviewed.

3. **MINOR — Section 1, Remark (b), has an off-by-one in its padding step.**
   M >= n+1 does not ensure that [2,M] contains an element outside A.
   For example, n=2 and A={2,3} give M=3=n+1 and no such element. The stated
   padding step requires M >= n+2. If that argument is used to prove global
   monotonicity, its boundary case M=n+1 needs a separate argument. Theorem C
   uses neither this remark nor monotonicity, and (R) is far from this boundary.

The requested proof checks follow.

**Setup and (a), Lemma C1.** Put s=2n+1, so M=sT. Condition (R) gives
T>s^2>s>=3. In particular,

    T^2 = M^2/s^2 > Ms > M.

Thus two components greater than T would have product greater than M.
The inequality chain in C1 is correct, including its strict signs.
The domain of x is the nonnegative integers, as in Section 1. Finiteness of
h follows from the distinctness of A: product(A) divides M!, and M! divides
product(x+1,...,x+M) by the binomial coefficient identity. This also checks
the existence assertion without ignoring repeated prime factors.

**(b), Lemma C2.** Group products Q are positive integers. Q<=T implies
M/Q>=s, and s is an integer, so floor(M/Q)>=s. There is no rounding loss.
The exact count in I is

    floor((x+M)/Q) - floor(x/Q) >= floor(M/Q).

Hence at least 2n+1 candidate numbers exist. Removing fewer than 2n+1
selected numbers leaves one. Equality Q=T is allowed.

**(c), Lemma C3.** Its hypotheses imply at least two components: a single
component would equal a>T and thus be big. In case (i), the chosen component
is one group and the other components form a nonempty second group. All
inequalities are valid:

    a/q_j < a^2/T^2 <= M^2/T^2 = s^2 < T.

The bound a<=M and (R) are both used here. In case (ii), minimality gives
P^(k−1)<a/T. Multiplication by the positive q_k<=T^2/a gives

    P^(k) < (a/T)(T^2/a) = T.

The strict sign comes from the previous partial product, so equality in the
bound for q_k causes no problem. Also P^(k)>=a/T, so a/P^(k)<=T. We have
k>=1, and k=r would give a=P^(k)<T, a contradiction. Both groups are nonempty.
T>1 justifies the endpoint P^(r)=a>=a/T used to find k.

Here is a numeric attempt to break the splitting lemma with three components
near T^0.6. Take n=5, M=11000, T=1000. The pairwise coprime prime powers
61, 64, 67 are all near 1000^0.6=63.095734448.... Their product is 261568.
Every two-component product exceeds T: they are 3904, 4087, and 4288. Thus
they cannot be packed into two groups at this threshold. But a=261568>M,
so this is not a counterexample. Condition (R) holds; the missing hypothesis
is exactly a<=M. If M is increased to 261568 to admit that element, T changes
to 261568/11, and C3 gives groups 61 and 4288, both below T.

The scaling explains the failed attack: (R) gives s<sqrt(T), hence
M=sT<T^(3/2), whereas three components each of size T^0.6 have product
T^1.8. This does not exclude all triples of comparable components. Valid
examples are handled: at n=5, M=1332, a=792 has components 8,9,11 and case
(ii) gives 8 and 99. At the same n,M, a=1230 has components 2,3,5,41 and
case (i) gives 41 and 30. These examples were checked with exact arithmetic.

**(d), Phase 1.** Fix a prime p and process its big tokens in decreasing
exponent order. Before a token of exponent v, let j tokens at p have been
placed. All j have exponent at least v. Together with the current token,
they come from j+1 distinct elements divisible by p^v. Thus

    j+1 <= D(p,v) <= N(p,v).

All j previous hosts are multiples of p^v, so excluding them leaves a host.
This proves the nested availability argument even when exponents differ.
Only earlier hosts at the same prime must be excluded. A host at p may also
host a token at p' != p; their required prime powers are coprime. Such reuse
is valid and can reduce the set size. It was observed in the directed tests.

**(e), Phase 2.** For an element with big component q,

    a* = a/q < M/T = s < T.

The last comparison follows from T>s^2. Hence its residual part needs zero
groups if a*=1, and one group otherwise. Elements without a big component
need at most two groups. To avoid a circular appeal to the final bound,
count the planned groups before choosing their hosts. If b elements have
big components and G is the number of Phase 2 groups, then

    G <= b + 2(n-b),
    |B_1|+G <= b+G <= 2n.

Before group j, the selected count is |B_1|+j−1, at most 2n−1, including
at the last step. Phase 1 hosts are included in that count. C2 therefore
applies at every step. The existing text has the needed count; making this
prefix form explicit would improve clarity, but no proof repair is needed.

**(f), Injectivity.** The groups of one element partition its prime-power
components, so a prime is assigned once for that element. At a fixed prime,
Phase 1 hosts are distinct. Each Phase 2 host differs from every Phase 1
host and every other Phase 2 host, and receives assigned components from
only one element. Incidental divisibility by other elements has no effect
on this assignment. Thus h(a,p) is injective in a for each fixed p.

**(g), Slot criterion.** Each assigned host for (a,p) is divisible by the
full component p^v_p(a). Restricting the injection to elements divisible by
p^v gives at least D(p,v) distinct hosts divisible by p^v. Summing those
counts over v gives the required total valuation at each prime, exactly
as in Lemma 3. Reuse across different primes causes no double counting
within any one of these sums.

**(h), Prime powers and small elements.** If a=p^v>T, there is one big
token, its residual is 1, and one Phase 1 host suffices. If a<=T, it has
no big component and is one Phase 2 group. No unnecessary empty group is
introduced. A prime-power component equal to T is small, as required.

**(i), Prior art and Corollary 6.** The prior sparse theorem and its source
are given in objection 1. Corollary 6's conclusion about a counterexample
is correct: a pair (A,x) with h(A,x)>2n must have M<=(2n+1)^3; combining
this with Theorem A gives the stated restriction on the number of prime
factors. The wording about g(n) is understood as a bound for this restricted
class of A, since unrestricted g(n) itself does not have an M parameter.
The prior result gives the sharper restriction M<8n^3. I found no earlier
journal source for the exact sparse statement in the bounded search; the
public prior proof is enough to rule out a novelty claim for Theorem C.

Computational evidence is in
[the test script](review_sol_theorem_c_check.py) and
[the complete results](REVIEW-SOL-THEOREM-C-RESULTS.json). Run:

```sh
cd /Users/davidpreil/Projects/open-problems/math/erdos708
.venv/bin/python review_sol_theorem_c_check.py
```

The script uses only the Python standard library and the existing PuLP/CBC
installation: Python 3.13.2, PuLP 2.9.0, bundled CBC. Seed: 708150103.
Every threshold comparison in the construction and splitting tests uses
integers after clearing positive denominators. The decimal T^0.6 value is
only a display value for the excluded example.

For the optimum, the model minimizes selected cardinality subject to the
total valuation demands, not the stronger slot demands. Equal valuation
vectors are grouped into integer variables with capacity equal to the
number of distinct interval integers having that vector. Valuations are
capped at their total demand, which preserves feasibility. Both PuLP status
and CBC solution status must report an optimum. Each recovered witness is
then checked by integer product division. No timeout or feasible-only
solution is accepted as an exact optimum.

The completed run passed all checks:

- 60 random sets: 12 each for n=1,2,3,4,5. Each set contains M and has its
  other elements sampled without replacement from [2,M−1]. Each M was
  sampled in ((2n+1)^3, 3(2n+1)^3].
- For each set, an initial x and eight proposals were evaluated by the exact
  solver. The hill climb accepts a proposal with at least the current best
  optimum. Proposals mix local changes, moves near prime-power multiples,
  and random positions in a finite valuation period. This gives 540 random
  interval evaluations. It is a short heuristic search, not a certificate
  of the worst x for any set.
- 12 directed interval evaluations cover mixed exponents at the same prime,
  cross-prime Phase 1 reuse, empty residuals, Q=T, prime maxima, three-component
  elements, and an instance requiring more than n selected integers.
- Total: 552 exact optimal solves and 1104 verified constructions, with both
  first-available and random host/group choices. Every constructed B lies
  in I, satisfies product(A) | product(B), and has size <=2n. Every exact
  optimum is <=2n. The script also checks the per-prime injections and every
  required slot inequality directly. There were zero violations.
- The largest constructed sizes for n=1,...,5 were 2,4,6,8,10. Thus the tests
  do reach the full count 2n and check freshness before the last choice.
- All 98,787 integers a in [2,M] were classified across these 13 pairs:
  (1,28), (1,81), (2,126), (2,375), (3,344), (3,1029), (4,730), (4,2187),
  (5,1332), (5,3993), (8,4914), (8,14739), (20,68922). All pairs satisfy (R).
  C3 applies to 59,998 of these integers: 39,814 in case (i), 20,184 in case
  (ii). Every computed split passed. An independent enumeration of component
  subsets also found a valid partition for every eligible integer.
- C2 was checked for every residue x mod Q and every integer Q<=T at
  (n,M)=(1,28),(2,126),(3,344),(5,1332): 8,976 exact count checks, all passed.

For the 60 hill-climbed random instances, the best optima were: n=1, twelve
values of 1; n=2, twelve values of 2; n=3, twelve values of 3; n=4, two values
of 3 and ten of 4; n=5, eight values of 4 and four of 5. These random sets
alone were not close to disproving 2n.

A directed hard instance avoids that limitation. Take

    A = {323,391,437} = {17·19,17·23,19·23},
    M = 437 > 343 = (2·3+1)^3,
    x = 49454635.

The exact optimum is 4, attained by
{49454644,49454646,49454649,49454853}. The construction selects the valid
six-element set
{49454644,49454646,49454649,49454663,49454666,49454669}.
There is also a direct lower-bound certificate: c=49454853 is the unique
multiple of any product of two of 17,19,23 in I, its valuation at each is 1,
and I has no multiple of 23^2. With c selected, three further single-prime
hosts are needed. Without c, two hosts are needed for 23 and one each for
17 and 19. Thus three selected integers cannot suffice.

The directed equality test has n=5, M=1452, T=132 and contains a=132. Its
single group Q=132 is exactly T; the script asserts that equality and
verifies its host. The mixed-exponent case A={128,256,512,1024,1536} at
x=234567 assigns the big 2-powers 1024,512,512,256 to four distinct hosts.
For cross-prime reuse, A={128,243,625,729,1332}, x=14171759999 assigns tokens
at primes 2,3,5 to the shared host 14171760000, while the second token at
prime 3 receives a different host. All slot checks still pass.

The initial NOTES.md SHA-256 was:

    465c189288841c47f0cf112f0eb223d299a1b4b8692f5c3aafb021038b3f13ea

Another writer revised the introduction and inserted Section 1A during
this review. I re-read the revised source; Lemma 3 and the mathematical
text of Section 3B are unchanged. The final tested and reviewed SHA-256 is:

    53157d03e9b4ed4533ced389827e2108eacd1a75beb26d6ab85970ae4567d4e1

The JSON records that same final hash before and after the completed test
run. I did not edit NOTES.md. The version change is recorded so that the
report does not claim the source stayed unchanged throughout the review.

The review and its required checks are complete within budget. Remaining
work belongs to the parent: assess the review, apply the document fixes if
accepted, and decide how to cite the prior result. No further computational
check or human decision is needed to complete this referee task. The broader
2n conjecture remains open; this review certifies only the stated sparse bound.
