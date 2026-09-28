# Round 6 · Lens A findings

Saved by the orchestrator from the reviewer's reply.

### A-01 · A booking request for a named Tax Pro has no owner that honors the Tax Pro
Anchor: §4 State 2 tax_pro_always callback item; §2 State 2 Appointment Type Rules > Tax Pro Requests; §2 State 5 broadening.scenario_selection items 8-10
Severity: Medium
Class: Human
Issue: A caller who wants a regular appointment (not a callback) with a named, non-prior, non-carried Tax Pro is sent from the Scheduler to speak_to_tax_pro, and Part 4 sends any non-callback booking back to appointment_scheduler without saying to carry taxProRef. Without taxProRef the loop repeats (D-051 limits it only after routed_to_scheduler); with it, scenario_selection honors only a prior Tax Pro (item 8) or callback, so the call falls to item 9 or 10 and silently changes the Tax Pro.
Proposed fix (options):
- A. Part 4 carries taxProRef and officeRef on that intent_changed; the Scheduler treats a carried non-prior taxProRef like returning_same_tax_pro at the carried office.
- B. Booking with a named non-own Tax Pro is out of scope; Part 4 states that once and offers callback, message, or another qualified Tax Pro (routed_to_scheduler, appointmentType null), never intent_changed.
- C. The Scheduler asks once whether any qualified Tax Pro is acceptable; a no returns customer_declined_options; never hands it back.

No other Medium-or-higher lens A issues found.
