# Round 9 · Lens A findings

Saved by the orchestrator from the reviewer's reply.

### A-01 · After Part 4, the Scheduler cannot tell the Part 4-named Tax Pro from any other named Tax Pro
Anchor: §2 State 2 Appointment Type Rules > After Part 4 (third sub-bullet); scheduler_always routed_to_scheduler item; §1.5 terminal_payload_contract (taxProRef clause); §4 agent_specific_outcomes.routed_to_scheduler
Severity: Medium
Class: Human
Issue: After Part 4, the own or Part 4-named Tax Pro gets the D-081 statement; any other named Tax Pro hands back to speak_to_tax_pro. After D-085 the another-Tax-Pro handoff carries no taxProRef, so the Scheduler cannot identify the Part 4-named Tax Pro. A mistaken handback loops the caller back to Part 4.
Fix: A. (Recommended) Treat any named Tax Pro after Part 4 like the own one. Prose: "On a request for their own Tax Pro or the one named in Part 4," becomes "On a request for their own or any named Tax Pro,". JSON: "On a request for the caller's own or the Part 4-named Tax Pro," becomes "On a request for the caller's own or any named Tax Pro,". B. Carry the Part 4-named taxProRef on the another-Tax-Pro handoff for recognition only (partly reverses D-085).
Footprint: A 2 edits, about -4 words, changes what the caller hears for a third named Tax Pro. B 4 edits, about +20 words.

### A-02 · The reschedule floor (D-095) conflicts with floor 1 on emerald_advance, tax_notice_service, and callback
Anchor: workflow.reschedule_existing[3]; §2 State 2 Complexity Matching > Reschedule; scheduler_always floor-1 item; §2 State 2 Appointment Type table
Severity: High
Class: Human
Issue: Same as C-02, D-03. Two rules require different floors on the same reschedule; the higher floor can hide every slot the first booking used.
Fix: A. (Recommended) "the higher of the inherited baseline floor (1 on emerald_advance, tax_notice_service, and callback), taken silently"; prose "Use the baseline silently (1 on types that skip screening),". B. Inherited baseline on every reschedule; scope the type item and rows to schedule_new.
Footprint: A 2 edits, +12 words. B 2-4 edits, +6 words.

### A-03 · schedule_new[1] still asks the keep-prior-Tax-Pro question after Part 4 (D-084 propagation)
Anchor: workflow.schedule_new[1]
Severity: Medium
Class: Safe
Issue: Same as D-01, E-03, C-04.
Fix: As D-01.

### A-04 · office_never still sends every appointment question to the Scheduler (D-097 propagation)
Anchor: §3 State 2 office_never[0]
Severity: Medium
Class: Safe
Issue: Same as E-01.
Fix: As E-01.

### A-05 · Tax Pro Requests again hands back a booking with the caller's own Tax Pro (L-252 regression)
Anchor: §2 State 2 Appointment Type Rules > Tax Pro Requests; §2 State 5 interruptions.intent_change
Severity: Medium
Class: Safe
Issue: L-252 (round 4) set this rule to "A request to speak to a specific or own Tax Pro" (D-034 split between a request for a person and a booking). Later decided commits dropped "to speak to". Now a returning client who wants to book with their own Tax Pro has two owners: handback under this rule, or the keep question / scenario_selection item 8.
Fix: Prose Old: "**Tax Pro Requests:** Requests for a specific or own Tax Pro," New: "**Tax Pro Requests:** Requests to speak to a specific or own Tax Pro,". JSON Old: "A request for a specific or own Tax Pro, a named Tax Pro other than the prior or carried one," New: "A request to speak to a specific or own Tax Pro, a named Tax Pro other than the prior or carried one,".

### A-06 · The gatekeeper item has no reschedule exception (D-095 propagation)
Anchor: §2 State 5 scheduler_always gatekeeper item
Severity: Low
Class: Safe
Issue: Same as D-02.
Fix: As D-02.

Summary: 6 findings (0 Critical, 1 High, 4 Medium, 1 Low).
