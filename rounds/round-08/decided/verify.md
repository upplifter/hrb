# Round 8 decided verification (D-084 to D-099)

Checked by the orchestrator against each decision. Lint: RESULT WARN, no FAIL; JSON valid. Frozen text changed only under D-098 (both outcome_unknown copies, no dialogue uses the line). No dialogue needed a C-9 edit: no mini-dialogue shows a Part 4 handoff asking to keep the prior Tax Pro, a new-customer callback number, or a readiness conflict.

L-418 | pass | Prose and JSON both skip the keep question; scenario_selection item 9 selects returning_tax_pro_unavailable when not asked. schedule_new[1] left unedited (oscillation guard, L-417); the routed item is the specific rule.
L-419 | pass | A Part 4 another-Tax-Pro handoff now carries officeRef only; the Scheduler asks the Tax Pro question.
L-420, L-401 | pass | Name confirmation lives in global_always and §1.2; §2 Third-Party prose mirror unchanged (C-2).
L-421 | pass
L-422 | pass
L-423 | pass | Prose and JSON mirror; the scheduler_always cap item still caps the second conflict.
L-424 | pass
L-398 | pass
L-399 | pass | §1.1 customerRef row ("unless the transaction subject changes") is consistent.
L-404 | pass | No other contact.callbackNumber reference remains.
L-397 | pass
L-395 | pass | scheduler_always floor-pass item ("raised on reschedule_existing per its step 4") still matches.
L-396 | pass | Prose and JSON mirror.
L-400 | pass | §4 Out-of-Scope (Appointments) already says "an existing one".
L-402 | pass | Two copies, identical.
L-403 | pass
