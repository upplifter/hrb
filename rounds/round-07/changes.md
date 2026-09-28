# Round 7 · Changes

Applied by the orchestrator (all replacement text was fully specified in the findings). Lint after the batch: RESULT WARN, no FAIL. Size 17,072 words, 136,700 bytes (round growth -0.22%).

| L-ID | Anchor | Change | Reason |
|---|---|---|---|
| L-386 | §4 State 2 interruptions.intent_change | Added "or per the tax_pro_always other-booking item" to the exceptions. | Propagates D-061 ("never intent_changed") to the JSON handler (E-01). |
| L-387 | §4 State 2 tax_pro_always by-name item; unavailable item | By-name corrections and unresolved location answers are "unmatched", not no_match; the skip now reads "a find_customer no_match". | A first-party by-name no_match had to both speak and skip the unavailable line; prose (§4 Generic Request, No Matches / Inactive) scopes the skip to find_customer per D-070 (C-02). |
| L-388 | §1.5 global_outcomes.validation_failed | Added invalid_constraints and delivery_failed to the exception list. | D-048 and D-001 send the second of each to system_failure (C-03). |
| L-389 | §2 State 5 scheduler_always carried-context item | "If customerRef and customerStatus arrive" -> "If customerRef arrives". | Prose and D-071 key the skip on customerRef alone (E-05). |
| L-390 | §2 State 1 Authentication Logic > No Match Outside a New Booking | Names the Authentication failed line. | D-070 names that line; the bare pointer left two rows (E-03). |
| L-391 | §1.5 global_never message item | "a Work Center message" -> "a caller's message". | One term; matches §1.3 (C-05). |
| L-392 | Editorial trims | F-03 §5.1 Transfer results points to global_always and global_outcomes.outcome_unknown; F-06 dropped the none_nearby sentence from the scheduler_always invalid_location item (in no_acceptable_availability); F-08 §4 find_customer entry -> "Read-only; per tax_pro_always."; F-12 dropped the stale "declines both" clause (outcome definition holds it); F-13 dropped the message clause (global_always, C-3 A); F-16 same_day rung points to the lexicon office_at_capacity line; F-18 dropped "proactively" and "explicitly"; F-19 merged the get_customer_appointments Note fragments; F-20 §1.1 customerRef "do not" -> "never". | Brevity and style; every trigger and limit kept. |
