# Round 7 · Lens E findings

Saved by the orchestrator from the reviewer's reply. Pairs touched by D-062 to D-065 and D-067 to D-071 checked clean.

### E-01 · Part 4 interruption handler has no exception for D-061's booking offer
Anchor: §4 State 2 interruptions.intent_change; §4 Out-of-Scope (Appointments) > Other booking with a confirmed Tax Pro; tax_pro_always other-booking item
Severity: Medium
Class: Safe
Issue: The prose says a non-callback booking with a confirmed Tax Pro gets the offer, "never intent_changed", and the callback item carries the exception. Part 4 `interruptions.intent_change` still hands back intent_changed with no exception. Same kind of gap as L-329.
Proposed fix: "Outside reaching a Tax Pro, other than a live-agent request, an identity-theft, fraud, or other-department question, or per the tax_pro_always other-booking item, hand back intent_changed."

### E-02 · After D-072, no example shows where contact.callbackNumber goes
Anchor: §5.2 book_appointment Note; scheduler_always new-customer contact item; §5.2 book_appointment Request JSON (New Customer)
Severity: Medium
Class: Human
Issue: Same as C-01. Options: A. Note says top-level contact.callbackNumber (+3 words). B. Add `contact` to the new-customer example (new key). C. Delete the field and use newCustomer.phoneNumber.

### E-03 · The D-070 no-match rule no longer names its recovery line
Anchor: §2 State 1 Authentication Logic > No Match Outside a New Booking; scheduler_always authentication-failure item
Severity: Low
Class: Safe
Issue: D-070 names the §1.4 "Authentication failed" line, but the bullet points only to "(see §1.4, Approved Recovery Lines)", leaving two plausible rows.
Proposed fix: "... a no_match transfers as identity_unresolved with the Authentication failed line (see §1.4, Approved Recovery Lines)."

### E-04 · Part 1 message-offer triggers leave out closed_for_season
Anchor: §1.3 Leave-a-Message Ownership third bullet; §1.5 global_always leave-message item
Severity: Low
Class: Safe on the merits; oscillation guard likely
Issue: Same as B-04.

### E-05 · The carried-customerRef JSON item also requires customerStatus
Anchor: scheduler_always carried-context item; §2 State 1 State Persistence; §1.1 customerRef
Severity: Low
Class: Safe
Issue: The prose and D-071 key the skip on customerRef alone; the JSON says "If customerRef and customerStatus arrive in the context_envelope".
Proposed fix: "If customerRef arrives in the context_envelope," (-2 words).
