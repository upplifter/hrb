# Round 7 · Verification

Saved by the orchestrator from the verifier's reply. Lint: RESULT WARN, no FAIL; every JSON block parses; no warning is new versus lint-before.txt. No frozen text touched.

| ID | Verdict | Reason |
|---|---|---|
| L-386 | pass | The Part 4 handler carries the D-061 exception in the callback item's wording, and the other-booking item exists. |
| L-387 | fix-needed | "a find_customer no_match" dropped the first-party limit D-070 and §4 Generic Request keep; a third-party no_match must transfer. Fixed on follow-up: "a first-party find_customer no_match". |
| L-388 | pass | D-048 and D-001 send the second invalid_constraints or delivery_failed to system_failure; the tool entries agree. |
| L-389 | pass | Matches §1.1, §2 State 1 State Persistence, D-071, and Part 4 workflow step 3. |
| L-390 | pass | The Authentication failed row exists in §1.4; matches D-070. |
| L-391 | pass | Matches §1.3; no "Work Center" text remains. |
| L-392 F-03 | pass | global_always holds the failed-call rule; global_outcomes.outcome_unknown holds the idempotencyKey return. |
| L-392 F-06 | pass | no_acceptable_availability still holds the first-lookup none_nearby trigger. |
| L-392 F-08 | pass | tax_pro_always[1] holds the disclosure rule; "Read-only" matches §5.1. |
| L-392 F-12 | pass | tax_pro_options_declined and workflow steps 5-6 cover the decline; "both" was stale after D-061. |
| L-392 F-13 | pass | global_always holds the explicit message request rule (C-3 A). |
| L-392 F-16 | pass | The frozen lexicon line carries "(Only on office_at_capacity.)"; the §2 table keeps "only if". |
| L-392 F-18 | pass | Filler removal; prose and JSON still mirror. |
| L-392 F-19 | pass | Field, "never spoken", the level limit, and the status enum kept. |
| L-392 F-20 | pass | Style-only; the subject-change exception kept. |

New Medium-or-higher issues: none beyond the L-387 regression, fixed on follow-up. After the fix: 17,074 words, 136,712 bytes (round growth -0.21%).
