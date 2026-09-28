# Round 5 · Lens A findings

Saved by the orchestrator from the reviewer's reply.

### A-01 · The "After Part 4" rule can recast a carried callback as tax_prep
Anchor: §2 State 2 Appointment Type Rules > After Part 4; scheduler_always routed_to_scheduler item
Severity: Medium
Class: Human (pick between readings; changes appointment type)
Issue: The rule has no scope limit, so the normal Part 4 callback handoff (appointmentType callback, taxProRef) also matches and can be booked as tax_prep.
Proposed fix: Decide whether the rule applies only when routed_to_scheduler carried appointmentType null; if so, add "with appointmentType null" to prose and JSON.

### A-02 · The Scheduler/Part 4 loop is still open for Tax Pro requests
Anchor: §2 State 2 Tax Pro Requests; interruptions.intent_change; §4 No Matches / Inactive
Severity: Medium
Class: Human (routing ownership)
Issue: After routed_to_scheduler, an own or named Tax Pro request in the Scheduler still hands back to speak_to_tax_pro, which returns routed_to_scheduler again, unbounded.
Proposed fix: Decide the Scheduler's handling of that request after routed_to_scheduler (e.g., Tax Pro trade-off, or customer_declined_options).

### A-03 · The Scheduler may re-offer the prior Tax Pro that Part 4 found unavailable
Anchor: §4 By Name Request > 1 Match; routed_to_scheduler; workflow.schedule_new[1]; scenario_selection item 8
Severity: Medium
Class: Human (scenario selection)
Issue: Part 4 finds a by-name Tax Pro unavailable via activeStatus or takingAppointmentsInd, but the Scheduler reads only priorTaxProStatus, so it can ask to keep and select returning_same_tax_pro for that Tax Pro.
Proposed fix: Decide whether routed_to_scheduler with appointmentType null skips the keep-prior question and selects returning_tax_pro_unavailable.

### A-04 · A seasonally closed office on the office_contact path has no end state
Anchor: §3 Office Contact Triage first bullet; workflow.office_contact_flow[1]-[2]; office_always closed_for_season item; office_contact_triage_complete
Severity: Medium
Class: Human (caller experience; outcome choice)
Issue: After the D-045 seasonal check, nothing says whether check_office_open_status still runs, whether a main line is given, or which outcome and nextAction return.
Proposed fix: Decide the office_contact closed_for_season terminal (e.g., office_contact_triage_complete with leave_message_offer after the YRO address).

### A-05 · Parts 3 and 4 have no route for appointment-details questions
Anchor: global_always informational item; §3 Out of Scope; §4 Out-of-Scope (Appointments); interruptions.intent_change (Parts 3, 4)
Severity: Medium
Class: Human (routing ownership)
Issue: D-049 makes the Scheduler own appointment-details questions, but Parts 3 and 4 route only schedule, reschedule, or cancel, so "when is my appointment?" gets intent_changed with no routingTarget.
Proposed fix: Decide whether Parts 3 and 4 route these to appointment_scheduler.

### A-06 · The Routed Office rule sits under the office_contact path only
Anchor: §3 Office Contact Triage > Routed Office; office_always[1]
Severity: Low
Class: Safe (incomplete propagation of D-044)
Issue: The bullet sits under Office Contact Triage, but D-044 and office_always[1] apply it on either path.
Proposed fix: "- **Routed Office:** On either path, the office resolved from the caller's ZIP or name becomes the routed office for the rest of the invocation."

### A-07 · The another-Tax-Pro handoff makes the Scheduler re-ask book, change, or cancel
Anchor: §4 No Matches / Inactive; routed_to_scheduler; §1.1 operation
Severity: Low
Class: Human (changes what the caller hears)
Issue: routed_to_scheduler with appointmentType null and operation null makes the Scheduler ask what the caller already answered.
Proposed fix: Decide whether that handoff means schedule_new.
