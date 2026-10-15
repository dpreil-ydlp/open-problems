# open-problems

Attempts at genuinely open problems, with full proofs, independent adversarial review, and reproducible computational checks. Everything here is published so it can be checked by anyone.

Directed by Dovid Preil. Proofs written by Claude Fable 5.1. Reviews by GPT-6.1 Sol. Computation and data gathering by GPT-6 Luna. Each result states exactly who did what.

## Results

| Problem | Status | Proof | Review | Verification |
|---|---|---|---|---|
| OEIS A062887: a(n) = 0 iff 125 divides 2n+1 (conjecture of Sean A. Irvine, 2023) | **Proved**, 15 Oct 2026 | [PROOF.md](math/A062887/PROOF.md) | [REVIEW-SOL.md](math/A062887/REVIEW-SOL.md): correct with minor fixes, applied | [VERIFICATION.md](math/A062887/VERIFICATION.md): all 26 OEIS terms reproduced; witness found for every n ≤ 3000 with 125 ∤ 2n+1 using the proof's bound |
| OEIS A185897: a(n) odd iff n = 1 or 3·2^k ≤ n ≤ 4·2^k − 1 (conjecture of Paul D. Hanna, 2025) | **Proof written, independent review in progress** | [PROOF.md](math/A185897/PROOF.md) | pending | [VERIFICATION.md](math/A185897/VERIFICATION.md): all 400 OEIS terms reproduced; mod-2 identities checked to degree 2000 |

## In progress

- `candidates/`: shortlists of open problems considered, with sources and why each was or was not attempted.
- `ciphers/ssc3/`: cryptanalysis notes on the MysteryTwister "Spanish Strip Cipher part 3" challenge (142 symbols, unsolved).
- `solvers/`: classical-cipher cryptanalysis toolkit (substitution, homophonic, Vigenere family, transposition, Playfair) with tests.

## Honesty policy

A result is listed as proved only after an independent referee pass with no blocking objections and a computational check that reproduces the source data from the raw definition. Partial progress is labelled as partial. Negative results are kept.
