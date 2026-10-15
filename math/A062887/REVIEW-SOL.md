# Independent mathematical review of A062887

VERDICT: CORRECT WITH MINOR FIXES

Reviewer: GPT-6.1 Sol, high effort, acting as the independent review sub-agent.
Date: 15 October 2026. Budget: 25 minutes.
Scope: the submitted `PROOF.md`, including its remarks and its reading of OEIS.
Reviewed file SHA-256: `88b083e83baea314fde0700d6dfa22759588106b5ff27e36556c8787d2d1c875`.

The main theorem is valid. I found no blocker. Lemma 1 contains a wrong local digit relation, but its correction is immediate and preserves the argument. Two remarks need qualifications. This report does not change the proof.

## OEIS text, fetched independently

I fetched both [the sequence entry](https://oeis.org/A062887) and [its internal form](https://oeis.org/A062887/internal) on 15 October 2026. The definition below is verbatim, with HTML entities decoded:

> Smallest multiple of 2n+1 with the property that its digits are odd and each digit is two less (mod 10) than the previous digit, or 0 if no such number exists.

The conjecture and attribution, verbatim from the displayed comment, are:

> Conjecture: The only numbers n for which a(n)=0 are those for which 2*n+1 is divisible by 125. - Sean A. Irvine, Apr 14 2023

The OEIS offset is `0,2`; thus the relevant domain is integers n >= 0. The entry still calls the assertion a conjecture. Its approved status is approval of the sequence entry, not certification of this theorem.

## Numbered objections

1. **MINOR — Lemma 1 applies the recurrence in the wrong direction to 375** (`PROOF.md`, line 29). It says that the hundreds digit 3 and tens digit 7 require `7 ≡ 3 + 2 (mod 10)`. Equation (1) instead requires `3 ≡ 7 + 2 (mod 10)`, or, reading left to right, `7 ≡ 3 - 2 (mod 10)`. Both correct relations are false for 375. Replacing the displayed relation repairs the argument immediately. The wrong relation is not a blocker because the same ending fails the actual rule.

2. **MINOR — Remark 1 needs the condition 125 does not divide m** (line 69). Taken without that condition, the statement that `X_L` is a witness is false. For m = 125, write a = 3 and m' = 1. The order of 10 modulo 99999 is 5, so the stated formula gives L = 25. But `X_25 ≡ 975 ≡ 100 (mod 125)`, so it is not a multiple of 125. The theorem already supplies the immediate qualification: first return 0 if 125 divides m; otherwise use the length bound with a <= 2. For the latter branch, enumerate all five candidates at each length, in increasing numerical order, through that bound to obtain the smallest one.

3. **MINOR — Remark 3 overstates which properties of the block are sufficient** (line 71). Nonzero and divisible by 25 are not sufficient by themselves. For example, 11175 has both properties and all its digits are odd, but even one copy fails the digit rule. The argument also uses the fact that a block, including the join between consecutive copies, gives an admissible number. The proposed extension to even s is valid with the appropriate periodic block and a fresh ending check. It cannot retain divisibility by 25 as a uniform block hypothesis: for s = 0, the units-5 block is 5; for s = 4, 6, 8, the length-five blocks are 17395, 93715, 79135. Each of these four cases has exactly one factor of 5, whereas 31975 has exactly two. State those structural requirements or narrow the remark. This does not affect the theorem.

4. **MINOR — The parenthetical after Lemma 3 promises a smaller witness for an arbitrary multiple of the order** (line 45). The existence claim is correct, but the size claim needs to specify the order itself. For example, k = 2*phi(99999*m) is a multiple of the order and gives twice the length of the stated Euler witness. This is only a wording issue.

There are no BLOCKER objections and thus no unfillable inference or counterexample to the main theorem.

## Checks of the requested steps

- **Definition and direction.** Decimal digits are read from left to right. The proof correctly converts a decrease of 2 in that direction to `c_(i+1) ≡ c_i + 2 (mod 10)` when indices increase from the units place. All digits must be odd, not only the first one. Starting with an odd units digit enforces that condition because adding 2 modulo 10 preserves oddness. Digits lie in {0,...,9}, so the residue specifies a unique digit. The leading digit is odd and cannot be 0. Zero has an even digit and cannot qualify. The OEIS title does not explicitly say “positive,” but its nonnegative sequence, its terms, and its positive-number enumeration specify positive multiples; allowing negative numbers would leave no smallest qualifying multiple. The proof uses the intended convention.

- **Length and units digit.** For every L >= 1 and each of the five odd units digits, the recurrence determines every digit. All resulting leading digits are nonzero. Different units digits give different numbers. Thus there are exactly five candidates of each length, with no missing choices and no leading-zero exception.

- **Lemma 1.** Since 125 divides 1000, the residue list is exhaustive. Positivity gives N >= 125, so the last three positions exist. Exactly one listed ending has three odd digits: 375. It fails the rule, as explained in objection 1. Equivalently, all admissible three-digit endings are 197, 319, 531, 753, 975, and none is divisible by 125.

- **Lemma 2.** The place values give `5 + 70 + 900 + 1000 + 30000 = 31975`. Shifting this block by multiples of five places gives the stated geometric sum without carries or overlap. I checked k = 1 and k = 2 by hand and with exact integer arithmetic; the values are below.

- **Lemma 3.** For positive m coprime to 10, `gcd(10,99999*m) = 1`. The factorization `99999 = 3^2 * 41 * 271` is correct. Euler gives `10^k ≡ 1 (mod 99999*m)` for k = phi(99999*m); raising to the fifth power gives the required exponent 5k. The quotient is an integer, either by the geometric sum or by the explicit identity `10^(5k)-1 = 99999*m*t`. Dividing that integer equality by 99999 gives `m*t`. This is valid even if m shares factors with 99999; no unjustified cancellation of a congruence occurs. Taking k to be the multiplicative order itself also works. Arbitrary multiples of that order work as well, although they need not give a smaller witness than the Euler choice.

- **Factorization, 25, and the final gcd.** For positive odd m with 125 not dividing m, a = v_5(m) is 0, 1, or 2, and m' = m/5^a is coprime to 10. Since k >= 1, the selected length 5k is at least 5 and therefore at least 2. The last two digits are 75, so 25 divides the witness. Also `gcd(5^a,m') = 1`, including a = 0 or m' = 1. Divisibility by these coprime factors implies divisibility by their product. No assumption about `gcd(25,99999*m')` is needed.

- **Corollary.** The witness makes the set of positive admissible multiples nonempty. The well-ordering principle then gives a least element; a finite search or an explicit formula for that element is not needed for existence. If 125 divides m, Lemma 1 makes the set empty. Finally, 2n+1 ≡ 0 modulo 125 is equivalent to n ≡ 62 modulo 125. The proof establishes both directions of the claimed equivalence.

- **Remarks.** Remark 1 works with objection 2's qualification. Remark 2 is correct: distinct positive multiples of the order give strictly increasing lengths and hence distinct positive witnesses, all with units digit 5. For Remark 3, reduction of s modulo 10 leaves s = 0, 2, 4, 6, 8. The units-5 periodic blocks listed in objection 3 give the existence argument after removing factors of 5. For s = 0, 4, 6, 8, no admissible number can be divisible by 25: a candidate would need to end in 75, which requires s = 2 in the right-indexed recurrence. Their exceptional power is therefore 25. For s = 2, it is 125 as proved here. Thus the generalization is elementary but needs its block and ending conditions stated.

## Independent recomputation

These checks used fresh Python code in the terminal, not the author's `verify.py` or its results.

- **a(5) = 319 = 11 * 29.** I scanned positive multiples of 11 and tested their actual decimal digits. The admissible positive integers below 319 are `1, 3, 5, 7, 9, 19, 31, 53, 75, 97, 197`; none is a multiple of 11. The digits 3,1,9 satisfy the required decrease modulo 10.
- **X_5 = 31975.** For k = 1, `(10^5-1)/99999 = 1`, so the closed form gives 31975.
- **X_10 = 3197531975.** For k = 2, `(10^10-1)/99999 = 100001`; multiplying 31975 by 100001 gives `3197500000 + 31975 = 3197531975`, exactly two consecutive copies of the block.
- **Endings divisible by 125, written in three places:** `000, 125, 250, 375, 500, 625, 750, 875`. If “three-digit” excludes the padded zero ending, omit 000. Only 375 has all three digits odd; no ending in the list is admissible.
- **OEIS data:** I fetched [the b-file](https://oeis.org/A062887/b062887.txt) and independently generated candidates from their leading digit, appending digits that decrease by 2 modulo 10. Enumerating lengths and leading digits in increasing order reproduced all 26 terms a(0) through a(25). The longest needed length was 18. This supports the reading of the definition; the mathematical argument supplies the unrestricted existence result.

Source caution: the OEIS example has an indexing error. It assigns 975 to a(7), while its data and independent computation give a(6) = 975 and a(7) = 75. In particular, 975 = 13 * 75 belongs to modulus 13, not the modulus 15 for n = 7. This is an error in the source example, not in this proof's a(5) check.

## Prior work and mathematical significance

The exact assertion remains labelled a conjecture in the live [A062887 entry](https://oeis.org/A062887). I found no earlier proof of this exact statement in the searches below. That is a bounded search result, not a claim of novelty or a complete literature survey.

I searched the web for `"A062887"`, `site:mathoverflow.net "A062887"`, `site:arxiv.org "A062887"`, `"digits" "125" "two less"`, `site:mathoverflow.net "digits" "two less"`, `site:mathoverflow.net "31975" multiple`, `site:arxiv.org "odd digits" "125"`, and `"A062887" proof conjecture 125 -site:oeis.org`. I also searched with MathOverflow and arXiv domain filters. The results contained OEIS, mirrors, and unrelated matches, but no exact proof.

For direct checks, the [MathOverflow search API](https://api.stackexchange.com/2.3/search/advanced?site=mathoverflow&q=A062887&filter=default) returned an empty question list with `has_more=false`. The [arXiv API query](https://export.arxiv.org/api/query?search_query=all%3AA062887&start=0&max_results=10) returned `totalResults=0`. These checks do not search every answer, PDF, or unindexed document. Firecrawl returned `USER_NOT_LOGGED_IN` (“is not connected”); the subsequent web searches and direct API requests succeeded.

The mathematical method is standard and elementary. Lemma 3 is the usual repunit divisibility argument in base 100000. [André Nicolas's 2013 answer on repunit divisibility](https://math.stackexchange.com/questions/472404/repunit-divisibility) gives the same Euler argument in base 10, enlarging the modulus by 9 before division. Here 99999 replaces 9. Once the periodic block and the 5-adic ending obstruction are identified, the theorem is an immediate application of that argument. I would describe this as an elementary resolution of a recorded OEIS conjecture, with novelty unestablished, rather than a new general number-theoretic method.

The related [A062886 entry](https://oeis.org/A062886), for digits increasing by 2 from left to right, already records the analogous 25-divisibility pattern through n = 500 and a program that handles that obstruction. It is relevant prior context, but it does not prove the exact A062887 assertion.

## Task record and limits

- Outcome: independent review complete; no blocker; four minor objections.
- Owner: this review sub-agent owns this report. The proof author owns any proof edits; the parent coordinator owns acceptance and integration.
- Proof: the step checks, exact recomputations, OEIS comparison, file hash, and bounded source search above.
- Remaining work: the author can correct the relation in Lemma 1 and qualify Remarks 1 and 3. The report does not certify publication priority or the author's separate verification artifacts.
- Next action: return this report to the coordinating task for disposition of the minor objections.
- Unresolved decisions: none needed for this review. No delegated tasks or schedules were created.
