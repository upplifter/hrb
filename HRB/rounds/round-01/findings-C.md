# Findings - Lens C (Contracts and vocabulary)

- anchor: §1.5 terminal_payload_contract
  also: §1.5 global_outcomes.transfer_unavailable; §1.5 global_outcomes.transferred_to_human; §2 State 5 agent_specific_outcomes.customer_declined_options; §4 Fulfillment: CDAS Callback Appointment; §1.5 context_envelope
  severity: High
  claim: Outcomes and agent rules carry appointmentType, appointmentRef, transferReason, supportHoursSpoken, and sourceUtterance, but the contract's field list defines none of them, and context_envelope has no appointmentType input for the Scheduler.
  evidence: "Carry applicable outcome fields: newAppointmentRef, rescheduledAppointmentRef" | "routingTarget = appointment_scheduler, and appointmentType = callback" | "Carry transferReason, supportHoursSpoken" | "Carry the surviving appointmentRef where applicable"
  class: human
  decision: terminal-contract-field-list

- anchor: §5.2 send_secure_link Request JSON
  also: §2 State 5 scheduler_never; §2 State 5 workflow.schedule_new step 6; §2 State 5 objective
  severity: High
  claim: send_secure_link writes but has no idempotencyKey and no confirmation object, and it requires customerRef, which a new DDO caller cannot have because only book_appointment creates profiles.
  evidence: "only book_appointment may create the profile at commit" | "call send_secure_link once with the confirmed destination and close" | "Enforce the confirmation gate before every write"
  class: human
  decision: ddo-write-contract

- anchor: §1.5 context_envelope.entryPoint
  also: §3 State 2 office_always; §3 State 2 workflow.office_info_flow; §4 State 2 tax_pro_always
  severity: High
  claim: The Office Information and Tax Pro agents need routedOfficeRef, but the envelope carries only dialedOfficeNumber, and only the Scheduler's find_offices_near resolves one to the other.
  evidence: "field_office_rollover or central_line; dialedOfficeNumber on rollover" | "resolve the dialed number to routedOfficeRef" | "Call get_office_details using the routed officeRef or captured ZIP"
  class: human
  decision: routed-office-ref-source

- anchor: §5.1 transfer_to_agent Request JSON transferReason
  also: §1.5 global_outcomes.system_failure; §2 State 5 scheduler_always (too_many rule)
  severity: Medium
  claim: transferReason has no defined enum, several transfer triggers (barging, too_many, isCancelable false, none_nearby, handoff_invalid) have no value, and "transfer default" is never defined.
  evidence: "A tool failed or the availability check failed. Follow the transfer default" | "transferReason identity_unresolved" | "preserve the appointment untouched and call transfer_to_agent immediately"
  class: human
  decision: transfer-reason-enum

- anchor: §1.5 global_outcomes
  also: §1.5 terminal_payload_contract; §2 State 5 agent_specific_outcomes.no_acceptable_availability
  severity: Medium
  claim: The contract makes transactionOccurred, callContained, and intent mandatory, but intent_changed, appointment_requested, and most transfer outcomes state none of their values.
  evidence: "All outcomes inherit mandatory fields" | "carry sourceUtterance, applicable reference and routingTarget, then route_intent" | "Carry sourceUtterance. route_intent"
  class: human
  decision: outcome-mandatory-field-values

- anchor: §1.5 global_outcomes.transfer_unavailable
  also: §3 State 2 agent_specific_outcomes.office_contact_triage_complete; §3 State 2 agent_specific_outcomes.office_open_unanswered; §4 State 2 agent_specific_outcomes.routed_to_message
  severity: Medium
  claim: callContained has no definition and takes opposite values for the same handback, true for leave_message in Parts 3-4 but false in transfer_unavailable.
  evidence: "callContained true, nextAction leave_message_offer or leave_message respectively" | "transactionOccurred false, callContained false." | "callContained false, nextAction capture_intent"
  class: human
  decision: call-contained-meaning

- anchor: §1.5 terminal_payload_contract routingTarget
  also: §2 State 5 interruptions.intent_change; §3 State 2 interruptions.intent_change; §4 State 2 interruptions.intent_change
  severity: Medium
  claim: The routingTarget enum lists tax_prep, an appointment type that no rule uses as a destination, ends with open-ended "named destination", and has no value for the Office Information or Tax Pro agents.
  evidence: "routingTarget (refund_status, faq_agent, appointment_scheduler, tax_prep, or named destination)" | "close any committed transaction, then hand back intent_changed"
  class: human
  decision: routing-target-enum

- anchor: §1.5 global_outcomes.appointment_requested
  also: §1.5 global_outcomes.intent_changed; §3 State 1 Intent Scope & Disambiguation > Out of Scope
  severity: Medium
  claim: No rule emits appointment_requested, and it overlaps intent_changed, so two outcome names cover one handback to the Scheduler.
  evidence: "Caller requested an appointment type outside the scope of this agent" | "Any request to schedule, reschedule, or cancel an appointment immediately hands back intent_changed"
  class: human
  decision: appointment-requested-outcome

- anchor: §2 State 5 agent_specific_tools.find_available_cdas_slots
  also: §5.2 find_available_cdas_slots; §5.2 check_search_readiness Note; §2 State 5 scheduler_always (floor rule)
  severity: Medium
  claim: No workflow step calls find_available_cdas_slots, and the callback path instead runs readiness with a null floor that the Scheduler says is mandatory; the tool's field names (hrbEmployeeId, availableSlots) also differ from find_available_slots.
  evidence: "Searches Appointment Manager for 15-minute Callback Appointment (CDAS) slots" | "For CDAS callbacks, send appointmentType = callback; appointmentMethod, taxProRatingFloor, and timeWindow may be null" | "Treat it as a mandatory eligibility filter, except on physical_drop_off"
  class: human
  decision: callback-search-contract

- anchor: §2 State 3 Readiness & Availability > CDAS
  also: §2 Appointment Type Rules table (callback row); §2 Ladders table; §5.2 find_available_slots Response JSON isCDAS
  severity: Medium
  claim: "CDAS" means both the 15-minute callback appointment type and any slot with no named Tax Pro, so isCDAS cannot tell a callback from an unnamed regular slot.
  evidence: "15-minute CDAS callback" | "returns taxProName as null or empty, treat the slot as CDAS" | "any qualified Tax Pro at that office, CDAS included"
  class: human
  decision: cdas-term-meaning

- anchor: §5.2 check_search_readiness Outcome Results
  also: §2 State 5 broadening.scenario_selection; §5.2 send_secure_link Outcome Results; §5.3 check_office_open_status Outcome Results; §5.1 search_knowledge_base; §2 State 5 agent_specific_outcomes.new_appointment_scheduled
  severity: Medium
  claim: Several tool results map to no rule or outcome: readiness out_of_scope (scenario_selection runs only after ready), delivery_failed, hours_unavailable, a sub-0.85 KB answer, and DDO link_sent, since new_appointment_scheduled requires a booking ref.
  evidence: "Request sits outside the pilot (e.g., Tax Pro Review)" | "First match wins after readiness returns ready" | "Link could not be sent to the provided destination" | "Schedule data missing for the requested location"
  class: human
  decision: unmapped-tool-results

- anchor: §2 State 5 agent_specific_outcomes.appointment_already_canceled
  also: §2 State 5 closure.continuation_context; §5.2 get_customer_appointments Outcome Results
  severity: Medium
  claim: No tool result can trigger appointment_already_canceled, because get_customer_appointments returns only active future appointments and defines no status enum.
  evidence: "Target was already canceled and no write ran" | "No active future appointments exist" | "a reference that comes back canceled is handled as already canceled"
  class: human
  decision: already-canceled-detection

- anchor: §5.2 reschedule_appointment Outcome Results
  also: §2 State 5 scheduler_always (tool-result handling rule); §5.2 book_appointment Outcome Results; §5.2 cancel_appointment Outcome Results
  severity: Medium
  claim: reschedule_appointment carries confirmation evidence but defines no not_confirmed or rejected result, unlike book_appointment and cancel_appointment, though the Scheduler handles both.
  evidence: "Confirmation evidence missing/incomplete" | "Requested change not permitted on existing appointment" | "On not_confirmed, re-gate"
  class: human
  decision: reschedule-result-set

- anchor: §2 State 3 Readiness & Availability > CDAS
  also: §2 State 5 objective; Part 5 Conventions Common to Every Tool
  severity: Medium
  claim: The CDAS exception names physical drop-off as an appointment type, but it is a method token, and the type enum has no such value.
  evidence: "unless the appointment type is physical drop-off" | "Five appointment types are in scope" | "isDropOff is true only for physical_drop_off"
  class: safe
  fix: Change "unless the appointment type is physical drop-off" to "unless appointmentMethod is physical_drop_off".

- anchor: §2 State 5 broadening.ladders.tax_notice.rungs[3]
  also: §5.2 find_available_slots Note (rung values); §2 State 5 agent_specific_tools.find_available_slots
  severity: Medium
  claim: The fourth tax_notice rung has no rung token, although find_available_slots requires one from the enum and other ladders prefix the same rung with any_qualified_tax_pro.
  evidence: "with permission (Tax Pro trade-off), any qualified EA/CPA at the primary office" | "Send scenario and rung from broadening."
  class: safe
  fix: Rewrite the rung as "any_qualified_tax_pro EA/CPA at the primary office, only after the Tax Pro trade-off returns permission".
