#!/usr/bin/env python3
"""Independent aggregated-pattern ILP for a proposed search counterexample."""
import argparse
import json
from collections import Counter

import pulp


def factor(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def verify(A, x):
    demand = Counter()
    for a in A:
        demand.update(factor(a))
    ps = sorted(demand)
    patterns = Counter()
    for t in range(x + 1, x + max(A) + 1):
        f = factor(t)
        vec = tuple(f.get(p, 0) for p in ps)
        if any(vec):
            patterns[vec] += 1
    # Aggregate equal valuation vectors. Integer multiplicities make this a distinct
    # covering formulation from the element-by-element binary model.
    model = pulp.LpProblem("erdos708_aggregated_patterns", pulp.LpMinimize)
    zs = [pulp.LpVariable(f"pattern_{i}", lowBound=0, upBound=count, cat="Integer")
          for i, (vec, count) in enumerate(patterns.items())]
    vectors = list(patterns)
    model += pulp.lpSum(zs)
    for j, p in enumerate(ps):
        model += pulp.lpSum(vectors[i][j] * zs[i] for i in range(len(zs))) >= demand[p]
    status = model.solve(pulp.PULP_CBC_CMD(msg=False, threads=1))
    if pulp.LpStatus[status] != "Optimal":
        raise RuntimeError(f"CBC status: {pulp.LpStatus[status]}")
    h = int(round(pulp.value(model.objective)))
    counts = {str(vec): int(round(z.value() or 0)) for vec, z in zip(vectors, zs)
              if int(round(z.value() or 0)) > 0}
    totals = {p: sum(vectors[i][j] * int(round(z.value() or 0))
                     for i, z in enumerate(zs)) for j, p in enumerate(ps)}
    return {"A": A, "n": len(A), "M": max(A), "x": x,
            "interval": [x + 1, x + max(A)], "demand": dict(demand),
            "h_aggregated_ilp": h, "selected_pattern_counts": counts,
            "selected_exponent_totals": totals, "distinct_patterns": len(patterns),
            "eligible_elements": sum(patterns.values()), "status": pulp.LpStatus[status]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=int, required=True)
    parser.add_argument("A", nargs="+", type=int)
    args = parser.parse_args()
    print(json.dumps(verify(args.A, args.x), indent=2))
