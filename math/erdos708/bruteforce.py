#!/usr/bin/env python3
"""Bounded exact search for the erdosproblems.com interpretation of g(n).

For each n and each n-element A subset [2, Mmax], check intervals
I=[s,s+max(A)-1] for s=1,...,200. A branch-and-bound set-cover search
uses prime-exponent vectors to find the least size of B subset I with
prod(A) | prod(B).
"""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations

LIMITS = {2: 24, 3: 24, 4: 16}
STARTS = 200


def factorize(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def min_cover(target: tuple[int, ...], values: tuple[tuple[int, ...], ...], cap: int):
    """Return an exact minimum cover, by bounded branch-and-bound."""
    useful = tuple(i for i, v in enumerate(values) if any(v))
    vecs = tuple(values[i] for i in useful)
    full = (1 << len(vecs)) - 1

    for limit in range(1, cap + 1):
        @lru_cache(None)
        def feasible(need: tuple[int, ...], avail: int, slots: int):
            if not any(need):
                return ()
            if slots == 0:
                return None
            options_by_prime = []
            for j, required in enumerate(need):
                if not required:
                    continue
                opts = [i for i, v in enumerate(vecs)
                        if (avail >> i) & 1 and v[j] > 0]
                if not opts:
                    return None
                # Even the best `slots` remaining contributions must suffice.
                top = sorted((vecs[i][j] for i in opts), reverse=True)[:slots]
                if sum(top) < required:
                    return None
                options_by_prime.append((len(opts), j, opts))
            _, j, opts = min(options_by_prime)
            opts.sort(key=lambda i: sum(min(need[t], vecs[i][t])
                                         for t in range(len(need))), reverse=True)
            for i in opts:
                v = vecs[i]
                nxt = tuple(max(0, need[t] - v[t]) for t in range(len(need)))
                result = feasible(nxt, avail ^ (1 << i), slots - 1)
                if result is not None:
                    return (i,) + result
            return None
        result = feasible(target, full, limit)
        if result is not None:
            return len(result), tuple(useful[i] for i in result)
    raise RuntimeError(f"no cover found with at most {cap} terms")


def prepare_interval(start: int, length: int, primes: tuple[int, ...]):
    index = {p: j for j, p in enumerate(primes)}
    vectors = []
    vals = tuple(range(start, start + length))
    for b in vals:
        v = [0] * len(primes)
        for p, e in factorize(b).items():
            if p in index:
                v[index[p]] = e
        vectors.append(tuple(v))
    return vals, tuple(vectors)


def check_n(n: int, mmax: int):
    universe = range(2, mmax + 1)
    worst = []
    max_min = 0
    count = 0
    cache = {}
    for A in combinations(universe, n):
        M = max(A)
        facA = [factorize(a) for a in A]
        prime_set = tuple(sorted({p for f in facA for p in f}))
        pi = {p: j for j, p in enumerate(prime_set)}
        target = [0] * len(prime_set)
        for f in facA:
            for p, e in f.items():
                target[pi[p]] += e
        target = tuple(target)
        for start in range(1, STARTS + 1):
            key = (M, start, prime_set)
            if key not in cache:
                cache[key] = prepare_interval(start, M, prime_set)
            vals, vectors = cache[key]
            k, inds = min_cover(target, vectors, n + 2)
            count += 1
            if k > max_min:
                max_min, worst = k, [(A, (start, start + M - 1), tuple(vals[i] for i in inds))]
            elif k == max_min:
                worst.append((A, (start, start + M - 1), tuple(vals[i] for i in inds)))
    return max_min, count, worst


def construction_report(primes: tuple[int, ...], include_diagonal: bool):
    A = tuple(sorted({primes[i] * primes[j]
                      for i in range(len(primes))
                      for j in range(i if include_diagonal else i + 1,
                                     len(primes))}))
    M = max(A)
    pset = tuple(sorted({p for a in A for p in factorize(a)}))
    idx = {p: i for i, p in enumerate(pset)}
    target = [0] * len(pset)
    for a in A:
        for p, e in factorize(a).items():
            target[idx[p]] += e
    best = (0, None, None)
    for start in range(1, STARTS + 1):
        vals, vecs = prepare_interval(start, M, pset)
        k, inds = min_cover(tuple(target), vecs, len(A) + 2)
        if k > best[0]:
            best = (k, (start, start + M - 1), tuple(vals[i] for i in inds))
    return A, M, best


if __name__ == "__main__":
    for n, mmax in LIMITS.items():
        value, checked, cases = check_n(n, mmax)
        print(f"n={n} Mmax={mmax} starts=1..{STARTS}: g_bound={value}; cases={checked}")
        for A, I, B in cases[:8]:
            print(f"  A={A} I={I} B={B}")
        if len(cases) > 8:
            print(f"  ({len(cases)-8} more tied worst cases)")
    for ps, diagonal in (((5, 7), False), ((7, 11, 13), False),
                         ((17, 19, 23), False), ((17, 19, 23), True)):
        A, M, best = construction_report(ps, diagonal)
        pset = tuple(sorted({p for a in A for p in factorize(a)}))
        pi = {p: j for j, p in enumerate(pset)}
        target = [0] * len(pset)
        for a in A:
            for p, e in factorize(a).items():
                target[pi[p]] += e
        start = M + 1
        vals, vectors = prepare_interval(start, M, pset)
        k, inds = min_cover(tuple(target), vectors, len(A) + 2)
        direct = (k, (start, start + M - 1), tuple(vals[i] for i in inds))
        print(f"construction primes={ps} diagonal={diagonal} A={A} maxA={M} "
              f"max_min_starts_1..{STARTS}={best}; I=[M+1,2M]={direct}")
    # The 1959 paper's explicit n=3 counterexample and the easy translated
    # interval for the same A make the quantifier issue directly checkable.
    A, start, length = (77, 91, 143), 5935, 143
    pset = (7, 11, 13)
    pi = {p: j for j, p in enumerate(pset)}
    target = [0] * len(pset)
    for a in A:
        for p, e in factorize(a).items():
            target[pi[p]] += e
    for start in (5935, 144):
        vals, vectors = prepare_interval(start, length, pset)
        k, inds = min_cover(tuple(target), vectors, 5)
        print(f"source n=3 A={A} I=({start},{start+length-1}) "
              f"min={k} B={tuple(vals[i] for i in inds)}")
