# Round 5 · Lens C findings

Saved by the orchestrator from the reviewer's reply.

### C-01 · Terminal appointmentType is re-read as a carried appointmentType
Anchor: terminal_payload_contract (appointmentType); §1.1 appointmentType, taxProRef, officeRef row; context_envelope.appointmentType; §2 State 4 Post-Commit Requests; §2 State 2 Tax Extension
Severity: Medium
Class: Human (pick between readings)
Issue: The terminal payload carries appointmentType, and §1.1 treats any appointmentType set by a prior handoff as carried ("a carried appointmentType means schedule_new"). A post-commit cancel handback, or the extension-to-tax_prep handback, could then start the wrong booking.
Proposed fix: Decide which handbacks set the next envelope's appointmentType, and what the Scheduler's intent_changed to appointment_scheduler sends.

### C-02 · "callback" has two meanings; After Part 4 collides with a carried callback type
Anchor: §2 State 2 After Part 4; scheduler_always routed_to_scheduler item; routed_to_scheduler; Part 5 Conventions CDAS bullet
Severity: Medium
Class: Human (pick between readings)
Issue: The rule does not say which routed_to_scheduler variant it covers, contradicts a carried callback type, and compares priorTransaction (not priorTransaction.finalOutcome) to an outcome name.
Proposed fix: Decide scope (appointmentType null only?), whether Head of Call sets priorTransaction after a Part 4 handback, and the meaning of "callback appointment" in the CDAS definition.

### C-03 · transfer_unavailable outcome omits the D-043 failed-call values
Anchor: §1.5 global_outcomes.transfer_unavailable
Severity: Medium
Class: Safe (incomplete propagation of D-043)
Issue: The outcome lists nextAction "... else close" and carries supportHoursSpoken, but a failed call returns nextAction transfer with no supportHoursSpoken.
Proposed fix: "transfer_to_agent returned agent_unavailable or failed. On agent_unavailable, if leaveMessageAvailable is false, speak supportHoursSpoken and invite a call back, else state only the outcome; nextAction leave_message if requested or accepted, leave_message_offer if not yet offered, else close; carry supportHoursSpoken. On a failed call, nextAction transfer. Carry transferReason and known context per global_always. transactionOccurred false; callContained true only on a message action." (60 words; also closes L-176)

### C-04 · office_contact on a closed_for_season office has no outcome
Anchor: §3 Office Contact Triage first bullet; workflow.office_contact_flow[1]; office_always closed_for_season item
Severity: Medium
Class: Human (changes what the caller experiences)
Issue: Same gap as A-04 and D-02.
Proposed fix: Decide the office_contact closed_for_season end.

### C-05 · Part 3 clarification_exhausted has no valid intent value
Anchor: terminal_payload_contract intent enum and default; §3 Unclear intent; office_always[1]
Severity: Medium
Class: Human (add or choose an enum value)
Issue: After D-042, an unresolved Part 3 intent ends in clarification_exhausted with no office_info or office_contact established, so the mandatory intent has no value. L-294's gap is still open.
Proposed fix: Decide a fixed default, omission on this path, or a new enum value (C-7).

### C-06 · Post-commit DDO change: two rules, no reference, no key
Anchor: §2 State 2 DDO Rules > Rescheduling; scheduler_always DDO item; §2 State 4 Post-Commit Requests; ddo_link_sent; idempotency item
Severity: Medium
Class: Human (pick between readings)
Issue: The DDO rule reads as a second send in this invocation with no key (ddo-2 is the re-send), while D-041 hands back with a committed reference that DDO does not have; the next invocation's "change" runs reschedule_existing and ends in none_found.
Proposed fix: Decide how a DDO change after ddo_link_sent works and what the handback carries.

### C-07 · canceledSummary means a write result and a retrieved record
Anchor: Part 5 Conventions summary bullet; appointment_already_canceled
Severity: Low
Class: Safe
Issue: Conventions says canceledSummary describes write results, but appointment_already_canceled carries it with no write.
Proposed fix: In appointment_already_canceled, "Carry canceledAppointmentRef, and the retrieved summary as canceledSummary." (Conventions edit held: oscillation guard, L-321.)

### C-08 · Dead synonyms for the envelope
Anchor: Part 5 Conventions first bullet
Severity: Low
Class: Safe
Issue: "sessionEnvelope" and "inbound JSON payload" appear nowhere else.
Proposed fix: "- context_envelope and the Head of Call envelope (§1.1) name the same input."
