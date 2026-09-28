# Round 6 changes (Safe)

Format: `ledger ID | anchor | change | net words (approx.)`. Applied by the orchestrator from the reviewers' exact fixes. Lint after the batch: RESULT WARN, no FAIL.

L-373 | scheduler_always carried-context item | "A carried appointmentType, taxProRef, or officeRef also outranks the prior Tax Pro question" -> "A carried taxProRef also outranks..." so a routed_to_scheduler carrying officeRef still asks per D-050 | -4
L-374 | scheduler_always authentication-failure item; workflow.reschedule_existing[1] | JSON now transfers on first-party multiple_matches and on none_found, matching §2 State 1 and §1.4 (C-1) | +12
L-380 | Ladders table (New Client, Returning Tax Pro Unavailable, Tax Notice step 4, Same-Day); broadening.ladders new_client, returning_tax_pro_unavailable, tax_notice.rungs[3], same_day; scenario_selection item 7 | "nearest", "primary", "desired", "preferred" office -> "selected office"; "primary office" clashed with primaryOfficeId and "nearest" with §1.1 rollover | 0
L-381 | see findings-F.md | 12 editorial trims | -62
L-111 | §2 State 1 State Persistence | Restated §1.1 customerRef rule replaced with a pointer; §1.1 wins on customerRef alone (C-1) | -25
L-192 | §1.4 multiple_matches row, Path cell | Scoped to find_customer so Part 4's by-name disambiguation (D-033, D-047) does not hit the transfer line; approved line unchanged | +1

Oscillation guard: B-01 (§1.3 Leave-a-Message Ownership, edited in rounds 1, 4, 5) reclassified Human as L-376.
