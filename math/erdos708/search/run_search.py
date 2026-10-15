#!/usr/bin/env python3
"""Bounded exact-ILP adversarial search for Erdős problem 708."""
from __future__ import annotations

import itertools
import json
import math
import os
import random
import subprocess
import sys
import time
from pathlib import Path

import pulp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "search.jsonl"
SEED = 70820261015
MAX_SOLVES = 200
DEADLINE = float(os.environ.get("ERDOS708_DEADLINE", time.time() + 75 * 60))
RNG = random.Random(SEED)
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19)


def factor(n: int) -> dict[int, int]:
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


def primes_of(A):
    return sorted(set().union(*(factor(a).keys() for a in A)))


def demand(A):
    ans = {}
    for a in A:
        for p, e in factor(a).items():
            ans[p] = ans.get(p, 0) + e
    return ans


def evaluator(A, x, detail=False):
    M = max(A)
    req = demand(A)
    eligible = []
    vals = {p: [] for p in req}
    for t in range(x + 1, x + M + 1):
        row = {p: 0 for p in req}
        for p in req:
            z = t
            while z % p == 0:
                row[p] += 1
                z //= p
        if any(row.values()):
            eligible.append(t)
            for p in req:
                vals[p].append(row[p])
    prob = pulp.LpProblem("erdos708", pulp.LpMinimize)
    y = [pulp.LpVariable(f"y_{i}", cat="Binary") for i in range(len(eligible))]
    prob += pulp.lpSum(y)
    for j, p in enumerate(req):
        prob += pulp.lpSum(vals[p][i] * y[i] for i in range(len(y))) >= req[p]
    solver = pulp.PULP_CBC_CMD(msg=False, threads=1)
    status = prob.solve(solver)
    if pulp.LpStatus[status] != "Optimal":
        raise RuntimeError(f"CBC status {pulp.LpStatus[status]} for A={A}, x={x}")
    h = int(round(pulp.value(prob.objective)))
    if detail:
        chosen = [eligible[i] for i, v in enumerate(y) if (v.value() or 0) > .5]
        return h, chosen, {p: sum(factor(t).get(p, 0) for t in chosen) for p in req}
    return h


def residue_moduli(A):
    M = max(A)
    result = []
    for p in primes_of(A):
        power = p
        while power * p <= M:
            power *= p
        result.append((p, power * p))
    return result


def crt_residues(residues, moduli):
    # Pairwise-coprime prime-power CRT.
    N = math.prod(moduli)
    return sum((r * (N // q) * pow(N // q, -1, q)) for r, q in zip(residues, moduli)) % N


def hub_x(A, mode=0):
    """CRT hub at the center of I, exact max exponents on selected primes."""
    ps = primes_of(A)
    mods = dict(residue_moduli(A))
    reqmax = {p: max(factor(a).get(p, 0) for a in A) for p in ps}
    # Rotate among full lcm hubs, single-prime omissions, and selected subsets.
    if mode == 0:
        selected = set(ps)
    elif mode <= len(ps):
        selected = {ps[(mode - 1) % len(ps)]}
    else:
        selected = {p for i, p in enumerate(ps) if (mode >> (i % 8)) & 1}
        if not selected:
            selected = set(ps)
    residues = []
    qs = []
    for p in ps:
        q = mods[p]
        e = reqmax[p] if p in selected else 0
        # p^e has exact valuation e modulo p^(e+1); lift it to the full coordinate modulus.
        r = pow(p, e, q)
        residues.append(r)
        qs.append(q)
    c0 = crt_residues(residues, qs)
    M = max(A)
    m = M // 2
    N = math.prod(qs)
    c = c0 if c0 > m else c0 + ((m - c0) // N + 1) * N
    return c - m


def coord_key(x, mods):
    return tuple((x % q) for _, q in mods)


def key_to_x(key, mods):
    return crt_residues(key, [q for _, q in mods])


def search_x(A):
    mods = residue_moduli(A)
    seen = {}
    solves = 0

    def score(x):
        nonlocal solves
        key = coord_key(x, mods)
        if key not in seen:
            seen[key] = evaluator(A, key_to_x(key, mods))
            solves += 1
        return seen[key], key

    best_h, best_key = -1, None
    # Several structurally distinct CRT hubs; use at most 20 initial solves.
    hub_count = min(20, MAX_SOLVES)
    for mode in range(hub_count):
        x = hub_x(A, mode)
        h, key = score(x)
        if h > best_h:
            best_h, best_key = h, key

    # Coordinate hill-climb. Each proposal changes exactly one prime-power residue.
    restarts = 0
    attempts = 0
    while solves < MAX_SOLVES and time.time() < DEADLINE and attempts < MAX_SOLVES * 20:
        current = best_key if restarts == 0 else tuple(RNG.randrange(q) for _, q in mods)
        cur_h, current = score(key_to_x(current, mods))
        passes = 0
        while solves < MAX_SOLVES and time.time() < DEADLINE and passes < max(1, 2 * len(mods)):
            improved = False
            order = list(range(len(mods)))
            RNG.shuffle(order)
            for j in order:
                if solves >= MAX_SOLVES or time.time() >= DEADLINE:
                    break
                q = mods[j][1]
                # Deterministic broad jump plus a random residue for this coordinate.
                candidates = {RNG.randrange(q), (current[j] + q // 2 + 1) % q}
                for r in candidates:
                    attempts += 1
                    proposal = list(current)
                    proposal[j] = r
                    h, k = score(key_to_x(proposal, mods))
                    if h >= cur_h and (h > cur_h or RNG.random() < .08):
                        current, cur_h, improved = k, h, True
                    if h > best_h:
                        best_h, best_key = h, k
                    if attempts >= MAX_SOLVES * 20:
                        break
            passes += 1
            if not improved:
                break
        restarts += 1
    x = key_to_x(best_key, mods)
    return x, best_h, solves


def brute_force_no_solution(A, x, limit):
    """Independent subset enumeration; return counts checked through limit."""
    req = demand(A)
    eligible, rows = [], []
    for t in range(x + 1, x + max(A) + 1):
        f = factor(t)
        row = tuple(f.get(p, 0) for p in req)
        if any(row):
            eligible.append(t)
            rows.append(row)
    checked = 0
    for k in range(limit + 1):
        for indices in itertools.combinations(range(len(eligible)), k):
            checked += 1
            sums = [sum(rows[j][i] for j in indices) for i in range(len(req))]
            if all(sums[i] >= req[p] for i, p in enumerate(req)):
                return False, k, checked, eligible
    return True, None, checked, eligible


def _candidate_stream():
    seen = set()

    def add(family, A):
        A = tuple(sorted(set(A)))
        if len(A) < 3 or len(A) > 10 or max(A) > 400 or min(A) < 2:
            return
        if A in seen:
            return
        seen.add(A)
        yield family, A

    # Pairwise products (square-included and square-excluded), including loose prime gaps.
    ps = (2, 3, 5, 7, 11, 13, 17, 19)
    for ell in (3, 4):
        for Q in itertools.combinations(ps, ell):
            pairs = list(itertools.combinations(Q, 2))
            for squares in (True, False):
                A = [a * b for a, b in pairs]
                if squares:
                    A += [p * p for p in Q]
                if max(A) <= 400:
                    yield from add(f"pairwise_l{ell}_{'sq' if squares else 'nosq'}", A)

    # Triple products of four or five primes.
    for k in (4, 5):
        for Q in itertools.combinations(ps, k):
            A = [math.prod(T) for T in itertools.combinations(Q, 3)]
            if max(A) <= 400:
                yield from add(f"triples_{k}p", A)

    # Mixed 2- and 3-prime products from compact prime sets; sampled combinations bound count.
    for k in (4, 5, 6):
        for Q in itertools.combinations((2, 3, 5, 7, 11, 13), k):
            allprod = [math.prod(T) for size in (2, 3) for T in itertools.combinations(Q, size)]
            if len(allprod) <= 10 and max(allprod) <= 400:
                yield from add(f"mixed_{k}p", allprod)
            elif max(allprod) <= 400:
                # Stable selected n-subsets of the mixed pool.
                n = 8
                for start in (0, max(0, len(allprod)//2 - n//2), len(allprod)-n):
                    yield from add(f"mixed_{k}p", allprod[start:start+n])

    # Choose M <= 400 among divisors of L; use divisors in (M/2,M] plus up to
    # four smaller divisors, so the 720 and 840 examples remain within the size cap.
    for L in (360, 720, 840):
        divisors = [d for d in range(2, L + 1) if L % d == 0]
        for M in divisors:
            if M > 400 or M < 60:
                continue
            ds = [d for d in divisors if d <= M]
            upper = [d for d in ds if d > M // 2]
            smaller = [d for d in ds if d <= M // 2]
            min_extra = max(0, 3 - len(upper))
            max_extra = min(4, 8 - len(upper), len(smaller))
            for k in range(min_extra, max_extra + 1):
                for extra in itertools.combinations(smaller, k):
                    yield from add(f"divisors_{L}_M{M}", upper + list(extra))

    # Small prime-power and mixed-power sets.
    power_sets = [
        (4, 8, 9, 6, 12, 18), (4, 8, 9, 6, 12, 18, 36),
        (8, 16, 9, 6, 12, 24, 36, 72), (9, 27, 25, 15, 45, 75),
        (4, 8, 16, 9, 27, 6, 12, 18), (25, 125, 49, 35, 175),
    ]
    for i, A in enumerate(power_sets):
        yield from add(f"prime_powers_{i+1}", A)

    # Random upper-half subsets, 30 per requested M.
    for M in (60, 120, 240):
        for j in range(30):
            A = tuple(sorted(RNG.sample(range(max(2, M//2), M + 1), RNG.choice((3, 4, 5, 6, 7, 8)))))
            yield from add(f"random_M{M}_sample{j+1}", A)

    # Exhaustive n=4 subsets of [2,30]; one global pass can be cut at the deadline.
    for A in itertools.combinations(range(2, 31), 4):
        yield from add("exhaustive_[2,30]_n4", A)


def candidates():
    """Round-robin families so a fixed wall-clock budget samples every type."""
    groups = {}
    for family, A in _candidate_stream():
        if family.startswith("random_"):
            group = family.rsplit("_sample", 1)[0]
        elif family.startswith("exhaustive_"):
            group = "exhaustive_n4"
        elif family.startswith("prime_powers_"):
            group = "prime_powers"
        else:
            group = family
        groups.setdefault(group, []).append((family, A))
    names = list(groups)
    for i in range(max(map(len, groups.values()))):
        for name in names:
            if i < len(groups[name]):
                yield groups[name][i]


def write_record(record):
    with OUT.open("a") as f:
        f.write(json.dumps(record, separators=(",", ":")) + "\n")
        f.flush()
        os.fsync(f.fileno())


def main():
    # Reuse existing completed records on restart, preserving the fixed random seed's work.
    done = set()
    if OUT.exists():
        for line in OUT.read_text().splitlines():
            try:
                r = json.loads(line)
                done.add(tuple(r["A"]))
            except Exception:
                continue
    validations = []
    h, chosen, totals = evaluator((77, 91, 143), 5934, True)
    assert h == 4, (h, chosen, totals)
    validations.append({"A": [77, 91, 143], "x": 5934, "h": h, "chosen": chosen, "totals": totals})
    lower = [((11,13),2107021,3), ((17,19,23),339391420595,7),
             ((37,41,43,47),7854246017435040183,13)]
    for P, x, expected in lower:
        A = tuple(p*q for i,p in enumerate(P) for q in P[i:])
        got = evaluator(A, x)
        assert got == expected, (A, x, got, expected)
        validations.append({"primes": list(P), "A": list(A), "x": x, "h": got, "expected": expected})
    print(json.dumps({"event":"validation_pass", "checks":validations}), flush=True)

    total_started = time.monotonic()
    completed_this_run = 0
    for family, A in candidates():
        if tuple(A) in done:
            continue
        if time.time() >= DEADLINE:
            break
        started = time.monotonic()
        x, h, solves = search_x(A)
        rec = {"family": family, "A": list(A), "n":len(A), "M":max(A), "x":x,
               "h":h,"two_n":2*len(A),"ratio":h/len(A),
               "gap":h-2*len(A),"adjusted":h-(2*len(A)-2*math.sqrt(2*len(A))),
               "solves":solves,"seconds":round(time.monotonic()-started,4)}
        write_record(rec)
        done.add(tuple(A))
        completed_this_run += 1
        if completed_this_run % 25 == 0:
            print(json.dumps({"event":"progress","records":len(done),"family":family,
                              "A":A,"h":h,"ratio":rec["ratio"],"elapsed_s":round(time.monotonic()-total_started,1)}), flush=True)
        if h > 2*len(A):
            check = {"method":"brute force over subsets of I up to 2n"}
            if max(A) <= 60:
                confirmed, found_size, checked, eligible = brute_force_no_solution(A, x, 2*len(A))
                check.update({"confirmed_no_subset_at_most_2n":confirmed,"subsets_checked":checked,
                              "eligible_count":len(eligible),"found_size":found_size})
                if not confirmed:
                    raise AssertionError("Independent brute force contradicts ILP optimum")
            else:
                check["method"] = "second CBC covering formulation required; candidate not verified"
            rec["independent_check"] = check
            print(json.dumps({"event":"counterexample_candidate",**rec}), flush=True)
            break
    print(json.dumps({"event":"finished","records":len(done),"this_run":completed_this_run,
                      "elapsed_s":round(time.monotonic()-total_started,1),
                      "deadline_reached":time.time()>=DEADLINE}), flush=True)


if __name__ == "__main__":
    main()
