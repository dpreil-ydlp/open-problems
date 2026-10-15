# Upper-bound research task

- Outcome: research report completed. No global linear bound or counterexample is claimed. Proved a Hall obstruction to the fixed largest-prime split, a 2n bound for M >= (2n)^3, and failure of the complement condition without interval excess.
- Owner: current Sol research sub-agent; director owns final acceptance. No child tasks created.
- Authority: user request of 2026-10-15, up to 90 minutes.
- Start: 2026-10-15 20:18:56 UTC. Deadline: 21:48:56 UTC.
- Scope: SOL-UPPER-ATTEMPT.md, this record, and isolated upper-attempt computational evidence. Preserve the source notes, lower-bound verifier, concurrent search/, and unrelated edits.
- Proof required: complete mathematical arguments; exact arithmetic for explicit examples; no solver-only claim of a new bound.
- Completion: 2026-10-15 20:48 UTC, approximately 30 minutes elapsed, within the 90-minute limit.
- Artifacts: SOL-UPPER-ATTEMPT.md; upper_attempt_verify.py; UPPER-ATTEMPT-EVIDENCE.json.
- Proof: complete arguments in the report; the standard-library checker passed in 19.03 seconds, one process, nice priority 10. It verifies the finite Hall deficit of 233721, 288 constructive sparse-range cases, exact CRT and induction certificates, and the component-packing obstruction. Exploratory matching checked 3120 small graphs; that sample did not predict the proved large Hall obstruction.
- File acceptance checks: the report has the required exact final line; math delimiters are balanced; source notes and the lower-bound verifier have no tracked diff. Unrelated edits were preserved.
- Work remaining: director review and acceptance. The global upper bound and the adaptive/exchange arguments remain mathematically unresolved, as stated in the report. No additional action is queued by this worker.
- Next action: director reads the report and chooses whether to pursue a further research task.
- Unresolved decisions: none requiring human input.
- Acceptance: pending director review; no independent review or accepted milestone is claimed. No child tasks, schedules, services, or owned threads were created, so no delegate cleanup is due.
