#!/usr/bin/env python3
"""Independent exact and F_2 verification for OEIS A185897."""

from __future__ import annotations

import argparse
import time
from pathlib import Path


HERE = Path(__file__).resolve().parent


def compute_a(nmax: int) -> list[int]:
    """Compute a(1)..a(nmax) from A(x-A(x)^2)=x/(1-x)."""
    a = [0] * (nmax + 1)
    t = [0] * (nmax + 1)  # T=x-A^2
    powers = [[0] * (nmax + 1) for _ in range(nmax + 1)]
    powers[0][0] = 1
    for n in range(1, nmax + 1):
        # [x^n]A^2 uses only a(1)..a(n-1). Extend every T^j coefficient
        # through degree n by truncated power-series multiplication.
        t[n] = 1 if n == 1 else -sum(a[i] * a[n - i] for i in range(1, n))
        powers[1][n] = t[n]
        for j in range(2, n + 1):
            powers[j][n] = sum(t[k] * powers[j - 1][n - k]
                               for k in range(1, n - j + 2))
        other = sum(a[j] * powers[j][n] for j in range(1, n))
        # The j=n term contributes exactly a(n), since [x^n]T^n=1.
        a[n] = 1 - other
    return a[1:]


def read_bfile(path: Path = HERE / "b185897.txt") -> list[int]:
    vals = []
    for line in path.read_text(encoding="ascii").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        n_s, value_s = line.split()
        n, value = int(n_s), int(value_s)
        if n != len(vals) + 1:
            raise ValueError(f"b-file index {n} is not contiguous at position {len(vals)+1}")
        vals.append(value)
    return vals


def parity_prediction(nmax: int) -> set[int]:
    result = {1} if nmax >= 1 else set()
    k = 0
    while 3 * (1 << k) <= nmax:
        lo, hi = 3 * (1 << k), 4 * (1 << k) - 1
        result.update(range(lo, min(hi, nmax) + 1))
        k += 1
    return result


# F_2[[x]] polynomials are nonnegative Python ints; bit i stores [x^i].
def f2_add(a: int, b: int) -> int:
    return a ^ b


def f2_mul(a: int, b: int, degree: int) -> int:
    mask = (1 << (degree + 1)) - 1
    if a.bit_count() > b.bit_count():
        a, b = b, a
    out = 0
    while a:
        low = a & -a
        shift = low.bit_length() - 1
        out ^= b << shift
        a ^= low
    return out & mask


def f2_square(a: int, degree: int) -> int:
    """Frobenius square: spread each input bit to twice its degree."""
    out = 0
    pos = 0
    while a:
        low = a & -a
        pos = low.bit_length() - 1
        out |= 1 << (2 * pos)
        a ^= low
    return out & ((1 << (degree + 1)) - 1)


def f2_inv(a: int, degree: int) -> int:
    """Invert a series with constant term 1 by precision-doubling Newton."""
    if not (a & 1):
        raise ValueError("series is not invertible: constant term must be 1")
    g, precision = 1, 1
    while precision < degree + 1:
        new_precision = min(2 * precision, degree + 1)
        trunc_degree = new_precision - 1
        # In characteristic two, g <- g*(a*g) squares the error.
        ag = f2_mul(a, g, trunc_degree)
        g = f2_mul(g, ag, trunc_degree)
        precision = new_precision
    return g & ((1 << (degree + 1)) - 1)


def f2_compose(coeffs: int, u: int, degree: int) -> int:
    """Horner composition C(u), where bit i of coeffs is [x^i]C."""
    out = 0
    for i in range(min(degree, coeffs.bit_length() - 1), -1, -1):
        out = f2_mul(out, u, degree)
        if (coeffs >> i) & 1:
            out ^= 1
    return out


def f2_l(y: int, degree: int) -> int:
    out = 0
    term = y
    while term:
        out ^= term
        term = f2_square(term, degree)
    return out & ((1 << (degree + 1)) - 1)


def bits_for_a(values: list[int]) -> int:
    out = 0
    for i, value in enumerate(values, 1):
        if value & 1:
            out |= 1 << i
    return out


def expected_b(degree: int) -> int:
    out = 1 << 1 if degree >= 1 else 0
    k = 0
    while 3 * (1 << k) <= degree:
        for n in range(3 * (1 << k), min(degree, 4 * (1 << k) - 1) + 1):
            out |= 1 << n
        k += 1
    return out


def check_mod2_recursion(degree: int) -> tuple[bool, int, list[int]]:
    """Check both candidate bits at each index using the actual recursion."""
    a = 0
    failures = []
    for n in range(1, degree + 1):
        valid = []
        for bit in (0, 1):
            candidate = a | (bit << n)
            t = (1 << 1) ^ f2_square(candidate, n)
            # [x^n] A(T), via Horner composition.
            lhs = f2_compose(candidate, t, n)
            if ((lhs >> n) & 1) == 1:  # [x^n] x/(1+x) is 1.
                valid.append(bit)
        if len(valid) != 1:
            failures.append(n)
            # Follow bit zero to keep the diagnostic bounded.
            chosen = 0
        else:
            chosen = valid[0]
        a |= chosen << n
    return not failures, degree, failures


def run_verification(nmax: int, degree: int, bfile: Path = HERE / "b185897.txt") -> dict:
    timings = {}
    start = time.perf_counter()
    bvals = read_bfile(bfile)
    timings["bfile_read"] = time.perf_counter() - start
    if nmax != len(bvals):
        raise ValueError(f"requested N={nmax}, but b-file has {len(bvals)} terms")

    start = time.perf_counter()
    values = compute_a(nmax)
    timings["integer_recompute"] = time.perf_counter() - start
    mismatches = [(i + 1, got, want) for i, (got, want) in enumerate(zip(values, bvals)) if got != want]

    odd = {i + 1 for i, v in enumerate(values) if v & 1}
    predicted = parity_prediction(nmax)
    symmetric_difference = sorted(odd ^ predicted)

    mask_degree = (1 << (degree + 1)) - 1
    x, one = 1 << 1, 1
    start = time.perf_counter()
    y = x ^ f2_mul(x, f2_square(x, degree), degree)  # x + x^3
    w = f2_l(y, degree)
    identity_i = (f2_square(w, degree) ^ w) == y

    inv_1px = f2_inv(one ^ x, degree)
    b = f2_mul(w, inv_1px, degree)
    b_expected = expected_b(degree)
    identity_ii = b == b_expected

    b2 = f2_square(b, degree)
    u = x ^ b2
    u_rhs = f2_mul(w, f2_square(inv_1px, degree), degree)
    identity_iii = u == u_rhs

    one_plus_u = one ^ u
    v = f2_mul(x, f2_mul(one_plus_u, inv_1px, degree), degree)
    lhs_iv = f2_square(v, degree) ^ v
    u3 = f2_mul(u, f2_square(u, degree), degree)
    rhs_iv = u ^ u3
    identity_iv = lhs_iv == rhs_iv

    composed = f2_compose(b, u, degree)
    target = ((1 << (degree + 1)) - 2)  # x + x^2 + ... + x^D
    identity_v = composed == target

    a_mod2 = bits_for_a(values)
    identity_vi = (a_mod2 & mask_degree) == (b & ((1 << (nmax + 1)) - 1))
    timings["mod2_identities"] = time.perf_counter() - start

    start = time.perf_counter()
    uniqueness_ok, uniqueness_n, uniqueness_failures = check_mod2_recursion(nmax)
    timings["mod2_uniqueness"] = time.perf_counter() - start

    return {
        "nmax": nmax, "degree": degree, "bvals": bvals, "values": values,
        "mismatches": mismatches, "odd": odd, "predicted": predicted,
        "symmetric_difference": symmetric_difference,
        "identities": {"i": identity_i, "ii": identity_ii, "iii": identity_iii,
                       "iv": identity_iv, "v": identity_v, "vi": identity_vi},
        "uniqueness_ok": uniqueness_ok, "uniqueness_n": uniqueness_n,
        "uniqueness_failures": uniqueness_failures, "timings": timings,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=None)
    parser.add_argument("--degree", type=int, default=2000)
    parser.add_argument("--bfile", type=Path, default=HERE / "b185897.txt")
    args = parser.parse_args()
    count = len(read_bfile(args.bfile))
    result = run_verification(args.n or count, args.degree, args.bfile)
    print(f"b-file terms: {len(result['bvals'])}")
    print(f"integer mismatches (n, recomputed, b-file): {result['mismatches']}")
    print(f"odd indices: {sorted(result['odd'])}")
    print(f"predicted indices: {sorted(result['predicted'])}")
    print(f"symmetric difference: {result['symmetric_difference']}")
    for key, passed in result["identities"].items():
        print(f"identity {key}: {'PASS' if passed else 'FAIL'} through degree {result['degree']}")
    print(f"mod-2 recursion uniqueness: {'PASS' if result['uniqueness_ok'] else 'FAIL'} at {result['uniqueness_n']} indices; failures={result['uniqueness_failures']}")
    for name, seconds in result["timings"].items():
        print(f"runtime {name}: {seconds:.6f}s")
    if result["mismatches"] or result["symmetric_difference"] or not all(result["identities"].values()) or not result["uniqueness_ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
