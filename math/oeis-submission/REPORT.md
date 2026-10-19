# OEIS submission report

Status: stopped before editing. No OEIS changes were submitted.

## Account and blocker

- An account already existed and was signed in. The page showed `dovid@sysmatic.ai` and the status `waiting to be approved`.
- This approval status blocks editing. I stopped before opening either edit form. I did not register another account, open Gmail, or try another submission route.
- The screen was `https://oeis.org/Submit.html`. Its header showed both the signed-in email and `waiting to be approved`.
- Checked and captured on 2026-10-15 at 23:08 Asia/Jerusalem (20:08 UTC).
- Password: not accessed, created, or recorded.

## A062887

- Exact text submitted: none. The edit form was not opened or submitted.
- Pending draft URL: https://oeis.org/draft/A062887 — not visited; no pending draft was created or verified.

## A185897

- Exact text submitted: none. The edit form was not opened or submitted.
- Pending draft URL: https://oeis.org/draft/A185897 — not visited; no pending draft was created or verified.

## Screenshot

- `oeis-account-approval-blocker.png` — screenshot of Edge showing the signed-in account and approval status.
- No pre-submit, confirmation, or draft screenshots exist because no edit could be submitted.

## Submission update — 2026-10-16

The earlier account-approval blocker no longer applied. In Edge, the account was signed in as Dovid Preil and both edit forms were available.

- A062887: saved the proposed comment, proof link, formula, and example indexing correction from `math/A062887/OEIS-EDIT.md`; then marked the draft ready for editor review. Draft: https://oeis.org/draft/A062887. The page showed status `proposed`.
- A185897: saved the proposed comment, proof link (preserving the existing b-file link), and formula from `math/A185897/OEIS-EDIT.md`; then marked the draft ready for editor review. Draft: https://oeis.org/draft/A185897. The page showed status `proposed`.
- Screenshots: `a062887-presubmit.png` and `a185897-presubmit.png`, captured with macOS `screencapture -x` while each completed edit form was ready to save.
- Problems: none. No other OEIS entries were changed, and neither draft was approved or published.

## Editor feedback — 2026-10-16

Michel Marcus's comments:

- "signature was not ok; please type ~~~~ verbatim"
- "you must also sign together your 2 new formulas"

Changes made in Edge:

- A185897: replaced the trailing hand-typed comment signature with `~~~~`; added a standalone `~~~~` after the two new formulas; posted the requested discussion note; submitted the draft for review.
- A062887: replaced the trailing hand-typed comment signature with `~~~~`; added a standalone `~~~~` after the two new formulas; submitted the draft for review. The `a(6)` example correction remains in place.
- Both current comment lines now show OEIS's expanded signature, `_Dovid Preil_, Oct 16 2026`. The old hand-typed lines remain only in OEIS's earlier edit history.
- OEIS saves each formula signature line as `~~~` and displays those three tildes on the draft page, even though the edit form showed four tildes before save. Re-entering four tildes produced no change. Formula signatures therefore remain unresolved.
- Final status: A185897 `proposed`; A062887 `proposed`.
- Discussion note on A185897: `Thank you. Fixed: signed with ~~~~ and added a signature for the two new formulas.`
- Final draft screenshots: `a185897-sigfix.png` and `a062887-sigfix.png`.

## Signature fix round 2 — 2026-10-16

- A185897: fixed the comment separator and placed the formula signature on the last new formula line. Submitted for review; status `proposed`.
- A062887: confirmed the comment separator and placed the formula signature on the last new formula line. Submitted for review; status `proposed`.
- Verified both latest combined drafts with `curl -s`: the changed comment and formula lines end in `- _Dovid Preil_, Oct 16 2026`; no tilde tokens remain in those lines. OEIS omitted the dash when it expanded `~~~~` in FORMULA, so the specified literal signature fallback was used. No new discussion comment was posted.
- Overwrote `a185897-sigfix.png` and `a062887-sigfix.png` using `screencapture -x`.

## Editor feedback — 2026-10-19

Michael S. Branicky's comment on the parallel A062887 draft:

> There is no reason to remove the conjecture only to restate it. Claude cannot be claimed as a co-author here (see Style Sheet).

- A185897: restored Paul D. Hanna's original conjecture as the first comment line; changed our comment to begin `The conjecture is true (see Preil link).` and kept the proof sketch and signature; removed Claude from our proof link; posted the requested discussion note and submitted the draft for review. Status: `proposed`.
- A062887: Branicky and Andrew Howroyd had already fixed that draft themselves. No A062887 edit was made in this update.
- Earlier attempts today were blocked by OEIS sign-in. After the user signed in, the A185897 edit was completed in the existing Edge session.
- Screenshot: `a185897-branicky-fix.png`.
