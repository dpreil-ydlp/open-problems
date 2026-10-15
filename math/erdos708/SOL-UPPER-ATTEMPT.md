# Erdős 708: upper-bound research attempt

15 October 2026. Research owner: the Sol research sub-agent. Final acceptance belongs to the director. Research limit: 90 minutes.

**No general bound \(g(n)\leq 2n\), \(g(n)\leq(2+o(1))n\), or \(g(n)\leq Cn\) is proved here. No counterexample to \(g(n)\leq2n\) is claimed.** The main outcome is a proved obstruction of the requested type (5): a natural, fixed rule for making two halves has a Hall violator. The obstruction persists when \(M/n\) is arbitrarily large.

There are also two useful results:

- A complete proof that \(h(A,x)\leq2n\) when \(M\geq(2n)^3\). This does not cover the full problem.
- A proof that the proposed complementary condition using only the exponent profile of \(C=[1,M]\setminus A\) is too strong. Even for \(n=1\), it can require arbitrarily many deletions.

I also give an exact obstruction to an induction step that allows additions but no exchanges, and a specific limit of the uniform-abundance charging method. These statements do not exclude more flexible methods. I make no claim of literature novelty for the partial lemmas.

I read `NOTES.md`, `STATEMENT.md`, `SOURCES.md`, and `VERIFICATION-LOWER.md` before this work. I did not redo the lower-bound construction, its verification, or the four failed repairs in the notes.

## 1. Notation and a valid matching reduction

Write

\[
P(S)=\prod_{s\in S}s,\qquad I=\{x+1,\ldots,x+M\}.
\]

For each \(a\in A\) and prime \(p\mid a\), call \(p^{v_p(a)}\) the full \(p\)-component of \(a\). Components for different primes are coprime. A component is kept intact in the matching arguments below.

### Lemma 1: matching the components for one prime

For a fixed prime \(p\), make one token for each \(a\in A\) divisible by \(p\). Join its token to every \(b\in I\) divisible by \(p^{v_p(a)}\). This graph has a matching that covers all its tokens. The same conclusion holds for any subset of the tokens.

**Proof.** Every interval of \(M\) consecutive integers has at least \(\lfloor M/q\rfloor\) multiples of each positive integer \(q\). For a nonempty set \(T\) of tokens, let \(t\) be its smallest exponent. The neighborhoods are nested, so the neighborhood of \(T\) is exactly \(I\cap p^t\mathbb Z\). Each element of \(A\) represented in \(T\) is a distinct multiple of \(p^t\) in \([1,M]\). Thus

\[
|T|\leq\left\lfloor\frac M{p^t}\right\rfloor
\leq |I\cap p^t\mathbb Z|=|N(T)|.
\]

Hall's theorem gives the matching. The argument applies to any subset. ∎

Matching independently for each prime, then taking the union of the hosts, gives the elementary bound

\[
h(A,x)\leq\sum_{a\in A}\omega(a).
\tag{1}
\]

Indeed, hosts are distinct for each fixed prime, so their valuations pay all the components for that prime. A host can pay components for several different primes. In particular, elements with at most two distinct prime factors cause no problem for the \(2n\) bound, regardless of their exponents. Thus (1) charges one host per distinct prime factor and keeps its full exponent intact.

### Lemma 2: a cofactor matching would suffice

For each \(a\in A\), choose one full prime-power component \(q_a\), and put \(d_a=a/q_a\). If the \(n\) cofactors \(d_a\) have distinct hosts \(b_a\in I\) with \(d_a\mid b_a\), then \(h(A,x)\leq2n\).

**Proof.** Start with \(B_0=\{b_a:a\in A\}\), of size \(n\). For each prime \(p\), the hosts \(b_a\) give a partial matching in the graph of Lemma 1: match every token whose component was not removed to \(b_a\). These hosts are distinct, and each has the required divisibility.

Let \(k_p\) be the number of removed components that are powers of \(p\). Exactly \(k_p\) tokens for this prime remain unmatched. A full matching exists by Lemma 1. The augmenting-path theorem therefore extends the partial matching to a full matching in \(k_p\) augmentations. Each augmentation adds one matched right vertex; its other right vertices remain matched. Hence at most \(k_p\) hosts outside \(B_0\) need be added. Hosts in \(B_0\) that were free for this prime can also be used.

Do this for each prime. Since one component was removed from each element, \(\sum_p k_p=n\). The union of \(B_0\) and all added hosts has size at most \(2n\). For each prime it supports a matching of all full components, so its product is divisible by \(P(A)\). ∎

This is a sufficient reduction. The next section identifies a Hall violator for one natural fixed choice of \(q_a\). Choosing the removed component separately for each element remains open in this attempt.

## 2. A proved Hall obstruction to splitting off the largest prime

The rule tested here is precise: let \(P^+(a)\) be the **largest prime factor**, and remove its entire power

\[
q_a=P^+(a)^{v_{P^+(a)}(a)},\qquad d_a=a/q_a.
\tag{2}
\]

This means largest prime by its base, not the numerically largest prime-power component. Try to match these cofactors to distinct hosts, then use Lemma 2. The rule (2) fails.

### Theorem 3: an asymptotic Hall violator

For every sufficiently large multiple \(M\) of \(30\), let

\[
A_M=\{2\leq a\leq M: 2\mid a\text{ and }a\text{ has at least two distinct odd prime factors}\}.
\tag{3}
\]

There is an \(x\geq0\) for which the graph with left side \(A_M\), right side \(I\), and edge \(a\sim b\) when \(d_a\mid b\), has

\[
|N(A_M)|<|A_M|<M/2.
\]

More precisely, the Hall deficit is at least

\[
\bigl(2e^{-\gamma}-1+o(1)\bigr)\frac M{\log M},
\tag{4}
\]

where \(\gamma\) is Euler's constant and \(2e^{-\gamma}-1>0\).

**Proof.** I use the classical prime number theorem and Mertens' product theorem, in the forms

\[
\pi(y)\sim\frac y{\log y},\qquad
\prod_{p\leq y}(1-1/p)\sim\frac{e^{-\gamma}}{\log y}.
\tag{5}
\]

First count the even integers excluded from (3). Each excluded integer is either \(2^s\), or \(2^s q^t\) for one odd prime \(q\), with \(s,t\geq1\). These representations are unique. If \(\Pi_{\rm odd}(y)\) counts odd prime powers at most \(y\), their number is exactly

\[
R(M)=\lfloor\log_2 M\rfloor+
\sum_{s=1}^{\lfloor\log_2 M\rfloor}
\Pi_{\rm odd}\bigl(\lfloor M/2^s\rfloor\bigr).
\tag{6}
\]

The number of powers of exponent at least two up to \(y\) is \(O(\sqrt y\log y)\), by summing the bounds \(y^{1/t}\) for \(2\leq t\leq\log_2 y\). Consequently

\[
\Pi_{\rm odd}(y)=\pi(y)+O(\sqrt y\log(2y)+1).
\]

Summing the errors in (6) gives \(O(\sqrt M\log M+\log M)=o(M/\log M)\). Also

\[
\sum_{s\geq1}\pi(M/2^s)\sim \frac M{\log M}.
\tag{7}
\]

For completeness, take \(L=\lceil2\log_2\log M\rceil\). For \(s\leq L\), the prime number theorem applies uniformly because \(M/2^s\geq M/(2(\log M)^2)\to\infty\), and \(\log(M/2^s)\sim\log M\) uniformly. The partial sum is therefore \((1+o(1))(M/\log M)\sum_{s\leq L}2^{-s}\). The remaining sum is at most \(\sum_{s>L}M/2^s=O(M/(\log M)^2)\). This proves (7). Thus

\[
R(M)=(1+o(1))\frac M{\log M},\qquad
|A_M|=M/2-R(M).
\tag{8}
\]

Next put \(Y=\sqrt{M/2}\). For every \(a\in A_M\), deleting the power of its largest prime leaves a cofactor divisible by \(2\) and by an odd prime \(q\leq Y\). To see the bound on \(q\), take the smallest odd prime factor \(q\) of \(a\) and another odd prime factor \(r>q\). Then \(2qr\mid a\), so \(q^2<qr\leq M/2\). The smallest odd prime is not the largest, so it remains in \(d_a\).

Therefore every neighbor of \(A_M\) is even and divisible by some odd prime at most \(Y\). Let \(U_x\) be the even integers of \(I\) with no such odd prime divisor. There are exactly \(M/2\) even integers in \(I\), whence

\[
|N(A_M)|\leq M/2-|U_x|.
\tag{9}
\]

Average \(x\) over a complete residue system modulo \(2\prod_{3\leq p\leq Y}p\). For each position in the interval, CRT gives probability \(\tfrac12\prod_{3\leq p\leq Y}(1-1/p)\) of being even with none of those odd prime divisors. Linearity of expectation gives

\[
\mathbb E|U_x|
=\frac M2\prod_{3\leq p\leq Y}(1-1/p)
=\bigl(2e^{-\gamma}+o(1)\bigr)\frac M{\log M}.
\tag{10}
\]

The last equality follows from (5), removal of the factor \(1-1/2\), and \(\log Y\sim\tfrac12\log M\). Some nonnegative residue \(x\) has \(|U_x|\geq\mathbb E|U_x|\). Subtract (9) from (8). Equations (8) and (10) give (4), which is positive for sufficiently large \(M\). This proves the Hall violation. Finally \(M\in A_M\) because \(30\mid M\), so this is an instance with the required maximum \(M\). ∎

All these cofactor halves contain a power of \(2\). Thus, even if hosts may be shared across different primes, the per-prime distinctness rule forces these halves to have distinct hosts. The Hall obstruction applies to that prescribed two-half assignment too.

### An exact finite instance

The checker gives the following finite certificate, without asymptotic estimates:

\[
M=300000000,\qquad x=2000000000000001416,
\]

with \(A=A_M\) from (3). Exact counts are

\[
R(M)=17652034,\qquad n=132347966<M/2.
\]

Among the \(150000000\) even integers in \(I\), exactly \(17885755\) have no odd prime divisor at most \(\lfloor\sqrt{M/2}\rfloor=12247\). Hence

\[
|N(A)|\leq150000000-17885755=132114245<n,
\]

with deficit at least \(233721\).

Here is how the exact certificate is obtained. Formula (6) is evaluated with an ordinary prime sieve and a list of higher odd prime powers. For the host count, write \(x=2y\), where \(y=10^{18}+708\). The even hosts are \(2(y+k)\), \(1\leq k\leq150000000\). For each odd prime \(p\leq12247\), remove the progression \(k\equiv-y\pmod p\). The remaining count is \(17885755\). The other \(132114245\) even hosts form a superset of the graph's neighbors. The source and all integer counts are in `upper_attempt_verify.py` and `UPPER-ATTEMPT-EVIDENCE.json`.

The checker also evaluates the exact rational CRT average in (10), whose ceiling is \(17883585>R(M)\). No floating-point comparison is used for acceptance.

### The obstruction persists for arbitrarily large \(M/n\)

Take the finite instance just given. For any power \(c=2^r\), replace \(A\) by \(cA\), \(M\) by \(cM\), and \(x\) by \(cx\). The number \(n\) is unchanged. The largest prime factor of every element remains its same odd prime, so its cofactor under (2) becomes \(cd_a\).

A neighbor of such a cofactor in the new interval must be divisible by \(c\). Writing it as \(cb\) gives exactly \(b\in I\) with \(d_a\mid b\). Thus the new neighbor set is exactly \(cN(A)\), with the same cardinality. The Hall deficit persists, while \(M/n\) tends to infinity.

**Scope of the obstruction.** It disproves the fixed rule (2). It does not disprove an adaptive choice of the removed component, a different partition into two groups, or the original \(2n\) bound. No value of \(h(A,x)\) was computed for this large family.

## 3. A complete \(2n\) bound when \(M\geq(2n)^3\)

### Theorem 4

For every legal \(A,x\), if \(M\geq(2n)^3\), then \(h(A,x)\leq2n\). In fact, the stronger assignment in the brief holds: each element uses at most two hosts, and for a fixed prime, different elements use different hosts for their full components.

**Proof.** Put \(T=M/(2n)\). The hypothesis implies

\[
T^{3/2}\geq M,\qquad T^2>M,\qquad T\geq2n.
\tag{11}
\]

Call a full prime-power component large if it exceeds \(T\). An element has at most one large component, since two would have product greater than \(T^2>M\geq a\). If \(a\) has a large component \(q\), the product of all its other components is

\[
a/q<M/T=2n\leq T.
\]

Keep the large component as one group, and combine all other components into one small group, omitting that group if its product is (1).

If \(a\) has no large component, start with its components as separate groups. Repeatedly merge any two groups whose product is at most \(T\). The process stops, since each merge reduces the number of groups. Every resulting group is at most \(T\), and every pair of different groups has product greater than \(T\).

There can be at most two groups at termination. Otherwise, for three group products \(u,v,w\), all three inequalities \(uv>T\), \(uw>T\), \(vw>T\) hold. Multiplication gives \((uvw)^2>T^3\), so \(uvw>T^{3/2}\geq M\). But \(uvw\mid a\leq M\), a contradiction. Thus every element has at most two groups. No prime-power component was split.

First assign all large groups to hosts. Each is a full component for one prime, so Lemma 1 matches the large groups for each prime to distinct hosts for that prime. Different primes may use the same host. Let \(B_L\) be the union of these hosts. Its cardinality is at most the number of large groups.

Now assign the small groups one at a time, using hosts outside all previously used hosts. Each small group \(d\leq T\) has at least

\[
\left\lfloor\frac Md\right\rfloor\geq2n
\]

multiples in \(I\). The total number of groups is at most \(2n\). Before any small group is assigned, fewer than \(2n\) hosts have been used. Therefore a new multiple is available. This greedy assignment finishes.

For a fixed prime, its large components have distinct hosts by construction. All small-group hosts are globally distinct and avoid \(B_L\). Each element's full component for that prime occurs in only one group. Hence distinct elements have distinct hosts for that prime. The host valuations therefore sum to at least the required valuations of \(P(A)\). There are at most \(2n\) hosts, and each element uses at most its two group hosts. ∎

This leaves the range

\[
2n<M<(2n)^3
\tag{12}
\]

unresolved; the range \(M\leq2n\) is immediate from \(B=I\). The theorem gives no bound \(g(n)\leq Cn\), since the omitted range grows with \(n\).

## 4. Induction with the full residual demand: a fixed-set obstruction

For a current selection \(B_0\), the correct residual demand is

\[
r_p=\max\{v_p(P(A))-v_p(P(B_0)),0\}.
\tag{13}
\]

This credits the full valuations of the selected numbers, including surplus factors. It does not use just the lcm supplied by a collision group.

I tested this proposed induction step: remove an element having the most multiples in \(I\); take a valid selection of at most \(2(n-1)\) hosts for the remaining elements; extend that selection by at most two new hosts using (13). Even with the full residual vector, this assertion is false for an arbitrary valid selection.

### Proposition 5: three additions can be necessary

Let \(\kappa(m)=|\{p\in\{2,3,5\}:p\mid m\}|\), and set

\[
\begin{split}
M&=180,\qquad I=\{181,\ldots,360\},\qquad a=30,\\
A_0&=\{31\leq m\leq180:\kappa(m)\geq2\}\\
&\quad\cup\{32,64,81,85,112,117,125,175\},\\
A&=A_0\cup\{30\},\\
B_0&=\{b\in I:\kappa(b)=0\text{ or }\kappa(b)\geq2\}.
\end{split}
\tag{14}
\]

Then \(|A_0|=48\), \(|A|=49\), \(|B_0|=96=2|A_0|\), and \(P(A_0)\mid P(B_0)\). The element \(30\) is one of the elements having the most multiples in \(I\). Nevertheless, extending this fixed \(B_0\) to cover \(P(A)\) needs exactly three new hosts, so extension alone needs \(99>2|A|=98\) hosts.

**Proof.** In each complete block of length \(30\), exactly eight integers have \(\kappa\geq2\), and eight have \(\kappa=0\). The first set defining \(A_0\) has \(40\) members, and the eight added members are distinct and have \(\kappa=1\). The interval \(I\) has six such blocks, so \(|B_0|=6(8+8)=96\).

The complete valuation comparison for primes dividing \(P(A_0)\) is:

```text
prime p       2   3   5   7  11  13  17  19  23  29
v_p(P(A0))   84  52  30   9   4   4   3   1   1   1
v_p(P(B0))   84  52  30  17   9   7   9   7   5   4
```

These finite counts are obtained by division of the explicitly defined sets; `induction_certificate()` checks every entry and exact product divisibility. They prove \(P(A_0)\mid P(B_0)\). They also show that the residual demand after adjoining \(30\) is exactly one factor each of \(2,3,5\), with no other prime deficit.

Every available host lies in \(I\setminus B_0\) and has \(\kappa=1\). It can pay only one of these three prime deficits. At least three additions are necessary. The hosts \(182,183,185\) pay them, since their product is divisible by \(30\), so exactly three suffice.

There are six multiples of \(30\) in \(I\). Every other element is at least \(32\), so it has at most \(\lceil180/32\rceil=6\) multiples in \(I\). Thus \(30\) is eligible for removal under the proposed rule. ∎

This is not a counterexample to the problem. In particular, \(181\in B_0\) is prime and does not divide \(P(A_0)\). Removing \(181\) and adding \(182,183,185\) gives a valid set of size \(98\). The old selection is not minimal. What fails is the assertion for **every** valid induction selection, with a size bound and residual vector but no exchange condition.

A strengthened induction must select a better old set, retain an exchange property, or prove an augmentation statement that can release old hosts. Proposition 5 does not exclude those possibilities. I did not prove such a statement.

## 5. Charging: the missing overlap cannot be replaced by a count

I considered ownership by the first element that opens a host. The supplied observation is valid: if an element has coprime components \(u,v,w\) and possibly further components, then \(uv\leq M/w\), so \(I\) has at least \(w\geq2\) multiples of \(uv\). This is initial supply, however. It does not imply an unused multiple after other hosts have been opened.

There is a specific example of this loss in (14). Every host divisible by two of \(2,3,5\) already belongs to \(B_0\), although the remaining demand is \(30\). Thus all three possible pair products have zero unused hosts. Extra valuation at a host can help one prime without restoring the other two. The example defeats a per-step bound of two additions; its removable host also shows why it does not defeat an amortized proof.

### Proposition 6: a uniform abundance threshold can force three groups per element

Consider the following restricted charging method: partition each element into products of its full prime-power components, require every such group to be at most \(T=M/(2n)\), then assign all groups to globally distinct hosts using their guaranteed \(2n\) multiples. Allow separately matched large prime-power components as in Theorem 4. This method does not always produce \(2n\) groups.

Take the eleven primes

\[
101,103,107,109,113,127,131,137,139,149,151
\]

and let \(A\) be all products of three different primes from this list. Unique factorization gives

\[
n=\binom{11}{3}=165,\qquad M=139\cdot149\cdot151=3127361.
\]

Here every component is at most \(151<T=M/330\), while every product of two components is at least

\[
101\cdot103=10403>M/330.
\]

Thus no group of size at most \(T\) can contain two components of one element. Each element needs three groups, so the method needs \(495\) distinct hosts rather than \(330\). There are no large prime-power components to handle separately. This proves the stated limitation.

It is not a lower bound of \(495\) on \(h(A,x)\). Allowing a host to carry components for different primes can reduce the cost. It identifies the exact missing step: an upper-bound proof must exploit that overlap, rather than charge every component group as a separate new host. I did not obtain the requested average ownership bound of two.

## 6. Complementary formulation: the excess valuations are essential

Let \(C=[1,M]\setminus A\), where \(1\in C\). Define

\[
E_p(x,M)=v_p(P(I))-v_p(M!).
\tag{15}
\]

For every prime \(p\), \(E_p\geq0\): at each power \(p^t\), the interval \(I\) has at least \(\lfloor M/p^t\rfloor\) multiples, and summing over \(t\geq1\) proves the assertion. This also proves that \(M!\mid P(I)\).

For \(X\subseteq I\), put \(B=I\setminus X\). Since \(P(A)P(C)=M!\), the exact equivalence is

\[
P(A)\mid P(B)
\quad\Longleftrightarrow\quad
v_p(P(X))\leq v_p(P(C))+E_p(x,M)
\quad\text{for every prime }p.
\tag{16}
\]

This follows by subtracting \(v_p(P(X))\) from \(v_p(P(I))\) and then subtracting \(v_p(P(A))\). Consequently, finding \(B\) of size at most \(2n\) is equivalent to finding \(X\) of size at least \(M-2n\) satisfying (16). Omitting \(E_p\) gives a sufficient condition, not an equivalent one.

### Theorem 7: omitting the excess has unbounded cost already for \(n=1\)

For every integer \(k\geq3\), there is an instance with \(A=\{M\}\) and \(h(A,x)=1\) such that every \(X\subseteq I\) whose exponent profile is dominated by that of \(C\) omits at least \(k\) integers of \(I\). This remains true if domination is checked only at primes dividing \(A\).

**Proof.** Choose \(k\) distinct primes \(p_1,\ldots,p_k\), and let \(M=\prod_i p_i\). Then \(k\leq M\), so positions \(1,\ldots,k\) are distinct positions of \(I\). Since \(M\) is squarefree and \(A=\{M\}\),

\[
v_{p_i}(P(C))=v_{p_i}(M!)-1.
\]

Put \(e_i=v_{p_i}(M!)\geq1\). By CRT there is a nonnegative \(x\) such that

\[
x+i\equiv0\pmod{p_i^{e_i}}\qquad(1\leq i\leq k).
\tag{17}
\]

If \(x+i\in X\), then

\[
v_{p_i}(P(X))\geq e_i>v_{p_i}(P(C)),
\]

so domination fails. Thus every one of the \(k\) distinct positions \(x+i\) must be omitted. Only primes dividing \(A\) were used in this argument.

On the other hand, any interval of \(M\) consecutive integers contains a multiple of \(M\). Selecting that one integer covers \(P(A)=M\). The empty selection does not, so \(h(A,x)=1\). ∎

Choosing \(k>2\) disproves the proposed complementary equivalence at the \(2n\) target. Choosing \(k\) arbitrarily large shows that replacing \(2n\) by any bound depending only on \(n\) cannot rescue this stronger complementary problem. Extra prime factors outside \(P(A)\) are not the cause; the obstruction already uses only the target primes.

### An exact \(M=30\) example

Take \(A=\{30\}\), \(C=[1,30]\setminus\{30\}\), and

\[
x=3188778734345781247.
\]

The CRT conditions used are

\[
x+1\equiv0\pmod{2^{26}},\quad
x+2\equiv0\pmod{3^{14}},\quad
x+3\equiv0\pmod{5^7}.
\]

The \(2,3,5\) exponents of \(P(C)\) are \(25,13,6\). The actual valuations of \(x+1,x+2,x+3\) at the respective primes are \(28,16,7\). Each of these three positions must be omitted from a complement dominated by \(C\). Hence its size is at most \(27\), below \(M-2n=28\).

Yet

\[
B=\{3188778734345781270\}
\]

is a single multiple of \(30\) in \(I\). All these assertions are checked by integer arithmetic in `complement_certificate()`.

## 7. Computations, proof status, and the remaining gap

The self-contained checker is `upper_attempt_verify.py`; its output is `UPPER-ATTEMPT-EVIDENCE.json`. It runs in one process and requires only the Python standard library. The recorded invocation was

```sh
nice -n 10 .venv/bin/python upper_attempt_verify.py --explore-matching
```

The recorded run took about \(19.03\) seconds and passed. The finite Hall certificate uses a byte sieve of \(150000001\) entries and exact progression deletion. Floating-point values are not used to decide any certificate. The asymptotic proof of Theorem 3 does not depend on these computations.

The checks cover:

1. The exact CRT example in Section 6, including its single valid host.
2. Every valuation in the induction table, exact product divisibility, the most-multiples rule, the necessary three additions, and the valid exchange.
3. The three-group obstruction in Section 5.
4. A constructive implementation of Theorem 4 on \(288\) instances, with \(1\leq n\leq24\), seed `70820261015`, and \(x<10^{30}\). This includes one equality case \(M=(2n)^3\) for each \(n\). Each check verifies host positions, cardinality, at most two hosts per element, distinct hosts for a fixed prime, and exact product divisibility.
5. The finite Hall deficit \(233721\), using the stated \(A,M,x\) and an exact upper bound on its neighborhood.

There was also a bounded exploratory matching search: \(3120\) graphs, seed `708708`, \(M=5,\ldots,100,120,150,180,210,250,300,400,500\), and fifteen random \(x<10^{18}\) per \(M\). It tested both the fixed rule (2) and the graph allowing any one full component to be removed. Each tested graph, with all inputs \(2,\ldots,M\) present, had a full matching. This small-range observation did not justify the fixed rule: Theorem 3 and the finite certificate disprove it. It proves nothing about the adaptive rule beyond those samples.

PuLP/CBC, single-threaded, was used only to discover the finite induction example before the checker was written. No claimed conclusion depends on CBC optimality. The lower bound of three additions in Proposition 5 follows from its explicit residual-prime argument. No ILP evaluation of the large Hall family or of a possible counterexample to \(g(n)\leq2n\) is claimed.

The remaining upper-bound gap is exact: neither the two-group construction in the range (12), an adaptive cofactor Hall theorem, an exchange-capable induction, nor the requested average charging inequality has been proved. The complementary method must retain the interval excess in (16). The fixed largest-prime split cannot be used as a universal reduction, even after assuming \(M/n\) large.

The final status below records that none of the requested global upper bounds or a counterexample has been established. The proved obstructions and the restricted-range bound are the output of this attempt. Independent director acceptance is still pending.

RESULT: NO NEW THEOREM
