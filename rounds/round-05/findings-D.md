# Round 5 · Lens D findings

Saved by the orchestrator from the reviewer's reply.

### D-01 · "rejecting it" can mean the Tax Pro or the office
Anchor: §2 State 5 workflow.schedule_new[1]
Severity: Medium
Class: Safe
Issue: "ask whether to keep them; yes selects returning_same_tax_pro at the last-served office; rejecting it moves to the same_tax_pro_nearby_offices rung". "It" can read as the Tax Pro. §2 State 3 Declined Offices settles it (C-1).
Proposed fix: "...yes selects returning_same_tax_pro at the last-served office, and rejecting that office moves to the same_tax_pro_nearby_offices rung; otherwise resolve the office by entryPoint." (59 words)

### D-02 · office_contact at a closed_for_season office has no stop point
Anchor: §3 Office Contact Triage (first bullet); workflow.office_contact_flow[1], [2]; office_always closed_for_season item
Severity: Medium
Class: Human (pick between readings; changes what the caller hears)
Issue: After D-045, office_contact applies office_info_flow step 2, so a closed_for_season office gets the closure line and Year-Round Office address, but nothing says whether the flow stops or continues to check_office_open_status, or which office's status and number apply.
Proposed fix: Decide: (a) return office_contact_triage_complete with leave_message_offer after the YRO address, or (b) make yroOfficeRef the routed office and continue.

### D-03 · Appointment-details path: mid-booking exit and unhandled results
Anchor: §2 State 3 Informational Interruptions > Appointment Details; agent_specific_tools.get_customer_appointments
Severity: Medium
Class: Human (changes what the caller hears)
Issue: Under a "mid-booking" trigger, the details rule ends the invocation, while other interruptions resume. No handling for none_found, several_appointments, too_many, false flags, or canceled status. Separate from L-324.
Proposed fix: Decide whether a mid-booking details question resumes, and what the path does on each result.

### D-04 · Scheduler re-asks book/change/cancel after Part 4's booking offer
Anchor: §4 No Matches / Inactive; Generic Request; routed_to_scheduler; §1.1 operation
Severity: Medium
Class: Human (changes what the caller hears)
Issue: routed_to_scheduler with appointmentType null sets no operation, so the Scheduler asks book, change, or cancel after the caller already said yes to booking.
Proposed fix: Decide whether routed_to_scheduler from Part 4 means schedule_new.

### D-05 · "After Part 4" rule may recast the Part 4 callback as tax_prep
Anchor: §2 State 2 Appointment Type Rules > After Part 4; scheduler_always routed_to_scheduler item
Severity: Medium
Class: Human (pick between readings)
Issue: The rule also matches the normal Part 4 callback handoff (appointmentType callback with taxProRef), so it can be read to book that as tax_prep phone_callback.
Proposed fix: Decide whether the rule applies only when routed_to_scheduler carried appointmentType null.

### D-06 · No cap on the Part 4 and Scheduler loop for an unavailable own Tax Pro
Anchor: §2 State 2 Tax Pro Requests; interruptions.intent_change; §4 No Matches / Inactive
Severity: Medium
Class: Human (moves routing between agents)
Issue: After Part 4 routes an unavailable-Tax-Pro caller to the Scheduler, a request for their own Tax Pro still hands back to speak_to_tax_pro, which re-offers the Scheduler, with no bound. D-040 covers only callback requests.
Proposed fix: Decide how the Scheduler handles an own or specific Tax Pro request after routed_to_scheduler.

### D-07 · Switching operations mid-invocation has no rule except cancel_said
Anchor: interruptions.cancel_said, intent_change; workflow.cancel_existing[2]; §2 State 2 DDO Rules > Rescheduling
Severity: Medium
Class: Human (changes what the caller hears)
Issue: "No, move it instead" at a cancellation gate returns customer_declined_options. A DDO change request answering "change" sets reschedule_existing, whose retrieval returns none_found and transfers, so "a new schedule_new DDO send" is unreachable.
Proposed fix: Decide whether a pre-commit operation switch restarts the new workflow in the same invocation, and how a DDO change reaches schedule_new.

### D-08 · Declining the closed-window tax_prep pivot on tax_extension has no exit
Anchor: §2 State 2 table tax_extension row; scheduler_always tax_extension item; customer_declined_options
Severity: Medium
Class: Human (assigns an outcome to a caller path)
Issue: When the extension window is closed and the caller declines the tax_prep offer, no outcome applies.
Proposed fix: Decide the exit, e.g., add the declined pivot to customer_declined_options.
