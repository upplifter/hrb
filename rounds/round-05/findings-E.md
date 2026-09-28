# Round 5 · Lens E findings

Saved by the orchestrator from the reviewer's reply.

### E-01 · transfer_unavailable still gives a failed call close and support hours
Anchor: global_outcomes.transfer_unavailable; global_always transfer-results item; §5.1 Transfer results
Severity: Medium
Class: Safe
Issue: D-043: a failed call returns nextAction transfer with no supportHoursSpoken; the outcome's nextAction clause and "Carry ... supportHoursSpoken" are not scoped to agent_unavailable.
Proposed fix: "transfer_to_agent returned agent_unavailable, or failed (nextAction transfer, no supportHoursSpoken). On agent_unavailable, if leaveMessageAvailable is false, speak supportHoursSpoken and invite a call back, else state only the outcome; nextAction leave_message if requested or accepted, leave_message_offer if still to be offered, else close. Carry transferReason, supportHoursSpoken, and known context per global_always. transactionOccurred false; callContained true only on a message action."

### E-02 · "After Part 4" rule turns Part 4's own callback handoff into tax_prep
Anchor: §2 State 2 After Part 4; scheduler_always routed_to_scheduler item; §1.1; routed_to_scheduler
Severity: Medium
Class: Human (pick between readings)
Issue: Same as A-01 / C-02.
Proposed fix: Scope D-040 to appointmentType null, or confirm it also applies to a carried callback.

### E-03 · Scheduler asks "book, change, or cancel" after Part 4 routes a caller to book
Anchor: §1.1 operation; context_envelope.operation; §4 No Matches / Inactive; routed_to_scheduler
Severity: Medium
Class: Human (changes what the caller hears)
Issue: Same as A-07 / D-04.
Proposed fix: Decide whether routed_to_scheduler means schedule_new.

### E-04 · DDO change request: new send in the same invocation, or post-commit handback
Anchor: §2 State 2 DDO Rules > Rescheduling; scheduler_always DDO item; §2 State 4 Post-Commit Requests
Severity: Medium
Class: Human (pick between readings)
Issue: Same as C-06.
Proposed fix: Decide timing and key.

### E-05 · schedule_new step 2: "rejecting it" can read as rejecting the Tax Pro
Anchor: workflow.schedule_new[1]; §2 State 3 Declined Offices
Severity: Medium
Class: Safe
Issue: Same as D-01.
Proposed fix: "rejecting that office moves to the same_tax_pro_nearby_offices rung".

### E-06 · By-name workflow states the options with no active-status branch
Anchor: workflow.speak_to_tp_by_name[4]; §4 1 Match; tax_pro_always unavailable item
Severity: Low
Class: Safe
Issue: By-name step 5 states the options unconditionally, so an inactive Tax Pro gets callback and message options.
Proposed fix: "5. If the Tax Pro is active and taking appointments, state the options per tax_pro_always; otherwise apply the tax_pro_always unavailable item."

### E-07 · "the deterministic flow" where the JSON names the Leave a Message flow
Anchor: §1.3 last bullet; workflow.office_contact_flow[0]
Severity: Low
Class: Safe
Issue: Since D-039 names Head of Call too, "the deterministic flow" is ambiguous.
Proposed fix: "the Leave a Message flow" in both places.
