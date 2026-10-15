#!/usr/bin/env python3
"""Bounded experiments for ASTRA-UPPER-ATTEMPT.md; no other files changed."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import math
import random
import time

import pulp


ROOT = Path(__file__).resolve().parent
SEED = 7081501


def factor(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def vp(n, p):
    e = 0
    while n % p == 0:
        e += 1
        n //= p
    return e


def solve(A, x, M, continuous=False):
    demand = Counter()
    for a in A:
        demand.update(factor(a))
    primes = sorted(demand)
    rows = [(b, tuple(vp(b, p) for p in primes))
            for b in range(x + 1, x + M + 1)]
    rows = [(b, v) for b, v in rows if any(v)]
    model = pulp.LpProblem('astra_cover', pulp.LpMinimize)
    z = [pulp.LpVariable(f'z_{j}', 0, 1,
                        cat='Continuous' if continuous else 'Binary')
         for j in range(len(rows))]
    model += pulp.lpSum(z)
    for i, p in enumerate(primes):
        model += pulp.lpSum(t * v[i] for t, (_, v) in zip(z, rows)) >= demand[p]
    status = model.solve(pulp.PULP_CBC_CMD(msg=False, threads=1, timeLimit=10))
    if pulp.LpStatus[status] != 'Optimal':
        raise RuntimeError(pulp.LpStatus[status])
    if continuous:
        return {'objective': pulp.value(model.objective)}
    B = [b for t, (b, _) in zip(z, rows) if pulp.value(t) > 0.5]
    assert math.prod(B) % math.prod(A) == 0
    return {'objective': len(B), 'B': B}


def two_extension(B, x, M, d):
    """Exact check of all 0, 1, or 2 unused-number repairs via gcd types."""
    if d == 1:
        return True
    selected = set(B)
    types = Counter(math.gcd(b, d) for b in range(x + 1, x + M + 1)
                    if b not in selected)
    if d in types:
        return True
    gs = list(types)
    for i, g in enumerate(gs):
        for h in gs[i:]:
            if g == h and types[g] < 2:
                continue
            if g * h % d == 0:
                return True
    return False


def prefix_search():
    rng = random.Random(SEED)
    start = time.perf_counter()
    checked = 0
    failed = []
    marginal_failures = []
    for trial in range(700):
        M = rng.choice([24, 30, 36, 48, 60, 72, 90, 120, 150, 180, 210])
        x = rng.randrange(10**8)
        smooth = [a for a in range(2, M) if max(factor(a)) <= 7]
        pool = smooth if trial % 2 == 0 else list(range(2, M))
        k = rng.randint(2, min(12, len(pool) + 1))
        A = sorted(rng.sample(pool, k - 1) + [M])
        result = solve(A, x, M)
        B = result['B']
        spare = math.prod(B) // math.prod(A)
        for a in range(2, M):
            if a in A:
                continue
            d = a // math.gcd(a, spare)
            checked += 1
            if not two_extension(B, x, M, d):
                added = solve(A + [a], x, M)
                row = {'trial': trial, 'A': A, 'a': a, 'M': M, 'x': x,
                       'prefix': result, 'added': added, 'residual': d,
                       'residual_factorization': factor(d)}
                failed.append(row)
                if added['objective'] > result['objective'] + 2:
                    marginal_failures.append(row)
                if len(failed) >= 8:
                    return {'seed': SEED, 'trials': trial + 1,
                            'extensions_checked': checked, 'failures': failed,
                            'marginal_failures': marginal_failures,
                            'seconds': time.perf_counter() - start}
        if (trial + 1) % 100 == 0:
            print(json.dumps({'progress': trial + 1, 'extensions': checked,
                              'failures': len(failed)}), flush=True)
    return {'seed': SEED, 'trials': 700, 'extensions_checked': checked,
            'failures': failed, 'marginal_failures': marginal_failures,
            'seconds': time.perf_counter() - start}


def crt_lp():
    from verify_lower import crt_c
    cases = []
    for ps in [(11, 13), (17, 19, 23), (37, 41, 43, 47)]:
        M = ps[-1] ** 2
        c = crt_c(ps, M // 2)
        x = c - M // 2
        A = [p * q for i, p in enumerate(ps) for q in ps[i:]]
        cases.append({'primes': ps, 'M': M, 'x': x, 'n': len(A),
                      'lp': solve(A, x, M, continuous=True),
                      'prediction': len(ps) ** 2 - len(ps) + 1})
    return cases


def main():
    result = {'pulp_version': pulp.__version__, 'solver_threads': 1,
              'crt_lp': crt_lp(), 'prefix_search': prefix_search()}
    path = ROOT / 'astra_experiments.json'
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
