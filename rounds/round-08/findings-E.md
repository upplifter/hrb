# Round 8 · Lens E findings

Saved by the orchestrator from the reviewer's reply.

### E-01 · book_appointment existing-customer example sends a phone_callback with no reason
Anchor: §5.2 book_appointment > Request JSON (Existing Customer) `appointmentMethod`, `appointmentNotes`
Severity: Medium
Class: Safe
Issue: D-083 requires the one-phrase reason in `appointmentNotes` on every phone_callback. The existing-customer example, whose null `appointmentNotes` D-072 fixed, is a tax_prep booking with `appointmentMethod` "phone_callback" and `appointmentNotes` null, so it breaks `scheduler_always` "On any phone_callback, capture the reason..." Changing the method keeps D-072's null and satisfies D-083. Filling in a reason instead would reverse D-072's named text.
Fix: Old: "\"appointmentMethod\": \"phone_callback\",\n    \"taxNoticeDetails\": null,\n    \"appointmentNotes\": null,\n    \"textConfirmation\"" New: "\"appointmentMethod\": \"in_person\",\n    \"taxNoticeDetails\": null,\n    \"appointmentNotes\": null,\n    \"textConfirmation\""

### E-02 · Prose limits the callback reason capture to the callback type
Anchor: §2 State 2 Appointment Type Rules table, callback row, Required Captures & Rules cell; `scheduler_always` phone_callback item
Severity: Low
Class: Safe
Issue: D-083 made the JSON read "On any phone_callback, capture the reason", and the §5.2 Note reads "null except on a phone_callback". The prose states the capture only in the callback type row, and After Part 4 points to that row. That leaves out a tax_prep appointment the caller books by phone and the tax_notice `phone_callback` rung. The edit reorders the cell so "Skip complexity screening" stays scoped to the callback type.
Fix: Old: "15-minute CDAS callback. Capture the reason for the call as one short phrase in appointmentNotes. Skip complexity screening. Send taxProRatingFloor = 1." New: "15-minute CDAS callback. Skip complexity screening. Send taxProRatingFloor = 1. On any phone_callback, of any type, capture the reason for the call as one short phrase in appointmentNotes."

Summary: 2 findings (1 Medium, 1 Low).
