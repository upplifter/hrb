# Round 8 · Lens F findings

Saved by the orchestrator from the reviewer's reply.

### F-01 · Callback reason rule covers only the callback type in prose
Anchor: §2 State 2 Appointment Type Rules (Eligibility bullet; After Part 4 first sub-bullet; type table callback row); scheduler_always phone_callback item
Severity: Medium
Class: Safe
Issue: D-083 requires the one-phrase reason on any phone_callback. The JSON says so, but the prose only says it on the callback row and in After Part 4 ("as on callback"). A tax_prep booking with the Phone method has no reason rule in prose, and prose outranks the JSON under C-1. This moves the rule to one general bullet. Net -1 word. After Part 4 has been edited in rounds 5-7, so the orchestrator may apply the oscillation guard.
Fix: (Safe)
Old: "- **Eligibility:** Gates office selection via acceptsAppointmentType."
New: "- **Eligibility:** Gates office selection via acceptsAppointmentType.
- **Callback Reason:** On any phone_callback, capture the reason for the call as one short phrase in appointmentNotes."
Old: "    - Book a callback request as a tax_prep phone_callback appointment, with the reason as on callback. Never hand it back."
New: "    - Book a callback request as a tax_prep phone_callback appointment. Never hand it back."
Old: "| callback | phone_callback | 15-minute CDAS callback. Capture the reason for the call as one short phrase in appointmentNotes. Skip complexity screening. Send taxProRatingFloor = 1. |"
New: "| callback | phone_callback | 15-minute CDAS callback. Skip complexity screening. Send taxProRatingFloor = 1. |"

### F-02 · book_appointment example sends a phone_callback with null appointmentNotes
Anchor: §5.2 book_appointment > Request JSON (Existing Customer) appointmentMethod, appointmentNotes; Note "appointmentNotes is null except on a phone_callback"
Severity: Medium
Class: Human
Issue: D-072 set this example's appointmentNotes to null while its appointmentMethod was phone_callback. After D-083, a phone_callback must carry the reason, so the example breaks the Note right below it. An implementer cannot tell whether the reason is optional on a tax_prep phone callback. Two fixes are valid, so this needs a choice.
Fix: Options:
A. Change `"appointmentMethod": "phone_callback"` to `"appointmentMethod": "in_person"` in the existing-customer example. This keeps D-072's null and matches the in-person confirmedSummary and the transfer_to_agent example. (Recommended: smallest edit)
B. Keep phone_callback and set `"appointmentNotes": "question about last year's return"`.
Footprint: A ≈ 1 edit, 0 words. B ≈ 1 edit, +5 words.

### F-03 · A readiness conflict that is neither a past date nor a closed window has no handling
Anchor: §2 State 5 agent_specific_tools.check_search_readiness; §2 State 3 Readiness & Availability; §5.2 check_search_readiness Outcome Results conflict row
Severity: Medium
Class: Human
Issue: After D-078, the tool entry covers only a past date (speak the line) and a closed window (follow the type item). §5.2 also defines conflict as "Constraints conflict", which now has no response. The Readiness Cap counts a second consecutive conflict but gives no first response. This is outside lens F, but D-078 left the gap.
Fix: Options:
A. Append to the check_search_readiness entry: "On any other conflict, ask once for a different date or time; the Readiness Cap applies." Add the same clause to the §2 Readiness Cap bullet. (Recommended: smallest edit)
B. Any other conflict transfers as validation_failed. This needs a matching edit to global_outcomes.validation_failed.
C. Narrow the §5.2 conflict meaning to "the date has passed or the type's window is closed". This changes the tool contract.
Footprint: A ≈ 2 edits, +22 words. B ≈ 2 edits, +12 words. C ≈ 1 edit, +6 words.

### F-04 · workflow.schedule_new[1] is over the 60-word JSON limit
Anchor: §2 State 5 workflow.schedule_new[1]
Severity: Low
Class: Human
Issue: Lint counts 62 words, over the 60-word JSON item limit in editorial rule 1. The anchor was edited in rounds 1 and 3-6, so the oscillation guard applies. The trim keeps every trigger. Only a client with a prior Tax Pro can have an active one, so "a returning client's" adds no condition.
Fix: Options:
A. Old: "2 Type, method, location. Each carried value skips only its own question. Establish the type, then ask (never infer) the method it permits and send appointmentMethod. If a returning client's prior Tax Pro is active, ask whether to keep them; yes selects returning_same_tax_pro at the last-served office; rejecting that office moves to the same_tax_pro_nearby_offices rung; otherwise resolve the office by entryPoint." New: "2 Type, method, location. Each carried value skips only its own question. Establish the type, then ask, never infer, its permitted method and send appointmentMethod. If the prior Tax Pro is active, ask whether to keep them; yes selects returning_same_tax_pro at the last-served office; rejecting that office moves to the same_tax_pro_nearby_offices rung; otherwise resolve the office by entryPoint." (Recommended)
B. Leave it as is and log it under the L-034 string-to-array restructure.
Footprint: A ≈ 1 edit, -3 words. B ≈ 0 edits.

Summary: 4 findings (0 Critical, 0 High, 3 Medium, 1 Low).
