# Erdős 708: independent upper-bound attempt

No proof of any requested general linear bound, and no counterexample to
`g(n) <= 2n`, was obtained. The auxiliary statements below have proofs. No claim
of novelty is made for them. The final result label refers to the requested
resolution, not to the absence of useful auxiliary statements.

## Task record

- Owner: this independent GPT-6 Astra run, with max reasoning effort.
- Authority: the user's request for independent research and this report.
- Start: 2026-10-15 20:19 UTC. Limit: 90 minutes, ending by 21:49 UTC.
- Scope: this report and the supporting `astra_*` files in this directory.
  No other agents were used. Existing notes and programs were not changed.
- Outcome: the requested general bound remains unproved. A proposed induction
  step is disproved by an explicit infinite family. A premise about the LP is
  corrected. Restricted upper bounds and a conditional LP route are proved.
- Proof: full arguments below, exact integer checks in `astra_verify.json`, and
  clearly identified numerical solver evidence in `astra_experiments.json`.
- Status: complete after proof and artifact audit, 2026-10-15 21:02 UTC,
  about 43 minutes after the start and within the 90-minute limit.
- Remaining deliverable work: none. The requested mathematical resolution was
  not obtained; the negative result and the precise gaps are recorded here.
- Next action: none scheduled. No computation or delegate remains active.
- Unresolved mathematical questions: an induction that accounts for unused size
  allowance, or a uniform bound for the capped LP in Section 3.

## 1. Definitions and two elementary bounds

Write `h(A,I)` for the minimum size of a subset of `I` whose product is divisible
by `P = product(A)`. I use the intended “at most” convention for the uniform
bound. In particular, when `M < 2n`, the target is met by taking the whole
interval; it does not require padding a subset past the size of the interval.
The interval endpoints and `x` are integers.

For each prime `p`, put

    E_p = sum_{a in A} v_p(a),
    D(p,t) = #{a in A : p^t divides a}.

An interval of length `M` contains at least `floor(M/q)` multiples of every
positive integer `q`. Consequently

    v_p(product(I))
      = sum_{t>=1} |I intersect p^t Z|
      >= sum_{t>=1} floor(M/p^t)
      = v_p(M!).

Since `A` is a set of distinct integers in `[2,M]`, `P` divides `M!`. Thus `P`
divides `product(I)`. This proves feasibility and the bound `h(A,I) <= M`.
Merely observing that each `a` has a multiple in `I` would not prove product
divisibility, because those multiples can coincide.

Let `omega(a)` denote the number of distinct prime divisors of `a`.

**Proposition 1.** For every instance,

    h(A,I) <= sum_{a in A} omega(a).

**Proof.** For each prime `p` dividing `P`, select the `D(p,1)` elements of `I`
with the largest `p`-adic valuations. There are at least that many multiples of
`p`. At level `p^t`, this selection contains

    min(D(p,1), |I intersect p^t Z|)
      >= D(p,t)

elements divisible by `p^t`: both arguments of the minimum are at least
`D(p,t)`. Summing over `t` shows that its product supplies at least `E_p`
copies of `p`. Take the union of these selections over all relevant primes.
Its size is at most `sum_p D(p,1) = sum_a omega(a)`, and its product meets every
prime demand. Overlap between selections for different primes causes no loss
in this argument. Each prime's entire demand is met by its own selection. ∎

This also explains a limit of the level-count reformulation. It is sufficient,
but is stronger than product divisibility. For example, `A={2,4}`, `M=4`, and
`I={5,6,7,8}` admit `B={8}`. This covers the product 8, but fails the level-count
condition `|B intersect 2Z| >= 2`.

## 2. A restricted upper bound by factor packing

**Proposition 2.** Let `K >= 2` be an integer. If

    M^(K-1) >= (Kn)^(K+1),

then `h(A,I) <= Kn`. In particular,

    M >= (2n)^3  implies  h(A,I) <= 2n,
    M >= (3n)^2  implies  h(A,I) <= 3n.

**Proof.** Set `T = M/(Kn)`. The hypothesis is equivalent to

    M <= T^((K+1)/2),

and implies `T > 1`.

For each `a`, start with its prime factors, with multiplicity. Repeatedly merge
any two current factors whose product is at most `T`. This process terminates.
Every resulting factor is either at most `T`, or is an original prime greater
than `T`. A prime greater than `T` cannot participate in a merge.

If the final factors are `f_1,...,f_r`, each pair has product greater than `T`.
For `r >= K+1`, multiplication of all these pair inequalities gives

    a^(r-1) > T^(r(r-1)/2),
    a > T^(r/2) >= T^((K+1)/2) >= M,

which contradicts `a <= M`. Each input therefore produces at most `K` factors.

Across all inputs let `L` be the number of factors that are primes greater
than `T`, counted with multiplicity. Let `S` be the number of remaining factors.
Then `L+S <= Kn`.

First supply all demands for primes greater than `T`. If such a prime has
demand `E_p` and there are `N_p` multiples of it in `I`, select at most
`min(E_p,N_p)` of them. When `N_p >= E_p`, any `E_p` multiples supply enough.
When `N_p < E_p`, select all of them; the feasibility calculation in Section 1
shows that they supply enough. The union of these choices has size at most
`sum_{p>T} E_p = L`.

Now process the `S` small factors in any order. A factor `f <= T` has at least
`floor(M/f) >= Kn` multiples in `I`. Before it is assigned a host, fewer than
`Kn` elements have been selected. Choose an unused multiple of `f`.

The small-factor hosts are all distinct and avoid the previously selected
large-prime hosts. Their product supplies every small factor, with its full
multiplicity. The first selection supplies every large-prime demand. The final
union therefore covers `P` and has size at most `L+S <= Kn`. ∎

The proof uses large **primes**, not an unsupported assumption that large prime
powers cannot have been spent on smaller powers of the same prime.

**What this does not prove.** Fixing `K` leaves the range

    Kn < M < (Kn)^((K+1)/(K-1))

uncovered by the combination of this argument and `B=I`. Choosing a larger
fixed `K` narrows that range but does not remove it. Allowing `K` to grow with
`n` does not give an absolute constant.

For reference, these elementary arguments do give a uniform nonlinear bound:

**Corollary 2.1.** With natural logarithms,

    g(n) <= (1+o(1)) n log(n)/log(log(n)).

This is not a claimed new result and does not answer any requested linear
upper-bound question.

**Proof.** Fix `delta>0`, and choose a constant integer `K` such that
`(K+1)/(K-1) < 1+delta`. For all sufficiently large `n`, the hypothesis of
Proposition 2 holds whenever `M >= n^(1+delta)`. These instances need at most
`Kn` elements.

In the remaining range, `n+1 <= M < n^(1+delta)`. If an integer `a <= M` has
`r` distinct prime factors, the `j`-th smallest of them is at least `j+1`, so
`(r+1)! <= a <= M`. The elementary estimate

    log(r!) >= integral_1^r log(t) dt = r log(r)-r+1

implies, uniformly in this range,

    r <= (1+delta+o(1)) log(n)/log(log(n)).

For completeness, if `r` exceeded `(1+delta+eta) log(n)/log(log(n))` for any
fixed `eta>0`, the displayed factorial estimate would exceed
`(1+delta)log(n)` for all sufficiently large `n`, a contradiction. Apply
Proposition 1. Since `Kn` is smaller than this nonlinear scale for large `n`,
and since `delta>0` was arbitrary, the stated bound follows. ∎

## 3. The LP premise and a possible LP route

### 3.1 The fully capped LP is exact on the stated lower-bound construction

The usual LP relaxation of the binary exponent-cover problem is

    minimize sum_{b in I} z_b
    subject to sum_b v_p(b) z_b >= E_p  for every p dividing P,
               0 <= z_b <= 1.

The upper bounds on **all** variables are essential.

Consider the interval in `NOTES.md` for `ell >= 2`. It has one number `c` with
valuation 1 at every listed prime, one number `s_i` with valuation 2 at `p_i`
and zero at the other listed primes, and otherwise only numbers with valuation
1 at one listed prime. The demand at each prime is `ell+1`.

**Proposition 3.** On this construction the fully capped LP has optimum

    ell^2 - ell + 1,

equal to the integer optimum.

**Proof.** Put `beta=z_c`, `sigma_i=z_{s_i}`, and let `r_i` be the total weight
on the remaining multiples of `p_i`. The remaining groups are disjoint.
The objective is at least `beta + sum_i sigma_i + sum_i r_i`, and the constraints
give `r_i >= ell+1-beta-2 sigma_i`. Therefore the objective is at least

    ell(ell+1) - (ell-1)beta - sum_i sigma_i
      >= ell(ell+1) - (ell-1) - ell
      = ell^2-ell+1.

This calculation uses only `beta<=1` and `sigma_i<=1`, so it applies to fractional
solutions. Equality is attained by the integer selection consisting of `c`,
all `s_i`, and `ell-2` other multiples of each `p_i`. The interval has enough
such multiples: at least `floor(M/p_i)-2 >= p_ell-2 >= ell-2`. ∎

For comparison, deleting **all** upper bounds gives optimum `ell+1`. Assign
weight `ell+1` to `c` for the upper bound. For the lower bound assign dual weight
`1/ell` to each prime: `c` has total weight 1, every square host has weight
`2/ell<=1`, and every other useful host has weight `1/ell<=1`.

Keeping only `z_c<=1`, while removing the bounds on the other variables, gives
optimum `1+ell^2/2`, which is about `n=ell(ell+1)/2`. Indeed, for a fixed `beta`,
the remaining hosts cost at least half the remaining total exponent demand,
and square hosts attain that bound. The objective is

    beta + ell(ell+1-beta)/2,

minimized at `beta=1` for `ell>=2`. This relaxation permits a square host to
receive weight `ell/2`, which exceeds 1 when `ell>2`.

Thus “the LP is only about n” does not hold for the usual fully capped LP.
This family supplies no integrality gap for that LP.

### 3.2 A constant capped-LP bound would suffice for a constant integer bound

The following is a **conditional reduction**, not a proof of its hypothesis.

**Proposition 4.** Suppose there is an absolute constant `kappa` such that the
fully capped LP has optimum at most `kappa n` for every instance. Then

    g(n) <= max(3,kappa+4) n.

In particular, proving the capped-LP bound `2n` would already prove the explicit
integer bound `6n`. Using the standard estimate `pi(t)=o(t)` improves the
conclusion to `max(3,kappa+1+o(1))n`.

**Proof.** If `M >= (3n)^2`, use Proposition 2. Otherwise `sqrt(M)<3n`.

An input `a<=M` contains at most one prime greater than `sqrt(M)`, and that
prime has exponent 1. The total demand at all such primes is therefore at
most `n`. For each of them select `E_p` distinct multiples in `I`. These exist
because `E_p=D(p,1)<=floor(M/p)`. Their union has size at most `n` and meets
all large-prime demands.

Retain only the small-prime constraints in the LP. Its optimum is at most
`kappa n`. There are at most `r=pi(sqrt(M))<=pi(3n)` such constraints. At an
optimal extreme point, at most `r` variables lie strictly between 0 and 1.
To see this, if there were more than `r`, the columns on these variables would
have a nonzero linear dependence. A sufficiently small perturbation in both
directions along that dependence would preserve all row values and all bounds,
contradicting extremality. An optimal extreme point exists because the
nonempty feasible region is a bounded polytope.

Round each fractional variable up to 1. All coefficients are nonnegative, so
the small-prime constraints remain satisfied. The size increases by at most
`r`. Unite this selection with the large-prime selection. Each prime demand
was already met by one of the two sets, so their union still meets it. Its size
is at most `(kappa+1)n+pi(3n) <= (kappa+4)n`. Combining the two ranges proves the
explicit assertion. Replacing the last elementary prime count by `pi(3n)=o(n)`
gives the stated asymptotic improvement. ∎

### 3.3 The missing LP inequality

For nonnegative weights `w_p` on any finite collection of primes, define the
completely additive function

    F_w(m) = sum_p w_p v_p(m).

In the dual one can restrict to primes dividing `P`. Finite-dimensional LP
duality gives the exact dual objective

    sum_{a in A} F_w(a) - sum_{b in I} (F_w(b)-1)_+,

maximized over `w_p>=0`. Indeed, a dual variable `u_b>=0` for `z_b<=1` must
satisfy `F_w(b)-u_b<=1`; its least possible value is `(F_w(b)-1)_+`.

A sufficient condition for the bound `kappa n` is therefore the uniform
inequality

    sum_{m=1}^M (F_w(m)-kappa)_+
      <= sum_{b in I} (F_w(b)-1)_+.                         (LP-kappa)

To check sufficiency, write `F_w(a)<=kappa+(F_w(a)-kappa)_+`, sum over `A`,
and use `(LP-kappa)` in the displayed dual objective.

In fact, the uniform capped-LP bound and this inequality are equivalent when
inputs with maximum at most the interval length are allowed. For necessity,
take `A={m in [2,M]:F_w(m)>kappa}`. Any feasible fractional solution of cost at
most `kappa|A|` satisfies

    sum_{a in A}F_w(a)
      <= sum_b z_b F_w(b)
      <= sum_b z_b + sum_b (F_w(b)-1)_+
      <= kappa|A| + sum_b (F_w(b)-1)_+.

This is `(LP-kappa)`; the empty input gives the inequality directly. Extending
the interval beyond `max(A)` makes a feasible solution available by using any
subinterval of length `max(A)`, so the extended formulation does not strengthen
the assumed uniform bound.

**Failure point.** I did not prove `(LP-kappa)` for any absolute constant.
Counts of multiples control `sum F_w`, but do not control the positive-part
sum after the threshold is applied. The lower construction already refutes
`kappa=1`: for `ell>=3`, its capped LP exceeds `n`. The same construction does
not refute `kappa=2`. This is a precise remaining LP problem, not a proof that
the LP approach is impossible.

## 4. Induction: unbounded increases in the per-instance minimum

### 4.1 A small exact example

Let

    A0 = {2,4,6,8,10,12,14,20},
    a = 16,  M = 20,  x = 25184,
    I = {25185,...,25204}.

Then

    h(A0,I) = 5,
    h(A0 union {16},I) = 9.

Thus adding one input can increase the exact optimum by more than two, even
when the old selection can be replaced in full.

**Proof.** The 2-adic demand of `A0` is 13. Its odd part is
`3^2 * 5^2 * 7 = 1575`. The five numbers

    B0 = {25188,25192,25196,25200,25204}

have 2-adic valuations `2,3,2,4,2`, whose sum is 13. The number
`25200=16*1575` supplies the entire odd part. Hence `B0` covers `A0`.

The interval's valuations, in decreasing order, are

    4,3,2,2,2,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0.

The four largest sum to 11, so no four numbers cover `A0`. Adding 16 raises
the 2-adic demand to 17. The eight largest valuations sum to 16, so at least
nine numbers are needed. Adding `25186,25190,25194,25198` to `B0` supplies four
more copies of 2, so nine suffice. ∎

Here the enlarged input has `n=9` and `2n=18<M=20`. This is not an example in
the trivial `M<=2n` range, but its optimum 9 is still well below `2n`.

### 4.2 An infinite family

**Proposition 5.** The increase `h(A0 union {a},I)-h(A0,I)` is unbounded,
even with `max(A0)=max(A0 union {a})=M` and `2|A0 union {a}|<M`.

**Proof.** Fix an integer `e>=4`, and set

    M = 2^e+4,
    r = M/4 = 2^(e-2)+1,
    a = 2^e,
    A0 = ({4j:1<=j<=r} minus {a}) union {4j-2:1<=j<=e}.

The two displayed parts of `A0` are disjoint. The second lies in `[2,M]`.
The set has size `r+e-1` and maximum `M`. Also `r>e`, so
`2(r+e)<4r=M`.

Let `H` be the odd part of `product(A0)`, and put

    x = 2^e(H-1),
    c = x+2^e = 2^e H.

Since `H` is odd, `x` is divisible by `2^(e+1)`. Since `M<2^(e+1)`,

    v_2(x+j)=v_2(j)  for 1<=j<=M.

Let `B0={x+4j:1<=j<=r}` and write

    S = sum_{j=1}^r v_2(4j) = 2r+v_2(r!) = 3r-2.

For the last equality, `r=2^(e-2)+1`, so
`sum_{t>=1}floor(r/2^t)=2^(e-2)-1=r-2`.
Deleting `a` from the multiples of 4 removes `e` copies of 2; adding the `e`
numbers congruent to 2 modulo 4 restores them. Thus `A0` has 2-adic demand `S`.
The set `B0` supplies exactly `S`, and it contains `c`, which is divisible by
the entire odd part `H`. Hence it covers `A0`.

Precisely the `r` numbers of `B0` have 2-adic valuation at least 2. Every other
number in `I` has valuation 0 or 1. Consequently the largest possible valuation
sum for `r-1` numbers is less than `S`, and `h(A0,I)=r`.

After adding `a`, the demand is `S+e`. Among `r+e-1` numbers, the largest possible
valuation sum is `S+e-1`: take all `r` high-valuation numbers and `e-1` numbers
of valuation 1. There are exactly `r` valuation-1 numbers, and `e<=r`. Therefore
at least `r+e` numbers are required. The union of `B0` with any `e` valuation-1
numbers attains that bound. The increase is exactly `e`. ∎

This disproves a uniform bounded increase for **a fixed instance**. It does
not disprove a bound on `g(n)-g(n-1)`, and it does not disprove `g(n)<=2n`.
Indeed, in this family the enlarged optimum equals its input size `r+e`.
An induction can still use unused size allowance accumulated at earlier
steps. What fails is an induction that demands at most two extra hosts at
every step, even after reoptimization.

### 4.3 What residual tracking does prove

**Proposition 6.** Let `F` be a forbidden set of `s` elements of an interval of
length `M`. Let `d<=M` be a positive integer dividing the product of the
remaining elements. If `k` is the minimum number of remaining elements whose
product is divisible by `d`, then, for `k>=2`,

    2^(k-2) <= s+k-2.

In particular, `k<=1` when `s=0`; when `s>=1`,

    k <= floor(log_2(s))+3.

**Proof.** Take a minimum set `{c_1,...,c_k}`. Distribute the required prime
exponents of `d` among these hosts, obtaining integers `d_i|c_i` with
`product_i d_i=d`. Such a distribution exists because their product covers `d`.
Each `d_i>=2`: otherwise the remaining `k-1` hosts would already cover `d`.

For distinct `i,j`, a multiple of `d_i d_j` outside `F union {c_1,...,c_k}`
would replace `c_i,c_j` by one host. A multiple equal to `c_i` or `c_j` would
let the other host be deleted. Both contradict minimality. Hence every
multiple of `d_i d_j` in the interval belongs to
`F union ({c_1,...,c_k} minus {c_i,c_j})`, a set of size `s+k-2`. But there are
at least

    floor(M/(d_i d_j))
      >= d/(d_i d_j)
      = product_{l!=i,j} d_l
      >= 2^(k-2)

such multiples. This proves the inequality.

If `s=0`, a multiple of `d` directly gives `k<=1`. For `s>=1`, the bound is
immediate when `k<=3`. For `k>=4`, put `m=k-2>=2`. Since `2^(m-1)>=m`,
`2^m<=s+m` implies `2^(m-1)<=s`, and therefore `k<=3+log_2(s)`. ∎

To apply this in an induction, suppose `B` covers `A0`, put

    R = product(B)/product(A0),
    d = a/gcd(a,R).

The integer `d` is the exact remaining demand. It divides the product of
`I minus B`: for each prime, the full interval has at least the demand of
`A0 union {a}`, and removing `B` leaves at least the positive deficit.
Proposition 6 therefore gives an extension by at most
`floor(log_2(|B|))+3` numbers when `B` is nonempty.

This proves a logarithmic extension bound, not a two-number bound. The family
in Proposition 5 has `|B0|=2^(e-2)+1` and needs `e` additional numbers, so the
logarithmic order is real, not merely a loose estimate from this proof.

## 5. The five proposed routes: exact limits of this attempt

**Residual-exponent induction.** The residual `d=a/gcd(a,R)` is the correct
quantity, and Proposition 6 bounds its repair cost. Proposition 5 rules out
a constant per-step cost. The missing assertion is an amortized one: expensive
extensions must be charged against earlier unused allowance within `2n`.
No invariant proving that assertion was found.

**Hall/König with element halves and per-prime capacities.** A unit-capacity
host graph discards useful sharing. For example, take `A={5,7}` and
`I={32,...,38}`. The only multiple of either prime is 35. There is no assignment
of distinct hosts to the two prime demands, or of disjoint one- or two-number
representations to the two inputs. Yet `{35}` covers their product. Splitting
either prime into integer factors cannot remove this obstruction.

Giving 35 separate capacities for 5 and 7 fixes that example, but changes the
problem: the cost is paid once when a host is activated, while its separate
prime capacities can all be used. Independent Hall conditions for each prime
control feasibility, not the number of activated hosts. The individual Hall
conditions hold in the lower construction too, where the optimum exceeds `n`.
No Hall condition establishing a cost of `2n` was proved. This is not a
counterexample to every possible strengthened matching formulation.

**Charging two new numbers per input.** The observation
`floor(M/(q_1 q_2))>=q_3` when `q_1 q_2 q_3<=M` is valid. It does not imply that
any of those hosts remain unused. In the exact example of Section 4.1,
`16=4*2*2`, and both multiples of 8 in the interval, 25192 and 25200, already
belong to `B0`. All remaining even numbers have valuation 1. The residual 16
therefore requires four new hosts. In the infinite family the corresponding
cost is unbounded. A successful charging proof must account for the previous
work done by these blocked hosts; counting their total supply is insufficient.
The factor-packing proof avoids this issue only when each small factor has at
least the entire proposed selection budget in available multiples.

**Complement `C=[1,M] minus A`.** Put

    Q = product(I)/M! = binomial(x+M,M),
    R = product(C) Q = product(I)/product(A).

For `B subset I`, with `J=I minus B`, there is an exact equivalence

    product(A) divides product(B)
      if and only if product(J) divides R.

Proof: `product(B)/product(A)=R/product(J)`, so one ratio is an integer exactly
when the other is. Thus `|B|<=2n` is equivalent to finding `|J|>=M-2n` whose
product divides `R` (the size condition is automatic when `M<=2n`). In prime
exponents, the constraints for `J` are exactly the original constraints after
substitution `z_B=1-z_J`. The binomial factor supplies the correct total
surplus, but the constraints still couple the same selected positions across
primes. No additional packing lemma was obtained from the complement.

**Direct CRT construction.** For fixed `A` let

    Q_A = product_{p|P} p^(E_p).

The capped value `min(v_p(x+j),E_p)` is determined by `x+j mod p^(E_p)`.
Therefore `h(A,I)` depends only on `x mod Q_A`. Conversely the prime-power
residues can be chosen independently and combined by CRT. This is an exact
finite formulation, but its state space can be enormous.

I considered replacing the semiprime lower construction by products of three
or more components. The exact obstacle to its simplest extension is that if
`q_1 q_2 q_3<=M`, the interval has at least two multiples of `q_1 q_2`. It cannot
have only one common center carrying every pair, with all other hosts carrying
at most one component. For example, for three distinct relevant primes this
already forces a second host carrying a pair. Thus the proof that makes the
semiprime construction hard does not extend by simply increasing its degree.
This observation neither proves an upper bound for all CRT arrangements nor
excludes a more complex counterexample. No such counterexample was found.

## 6. Computation and exact proof status

All runs were local, sequential, at nice level 10. CBC used one solver thread.
The Python driver invoked one CBC solve at a time. No agents or external model
calls were used.

`astra_experiments.py` used PuLP 2.9.0/CBC. Its recorded output is
`astra_experiments.json`.

- It checked the capped LP on the existing CRT examples with primes
  `(11,13)`, `(17,19,23)`, and `(37,41,43,47)`. Solver objectives were 3, 7,
  and 13, respectively. Proposition 3 proves these values without relying on
  floating-point optimizer certificates.
- With seed 7081501 it sampled 700 prefix instances, with `M` chosen from
  `{24,30,36,48,60,72,90,120,150,180,210}` and `x` from `[0,10^8)`.
  It tested 58,201 additions to the solver-reported optimal prefix covers.
- The test for a repair using at most two unused numbers was exact: group
  unused numbers by `gcd(b,d)`, and check all pairs of group types, including
  the requirement for two distinct numbers when both types agree.
- It found one failed two-number extension. The solver also reported that
  the fully reoptimized minimum rose from 5 to 8. This led to the smaller
  exact example and infinite family in Section 4. The sampled solver run took
  about 173.15 seconds. It was not an exhaustive search over inputs or CRT
  residues.

`astra_verify.py` uses Python integer arithmetic and no optimizer. Its output
is `astra_verify.json`.

- It checks the family in Proposition 5 for `e=4,...,10`, with exact sorted
  valuation bounds and explicit selections. The increases are 4 through 10.
- For `e=4` it directly verifies both product divisibilities with Python
  integers. The larger family checks verify the odd-part carrier, every
  interval 2-adic valuation, both exact lower bounds, and the host counts.
- It runs the constructive factor-packing method on 90 seeded instances:
  45 for `K=2` at `M=(2n)^3`, and 45 for `K=3` at `M=(3n)^2`, with
  `2<=n<=10`. It checks the number of factors, the number of chosen hosts,
  and exact product divisibility. All checks passed. These tests are checks
  of an implementation; the uniform theorem is proved in Section 2.

Reproduce the recorded computations from this directory with:

```sh
nice -n 10 .venv/bin/python astra_experiments.py
nice -n 10 python3 astra_verify.py
```

## 7. What remains open after this attempt

There is no verified counterexample to `g(n)<=2n` in this report. The explicit
counterexamples concern a proposed induction step, not the conjecture.

The strongest uniform upper bound proved here is nonlinear. The `2n` and `3n`
factor-packing bounds have explicit restrictions on `M`. The LP reduction is
conditional, and its required constant bound remains unproved. In particular,
the conditional value `6n` in Section 3 is not an established upper bound.

The two concrete unresolved steps are an induction with a valid account of
unused size allowance, or `(LP-kappa)` for some absolute constant. None of the
arguments above supplies either step.

RESULT: NO NEW THEOREM
