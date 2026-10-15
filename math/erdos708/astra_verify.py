#!/usr/bin/env python3
"""Exact integer checks for the explicit examples and factor-packing construction."""
from collections import Counter
from pathlib import Path
import json
import math
import random
import time


def vp(n, p):
    e = 0
    while n % p == 0:
        e += 1
        n //= p
    return e


def factor(n):
    out = Counter()
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] += 1
            n //= p
        p += 1
    if n > 1:
        out[n] += 1
    return out


def increment_family(e):
    M = 2**e + 4
    r = M // 4
    a = 2**e
    A0 = sorted(({4*j for j in range(1, r+1)} - {a})
                | {4*j-2 for j in range(1, e+1)})
    H = math.prod(t // 2**vp(t, 2) for t in A0)
    x = 2**e * (H - 1)
    B0 = [x + 4*j for j in range(1, r+1)]
    B1 = B0 + [x + 4*j-2 for j in range(1, e+1)]
    vals = sorted((vp(x+j, 2) for j in range(1, M+1)), reverse=True)
    S = sum(vp(t, 2) for t in A0)
    assert max(A0) == M and len(A0) == r+e-1 and a not in A0
    assert 2*len(A0+[a]) < M if e >= 5 else 2*len(A0+[a]) <= M
    assert sum(vals[:r-1]) < S == sum(vals[:r])
    assert sum(vals[:r+e-1]) < S+e == sum(vals[:r+e])
    assert sum(vp(b, 2) for b in B0) == S
    assert sum(vp(b, 2) for b in B1) == S+e
    assert x+a in B0 and (x+a) % H == 0
    assert all(vp(x+j, 2) == vp(j, 2) for j in range(1, M+1))
    assert len(set(B0)) == r and len(set(B1)) == r+e
    if e == 4:
        assert math.prod(B0) % math.prod(A0) == 0
        assert math.prod(B1) % math.prod(A0+[a]) == 0
    row = {'e': e, 'M': M, 'n_before': len(A0), 'n_after': len(A0)+1,
           'h_before': r, 'h_after': r+e, 'increment': e,
           'demand_2_before': S, 'demand_2_after': S+e,
           'top_before_minus_one': sum(vals[:r-1]),
           'top_after_minus_one': sum(vals[:r+e-1])}
    if e == 4:
        row.update({'A_before': A0, 'added': a, 'x': x, 'H': H,
                    'B_before': B0, 'B_after': B1,
                    'descending_interval_2_valuations': vals})
    return row


def packing_cover(A, x, K):
    n = len(A)
    M = max(A)
    budget = K*n
    assert M**(K-1) >= budget**(K+1)
    small = []
    large = Counter()
    per_input = []
    for a in A:
        fs = [p for p, e in factor(a).items() for _ in range(e)]
        while True:
            pair = next(((i,j) for i in range(len(fs))
                         for j in range(i+1,len(fs))
                         if fs[i]*fs[j]*budget <= M), None)
            if pair is None:
                break
            i,j = pair
            product = fs[i]*fs[j]
            fs.pop(j)
            fs.pop(i)
            fs.append(product)
        assert len(fs) <= K and math.prod(fs) == a
        per_input.append(len(fs))
        for f in fs:
            if f*budget > M:
                assert factor(f) == {f:1}
                large[f] += 1
            else:
                small.append(f)
    B = set()
    for p, demand in large.items():
        multiples = list(range(((x+1+p-1)//p)*p, x+M+1, p))
        chosen = multiples[:demand]
        assert sum(vp(b,p) for b in chosen) >= demand
        B.update(chosen)
    for f in small:
        b = next(b for b in range(((x+1+f-1)//f)*f, x+M+1, f)
                 if b not in B)
        B.add(b)
    assert len(B) <= budget
    assert math.prod(B) % math.prod(A) == 0
    return len(B), max(per_input)


def main():
    start = time.perf_counter()
    family = [increment_family(e) for e in range(4, 11)]
    rng = random.Random(7081502)
    checks = []
    for K in [2,3]:
        counts = []
        max_groups = 0
        for n in range(2,11):
            M = (K*n)**(3 if K == 2 else 2)
            for _ in range(5):
                A = sorted(rng.sample(range(2,M), n-1) + [M])
                x = rng.randrange(10**9)
                size, groups = packing_cover(A,x,K)
                counts.append(size/(K*n))
                max_groups = max(max_groups, groups)
        checks.append({'K':K,'cases':len(counts),
                       'largest_budget_fraction_used':max(counts),
                       'largest_groups_per_input':max_groups})
    result = {'arithmetic':'Python integers only; no optimizer',
              'seed':7081502,'increment_family':family,
              'packing_checks':checks,'seconds':time.perf_counter()-start}
    path = Path(__file__).with_name('astra_verify.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
