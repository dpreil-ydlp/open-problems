# Independent mathematical review of A185897

The proof is correct. I found no failing inference or counterexample in the
stated theorem. The verdict rests on the argument for all coefficients, with
computer checks as supporting evidence. It does not certify priority.

## Review record

- Owner: review sub-agent, GPT-6.1 Sol / xhigh.
- Authority: the user's request to review PROOF.md and write REVIEW-SOL.md.
- Started: 15 October 2026, approximately 19:16:35 UTC.
- Completed: 2026-10-15 19:25:23 UTC.
- Budget: 35 minutes; completed within that limit.
- Scope: mathematical review and public-source search. This review writes only
  REVIEW-SOL.md in the project. It does not edit PROOF.md or the author's checks.
- Proof reviewed: PROOF.md, 115 lines, SHA-256
  `4446fda20dcb0c2775e812451997978a97a73c07d3d0995ed528628195135568`.
  The hash was unchanged when this report was written.
- Proof of work: the source quotations, audit, executed code, and output below.
- Remaining review work: none. Next action: return this report to the coordinator.
- Unresolved decisions: none. Priority remains outside what a bounded search can
  establish.

## OEIS definition and conjecture, verbatim

I fetched [A185897](https://oeis.org/A185897) myself on 15 October 2026.
I also fetched its [internal form](https://oeis.org/A185897/internal) and
[b-file](https://oeis.org/A185897/b185897.txt) directly with Python's HTTP client.
Both HTTP requests for the entry and b-file returned status 200.

The entry's definition is:

```text
G.f. A(x) satisfies: A(x - A(x)^2) = x/(1-x).
```

The first FORMULA line states:

```text
G.f. A(x) = Sum_{n>=1} a(n)*x^n and the related series G(x) (the g.f. of A389476) satisfy the following formulas.
```

The conjecture, including its attribution, is:

```text
Conjecture: for n > 1, a(n) is odd when n = 3*2^k through 4*2^k - 1 for k >= 0. - Paul D. Hanna, Oct 05 2025
```

Thus the zero constant term is explicit in OEIS. It is not inferred from the
offset alone. The source says "when"; the submitted theorem proves the full
if-and-only-if classification requested in this review.

## Numbered objections

1. **BLOCKER: none found.** No specified attack exposed a failing inference.
2. **MINOR: none requiring a correction.** The known support and binary pattern
   deserve references in a publication, but they do not invalidate this proof.

No proof revision is required for mathematical correctness. The following audit
records the attempted objections and why they fail.

## Audit of the requested attacks

### (a) Section 1: recursion, existence, and constant term

The coefficient argument is valid. Set h = x - A^2. Since A has zero constant
term, h = x + O(x^2). Terms with j > n cannot contribute to [x^n] A(h), and the
j = n term contributes exactly a(n). For j < n and i >= 1, the relevant degree
in A^(2i) is n-j+i. All 2i factors have positive degree. Hence each coefficient
index k used in that product satisfies

```text
k <= (n-j+i) - (2i-1) = n-j-i+1 <= n-1.
```

The outer coefficient a(j) is also already known. The i = 0 piece is x^j and
contributes nothing at degree n. There is no hidden a(n) in h that can affect
the current coefficient. The n = 1 equation first gives a(1) = 1; the n = 2
equation gives a(2) = 2.

The recursion also proves existence over Z: at each step set a(n) equal to
1 minus the known integer polynomial. No division is required. Each coefficient
of the resulting formal composition then satisfies the equation. The stated
lowest degree j+i is exact once a(1) = 1. Before that step, the lower bound j+i
already suffices. If a binomial piece vanishes modulo 2, this cannot create a
new contribution at a lower degree.

### (b) Reduction modulo 2 and uniqueness there

Reduction is legitimate. Every coefficient of a composition with inner constant
term zero is a finite integer polynomial in the relevant coefficients. Reducing
that polynomial commutes with composition. The denominator 1-x is a unit, so
its inverse also reduces to the inverse of 1+x.

The same triangular argument works over F2. The coefficient of the new unknown
is 1, even though some other binomial coefficients become zero. Thus there is
exactly one zero-constant-term solution over F2. This is stronger than merely
observing that an integer solution has a reduction. The separate recursive
computation below agrees with B through degree 300.

### (c) Section 2: ell and Artin-Schreier uniqueness

There is no convergence defect. For a nonzero y of order d >= 1, the order of
y^(2^k) is d*2^k. Only finitely many summands affect any fixed degree. For y = 0
the conclusion is immediate. Frobenius therefore proves the stated additivity
and permits shifting the index in the squared sum. It gives ell(y)^2 + ell(y) = y.

The kernel claim is also correct in F2[[x]]. If z^2+z = 0, every positive odd
coefficient of z is zero, and each positive even coefficient equals the
coefficient at half its index. Repeated division of the index by 2 reaches an
odd index. All positive coefficients vanish. The constant can only be 0 or 1.
Consequently, restricting to constant term zero removes the second root.
The proof does not apply an unjustified uniqueness claim over a larger ring.

### (d) Lemma 1: support, ordering, and the b-file

The two subsets of E are disjoint: no power of 2 equals three times a power of
2. After the initial 1, their order follows from
2^(k+1) < 3*2^k < 2^(k+2). Multiplication by 1/(1+x) in F2 takes partial sums.
The odd counts give exactly [1,1] and [3*2^k,4*2^k-1]. There is no endpoint error.
The alternative summation at line 51 also passes.

The downloaded b-file contains all indices 1 through 400. Its first 60 parities,
in six consecutive blocks of ten, are:

```text
1010011000 0111100000 0001111111 1000000000 0000000111 1111111111
```

The odd indices among those 60 terms are exactly

```text
{1, 3} union [6,7] union [12,15] union [24,31] union [48,60].
```

The last interval is cut at 60 by the check's stated range. These are the claimed
intervals. The code also compares every b-file parity through index 300 and
checks the original equation over Z through degree 60 using the exact integers.
All comparisons pass.

### (e) Lemma 2: substitution at y

The assertion is composition. Substitution x -> y, with y(0) = 0, is a continuous
ring homomorphism for the formal power series topology. It carries the locally
finite sum defining ell(x+x^3) to ell(y+y^3), and the inverse of 1+x to the
inverse of 1+y. The latter exists because its constant term is 1. This includes
y = 0. No analytic convergence assumption is needed.

### (f) Section 4: every algebraic line

I checked equations (1)-(4), every displayed intermediate expression in (2),
the full right-side expansion at lines 79-85, both expressions for v at lines
89-90, the product at line 92, and each sum at lines 94-97. All are correct.
Both sides reduce to the same numerator over (1+x)^6:

```text
x + x^3 + w*(x + x^3 + x^4).
```

All denominators used are units. Both series compared by their Artin-Schreier
images have constant term zero. That comparison therefore proves (4), rather
than leaving an unresolved possible difference of 1. The final cancellation by
1+u is valid. The independent degree-300 calculation below confirms these lines
and B(x+B(x)^2) = x/(1+x).

The finite checks do not establish identities at untested degrees. The formal
arguments and exact algebra above establish the theorem; the computations test
for transcription and coefficient errors.

## (g) Prior-work statement

I found the conjecture, related conjectures, and older descriptions of the same
support and binary pattern. I did not find an earlier proof that A185897 has
this parity, or an earlier proved formula identifying A185897 modulo 2 with
ell(x+x^3)/(1+x). This is a bounded search result, not a claim of priority.

Sources inspected:

- [A185897](https://oeis.org/A185897) still labels the assertion a conjecture.
  Its fetched entry gives no parity proof or ell formula.
- Its direct cross-reference [A389476](https://oeis.org/A389476), by Hanna,
  gives G = A/(1+A) and a related parity conjecture using A027383.
- Its other direct cross-reference [A213591](https://oeis.org/A213591), also
  by Hanna, concerns A(x-A(x)^2) = x. The inspected formulas do not supply this
  theorem.
- Hanna's [A380678](https://oeis.org/A380678) has another related parity
  conjecture involving A027383. Hanna's [A324615](https://oeis.org/A324615)
  conjectures odd coefficients only at 0 and members of E for a different
  equation. Neither inspected entry proves the present result.
- [A029744](https://oeis.org/A029744) already lists E, the numbers 2^k or 3*2^k.
  [A027383](https://oeis.org/A027383) is its shifted relative.
- [A079944](https://oeis.org/A079944), created in 2003, already describes runs
  of 2^k zeros followed by 2^k ones. With its published offset 0, the proposed
  parity is 1 at n=1 and A079944(n-2) at n>=2. If C is that entry's generating
  function, the proposed B is x+x^2*C over F2. Thus the binary pattern is old;
  its identification with A185897 is the point requiring proof. The ell formula
  is also an equivalent encoding of Hanna's stated pattern.

Searches included the following literal query strings:

```text
"A185897" proof parity Hanna
"A185897" arxiv MathOverflow
site:arxiv.org "A185897"
site:mathoverflow.net "A185897"
"A185897" "parity"
"A185897" "proof"
"A185897" "mod 2"
"A185897" "x+x^3"
"A(x - A(x)^2)" parity proof
site:oeis.org "Hanna" "3*2^k" "odd"
site:arxiv.org Hanna "formal power series" parity
site:mathoverflow.net Hanna "power series" parity
```

The arXiv and MathOverflow searches found no relevant earlier proof. I inspected
the abstract of Pakovich's
[Functional equations in formal power series](https://arxiv.org/abs/2208.08365):
it studies a different composition problem in characteristic zero and does not
provide the present result in its abstract. I do not claim a full review of that
paper.

I also checked the complete HTML text of
[OEIS Open](https://arxiv.org/html/2608.11941), which contains no occurrence of
185897, and its published complete
[conjecture metadata](https://raw.githubusercontent.com/epoch-research/LeanOpenProblems-results/main/metadata/oeis/conjectures.json)
and
[sequence metadata](https://raw.githubusercontent.com/epoch-research/LeanOpenProblems-results/main/metadata/oeis/sequences.json).
Those files contain 492 and 444 records respectively; neither contains 185897.
A recursive tree listing of the whole results repository was truncated, so I did
not use it as evidence of absence. The narrower metadata reads were complete.

I did not search every Hanna entry, unpublished correspondence, or every run log
in that repository. A missing search hit cannot establish that no prior proof
exists. Nothing found in this search defeats mathematical correctness.

## Executed computer checks

I used my own code and my own HTTP download, rather than the author's verify.py
or test_verify.py. Python version: 3.14.4. Command exit status: 0.

All finite-field calculations use F2[x]/(x^301), so degrees 0 through 300 are
included. Bits encode polynomial coefficients; addition is XOR. Multiplication,
inversion, composition, and ell all respect that truncation. A separate loop
solves the defining equation without using ell or the candidate B. The final
check uses ordinary integer arithmetic on the first 60 exact b-file terms.

B-file SHA-256:
`805d450352e9da329db9ef5aa4ef6b518835912de2d1d42c32b1e81dce8cbc09`.

Checker SHA-256:
`608c3de9c0f679efc79dc1ba57c67a61b61020a5cdb5e66d07f17bf7de5484b4`.

The temporary input and checker are in
`/tmp/a185897-sol-review-20261015-191635/`. To reproduce elsewhere, set ROOT to a
directory containing the b-file downloaded from the URL above. The code below
is the exact checker I ran.

```python
from pathlib import Path
from functools import lru_cache
import hashlib

ROOT = Path('/tmp/a185897-sol-review-20261015-191635')
N = 300
MASK = (1 << (N + 1)) - 1
ONE, X = 1, 2

def mul(a, b):
    c = 0
    a &= MASK
    b &= MASK
    while a:
        bit = a & -a
        c ^= b << (bit.bit_length() - 1)
        a ^= bit
    return c & MASK

def power(a, n):
    out = ONE
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n //= 2
    return out

def square(a):
    out = 0
    for i in range(N // 2 + 1):
        out |= ((a >> i) & 1) << (2 * i)
    return out

@lru_cache(None)
def inv(a):
    assert a & 1
    q = a ^ ONE
    out = term = ONE
    while term:
        term = mul(term, q)
        out ^= term
    return out

def div(a, b):
    return mul(a, inv(b))

def compose(f, g):
    assert not g & 1
    out = 0
    for i in range(f.bit_length() - 1, -1, -1):
        out = mul(out, g) ^ ((f >> i) & 1)
    return out

def ell(y):
    assert not y & 1
    out = 0
    while y:
        out ^= y
        y = square(y)
    return out

checks = []
def check(label, *expressions):
    assert all(e == expressions[0] for e in expressions), label
    checks.append(label)

x2, x3, x4 = power(X, 2), power(X, 3), power(X, 4)
x5, x6 = power(X, 5), power(X, 6)
d = ONE ^ X
d2, d3, d6 = power(d, 2), power(d, 3), power(d, 6)
w = ell(X ^ x3)
B = div(w, d)
u = X ^ square(B)
t = ONE ^ x2 ^ w
v = div(mul(X, ONE ^ u), d)
check('Frobenius square', square(w), mul(w, w))
check('ell additivity', ell(X ^ x3), ell(X) ^ ell(x3))
check('Section 2 Artin-Schreier identity', square(w), w ^ X ^ x3)
check('(1)', square(w), w ^ X ^ x3)
check('(2), every expression', u, X ^ div(square(w), d2),
      div(mul(X, d2) ^ w ^ X ^ x3, d2),
      div(X ^ x3 ^ w ^ X ^ x3, d2), div(w, d2))
check('(3)', ONE ^ u, div(d2 ^ w, d2), div(t, d2))
check('(4), both definitions and ell', ell(u ^ power(u, 3)), v,
      div(mul(X, t), d3))
check('Lemma 2 at u', compose(B, u), div(ell(u ^ power(u, 3)), ONE ^ u))
check('RHS lines 79-85', u ^ power(u, 3), mul(u, square(ONE ^ u)),
      div(mul(w, square(t)), d6),
      div(mul(w, ONE ^ x4 ^ square(w)), d6),
      div(mul(w, ONE ^ x4 ^ w ^ X ^ x3), d6),
      div(mul(w, ONE ^ X ^ x3 ^ x4) ^ square(w), d6),
      div(mul(w, ONE ^ X ^ x3 ^ x4) ^ w ^ X ^ x3, d6),
      div(X ^ x3 ^ mul(w, X ^ x3 ^ x4), d6))
check('LHS line 89', square(v), div(mul(x2, square(t)), d6),
      div(mul(x2, ONE ^ x4 ^ w ^ X ^ x3), d6))
check('LHS line 90', v, div(mul(mul(X, t), d3), d6),
      div(mul(mul(X, t), ONE ^ X ^ x2 ^ x3), d6))
check('LHS line 92 product expansion', mul(t, ONE ^ X ^ x2 ^ x3),
      ONE ^ X ^ x2 ^ x3 ^ x2 ^ x3 ^ x4 ^ x5 ^ mul(w, d3),
      ONE ^ X ^ x4 ^ x5 ^ mul(w, ONE ^ X ^ x2 ^ x3))
check('LHS lines 94-97', mul(d6, square(v) ^ v),
      mul(x2, ONE ^ X ^ x3 ^ x4 ^ w) ^ mul(X, ONE ^ X ^ x4 ^ x5)
      ^ mul(mul(X, w), ONE ^ X ^ x2 ^ x3),
      x2 ^ x3 ^ x5 ^ x6 ^ mul(x2, w) ^ X ^ x2 ^ x5 ^ x6
      ^ mul(w, X ^ x2 ^ x3 ^ x4),
      X ^ x3 ^ mul(w, x2 ^ X ^ x2 ^ x3 ^ x4),
      X ^ x3 ^ mul(w, X ^ x3 ^ x4))
check('Artin-Schreier comparison', square(v) ^ v, u ^ power(u, 3))
check('Final functional equation', compose(B, X ^ square(B)), div(X, d))

# Solve the functional equation coefficient by coefficient, without using ell or B.
a = 0
for n in range(1, N + 1):
    known = (compose(a, X ^ square(a)) >> n) & 1
    a |= (1 ^ known) << n
check('Independent triangular recursion', a, B)

E = {2**k for k in range(10) if 2**k <= N}
E |= {3 * 2**k for k in range(10) if 3 * 2**k <= N}
interval = lambda n: n == 1 or any(3*2**k <= n <= 4*2**k-1 for k in range(10))
for n in range(N + 1):
    assert ((B >> n) & 1) == (sum(e <= n for e in E) % 2) == int(interval(n))
check('Lemma 1 support and intervals, degrees 0..300', True)
check('Lemma 1 alternative summation', B,
      X ^ div(ell(x3) ^ ell(X) ^ X ^ x2, d))

raw = (ROOT / 'b185897.txt').read_bytes()
rows = {}
for line in raw.decode().splitlines():
    line = line.split('#', 1)[0].strip()
    if line:
        n, value = map(int, line.split())
        assert n not in rows
        rows[n] = value
assert all(n in rows for n in range(1, 401))
first60 = ''.join(str(rows[n] % 2) for n in range(1, 61))
assert all(rows[n] % 2 == ((B >> n) & 1) for n in range(1, N + 1))
check('b-file parity, terms 1..300 (includes requested 1..60)', True)

# Check that the first 60 exact b-file integers satisfy the original equation.
M = 60
A = [0] + [rows[n] for n in range(1, M + 1)]
def zmul(p, q):
    r = [0] * (M + 1)
    for i, c in enumerate(p):
        if c:
            for j in range(M + 1 - i):
                r[i + j] += c * q[j]
    return r
h = [-c for c in zmul(A, A)]
h[1] += 1
r = [0] * (M + 1)
for c in reversed(A):
    r = zmul(r, h)
    r[0] += c
check('Original integer equation on exact b-file terms 1..60', r, [0] + [1]*M)

print('All arithmetic over GF(2)[x]/(x^301), except the exact integer check.')
for label in checks:
    print('PASS:', label)
print('TOTAL CHECK GROUPS:', len(checks))
print('b-file SHA256:', hashlib.sha256(raw).hexdigest())
print('FIRST 60 PARITIES:', first60)
print('FIRST 60 PARITIES IN BLOCKS OF TEN:', ' '.join(first60[i:i+10] for i in range(0, 60, 10)))
print('ODD INDICES 1..60:', [n for n in range(1, 61) if rows[n] % 2])
print('E UP TO 60:', sorted(e for e in E if e <= 60))

```

Command run:

```sh
python3 /tmp/a185897-sol-review-20261015-191635/check_review.py
```

Observed output:

```text
All arithmetic over GF(2)[x]/(x^301), except the exact integer check.
PASS: Frobenius square
PASS: ell additivity
PASS: Section 2 Artin-Schreier identity
PASS: (1)
PASS: (2), every expression
PASS: (3)
PASS: (4), both definitions and ell
PASS: Lemma 2 at u
PASS: RHS lines 79-85
PASS: LHS line 89
PASS: LHS line 90
PASS: LHS line 92 product expansion
PASS: LHS lines 94-97
PASS: Artin-Schreier comparison
PASS: Final functional equation
PASS: Independent triangular recursion
PASS: Lemma 1 support and intervals, degrees 0..300
PASS: Lemma 1 alternative summation
PASS: b-file parity, terms 1..300 (includes requested 1..60)
PASS: Original integer equation on exact b-file terms 1..60
TOTAL CHECK GROUPS: 20
b-file SHA256: 805d450352e9da329db9ef5aa4ef6b518835912de2d1d42c32b1e81dce8cbc09
FIRST 60 PARITIES: 101001100001111000000001111111100000000000000001111111111111
FIRST 60 PARITIES IN BLOCKS OF TEN: 1010011000 0111100000 0001111111 1000000000 0000000111 1111111111
ODD INDICES 1..60: [1, 3, 6, 7, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
E UP TO 60: [1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48]
```

VERDICT: CORRECT
