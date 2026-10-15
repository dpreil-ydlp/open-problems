#!/usr/bin/env python3
"""Independent Theorem C tests. Standard library plus existing PuLP/CBC only.

Run from this folder: .venv/bin/python review_sol_theorem_c_check.py
Writes REVIEW-SOL-THEOREM-C-RESULTS.json. Never writes NOTES.md.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import platform
import random
import time
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path

import pulp


ROOT = Path(__file__).resolve().parent
SEED = 708_150_103
COUNTS = Counter()


@lru_cache(None)
def factor(a):
    out = []
    p = 2
    while p * p <= a:
        v = 0
        while a % p == 0:
            a //= p
            v += 1
        if v:
            out.append((p, v))
        p = 3 if p == 2 else p + 2
    if a > 1:
        out.append((a, 1))
    return tuple(out)


def valuation(a, p):
    v = 0
    while a % p == 0:
        v += 1
        a //= p
    return v


def split(a, n, M):
    """C3 verbatim, with rational comparisons cleared by positive factors."""
    s = 2 * n + 1
    qs = sorted(p**v for p, v in factor(a))
    assert M > s**3 and 1 < a <= M
    assert a * s > M and all(q * s <= M for q in qs)
    assert len(qs) >= 2
    large = [q for q in qs if q * a * s * s > M * M]
    if large:
        Q1 = large[0]
        Q2 = a // Q1
        case = "i"
        assert Q2 * M * M < a * a * s * s
        assert a * a * s * s <= M * M * s * s
        assert s * s * s < M
    else:
        Q1 = 1
        k = 0
        for q in qs:
            assert Q1 * M < a * s
            assert q * a * s * s <= M * M
            Q1 *= q
            k += 1
            if Q1 * M >= a * s:
                break
        assert Q1 * s < M
        assert k < len(qs)
        Q2 = a // Q1
        case = "ii"
    assert Q1 > 1 and Q2 > 1 and Q1 * Q2 == a
    assert Q1 * s <= M and Q2 * s <= M
    assert math.gcd(Q1, Q2) == 1
    return (Q1, Q2), case


def multiple_count(x, M, q):
    return (x + M) // q - x // q


def construct(A, x, rng=None):
    n, M = len(A), max(A)
    s = 2 * n + 1
    assert len(set(A)) == n and min(A) >= 2 and x >= 0
    assert M > s**3
    fs = {a: dict(factor(a)) for a in A}
    big = {}
    tokens = defaultdict(list)
    hosts = {}
    B1 = set()
    phase1 = []
    phase2 = []

    def choose(q, forbidden):
        candidates = [b for b in range((x // q + 1) * q, x + M + 1, q)
                      if b not in forbidden]
        assert candidates, (A, x, "no available host", q, sorted(forbidden))
        return rng.choice(candidates) if rng else candidates[0]

    for a in A:
        parts = [(p, v, p**v) for p, v in fs[a].items()]
        bs = [part for part in parts if part[2] * s > M]
        assert len(bs) <= 1
        if bs:
            p, v, q = bs[0]
            big[a] = q
            tokens[p].append((a, v))
    for p in sorted(tokens):
        used_at_p = set()
        for a, v in sorted(tokens[p], key=lambda item: (-item[1], item[0])):
            q = p**v
            D = sum(b % q == 0 for b in A)
            N = multiple_count(x, M, q)
            assert len(used_at_p) < D <= M // q <= N
            # Other primes' hosts are allowed; only same-prime hosts are barred.
            h = choose(q, used_at_p)
            assert h not in used_at_p
            used_at_p.add(h)
            hosts[a, p] = h
            B1.add(h)
            phase1.append({"a": a, "p": p, "v": v, "q": q, "h": h})
    assert len(B1) <= len(big)
    groups = []
    per_element = Counter()
    for a in A:
        rest = a // big.get(a, 1)
        if a in big:
            assert rest < s and s * s < M
        if rest == 1:
            COUNTS["empty_remainder"] += 1
            continue
        if rest * s <= M:
            pieces = (rest,)
            case = "single"
        else:
            pieces, case = split(rest, n, M)
            COUNTS[f"construction_split_{case}"] += 1
        for q in pieces:
            groups.append((a, q, case))
            per_element[a] += 1
        assert per_element[a] <= (1 if a in big else 2)
    total_slots = len(B1) + len(groups)
    assert total_slots <= len(big) + sum(per_element.values()) <= 2 * n
    if rng:
        rng.shuffle(groups)
    B = set(B1)
    for j, (a, q, case) in enumerate(groups):
        assert q * s <= M and M // q >= s
        assert multiple_count(x, M, q) >= M // q
        # Bound precedes selection: at the final step there are at most 2n-1.
        assert len(B) == len(B1) + j <= total_slots - 1 <= 2 * n - 1
        h = choose(q, B)
        B.add(h)
        for p, v in factor(q):
            assert (a, p) not in hosts
            assert v == fs[a][p]
            hosts[a, p] = h
        phase2.append({"a": a, "q": q, "h": h, "case": case})
    primes = sorted({p for a in A for p in fs[a]})
    for p in primes:
        aa = [a for a in A if p in fs[a]]
        hs = [hosts[a, p] for a in aa]
        assert len(set(hs)) == len(aa), (A, x, "noninjective", p, hs)
        assert all(hosts[a, p] % (p ** fs[a][p]) == 0 for a in aa)
        for v in range(1, 1 + max(fs[a].get(p, 0) for a in A)):
            assert sum(b % (p**v) == 0 for b in B) >= sum(a % (p**v) == 0 for a in A)
    assert len(B) <= 2 * n and all(x < b <= x + M for b in B)
    assert math.prod(B) % math.prod(A) == 0
    COUNTS["constructions"] += 1
    COUNTS["phase1_tokens"] += len(phase1)
    COUNTS["phase1_cross_prime_reuses"] += len(phase1) - len(B1)
    return {"B": sorted(B), "size": len(B), "phase1": phase1, "phase2": phase2,
            "total_slots": total_slots}


def exact_optimum(A, x):
    """Minimum cardinality via integer counts of equal capped valuation vectors.

    Each vector has capacity equal to the number of distinct interval integers
    with that vector. Capping at the demand preserves feasible cardinalities.
    This model uses total valuations, not the stronger slot criterion.
    """
    demand = Counter()
    for a in A:
        demand.update(dict(factor(a)))
    ps = sorted(demand)
    buckets = defaultdict(list)
    for b in range(x + 1, x + max(A) + 1):
        vector = tuple(min(valuation(b, p), demand[p]) for p in ps)
        if any(vector):
            buckets[vector].append(b)
    vectors = sorted(buckets)
    model = pulp.LpProblem("independent_theorem_c_optimum", pulp.LpMinimize)
    ys = [pulp.LpVariable(f"y_{i}", 0, len(buckets[v]), cat=pulp.LpInteger)
          for i, v in enumerate(vectors)]
    model += pulp.lpSum(ys)
    for i, p in enumerate(ps):
        model += pulp.lpSum(y * v[i] for y, v in zip(ys, vectors)) >= demand[p]
    status = model.solve(pulp.PULP_CBC_CMD(msg=False, timeLimit=15,
                                         gapRel=0, gapAbs=0))
    assert pulp.LpStatus[status] == "Optimal", (A, x, pulp.LpStatus[status])
    assert model.sol_status == pulp.LpSolutionOptimal, (A, x, model.sol_status)
    B = []
    for y, v in zip(ys, vectors):
        value = y.value()
        assert value is not None and abs(value - round(value)) < 1e-7
        B.extend(buckets[v][:round(value)])
    assert len(B) == len(set(B)) == round(pulp.value(model.objective))
    assert all(x < b <= x + max(A) for b in B)
    assert math.prod(B) % math.prod(A) == 0
    assert len(B) <= 2 * len(A), ("BLOCKER", A, x, B)
    COUNTS["optimal_CBC_solves"] += 1
    return {"optimum": len(B), "B": B, "status": pulp.LpStatus[status],
            "solution_status": model.sol_status, "vectors": len(vectors)}


def exhaustive_splitting():
    results = []
    for n, M in [(1, 28), (1, 81), (2, 126), (2, 375), (3, 344),
                 (3, 1029), (4, 730), (4, 2187), (5, 1332), (5, 3993),
                 (8, 4914), (8, 14739), (20, 68922)]:
        s = 2 * n + 1
        assert M > s**3
        counts = Counter()
        examples = {}
        for a in range(2, M + 1):
            qs = [p**v for p, v in factor(a)]
            if a * s <= M:
                counts["a_at_most_T"] += 1
                continue
            if any(q * s > M for q in qs):
                counts["big_component"] += 1
                continue
            pieces, case = split(a, n, M)
            counts[f"case_{case}"] += 1
            # Independent finite check: enumerate component subsets, then use
            # their products. This is not another implementation of C3's rule.
            possible = any(
                math.prod(subset) * s <= M and
                (a // math.prod(subset)) * s <= M
                for k in range(1, len(qs)) for subset in itertools.combinations(qs, k)
            )
            assert possible, ("BLOCKER", n, M, a, qs)
            examples.setdefault(case, {"a": a, "components": qs, "groups": pieces})
        results.append({"n": n, "M": M, "all_a_tested": M - 1,
                        "counts": dict(counts), "examples": examples})
    return results


def all_residue_counts():
    checks = 0
    for n, M in [(1, 28), (2, 126), (3, 344), (5, 1332)]:
        s = 2 * n + 1
        for q in range(1, M // s + 1):
            for x in range(q):
                assert multiple_count(x, M, q) >= M // q >= s
                checks += 1
    return checks


def component_examples():
    # A real near-T^0.6 obstruction without a<=M, followed by valid C3 cases.
    n, M, qs = 5, 11000, [61, 64, 67]
    a = math.prod(qs)
    assert M > 11**3 and all(q * 11 <= M for q in qs) and a > M
    assert all(u * v * 11 > M for u, v in itertools.combinations(qs, 2))
    excluded = {"n": n, "M": M, "T": M / 11, "T_power_0_6": (M / 11)**0.6,
                "a": a, "components": qs, "reason_excluded": "a > M"}
    valid = []
    for nn, MM, aa in [(5, a, a), (5, 1332, 792), (5, 1332, 1230)]:
        pieces, case = split(aa, nn, MM)
        valid.append({"n": nn, "M": MM, "a": aa, "groups": pieces, "case": case})
    return {"excluded": excluded, "valid": valid}


def directed_cases():
    # Includes mixed exponents at one prime, the equality Q=T, both C3 cases,
    # three coprime comparable components, and a shared Phase 1 host.
    return [
        ((2, 4, 8, 16, 1332), 0, "prime-powers-small"),
        ((128, 256, 512, 1024, 1536), 234567, "mixed-big-exponents"),
        ((128, 256, 512, 1024, 1536), 0, "mixed-big-exponents-zero"),
        ((128, 243, 625, 729, 1332), 128 * 243 * 625 * 729 - 1,
         "cross-prime-phase1-host"),
        ((2, 30, 72, 792, 1332), 10**12 + 91, "three-components-8-9-11"),
        ((2, 30, 72, 780, 1332), 10**12 + 121, "composite-maximum-and-remainders"),
        ((2, 3, 4, 5, 2017), 123456, "prime-maximum"),
        ((132, 264, 396, 528, 1452), 1451, "Q-equals-T"),
        ((347,), 694, "n1-prime"),
        ((128, 375), 10**9 + 7, "n2-prime-power"),
        ((77, 91, 731), 5934, "n3-three-input"),
        # Center c=49454853 has residues (17,19,230) modulo (17^2,19^2,23^2).
        # It is the only common multiple of any two demanded primes in I,
        # and I has no multiple of 23^2. Thus three numbers cannot suffice.
        ((323, 391, 437), 49454635, "three-input-requires-four"),
    ]


def main():
    started = time.monotonic()
    before = hashlib.sha256((ROOT / "NOTES.md").read_bytes()).hexdigest()
    rng = random.Random(SEED)
    report = {
        "seed": SEED, "python": platform.python_version(), "pulp": pulp.__version__,
        "cbc_path": pulp.PULP_CBC_CMD().path, "notes_sha256_before": before,
        "random_instances": [], "directed": [], "violations": [],
        "hill_climb_proposals_per_instance": 8,
    }
    try:
        report["component_examples"] = component_examples()
        report["splitting"] = exhaustive_splitting()
        report["residue_count_checks"] = all_residue_counts()
        print("exhaustive splitting and residue counts: PASS", flush=True)
        for n in range(1, 6):
            threshold = (2 * n + 1)**3
            for trial in range(12):
                M = rng.randint(threshold + 1, 3 * threshold)
                A = tuple(sorted(rng.sample(range(2, M), n - 1) + [M]))
                fs = {p: max(v for a in A for pp, v in factor(a) if pp == p)
                      for p in {pp for a in A for pp, _ in factor(a)}}
                period = math.prod(p ** (v * n + 1) for p, v in fs.items())
                x = rng.randrange(period)
                history = []
                best = None
                for step in range(9):
                    if step == 0:
                        proposal = x
                    elif step % 3 == 0:
                        proposal = rng.randrange(period)
                    elif step % 3 == 1:
                        proposal = max(0, x + rng.randint(-2 * M, 2 * M))
                    else:
                        p = rng.choice(sorted(fs))
                        q = p ** rng.randint(1, fs[p] + 1)
                        proposal = max(0, x - x % q - rng.randint(1, M))
                    exact = exact_optimum(A, proposal)
                    constructed = construct(A, proposal)
                    random_constructed = construct(A, proposal, rng)
                    assert exact["optimum"] <= constructed["size"] <= 2 * n
                    assert exact["optimum"] <= random_constructed["size"] <= 2 * n
                    history.append({"step": step, "x": proposal, "exact": exact,
                                    "construction": constructed,
                                    "random_construction": random_constructed})
                    if best is None or exact["optimum"] >= best:
                        x, best = proposal, exact["optimum"]
                chosen = next(row for row in reversed(history)
                              if row["x"] == x and row["exact"]["optimum"] == best)
                report["random_instances"].append({"n": n, "M": M, "A": A,
                    "best_x": x, "best_optimum": best, "chosen": chosen, "history": history})
            print(f"n={n}: 12 random instances, 108 exact optima: PASS", flush=True)
        for A, x, label in directed_cases():
            exact = exact_optimum(A, x)
            if label == "three-input-requires-four":
                assert exact["optimum"] == 4
            constructed = construct(A, x)
            random_constructed = construct(A, x, rng)
            if label == "Q-equals-T":
                assert any(g["q"] * (2 * len(A) + 1) == max(A)
                           for g in constructed["phase2"])
            assert exact["optimum"] <= constructed["size"] <= 2 * len(A)
            report["directed"].append({"label": label, "A": A, "x": x,
                "exact": exact, "construction": constructed,
                "random_construction": random_constructed})
        report["status"] = "PASS"
    except Exception as exc:
        report["status"] = "BLOCKER"
        report["violations"].append({"type": type(exc).__name__, "instance": repr(exc)})
        raise
    finally:
        report["counts"] = dict(COUNTS)
        report["elapsed_seconds"] = time.monotonic() - started
        report["notes_sha256_after"] = hashlib.sha256((ROOT / "NOTES.md").read_bytes()).hexdigest()
        report["notes_unchanged_during_run"] = report["notes_sha256_after"] == before
        (ROOT / "REVIEW-SOL-THEOREM-C-RESULTS.json").write_text(json.dumps(report, indent=2) + "\n")
        print(json.dumps({k: report[k] for k in ("status", "counts", "elapsed_seconds",
              "notes_unchanged_during_run", "violations")}), flush=True)


if __name__ == "__main__":
    main()
