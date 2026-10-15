#!/usr/bin/env python3
"""Independent, bounded checks for OEIS A062887 (Python standard library only)."""

from __future__ import annotations

import argparse
import csv
import math
import random
import time
from pathlib import Path


def admissible_numbers(length: int, step: int = 2) -> list[int]:
    """Return admissible numbers of one length, in increasing numeric order.

    ``step`` is the change in digits when moving from the units place toward
    the leading place.  The OEIS reading has step +2; the alternate reading
    (two more from left to right) has step -2.
    """
    if length < 1:
        raise ValueError("length must be positive")
    numbers = []
    for units in (1, 3, 5, 7, 9):
        digits = [(units + step * i) % 10 for i in range(length)]
        numbers.append(int("".join(map(str, reversed(digits)))))
    return sorted(numbers)


def first_multiple(multiplier: int, max_len: int = 2000, step: int = 2):
    """Return the first admissible multiple and its length, or ``(None, None)``."""
    if multiplier < 1:
        raise ValueError("multiplier must be positive")
    for length in range(1, max_len + 1):
        for value in admissible_numbers(length, step):
            if value % multiplier == 0:
                return value, length
    return None, None


def first_multiples_through(n_max: int, max_len: int):
    """Search all m=2n+1 together, reusing each length's five candidates."""
    unresolved = list(range(n_max + 1))
    results = [None] * (n_max + 1)
    for length in range(1, max_len + 1):
        for value in admissible_numbers(length):
            remaining = []
            for n in unresolved:
                if value % (2 * n + 1) == 0:
                    results[n] = (value, length)
                else:
                    remaining.append(n)
            unresolved = remaining
            if not unresolved:
                break
        if not unresolved:
            break
    return results


def parse_bfile(path: Path) -> dict[int, int]:
    terms = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        index, value = line.split()[:2]
        terms[int(index)] = int(value)
    return terms


def is_admissible(value: int) -> bool:
    digits = str(value)
    return all(int(d) % 2 == 1 for d in digits) and all(
        int(digits[i + 1]) == (int(digits[i]) - 2) % 10
        for i in range(len(digits) - 1)
    )


def multiplicative_order_10(modulus: int, cap: int):
    """Find ord_modulus(10), or return None once the loop cap is exceeded."""
    if math.gcd(10, modulus) != 1:
        raise ValueError("10 must be coprime to the modulus")
    value = 1
    for exponent in range(1, cap + 1):
        value = value * 10 % modulus
        if value == 1:
            return exponent
    return None


def geometric_sum_mod(base: int, count: int, modulus: int) -> int:
    """Compute 1 + base + ... + base**(count-1) modulo modulus in O(log count)."""
    if count < 0 or modulus < 1:
        raise ValueError("count must be nonnegative and modulus positive")
    if modulus == 1:
        return 0
    # Pair (base**n, sum(base**j, j=0..n-1)); compose pairs by doubling.
    result_power, result_sum = 1, 0
    block_power, block_sum = base % modulus, 1
    n = count
    while n:
        if n & 1:
            result_sum = (result_sum + result_power * block_sum) % modulus
            result_power = result_power * block_power % modulus
        block_sum = block_sum * (1 + block_power) % modulus
        block_power = block_power * block_power % modulus
        n >>= 1
    return result_sum


def x_5k_mod(k: int, modulus: int) -> int:
    """Compute X_(5k) modulo modulus without constructing its decimal integer."""
    return 31975 * geometric_sum_mod(pow(10, 5, modulus), k, modulus) % modulus


def run_checks(max_len: int = 2000, n_max: int = 3000, seed: int = 62887,
               order_cap: int = 100_000, bfile: Path | None = None):
    started = time.perf_counter()
    out = []
    bfile = bfile or Path(__file__).with_name("b062887.txt")
    terms = parse_bfile(bfile)

    out.append("a(0..25) comparison (OEIS text reading, increasing numeric search):")
    out.append("n | m=2n+1 | computed a(n) | b-file a(n) | match")
    out.append("--|---------|--------------|------------|------")
    mismatches = []
    for n in range(26):
        value, _ = first_multiple(2 * n + 1, max_len)
        actual = value if value is not None else 0
        expected = terms.get(n)
        match = actual == expected
        if not match:
            mismatches.append(n)
        out.append(f"{n} | {2*n+1} | {actual} | {expected} | {'yes' if match else 'NO'}")
    if mismatches:
        out.append("Mismatch: trying the alternate left-to-right +2 reading:")
        alt_bad = []
        for n in range(26):
            value, _ = first_multiple(2 * n + 1, max_len, step=-2)
            actual = value if value is not None else 0
            if actual != terms.get(n):
                alt_bad.append(n)
        out.append(f"alternate mismatches at n={alt_bad}; OEIS reading mismatches at n={mismatches}")
    out.append(f"Comparison result: {'PASS' if not mismatches else 'FAIL'}")

    check_start = time.perf_counter()
    witnesses = []
    violations = []
    found_count = 0
    all_results = first_multiples_through(n_max, max_len)
    for n, result in enumerate(all_results):
        m = 2 * n + 1
        value, length = result if result is not None else (None, None)
        found = result is not None
        if found:
            found_count += 1
            witnesses.append((length, n))
        expected_found = m % 125 != 0
        row = (n, m, found, length, m % 125 == 0)
        if found != expected_found:
            violations.append(row)
    result_path = Path(__file__).with_name("n3000-results.csv")
    with result_path.open("w", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(("n", "m", "found", "witness_length", "125_divides_m"))
        for n, result in enumerate(all_results):
            m = 2 * n + 1
            writer.writerow((n, m, result is not None,
                             result[1] if result is not None else "", m % 125 == 0))
    maximum_length, maximum_n = max(witnesses, default=(0, None))
    out.append("")
    out.append(f"n=0..{n_max}, max-len={max_len}: found {found_count}/{n_max+1}; "
               f"expected found iff 125 does not divide m: {'PASS' if not violations else 'FAIL'}")
    out.append(f"Maximum witness length: {maximum_length} digits at n={maximum_n}")
    out.append(f"Per-n records: {result_path.name} ({n_max + 1} rows plus header)")
    out.append(f"Violations: {violations[:20]}" if violations else "Violations: none")
    out.append(f"n-range runtime: {time.perf_counter() - check_start:.3f} s")

    # Check the closed formula for k=1..40 using exact integer arithmetic.
    formula_start = time.perf_counter()
    formula_failures = []
    for k in range(1, 41):
        length = 5 * k
        digits = [str((5 + 2 * i) % 10) for i in range(length)]
        x_digits = int("".join(reversed(digits)))
        formula_value = 31975 * (10 ** length - 1) // 99999
        if x_digits != formula_value:
            formula_failures.append(k)
    out.append("")
    out.append(f"X_(5k) closed identity k=1..40: {'PASS' if not formula_failures else 'FAIL'}")
    out.append(f"Identity failures: {formula_failures or 'none'}")

    rng = random.Random(seed)
    samples = []
    while len(samples) < 200:
        m_prime = rng.randrange(1, 1_000_001)
        if m_prime % 2 and m_prime % 5:
            samples.append(m_prime)
    order_checked = 0
    order_skipped = 0
    divisibility_failures = []
    for m_prime in samples:
        order = multiplicative_order_10(99999 * m_prime, order_cap)
        if order is None:
            order_skipped += 1
            continue
        order_checked += 1
        remainder = x_5k_mod(order, m_prime)
        if remainder:
            divisibility_failures.append((m_prime, order, remainder))
    out.append(f"Random order/divisibility checks (seed={seed}, 200 odd m' coprime to 10 <= 1e6): "
               f"checked={order_checked}, skipped at order cap {order_cap}={order_skipped}; "
               f"{'PASS' if not divisibility_failures else 'FAIL'}")
    out.append(f"Divisibility failures: {divisibility_failures or 'none'}")
    assert not formula_failures and not divisibility_failures
    out.append(f"Identity/random runtime: {time.perf_counter() - formula_start:.3f} s")

    scan_start = time.perf_counter()
    scanned = 0
    admissible_multiples = []
    for value in range(125, 10_000_001, 125):
        scanned += 1
        if is_admissible(value):
            admissible_multiples.append(value)
    out.append("")
    out.append(f"Direct scan of {scanned:,} multiples of 125 through 10,000,000: "
               f"{'PASS' if not admissible_multiples else 'FAIL'}")
    out.append(f"Admissible multiples found: {admissible_multiples or 'none'}")
    out.append(f"125 scan runtime: {time.perf_counter() - scan_start:.3f} s")
    assert not admissible_multiples
    out.append(f"Total runtime: {time.perf_counter() - started:.3f} s")
    return "\n".join(out), not violations


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-len", type=int, default=2000)
    parser.add_argument("--n-max", type=int, default=3000)
    parser.add_argument("--seed", type=int, default=62887)
    parser.add_argument("--order-cap", type=int, default=100_000)
    parser.add_argument("--bfile", type=Path)
    args = parser.parse_args()
    if args.max_len < 1 or args.n_max < 0 or args.order_cap < 1:
        parser.error("--max-len and --order-cap must be positive; --n-max must be nonnegative")
    report, conjecture_pass = run_checks(
        args.max_len, args.n_max, args.seed, args.order_cap, args.bfile
    )
    print(report)
    assert conjecture_pass, "Some n did not find a witness within --max-len despite 125 not dividing m."


if __name__ == "__main__":
    main()
