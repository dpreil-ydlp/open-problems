#!/usr/bin/env python3
"""Uncapped exact-order verification for OEIS A062887, n <= 3000."""

from __future__ import annotations

import math
import csv
import time
from pathlib import Path


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return [p for p, prime in enumerate(sieve) if prime]


def factor_integer(n: int, primes: list[int] | None = None) -> dict[int, int]:
    """Return the exact prime factorization of positive n by trial division."""
    if n < 1:
        raise ValueError("n must be positive")
    factors: dict[int, int] = {}
    if n == 1:
        return factors
    if primes is None:
        primes = primes_up_to(math.isqrt(n))
    remaining = n
    for p in primes:
        if p * p > remaining:
            break
        if remaining % p == 0:
            exponent = 0
            while remaining % p == 0:
                remaining //= p
                exponent += 1
            factors[p] = exponent
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def euler_phi(n: int, primes: list[int] | None = None) -> int:
    result = n
    for p in factor_integer(n, primes):
        result -= result // p
    return result


def multiplicative_order_10(modulus: int, primes: list[int] | None = None) -> int:
    """Compute ord_modulus(10) exactly by reducing phi with its prime factors."""
    if modulus < 1 or math.gcd(10, modulus) != 1:
        raise ValueError("modulus must be positive and coprime to 10")
    if modulus == 1:
        return 1
    order = euler_phi(modulus, primes)
    for p in factor_integer(order, primes):
        while order % p == 0 and pow(10, order // p, modulus) == 1:
            order //= p
    assert pow(10, order, modulus) == 1
    return order


def x_5k_mod(k: int, modulus: int) -> int:
    """Compute X_(5k) modulo modulus without constructing X_(5k)."""
    if modulus == 1:
        return 0
    base = pow(10, 5, modulus)
    power, total = 1, 0
    block_power, block_sum = base, 1
    count = k
    while count:
        if count & 1:
            total = (total + power * block_sum) % modulus
            power = power * block_power % modulus
        block_sum = block_sum * (1 + block_power) % modulus
        block_power = block_power * block_power % modulus
        count >>= 1
    return 31975 * total % modulus


def x_5k_horner_mod(k: int, modulus: int) -> int:
    """Evaluate X_(5k) digit by digit from left to right modulo modulus."""
    if k < 1 or modulus < 1:
        raise ValueError("k and modulus must be positive")
    residue = 0
    for i in range(5 * k - 1, -1, -1):
        digit = (5 + 2 * i) % 10
        residue = (10 * residue + digit) % modulus
    return residue


def first_witness_residue_scan(m: int, bound: int) -> tuple[int, int] | None:
    """Find the shortest admissible multiple by incrementally tracking residues.

    Return (length, units digit). Ties use increasing numeric order, which at a
    fixed length means increasing leading digit.
    """
    if m < 1 or bound < 1:
        raise ValueError("m and bound must be positive")
    units = (1, 3, 5, 7, 9)
    residues = [0] * 5
    power10 = 1 % m
    for length in range(1, bound + 1):
        for i, e in enumerate(units):
            leading = (e + 2 * (length - 1)) % 10
            residues[i] = (leading * power10 + residues[i]) % m
        hits = [i for i, residue in enumerate(residues) if residue == 0]
        if hits:
            i = min(hits, key=lambda j: (units[j] + 2 * (length - 1)) % 10)
            return length, units[i]
        power10 = power10 * 10 % m
    return None


def strip_fives(m: int) -> tuple[int, int]:
    a = 0
    while m % 5 == 0:
        m //= 5
        a += 1
    return a, m


def run(n_max: int = 3000, random_count: int = 200, seed: int = 62887) -> dict:
    started = time.perf_counter()
    largest_modulus = 99999 * (2 * n_max + 1)
    primes = primes_up_to(math.isqrt(max(largest_modulus, 99999 * 1_000_000)))
    factor_start = time.perf_counter()

    rows: list[tuple[int, int, int, int, int, int]] = []
    all_rows: list[tuple[int, int, int, int, int | None, int | None, bool]] = []
    failures = []
    max_witness = (0, None)
    excluded_scans = 0
    for n in range(n_max + 1):
        m = 2 * n + 1
        a, m_prime = strip_fives(m)
        k = multiplicative_order_10(99999 * m_prime, primes)
        bound = 5 * k
        witness = first_witness_residue_scan(m, bound)
        all_rows.append((n, m, k, bound,
                         witness[0] if witness else None,
                         witness[1] if witness else None,
                         m % 125 == 0))
        if m % 125 == 0:
            excluded_scans += 1
            if witness is not None:
                failures.append(("125-multiple witness", n, m, witness))
        else:
            if witness is None:
                failures.append(("missing witness", n, m, k, bound))
            else:
                length, units = witness
                rows.append((n, m, k, bound, length, units))
                if length > max_witness[0]:
                    max_witness = (length, n)
                # The units=5 member of the certified length is divisible by m.
                horner_remainder = x_5k_horner_mod(k, m)
                if horner_remainder != 0 or x_5k_mod(k, m_prime) != 0 or length > bound:
                    failures.append(("bound residue", n, m, k, length, horner_remainder))
    exact_range_seconds = time.perf_counter() - factor_start

    # Independently check all five families modulo 125 for every L <= 3000.
    mod125_residues = [0] * 5
    mod125_power = 1
    mod125_hits = []
    for length in range(1, 3001):
        for i, e in enumerate((1, 3, 5, 7, 9)):
            leading = (e + 2 * (length - 1)) % 10
            mod125_residues[i] = (leading * mod125_power + mod125_residues[i]) % 125
        if 0 in mod125_residues:
            mod125_hits.append((length, tuple((1, 3, 5, 7, 9)[i]
                                               for i, r in enumerate(mod125_residues) if r == 0)))
        mod125_power = mod125_power * 10 % 125
    if mod125_hits:
        failures.append(("admissible divisible by 125", mod125_hits[:5]))

    # Reproduce round 1's deterministic sample, with no order cap.
    import random
    rng = random.Random(seed)
    samples = []
    while len(samples) < random_count:
        candidate = rng.randrange(1, 1_000_001)
        if candidate % 2 and candidate % 5:
            samples.append(candidate)
    random_start = time.perf_counter()
    random_rows = []
    for m_prime in samples:
        k = multiplicative_order_10(99999 * m_prime, primes)
        remainder = x_5k_mod(k, m_prime)
        random_rows.append((m_prime, k, remainder))
        if remainder:
            failures.append(("random order divisibility", m_prime, k, remainder))
    random_seconds = time.perf_counter() - random_start

    csv_path = Path(__file__).with_name("n3000-round2-results.csv")
    with csv_path.open("w", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(("n", "m", "k", "bound_5k", "smallest_witness_length",
                         "smallest_witness_units_digit", "125_divides_m"))
        writer.writerows(all_rows)

    return {
        "rows": rows,
        "failures": failures,
        "max_witness": max_witness,
        "excluded_scans": excluded_scans,
        "mod125_hits": mod125_hits,
        "random_rows": random_rows,
        "csv_path": csv_path,
        "factor_range_seconds": exact_range_seconds,
        "random_seconds": random_seconds,
        "total_seconds": time.perf_counter() - started,
    }


if __name__ == "__main__":
    result = run()
    print(f"full n range rows: {len(result['rows'])}; failures: {result['failures']}")
    print(f"excluded m divisible by 125 scanned: {result['excluded_scans']}")
    print(f"max smallest witness length/n: {result['max_witness']}")
    print(f"mod 125 hits through 3000 digits: {result['mod125_hits']}")
    print(f"exact range runtime: {result['factor_range_seconds']:.3f}s")
    print(f"random checks: {len(result['random_rows'])}, runtime: {result['random_seconds']:.3f}s")
    print(f"per-n results: {result['csv_path'].name} ({3001} rows plus header)")
    print(f"total runtime: {result['total_seconds']:.3f}s")
    print("previously unresolved n | m | k | 5k | shortest witness length")
    for n, m, k, bound, length, units in result["rows"]:
        if length > 2000:
            print(f"{n} | {m} | {k} | {bound} | {length} | {units}")
    if result["failures"]:
        raise SystemExit(1)
