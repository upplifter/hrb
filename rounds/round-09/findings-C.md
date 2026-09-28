# Round 9 · Lens C findings

Saved by the orchestrator from the reviewer's reply.

### C-01 · The terminal contract's "officeRef on either handoff" leaves out Part 4's another-Tax-Pro handoff
Anchor: §1.5 terminal_payload_contract (taxProRef/officeRef clause); §4 State 2 agent_specific_outcomes.routed_to_scheduler
Severity: Medium
Class: Human
Issue: D-085 text reads "taxProRef when handing off to leave a message or to appointment_scheduler for a callback, and officeRef on either handoff." Literally, "either handoff" names only the message and callback handoffs, while §4 routed_to_scheduler carries officeRef on the another-Tax-Pro handoff (D-040). Part 1 wins under C-1, so the literal reading drops it. An implementer must guess whether officeRef rides only on routed_to_scheduler or on every handoff to appointment_scheduler.
Fix: Options:
A. (Recommended) Old: "taxProRef when handing off to leave a message or to appointment_scheduler for a callback, and officeRef on either handoff." New: "taxProRef when handing off to leave a message or to appointment_scheduler for a callback, and officeRef, when known, on a message handoff or any routed_to_scheduler."
B. "... and officeRef on a message handoff or any handoff to appointment_scheduler." (adds carrying on Part 3 and Scheduler intent_changed handoffs).
Footprint: A 1 edit, about +7 words, no behavior change. B 1 edit, about +6 words, changes office resolution after a Part 3 or post-commit handback.

### C-02 · The reschedule floor rule (D-095) conflicts with the fixed per-type floors
Anchor: workflow.reschedule_existing[3]; §2 State 2 Complexity Matching > Reschedule; scheduler_always emerald_advance/tax_notice_service/callback floor item; §2 State 2 Appointment Type table; §5.2 check_search_readiness > Callbacks
Severity: Medium
Class: Human
Issue: Step 4 sends the higher of the baseline and the bound taxProCertLevel on every reschedule. Other rules fix the floor at 1 (emerald_advance, tax_notice_service, callback) or null (Physical Drop-Off). scenario_selection schedules callback and physical_drop_off reschedules, so a callback reschedule could get a floor up to 5.
Fix: Options:
A. (Recommended) Fixed floors win on reschedule. reschedule_existing[3]: "Send taxProRatingFloor as the higher of" becomes "Except on emerald_advance, tax_notice_service, callback, or physical_drop_off (per scheduler_always), send taxProRatingFloor as the higher of". §2 Reschedule bullet adds ", except where the type table sets the floor."
B. D-095 wins for every type; add "on schedule_new" to the fixed-floor item, the type-table callback cell, and §5.2 Callbacks.
Footprint: A 2 edits, about +20 words, matches pre-D-095 behavior. B 3 edits, about +9 words, narrows availability.

### C-03 · office_never still hands every appointment question to the Scheduler, against D-097
Anchor: §3 State 2 office_never[0]
Severity: Medium
Class: Safe
Issue: Same as E-01.
Fix: Old: "Never schedule, reschedule, or cancel appointments or answer questions about them. Hand back intent_changed to appointment_scheduler immediately." New: "Never schedule, reschedule, or cancel appointments or answer questions about an existing one. Hand back intent_changed to appointment_scheduler immediately."

### C-04 · workflow.schedule_new[1] still asks the keep-prior-Tax-Pro question after a Part 4 route (D-084)
Anchor: workflow.schedule_new[1]; scheduler_always routed_to_scheduler item
Severity: Low
Class: Safe (oscillation guard, L-417)
Issue: Same as E-03.
Fix: Pair with L-417 or hold in backlog.

### C-05 · "method-specific contact detail" has no referent after D-093
Anchor: workflow.schedule_new[2]
Severity: Low
Class: Human
Issue: The only method-specific contact field was contact.callbackNumber, removed by D-093. The phrase is now dead text or means the DDO destination.
Fix: A. (Recommended) Delete "method-specific contact detail, " (-3 words). B. Replace with "the digital drop-off destination".

### C-06 · Three names for the D-097 question class, and Part 4 omits it
Anchor: §1.2 Tax/Financial Boundary sub-bullet; §2 State 3 Informational Interruptions > Hand back; §4 State 1 Out-of-Scope (FAQ Agent); global_always informational item
Severity: Low
Class: Safe
Issue: "out-of-task appointments_and_logistics questions" (JSON), "out-of-task appointment-logistics questions" (§1.2), "out-of-task logistics questions" (§2). §4 FAQ list omits it; global_always covers Part 4, so no behavior gap.
Fix: Unify to "out-of-task appointments_and_logistics questions" in §1.2 and §2; add to §4 FAQ list.

Verified clean: no callbackNumber or contact object remains; all 33 JSON blocks parse; every enum defined and used; idempotency keys and confirmation evidence present on every write.

Summary: 6 findings (0 Critical, 0 High, 3 Medium, 3 Low).
