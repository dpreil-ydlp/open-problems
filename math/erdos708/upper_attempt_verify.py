#!/usr/bin/env python3
"""Exact certificates for SOL-UPPER-ATTEMPT.md; one process, no solver.

Run: nice -n 10 .venv/bin/python upper_attempt_verify.py
Optional historical matching experiment: add --explore-matching.
The finite Hall certificate uses a sieve of 150,000,001 bytes.
"""

from __future__ import annotations

import argparse
import bisect
import json
import math
import random
import time
from fractions import Fraction
from pathlib import Path


def factor(a: int) -> dict[int, int]:
    out = {}
    p = 2
    while p * p <= a:
        while a % p == 0:
            out[p] = out.get(p, 0) + 1
            a //= p
        p += 1
    if a > 1:
        out[a] = out.get(a, 0) + 1
    return out


def valuation(a: int, p: int) -> int:
    out = 0
    while a % p == 0:
        out += 1
        a //= p
    return out


def factorial_valuation(M: int, p: int) -> int:
    out = 0
    while M:
        M //= p
        out += M
    return out


def complement_certificate() -> dict:
    M = 30
    primes = (2, 3, 5)
    exponents = [factorial_valuation(M, p) for p in primes]
    moduli = [p**e for p, e in zip(primes, exponents)]
    modulus = math.prod(moduli)
    x = sum(-j * (modulus // q) * pow(modulus // q, -1, q)
            for j, q in enumerate(moduli, 1)) % modulus
    forced = [x + j for j in range(1, 4)]
    for p, e, b in zip(primes, exponents, forced):
        assert b % (p**e) == 0
        assert valuation(b, p) > e - 1
    host = ((x // M) + 1) * M
    assert x < host <= x + M and host % M == 0
    assert x == 3188778734345781247
    return {"A": [M], "M": M, "x": x, "moduli": moduli,
            "C_valuations_2_3_5": [e - 1 for e in exponents],
            "forced_omissions": forced,
            "forced_valuations": [valuation(b, p)
                                  for b, p in zip(forced, primes)],
            "single_host": host, "h": 1,
            "maximum_size_of_stronger_complement_at_most": 27}


def induction_certificate() -> dict:
    primes = (2, 3, 5)

    def kappa(a: int) -> int:
        return sum(a % p == 0 for p in primes)

    base = [a for a in range(31, 181) if kappa(a) >= 2]
    extras = [32, 64, 81, 85, 112, 117, 125, 175]
    A0 = sorted(base + extras)
    I = range(181, 361)
    B0 = [b for b in I if kappa(b) != 1]
    ps = sorted(set().union(*(set(factor(a)) for a in A0)))
    rows = [{"p": p, "A0": sum(valuation(a, p) for a in A0),
             "B0": sum(valuation(b, p) for b in B0)} for p in ps]
    assert len(base) == 40 and len(set(A0)) == 48 and len(B0) == 96
    assert all(row["B0"] >= row["A0"] for row in rows)
    assert all(row["A0"] == row["B0"]
               for row in rows if row["p"] in primes)
    assert math.prod(B0) % math.prod(A0) == 0
    assert all(kappa(b) == 1 for b in I if b not in B0)
    new = [182, 183, 185]
    assert all(b not in B0 for b in new)
    assert math.prod(new) % 30 == 0
    counts = {a: sum(b % a == 0 for b in I) for a in A0 + [30]}
    assert counts[30] == max(counts.values()) == 6
    fixed = [b for b in B0 if b != 181] + new
    assert len(fixed) == 98 and len(set(fixed)) == 98
    assert math.prod(fixed) % (30 * math.prod(A0)) == 0
    return {"M": 180, "x": 180, "removed_element": 30,
            "A0": A0, "A0_size": 48, "full_n": 49,
            "B0_size": 96, "valuation_rows": rows,
            "most_multiples": 6, "exact_minimum_new_hosts": 3,
            "extension": new, "extension_only_size": 99,
            "exchange_remove": 181, "exchange_result_size": 98}


def packing_certificate() -> dict:
    primes = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151]
    assert all(factor(p) == {p: 1} for p in primes)
    n = math.comb(len(primes), 3)
    M = math.prod(primes[-3:])
    assert n == 165 and M == 3127361
    assert primes[-1] * (2 * n) <= M
    assert primes[0] * primes[1] * (2 * n) > M
    return {"primes": primes, "n": n, "M": M,
            "threshold_numerator": M, "threshold_denominator": 2 * n,
            "smallest_pair_product": primes[0] * primes[1],
            "required_separate_small_chunks": 3 * n, "2n": 2 * n}


def sparse_construction(A: list[int], x: int) -> tuple[set[int], dict]:
    """Construct the stronger two-host assignment when M >= (2n)^3."""
    n, M = len(A), max(A)
    assert M >= (2 * n)**3
    large: dict[int, list[tuple[int, int]]] = {}
    small = []
    assignment = {a: {} for a in A}
    for a in A:
        atoms = [{p: p**e} for p, e in factor(a).items()]
        big = [g for g in atoms if math.prod(g.values()) * 2 * n > M]
        assert len(big) <= 1
        rest = [g for g in atoms if g not in big]
        if big:
            p, q = next(iter(big[0].items()))
            large.setdefault(p, []).append((q, a))
            if rest:
                merged = {p: q for g in rest for p, q in g.items()}
                assert math.prod(merged.values()) * 2 * n <= M
                small.append((a, merged))
        else:
            while True:
                pair = next(((i, j) for i in range(len(rest))
                             for j in range(i + 1, len(rest))
                             if math.prod(rest[i].values())
                             * math.prod(rest[j].values()) * 2 * n <= M), None)
                if pair is None:
                    break
                i, j = pair
                rest[i] = rest[i] | rest[j]
                rest.pop(j)
            assert len(rest) <= 2
            small.extend((a, g) for g in rest)
    opened: set[int] = set()
    for p, tasks in large.items():
        used: set[int] = set()
        for q, a in sorted(tasks, reverse=True):
            b = ((x // q) + 1) * q
            while b in used:
                b += q
            assert x < b <= x + M
            used.add(b)
            opened.add(b)
            assignment[a][p] = b
    for a, group in small:
        d = math.prod(group.values())
        assert d * 2 * n <= M
        b = ((x // d) + 1) * d
        while b in opened:
            b += d
        assert x < b <= x + M
        opened.add(b)
        for p in group:
            assignment[a][p] = b
    assert len(opened) <= 2 * n
    for a in A:
        assert set(assignment[a]) == set(factor(a))
        assert len(set(assignment[a].values())) <= 2
        for p, e in factor(a).items():
            assert assignment[a][p] % (p**e) == 0
    for p in set().union(*(set(factor(a)) for a in A)):
        hosts = [assignment[a][p] for a in A if p in assignment[a]]
        assert len(hosts) == len(set(hosts))
    assert math.prod(opened) % math.prod(A) == 0
    return opened, assignment


def sparse_checks() -> dict:
    seed = 70820261015
    rng = random.Random(seed)
    cases = 0
    maximum_selected = 0
    for n in range(1, 25):
        base = (2 * n)**3
        for j in range(12):
            M = base if j == 0 else base + rng.randrange(base + 1)
            A = sorted(rng.sample(range(2, M), n - 1) + [M])
            B, _ = sparse_construction(A, rng.randrange(10**30))
            cases += 1
            maximum_selected = max(maximum_selected, len(B))
    return {"seed": seed, "cases": cases, "n_range": [1, 24],
            "boundary_cases_M_equals_8n_cubed": 24,
            "maximum_selected": maximum_selected,
            "checks": ["all hosts in I", "at most 2n hosts",
                       "each element uses at most two hosts",
                       "distinct hosts for each fixed prime",
                       "exact product divisibility"]}


def finite_hall_certificate() -> dict:
    M = 300_000_000
    N = M // 2
    sieve = bytearray(b"\1") * (N + 1)
    sieve[0:2] = b"\0\0"
    small_primes = []
    for p in range(2, math.isqrt(N) + 1):
        if sieve[p]:
            small_primes.append(p)
            start = p * p
            sieve[start::p] = b"\0" * ((N - start) // p + 1)
    higher_odd_powers = []
    for p in small_primes[1:]:
        q = p * p
        while q <= N:
            higher_odd_powers.append(q)
            q *= p
    higher_odd_powers.sort()
    bad_even = M.bit_length() - 1  # Pure powers 2^s, s >= 1.
    count_terms = []
    for s in range(1, M.bit_length()):
        limit = M // (2**s)
        pi = sieve.count(1, 0, limit + 1)
        higher = bisect.bisect_right(higher_odd_powers, limit)
        odd_powers = pi - int(limit >= 2) + higher
        bad_even += odd_powers
        count_terms.append({"s": s, "limit": limit, "pi": pi,
                            "higher_odd_prime_powers": higher,
                            "all_odd_prime_powers": odd_powers})
    del sieve
    n = N - bad_even
    density = Fraction(1)
    for p in small_primes[1:]:
        density *= Fraction(p - 1, p)
    expected = N * density
    ceil_expected = -(-expected.numerator // expected.denominator)
    assert expected > bad_even
    y = 10**18 + 708
    x = 2 * y
    surviving = bytearray(b"\1") * N
    for p in small_primes[1:]:
        start = (-y - 1) % p
        surviving[start::p] = b"\0" * ((N - 1 - start) // p + 1)
    rough_even = surviving.count(1)
    assert bad_even == 17_652_034
    assert n == 132_347_966
    assert rough_even == 17_885_755
    assert N - rough_even < n < M // 2
    assert M % 30 == 0
    return {"M": M, "x": x, "interval_end": x + M,
            "A_description": "even a <= M with at least two distinct odd prime divisors",
            "n": n, "excluded_even_count": bad_even,
            "Y": math.isqrt(N), "odd_sieving_primes": len(small_primes) - 1,
            "rough_even_hosts": rough_even,
            "neighbor_upper_bound": N - rough_even,
            "Hall_deficit_at_least": rough_even - bad_even,
            "ceil_CRT_average": ceil_expected,
            "exact_CRT_average_exceeds_excluded_count": expected > bad_even,
            "prime_power_count_terms": count_terms}


def exploratory_matching() -> dict:
    rng = random.Random(708708)
    count = 0
    for M in list(range(5, 101)) + [120, 150, 180, 210, 250, 300, 400, 500]:
        A = list(range(2, M + 1))
        factors = [factor(a) for a in A]
        for _ in range(15):
            x = rng.randrange(10**18)
            for mode in ("largest", "any_component"):
                edges = []
                for a, f in zip(A, factors):
                    divisors = ([a // (max(f)**f[max(f)])] if mode == "largest"
                                else [a // p**e for p, e in f.items()])
                    edges.append(sorted({b - x - 1 for d in divisors
                                         for b in range((x // d + 1) * d,
                                                        x + M + 1, d)}))
                matched = [-1] * M

                def augment(u: int, seen: set[int]) -> bool:
                    for b in edges[u]:
                        if b in seen:
                            continue
                        seen.add(b)
                        if matched[b] < 0 or augment(matched[b], seen):
                            matched[b] = u
                            return True
                    return False

                assert all(augment(u, set()) for u in range(len(A)))
                count += 1
    return {"seed": 708708, "cases": count, "observed_Hall_failures": 0,
            "M_values": list(range(5, 101)) + [120, 150, 180, 210, 250, 300, 400, 500],
            "x_draws_per_M": 15, "modes": ["largest", "any_component"],
            "limit": "Exploration only; the finite certificate disproves the largest rule."}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--explore-matching", action="store_true")
    args = parser.parse_args()
    start = time.monotonic()
    evidence = {"method": "exact Python integer arithmetic; no floating-point acceptance",
                "processes": 1, "complement": complement_certificate(),
                "induction": induction_certificate(),
                "packing": packing_certificate(),
                "sparse_construction": sparse_checks(),
                "finite_Hall": finite_hall_certificate()}
    if args.explore_matching:
        evidence["exploratory_matching"] = exploratory_matching()
    evidence["seconds"] = time.monotonic() - start
    path = Path(__file__).with_name("UPPER-ATTEMPT-EVIDENCE.json")
    path.write_text(json.dumps(evidence, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "evidence": str(path),
                      "seconds": evidence["seconds"],
                      "finite_Hall_deficit": evidence["finite_Hall"]["Hall_deficit_at_least"],
                      "sparse_cases": evidence["sparse_construction"]["cases"]}, indent=2))


if __name__ == "__main__":
    main()
