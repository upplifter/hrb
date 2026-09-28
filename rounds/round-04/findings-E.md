# Round 4 findings - Lens E (Prose and JSON parity)

Saved by the orchestrator from the reviewer's reply (write blocked).

### E-01 · Tax Pro Requests prose drops "to speak to"
Anchor: §2 State 2 Appointment Type Rules > Tax Pro Requests; §2 State 5 interruptions.intent_change; workflow.schedule_new[1]; broadening.scenario_selection item 8
Severity: Medium
Class: Safe. The JSON mirror, the round 3 verifier fix for L-177, and schedule_new[1] and item 8 allow only one reading.
Issue: Prose says "A request for a specific or own Tax Pro ... hands back intent_changed to speak_to_tax_pro"; `interruptions.intent_change` says "A request to speak to a specific or their own Tax Pro". The prose would hand back a returning client booking with their own Tax Pro.
Proposed fix: "A request to speak to a specific or own Tax Pro", trimming to stay within 35 words.

### E-02 · Failed transfer call on the outcome_unknown path
Anchor: §1.5 global_always transfer-results item; global_outcomes.outcome_unknown; §5.1 transfer_to_agent Transfer results; terminal_payload_contract idempotencyKey
Severity: Medium
Class: Human (picks between D-015 and D-026)
Issue: A failed call returns "transfer_unavailable with nextAction close" with no outcome_unknown exception, while outcome_unknown says "Return this outcome either way, with ... idempotencyKey", so the reconciliation key is lost.
Proposed fix: Decide whether a failed call on outcome_unknown keeps outcome_unknown and idempotencyKey.

### E-03 · handoff_invalid and configuration_missing: transfer_to_agent or not
Anchor: §1.4 intro and handoff_invalid or configuration_missing row; §1.5 global_outcomes.handoff_invalid, configuration_missing
Severity: Medium
Class: Human
Issue: The §1.4 intro says "On a path that ends in a transfer, call `transfer_to_agent` first", and both outcomes carry "transferReason system_failure ... nextAction transfer", but also "Say nothing, ask nothing, hand back immediately", which reads as no tool call.
Proposed fix: State whether the agent calls `transfer_to_agent` silently or hands back without calling it.

### E-04 · cancel_existing workflow never checks status canceled
Anchor: §2 State 5 workflow.cancel_existing[1],[2]; agent_specific_outcomes.appointment_already_canceled
Severity: Medium
Class: Safe. D-021 and D-028 fix the trigger, and the outcome says "no write ran".
Issue: The workflow binds the appointment and goes straight to the cancellation gate, so it reads back and gates a canceled appointment.
Proposed fix: Add to cancel_existing[1]: "If the bound appointment's status is canceled, return appointment_already_canceled."

### E-05 · Cancel scope: "mid-booking" vs "before any commit"
Anchor: §2 State 4 Write Tools > cancel_appointment; §2 State 5 objective; interruptions.cancel_said
Severity: Medium
Class: Human (two plausible readings of D-028)
Issue: Prose allows cancel "only on operation cancel_existing or a mid-booking cancel request", but `cancel_said` cancels whenever "the caller wants to cancel before any commit", including during reschedule_existing.
Proposed fix: Decide whether a cancel request during reschedule_existing runs cancel_existing, then align both.

### E-06 · no_acceptable_availability definition omits first-lookup none_nearby
Anchor: §2 State 5 agent_specific_outcomes.no_acceptable_availability; scheduler_always find_offices_near item
Severity: Low
Class: Safe. D-015 and D-016 map first-lookup none_nearby to this reason.
Issue: The outcome is defined only as ladder exhaustion.
Proposed fix: Append "or find_offices_near returned none_nearby at the first office lookup".

### E-07 · too_many row not updated for D-028
Anchor: §5.2 get_customer_appointments Outcome Results (too_many)
Severity: Low
Class: Safe. D-028; the other three rows were updated.
Issue: too_many says only "More than three appointments".
Proposed fix: "More than three future appointments, active or canceled."

### E-08 · global_never web-deflection item narrower than §1.2
Anchor: §1.2 Zero Web Deflection & Prohibited Speech; §1.5 global_never web-deflection item
Severity: Low
Class: Safe. C-1 and C-2 A.
Issue: Prose: "Never suggest going online or speak a URL, website, portal, or app name". JSON omits the app-name and website ban.
Proposed fix: Change the JSON item to match the prose and keep its exceptions.

### E-09 · Scheduler JSON has no check_search_readiness conflict branch
Anchor: §1.4 conflict from readiness row; §2 State 5 agent_specific_tools.check_search_readiness
Severity: Low
Class: Safe (propagation; scope question stays with L-146)
Issue: The JSON entry handles needs_more and out_of_scope but not conflict.
Proposed fix: Add "On conflict, speak the approved conflict line and re-ask the date."

### E-10 · context_envelope carried fields omit the precedence clause
Anchor: §1.1 appointmentType, taxProRef, officeRef row; §1.5 context_envelope.appointmentType, taxProRef, officeRef
Severity: Low
Class: Safe. D-027 under C-2 A.
Issue: §1.1 says each carried value "skips its own question and outranks entryPoint and routedOfficeRef"; the context_envelope strings say only "skip its question".
Proposed fix: Append "; outranks entryPoint and routedOfficeRef" and trim the scheduler_always duplicate.
