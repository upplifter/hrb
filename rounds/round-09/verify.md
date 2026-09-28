# Round 9 · Verify

Verified by the orchestrator against the diff, the decisions log, and lint.

| Ledger | Result | Note |
|---|---|---|
| L-425 | pass | office_never now matches D-097 and §3 Out of Scope. |
| L-426 | pass | Prose matches reschedule_existing[3]. Fixed-floor conflict stays open as L-438. |
| L-427 | pass | Matches D-095 and reschedule_existing[3]. |
| L-428 | pass | Matches D-084, the After Part 4 prose, and the routed item. |
| L-429 | pass | Matches §1.4 condition and the prose Same-Day row. |
| L-430 | pass | Precedence kept; partial_acceptance restarts no longer wipe identity. |
| L-431 | pass | Matches speak_to_tp_generic[2] and §4 Generic Request. |
| L-432 | pass | Wording equals method_descriptions.digital_drop_off; turn still 2 sentences. |
| L-433 | pass | Readback type and write-once limit kept in each entry; scheduler_always keeps the yes rule. |
| L-434 | pass | §1.2 and global_always still require the readback; dialogue 1B unchanged. |
| L-435 | pass | Trigger matches tax_pro_always matchedTpCount > 1. |
| L-436 | pass | Question, "once", and the year-gap trigger kept. |
| L-437 | pass | Matches global_always and the §5.1 category. |

All JSON blocks parse. Lint RESULT WARN, no FAIL. 0 reverted.
