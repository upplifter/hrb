# Round 8 changes

Format: `ledger ID | anchor | change | net words`. Applied by the orchestrator from the reviewers' exact replacement text. Lint after the batch: RESULT WARN, no FAIL, no new warning; round growth +0.05%; JSON valid.

L-412 | §5.2 book_appointment Request JSON (Existing Customer).appointmentMethod | phone_callback -> in_person; keeps D-072's null appointmentNotes and matches the in-person confirmedSummary and the transfer_to_agent example | 0
L-413 | §2 State 2 type table, callback row | Reason capture restated as "On any phone_callback, of any type" and moved after the callback-only rules (D-083) | +5
L-414 | agent_specific_tools.check_search_readiness | "follow the appointment-type item" -> "follow the emerald_advance or tax_extension item" | +3
L-415 | §5.2 check_search_readiness Request and Response examples | source and taxProSource caller_stated -> existing_appointment (D-079) | 0
L-416 | §2 State 2 Tax Pro Requests | "except After Part 4" -> "except as After Part 4 lists"; trimmed to 35 words ("Requests for", "without carried taxProRef") | -2

Skipped for the oscillation guard: After Part 4 sub-bullet (edited rounds 5-7), workflow.schedule_new[1] trim (L-417, backlog).
