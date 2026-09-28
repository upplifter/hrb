# Round 6 · Lens E findings

Saved by the orchestrator from the reviewer's reply.

### E-01 · A carried officeRef skips the keep-prior-Tax-Pro question that D-050 keeps
Anchor: scheduler_always carried-context item; §1.1 appointmentType, taxProRef, officeRef row
Severity: Medium
Class: Safe
Issue: JSON "A carried appointmentType, taxProRef, or officeRef also outranks the prior Tax Pro question" contradicts D-050 on a routed_to_scheduler that carries officeRef. A carried callback type always comes with taxProRef.
Proposed fix: "A carried taxProRef also outranks the prior Tax Pro question."

### E-02 · No JSON handler for first-party multiple_matches or none_found on reschedule or cancel
Anchor: scheduler_always authentication-failure item; workflow.reschedule_existing[1]; §1.4 multiple_matches and none_found rows; §2 State 1 Authentication Logic
Severity: Medium
Class: Safe (prose wins, C-1)
Proposed fix: authentication-failure item adds "or find_customer returns multiple_matches"; reschedule_existing[1] adds "On none_found, transfer as identity_or_appointment_mismatch."

### E-03 · Automation flags transfer on every operation, including an appointment-details question
Anchor: scheduler_always too_many/flags item; §2 State 3 Appointment Details; §5.2 get_customer_appointments > Automation Flags
Severity: Medium
Class: Human
Issue: Flags are unscoped: a details question on a non-reschedulable appointment transfers (JSON) or is answered (prose); a reschedule with isCancelable false transfers; an unbound appointment's flag transfers before binding.
Options: A. Scope flags to their operation and the bound appointment; details questions ignore them. B. Exempt only details questions. C. Leave unscoped and add the flag transfer to the details bullet.

### E-04 · customer_declined_options excludes the D-051 second own-Tax-Pro request
Anchor: agent_specific_outcomes.customer_declined_options
Severity: Medium
Class: Safe
Note: already fixed in the round 5 decided follow-up (duplicate).
