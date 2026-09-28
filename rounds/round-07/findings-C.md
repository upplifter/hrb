# Round 7 · Lens C findings

Saved by the orchestrator from the reviewer's reply.

### C-01 · `contact.callbackNumber` is required but no request schema has it
Anchor: §2 State 5 scheduler_always new-customer contact item; §5.2 book_appointment Note, first bullet
Severity: Medium
Class: Human
Issue: `scheduler_always` says "include contact.callbackNumber for phone callbacks" and the Note says "New-customer contact.callbackNumber is required on phone callbacks." After D-072 removed `contact` from the existing-customer example, no request JSON contains `contact`. `newCustomer.phoneNumber` is also captured "regardless of method", so the implementer must guess placement and whether the two numbers differ.
Proposed fix:
- A. (Recommended, -8 words) `newCustomer.phoneNumber` is the callback number; drop `contact.callbackNumber` (removes a field).
- B. (+3 words) Note: "On a new-customer phone callback, send top-level contact.callbackNumber."
- C. As B, and add `contact` to a phone_callback new-customer example (new JSON key).

### C-02 · Part 4 JSON uses `no_match` for three different things
Anchor: §4 State 2 tax_pro_always by-name item and unavailable item
Severity: Medium
Class: Safe
Issue: The by-name item calls a caller correction and an unresolved location answer "no_match". The unavailable item says "If the Tax Pro is unmatched ... say so" but "with ... a first-party no_match, skip the unavailable line", so a first-party by-name no_match must both speak and skip the line. Prose (§4 Generic Request; By Name > No Matches / Inactive) scopes the skip to find_customer.
Proposed fix: By-name item "is no_match" -> "is unmatched" (twice); unavailable item "a first-party no_match" -> "a find_customer no_match".

### C-03 · `validation_failed` definition also covers results the decisions send to system_failure
Anchor: §1.5 global_outcomes.validation_failed
Severity: Medium
Class: Safe
Issue: "A tool rejects an uncorrectable request with a result other than rejected, change_not_allowed, or not_cancelable." A second invalid_constraints (D-048) and a second delivery_failed (D-001) transfer as system_failure, so the payload could carry either transferReason.
Proposed fix: Add "invalid_constraints, or delivery_failed" to the exception list.

### C-04 · Part 3 CLOSED branch names no finalOutcome
Anchor: §3 Office Contact Triage > If CLOSED; §3 State 2 office_always CLOSED item
Severity: Low
Class: Safe
Issue: Every other office_contact branch names its outcome; CLOSED says only "return nextAction = leave_message_offer".
Proposed fix: Return office_contact_triage_complete (nextAction = leave_message_offer) in prose and JSON.

### C-05 · "Work Center message" is a second, undefined term for the caller's message
Anchor: §1.5 global_never message item
Severity: Low
Class: Safe
Issue: The term appears only here; §1.3 says "a caller's message".
Proposed fix: "confirm delivery of a Work Center message" -> "confirm delivery of a caller's message".

### C-06 · `textConfirmation` channel `email` is defined but nothing captures an email
Anchor: §2 State 5 scheduler_always textConfirmation item; §2 State 4 Optional Text Confirmation
Severity: Low
Class: Human
Issue: `textConfirmation` defines "channel (sms or email)", but every rule captures only a phone number.
Proposed fix: A. channel sms only. B. Add an email-confirmation rule (decision).

No other new Medium-or-higher lens C issues. Seen and not re-raised: L-162, L-168, L-169, L-197, L-198, L-355, L-356, L-383 to L-385.
