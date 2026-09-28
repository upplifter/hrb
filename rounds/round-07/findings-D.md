# Round 7 · Lens D findings

Saved by the orchestrator from the reviewer's reply. One High, six Medium.

### D-01 · Reschedule cannot fill the bound appointment's office, Tax Pro, or time
Anchor: §2 State 5 workflow.reschedule_existing[3], [4]; scheduler_always changing-array item; §5.2 get_customer_appointments Response JSON
Severity: High
Class: Human
Issue: Step 4 says "Preserve unchanged constraints, call check_search_readiness", and the changing array compares 'office' (officeRef) and 'taxPro' (taxProRef) to the bound appointment. `get_customer_appointments` returns only officeName, taxProName, dateSpoken, and timeSpoken, with no officeRef, taxProRef, ISO date, or requestedTime. Readiness (which requires officeRef), the same_tax_pro_nearby_offices rung, and requestedTimeSource existing_appointment cannot be filled, and spoken fields may not be reformatted.
Proposed fix:
- A. (Recommended) Add officeRef, taxProRef (null when no Tax Pro), date, and requestedTime to each appointment in the Response JSON.
- B. Add only officeRef and taxProRef; drop requestedTimeSource existing_appointment.
- C. Add appointmentRef to the check_search_readiness request; the tool resolves bound constraints.

### D-02 · Unclear whether reschedule re-runs complexity screening
Anchor: §2 State 5 workflow.reschedule_existing[3]; scheduler_always gatekeeper, waterfall, and floor items
Severity: Medium
Class: Human
Issue: Step 4 uses "the higher of the computed floor and the bound appointment's taxProCertLevel", but the reschedule workflow never computes a floor. The gatekeeper item is unscoped, so a yes runs the waterfall and can raise the floor above the bound Tax Pro, emptying the same-Tax-Pro rungs.
Proposed fix: A. (Recommended) On reschedule_existing, take the baseline floor from find_customer silently, with no gatekeeper or waterfall. B. Screening runs as on a booking. C. Use taxProCertLevel alone.

### D-03 · Reschedule ladder when the bound appointment has no named Tax Pro
Anchor: §2 State 3 Ladders, Rescheduling row; broadening.ladders.reschedule.rungs[2], [3]; §2 State 3 Tax Pro Trade-off
Severity: Medium
Class: Human
Issue: Rung 3 is "The same Tax Pro at nearby offices" and rung 4's trade-off asks "Do you want to stay with [Name]". With a CDAS appointment (taxProName null), there is no Tax Pro to keep and no name to speak.
Proposed fix: A. (Recommended) With no named Tax Pro, rung 3 searches nearby offices for any qualified Tax Pro and rung 4 is skipped. B. Limit to rungs 1-2. C. Replace the trade-off with an office-only consent line (frozen text).

### D-04 · Repeated readiness needs_more or conflict has no cap
Anchor: §2 State 5 agent_specific_tools.check_search_readiness; §1.4 "conflict from readiness" row; §1.2 Input Exhaustion & Silence
Severity: Medium
Class: Human
Issue: The No-Match Rule counts only unrecognized input, so recognizable answers readiness keeps rejecting (repeated past dates, a repeated askFor) loop with no exit. D-048 and D-030 cap other results; readiness has no cap. Adjacent to L-146.
Proposed fix: A. (Recommended) A second consecutive needs_more for the same askFor item, or a second conflict, counts as a no-match; then transfer as clarification_exhausted. B. A second conflict transfers as validation_failed. C. MAX_INPUT_ATTEMPTS on every non-ready result, then system_failure.

### D-05 · office_contact has no step to resolve an office the caller names
Anchor: §3 Office Contact Triage first bullet; workflow.office_contact_flow[1]; §3 Office Details Logic (office_info path) > Named Office; office_always[2]
Severity: Medium
Class: Human
Issue: Named Office sits under the office_info path; office_contact only captures a ZIP if routedOfficeRef is null. A rollover caller asking for "the receptionist at the Oak Ridge office" (3B) gets the routed office, while "Routed Office: On either path, the office resolved from the caller's ZIP or name" assumes both paths resolve names.
Proposed fix: A. (Recommended) Add "or resolve a caller-named office per Named Office" to the triage bullet and office_contact_flow[1]. B. Drop "(office_info path)" from the heading and point from the flow.

### D-06 · Part 4 has no branch for find_customer multiple_matches
Anchor: §4 State 2 agent_specific_tools.transfer_to_agent; workflow.speak_to_tp_generic[3]; §4 Generic Request
Severity: Medium
Class: Human
Issue: Part 4 covers third-party or authentication failure and a first-party no_match (D-070). A first-party multiple_matches (shared household line) could follow the no_match path or the §1.4 multiple_matches transfer.
Proposed fix: A. (Recommended, +6 words) Transfer as identity_unresolved on find_customer multiple_matches; add a pointer to §1.4 in Generic Request. B. Treat it like a first-party no_match.

### D-07 · A change of subject keeps the carried Tax Pro, office, and type
Anchor: §2 State 5 invalidation.customer_identity; §2 State 1 Dynamic State Invalidation: Identity; §1.1 appointmentType, taxProRef, officeRef row
Severity: Medium
Class: Human
Issue: Invalidation preserves "the context_envelope except priorTransaction", and carried appointmentType, taxProRef, and officeRef skip their questions. A caller routed from Part 4 for their own Tax Pro's callback who switches to booking for a spouse keeps the first owner's callback type, Tax Pro, and office with no question asked.
Proposed fix: A. (Recommended) Also clear the carried customerRef, appointmentType, taxProRef, and officeRef on an identity change (JSON and prose). B. Keep them but confirm each after an identity change.
