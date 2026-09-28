# Round 8 · Lens B findings

Saved by the orchestrator from the reviewer's reply.

### B-01 · After Part 4, the Scheduler still offers to keep the prior Tax Pro, but D-081 refuses a request for that same Tax Pro
Anchor: §2 State 2 Appointment Type Rules > After Part 4; scheduler_always routed_to_scheduler item; workflow.schedule_new[1] ("If a returning client's prior Tax Pro is active, ask whether to keep them")
Severity: Medium
Class: Human
Issue: D-050 says that after a Part 4 `routed_to_scheduler` the Scheduler still asks whether to keep the prior Tax Pro. D-081 says a request for the caller's own Tax Pro gets "this booking is with another Tax Pro" and a second request returns `customer_declined_options`. Take a caller whose active prior Tax Pro was confirmed in Part 4 and who chose "another qualified Tax Pro" under D-061. The Scheduler's step 2 asks "keep Sarah?". If the caller says yes, one rule selects returning_same_tax_pro and the other refuses the request, so the implementer has to guess which applies.
Fix: Options: A. After Part 4, skip the keep-prior-Tax-Pro question and select by scenario_selection items 9 and 10. Add one clause to the After Part 4 bullet and to the scheduler_always routed_to_scheduler item: "Skip the keep-prior-Tax-Pro question." (Recommended, smallest edit.) B. Keep the question. A yes selects returning_same_tax_pro, and D-081 applies only to a Tax Pro the Scheduler did not offer. Edit the same two places. C. Ask the question only when the prior Tax Pro is not the one Part 4 confirmed. This needs the confirmed taxProRef carried on the handoff. Footprint: A = 2 edits, about +12 words. B = 2 edits, about +20 words. C = 3 or 4 edits, about +25 words, and it touches the handoff fields.

### B-02 · Part 1 carries taxProRef on every handoff to appointment_scheduler, including Part 4's "another Tax Pro" handoff
Anchor: §1.5 terminal_payload_contract ("taxProRef and officeRef when handing off to leave a message or to appointment_scheduler"); §4 agent_specific_outcomes.routed_to_scheduler; §1.1 appointmentType, taxProRef, officeRef row
Severity: Medium
Class: Human
Issue: The Part 1 contract includes taxProRef on any handoff to appointment_scheduler. Part 4's another-Tax-Pro `routed_to_scheduler` says only "with officeRef only when known". If the declined or inactive Tax Pro's taxProRef is carried, §1.1 makes it skip its question and outrank everything else, so the Scheduler books with the Tax Pro the caller moved away from. That breaks D-061 and D-081. Part 1 wins under C-1, and the Part 4 wording supports either reading.
Fix: Options: A. In terminal_payload_contract, change "to appointment_scheduler" to "to appointment_scheduler for a callback". (Recommended, smallest edit.) B. Add "no taxProRef" to routed_to_scheduler's another-Tax-Pro clause and leave the contract as it is. Footprint: A = 1 edit, +3 words. B = 1 edit, +3 words, but Part 1 keeps the wider rule.

### B-03 · Part 1's confirm-at-capture rule reaches the callback reason that D-083 extends to every phone_callback
Anchor: §1.2 Confirmation Strategy > Confirmed at capture; §1.5 global_always confirm-at-capture item; scheduler_always "On any phone_callback, capture the reason" item
Severity: Medium
Class: Human
Issue: global_always says to "Confirm at capture any dictated value that cannot be checked against a tool result and will not be spoken later." The appointmentNotes reason matches that test: it is dictated, no tool can check it, and the pre-commit gate never reads it back. D-083 extends the reason capture to every phone_callback. The spec never says whether the reason is read back, so the implementer has to guess, and the answer changes what the caller hears.
Fix: Options: A. Exempt the reason. In the global_always item, change "Date of birth and ssnLast4 are exempt." to "Date of birth, ssnLast4, and a phone_callback reason are exempt." Mirror the change in the §1.2 Exceptions bullet. (Recommended, smallest edit.) B. Read the reason back at capture. Add "Confirm it at capture." to the scheduler_always phone_callback item and the callback row. Footprint: A = 2 edits, about +6 words. B = 2 edits, about +8 words, and each phone_callback booking gets one more turn.

### B-04 · The global_always empathy item allows recovery lines that promise a person as free acknowledgments
Anchor: §1.5 global_always empathy item; global_voice_lexicon.empathy (lines added by D-076 and the untagged recovery lines); global_always transfer item ("always before promising a person")
Severity: Medium
Class: Human
Issue: The empathy item says to acknowledge "in one clause with global_voice_lexicon.empathy when the moment calls for it, and add no facts". After D-076 the empathy list holds 20 lines, and most are path-bound recovery lines of two sentences. Several promise a person with no path tag (e.g., "Let me get you to a person rather than have you start over."). This conflicts with the Part 1 rule to call `transfer_to_agent` before any promise of a person and to speak a path's line only on that path.
Fix: Options: A. In the empathy item, change "with global_voice_lexicon.empathy when the moment calls for it, and add no facts." to "with a global_voice_lexicon.empathy line that promises no person when the moment calls for it, and add no facts. Speak every other empathy line only on its own path." (Recommended, smallest edit; the frozen lexicon is unchanged.) B. Limit free acknowledgment to the first three empathy lines by quoting them in the item. Footprint: A = 1 edit, about +16 words. B = 1 edit, about +25 words.

### B-05 · The "except After Part 4" clause switches off the whole Tax Pro Requests rule, but D-081 covers only two Tax Pros
Anchor: §2 State 2 Appointment Type Rules > Tax Pro Requests; interruptions.intent_change
Severity: Medium
Class: Safe
Issue: The prose exception "except After Part 4" removes the whole Tax Pro Requests rule after a Part 4 handoff. After Part 4 (D-081) covers only a callback request, the caller's own Tax Pro, and the Tax Pro named in Part 4. That leaves a request for a third named Tax Pro with no rule. The JSON reads the exception narrowly ("except per the scheduler_always routed_to_scheduler item"), which matches D-081's scope.
Fix: Old: "A request for a specific or own Tax Pro, a named Tax Pro neither prior nor carried, or a callback with no carried taxProRef returns intent_changed to speak_to_tax_pro, except After Part 4." New: "A request for a specific or own Tax Pro, a named Tax Pro neither prior nor carried, or a callback with no carried taxProRef returns intent_changed to speak_to_tax_pro, except a request After Part 4 covers."

### B-06 · The prose still limits the callback reason to the callback type after D-083
Anchor: §2 State 2 Appointment Type Rules table, callback row; scheduler_always phone_callback item; §5.2 book_appointment Note
Severity: Low
Class: Safe
Issue: D-083 captures the reason on any phone_callback (e.g., a tax_prep, tax_extension, or tax_notice_service phone appointment), and the JSON and §5.2 already say so. The prose states the capture only in the callback row and the After Part 4 bullet. Under C-2 the prose should mirror the JSON.
Fix: Old: "Capture the reason for the call as one short phrase in appointmentNotes. Skip complexity screening." New: "On any phone_callback, capture the reason for the call as one short phrase in appointmentNotes. Skip complexity screening."

Summary: 6 findings (4 Medium, 1 Medium Safe counted in Medium, 1 Low; by severity: 0 Critical, 0 High, 5 Medium, 1 Low).
