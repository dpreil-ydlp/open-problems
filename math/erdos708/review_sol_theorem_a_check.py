#!/usr/bin/env python3
"""Reproducible independent tests for Section 3A; does not edit NOTES.md."""

from __future__ import annotations

import hashlib
import json
import math
import random
import time
from collections import Counter, defaultdict
from pathlib import Path

import pulp

from verify_lower import valuation


ROOT = Path(__file__).resolve().parent
SEED = 708150026


def factor(n: int) -> dict[int, int]:
    result = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


FACTORS = {a: factor(a) for a in range(2, 151)}


def exact_optimum(A: tuple[int, ...], x: int) -> dict:
    M = max(A)
    demand = Counter()
    for a in A:
        demand.update(FACTORS[a])
    primes = sorted(demand)
    rows = [(b, tuple(valuation(b, p) for p in primes))
            for b in range(x + 1, x + M + 1)]
    rows = [(b, vs) for b, vs in rows if any(vs)]
    # Equal valuation vectors are interchangeable. An integer count replaces
    # their binary variables, preserving the exact feasible cardinalities.
    buckets = defaultdict(list)
    for b, vs in rows:
        buckets[vs].append(b)
    vectors = sorted(buckets)
    problem = pulp.LpProblem("independent_upper_review", pulp.LpMinimize)
    z = [pulp.LpVariable(f"z_{i}", lowBound=0, upBound=len(buckets[vs]),
                        cat=pulp.LpInteger) for i, vs in enumerate(vectors)]
    problem += pulp.lpSum(z)
    for j, p in enumerate(primes):
        problem += pulp.lpSum(var * vs[j] for var, vs in zip(z, vectors)) >= demand[p]
    status = problem.solve(pulp.PULP_CBC_CMD(msg=False, timeLimit=10))
    if pulp.LpStatus[status] != "Optimal" or problem.sol_status != pulp.LpSolutionOptimal:
        raise AssertionError((A, x, "nonoptimal solver termination", pulp.LpStatus[status],
                              problem.sol_status))
    B = [b for var, vs in zip(z, vectors) for b in buckets[vs][:round(var.value())]]
    assert len(B) == round(pulp.value(problem.objective))
    assert len(B) == len(set(B))
    assert all(x < b <= x + M for b in B)
    assert math.prod(B) % math.prod(A) == 0
    return {"optimum": len(B), "B": B, "status": pulp.LpStatus[status]}


def check_bounds(A: tuple[int, ...], x: int, optimum: int) -> dict:
    M = max(A)
    I = set(range(x + 1, x + M + 1))
    groups = defaultdict(list)
    for a in A:
        hub = (x // a + 1) * a
        assert hub in I
        groups[hub].append(a)
    C = set(groups)
    H = len(C)
    primes = sorted({p for a in A for p in FACTORS[a]})
    theorem_b = sum(1 + sum(len(FACTORS[a]) for a in group)
                    - len({p for a in group for p in FACTORS[a]})
                    for group in groups.values())
    B = set(C)
    fill_data = {}
    nonmonotone = []
    for p in primes:
        max_v = max(FACTORS[a].get(p, 0) for a in A)
        deficit = {}
        available = {}
        for v in range(1, max_v + 2):
            q = p ** v
            D = sum(a % q == 0 for a in A)
            K = sum(c % q == 0 for c in C)
            N = sum(b % q == 0 for b in I)
            assert D <= M // q <= N
            deficit[v] = max(D - K, 0)
            available[v] = N - K
            G = sum(any(a % q == 0 for a in group) for group in groups.values())
            assert G <= K
        if any(deficit[v] < deficit[v + 1] for v in range(1, max_v + 1)):
            nonmonotone.append(p)
        F = set()
        for v in range(max_v + 1, 0, -1):
            q = p ** v
            envelope = max(deficit[w] for w in deficit if w >= v)
            assert available[v] >= envelope
            need = max(0, deficit[v] - sum(b % q == 0 for b in F))
            candidates = sorted(b for b in I - C - F if b % q == 0)
            assert len(candidates) >= need
            F.update(candidates[:need])
            assert len(F) == envelope
        f = max(deficit.values())
        assert len(F) == f
        assert not (F & C)
        assert all(sum(b % (p ** v) == 0 for b in F) >= d
                   for v, d in deficit.items())
        lemma_4_rhs = sum(max(sum(p in FACTORS[a] for a in group) - 1, 0)
                         for group in groups.values())
        assert f <= lemma_4_rhs
        fill_data[p] = {"f": f, "F": sorted(F), "deficits": deficit}
        B.update(F)
    slot_bound = H + sum(entry["f"] for entry in fill_data.values())
    assert math.prod(B) % math.prod(A) == 0
    for p in primes:
        for v in range(1, 1 + max(FACTORS[a].get(p, 0) for a in A)):
            assert sum(b % (p ** v) == 0 for b in B) >= sum(a % (p ** v) == 0 for a in A)
    assert optimum <= len(B) <= slot_bound <= theorem_b
    theorem_a = 2 * len(A) - H
    if all(len(FACTORS[a]) <= 2 for a in A):
        assert theorem_b <= theorem_a <= 2 * len(A) - 1
    return {"H": H, "groups": dict(groups), "theorem_B": theorem_b,
            "theorem_A": theorem_a, "slot_bound": slot_bound,
            "constructed_B": sorted(B), "fill": fill_data,
            "nonmonotone_primes": nonmonotone}


def main() -> None:
    start = time.perf_counter()
    rng = random.Random(SEED)
    runs = []
    all_evaluations = []
    seen_A = set()
    for i in range(300):
        n = i % 7 + 1
        while True:
            M = rng.randint(max(2, n + 1), 150)
            if len(FACTORS[M]) > 2:
                continue
            pool = [a for a in range(2, M) if len(FACTORS[a]) <= 2]
            if len(pool) < n - 1:
                continue
            A = tuple(sorted(rng.sample(pool, n - 1) + [M]))
            if A not in seen_A:
                seen_A.add(A)
                break
        cache = {}

        def evaluate(x: int) -> dict:
            if x not in cache:
                solved = exact_optimum(A, x)
                bounds = check_bounds(A, x, solved["optimum"])
                cache[x] = {"x": x, **solved, **bounds}
                all_evaluations.append({"case": i, "A": A, **cache[x]})
            return cache[x]

        x = rng.randint(0, 1_000_000)
        initial = evaluate(x)["optimum"]
        # Three greedy local rounds. Both unit and random offsets are checked.
        # These are local searches, not a claim of a global maximum over x.
        for _ in range(3):
            step = rng.randint(2, 2 * M)
            candidates = {x, max(0, x - 1), x + 1, max(0, x - step), x + step}
            scored = [evaluate(y) for y in sorted(candidates)]
            best_score = max(row["optimum"] for row in scored)
            best = [row for row in scored if row["optimum"] == best_score]
            improving = [row for row in best if row["x"] != x]
            x = rng.choice(improving or best)["x"]
        result = evaluate(x)
        assert result["optimum"] == max(row["optimum"] for row in cache.values())
        runs.append({"case": i, "A": A, "n": n, "M": M,
                     "initial_optimum": initial, "evaluated_positions": len(cache), **result})
        if (i + 1) % 25 == 0:
            print(f"Completed {i+1}/300 cases; {len(all_evaluations)} exact ILPs", flush=True)

    directed = []
    for A, x, label in [((4, 5, 12), 8, "nonmonotone_deficit"),
                         ((2,), 1, "n1_prime"),
                         ((64,), 111, "n1_prime_power"),
                         ((6,), 10, "n1_two_primes"),
                         ((2, 4, 8, 16, 32, 64, 128), 127, "only_prime_powers"),
                         ((6, 10, 15, 30, 42, 70, 105), 100, "general_omega3")]:
        solved = exact_optimum(A, x)
        directed.append({"label": label, "A": A, "x": x, **solved,
                         **check_bounds(A, x, solved["optimum"])})

    summary = {"seed": SEED, "random_cases": len(runs),
               "n_counts": dict(Counter(row["n"] for row in runs)),
               "M_range": [min(row["M"] for row in runs), max(row["M"] for row in runs)],
               "total_random_position_evaluations": len(all_evaluations),
               "positions_improved": sum(row["optimum"] > row["initial_optimum"] for row in runs),
               "optimum_range": [min(row["optimum"] for row in runs), max(row["optimum"] for row in runs)],
               "min_theorem_A_slack": min(row["theorem_A"] - row["optimum"] for row in runs),
               "min_theorem_B_slack": min(row["theorem_B"] - row["optimum"] for row in runs),
               "min_2n_minus_1_slack": min(2*row["n"]-1-row["optimum"] for row in runs),
               "nonmonotone_random_positions": sum(bool(row["nonmonotone_primes"]) for row in all_evaluations),
               "violations": [], "seconds": time.perf_counter() - start}
    result = {"summary": summary, "pulp_version": pulp.__version__,
              "cbc_path": pulp.PULP_CBC_CMD().path,
              "notes_sha256": hashlib.sha256((ROOT / "NOTES.md").read_bytes()).hexdigest(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "random_cases": runs, "random_position_evaluations": all_evaluations,
              "directed_cases": directed}
    output = ROOT / "REVIEW-SOL-THEOREM-A-RESULTS.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == "__main__":
    main()
