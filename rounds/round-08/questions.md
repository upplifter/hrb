# Round 8 questions

Write a letter, your own text, "defer", or "not an issue" after each `Answer:`. Then run `/continue`.
Round 8 is the last round under C-12. These 12 questions cover the 7 new round 8 Mediums and 6 of the 10 items carried from round 7. The last 4 carried items are listed at the end. Answer them inline as "L-xxx: A", or leave them open in `rounds/FINAL.md`.

### Q-84 · Keep-prior-Tax-Pro question after Part 4 (resolves L-418)
Conflict: `workflow.schedule_new[1]` asks a returning client whether to keep an active prior Tax Pro, and D-050 keeps that question after a Part 4 routed_to_scheduler. D-081 now answers a request for the caller's own Tax Pro after Part 4 with "this booking is with another Tax Pro". A yes to the question selects returning_same_tax_pro, which D-081 then refuses.
Options:
  A. After a Part 4 routed_to_scheduler, skip the keep-prior question and select by scenario_selection; supersedes the D-050 "still asks" clause. (Recommended: smallest edit)
  B. Keep the question; a yes books with the prior Tax Pro, and D-081 applies only to the Tax Pro named in Part 4 when that is not the prior one.
Footprint: A ≈ 2 edits, +12 words. B ≈ 3 edits, +20 words.
Answer: A

### Q-85 · taxProRef on Part 4's "another Tax Pro" handoff (resolves L-419)
Conflict: `terminal_payload_contract` carries taxProRef "when handing off ... to appointment_scheduler", with no exception. §4 `routed_to_scheduler` for another Tax Pro names only officeRef. A carried taxProRef skips the Tax Pro question in the Scheduler, so the booking could go to the Tax Pro the caller moved away from.
Options:
  A. Contract: "to appointment_scheduler" becomes "to appointment_scheduler for a callback". (Recommended: Part 1 wins under C-1)
  B. Add "no taxProRef" to the §4 routed_to_scheduler another-Tax-Pro clause only.
Footprint: A ≈ 1 edit, +3 words. B ≈ 1 edit, +3 words.
Answer: A 

### Q-86 · What is confirmed at capture (resolves L-420, L-401)
Conflict: The `global_always` confirm-at-capture item covers "any dictated value that cannot be checked against a tool result and will not be spoken later". That test catches the phone_callback reason (D-083), but the spec never says whether the reason is read back. The same item also drops §1.2's "plus the third-party owner's name". Only `scheduler_always` restores that, and Part 4 never confirms the name.
Options:
  A. In global_always and §1.2, exempt the phone_callback reason, and add "and a third-party owner's name" to the confirmed values; delete "Confirm the name at capture." from scheduler_always (C-3 A). (Recommended)
  B. Read the reason back at capture; third-party name as in A.
  C. Exempt the reason; scope the third-party name readback to the Scheduler (§1.2 edit).
Footprint: A ≈ 3 edits, +8 words. B ≈ 4 edits, +12 words. C ≈ 3 edits, 0 words.
Answer: A

### Q-87 · Which empathy lines are free acknowledgments (resolves L-421)
Conflict: The `global_always` empathy item lets the agent acknowledge "with global_voice_lexicon.empathy when the moment calls for it". After D-076 that list holds 20 lines, most of them path-bound recovery lines that promise a person. The item therefore permits "Let me get you to a person..." before `transfer_to_agent`, which D-014 forbids.
Options:
  A. Edit only the global_always item: acknowledge with an empathy line that promises no person, and speak every other empathy line only on its own path. (Recommended: no frozen text)
  B. Move the path-bound lines into a new `recovery_lines` lexicon key and repoint the references (new key, frozen edit).
Footprint: A ≈ 1 edit, +16 words. B ≈ 5 edits, +5 words, 1 new key.
Answer: A

### Q-88 · efile entry and an inactive prior Tax Pro (resolves L-422)
Conflict: The `scheduler_always` efile_rejection_retail item proposes "the prior Tax Pro returned by find_customer where there is one". find_customer returns the name even when priorTaxProStatus is inactive, and scenario_selection then picks returning_tax_pro_unavailable, which never searches that Tax Pro.
Options:
  A. "where there is one" becomes "when priorTaxProStatus is active". (Recommended)
  B. Keep the proposal; on an inactive prior Tax Pro, state once they are unavailable, then follow workflow.schedule_new.
Footprint: A ≈ 1 edit, +3 words. B ≈ 1 edit, +14 words.
Answer: A

### Q-89 · Readiness conflicts that are neither a past date nor a closed window (resolves L-423)
Conflict: After D-078, a readiness conflict speaks the past-date line for a past date, and a closed window follows the tax_extension or emerald_advance item. §5.2 defines conflict more widely ("Constraints conflict"), and a closed window on another type has no row. The first response to any other conflict is undefined; only the second is capped.
Options:
  A. On any other conflict, ask once for a different date or time; the Readiness Cap applies. (Recommended)
  B. On any other conflict, transfer as system_failure.
  C. Narrow the §5.2 conflict meaning to "the date has passed or the type's window is closed" (tool contract change).
Footprint: A ≈ 2 edits, +20 words. B ≈ 2 edits, +10 words. C ≈ 1 edit, +6 words.
Answer: A

### Q-90 · Scenario and rung after a partial rejection (resolves L-424)
Conflict: After D-074, rejecting a proposed Tax Pro while keeping the office widens to eligible Tax Pros without the trade-off. find_available_slots needs a scenario and rung. returning_same_tax_pro and reschedule reach "any qualified Tax Pro" only at their last rung, so it is unclear whether to re-select the scenario or jump rungs.
Options:
  A. Treat the rejection as a caller-initiated constraint change under invalidation.ladder_state: returning_same_tax_pro re-selects returning_tax_pro_unavailable at that office; other scenarios restart at their primary offer. (Recommended)
  B. Send rung any_qualified_tax_pro in the current scenario and mark earlier rungs skipped.
Footprint: A ≈ 1 edit, +12 words. B ≈ 2 edits, +15 words.
Answer: A

### Q-91 · Part 4 and find_customer multiple_matches (resolves L-398)
Conflict: Part 4 covers third-party or authentication failure and a first-party no_match (D-070). A first-party multiple_matches (e.g., a shared household line) could follow either the no_match path or the §1.4 multiple_matches transfer.
Options:
  A. Transfer as identity_unresolved with the §1.4 multiple_matches line; add a pointer in §4 Generic Request. (Recommended)
  B. Treat it like a first-party no_match (offer only the Scheduler).
Footprint: A ≈ 2 edits, +6 words. B ≈ 2 edits, +6 words.
Answer: A

### Q-92 · Carried values after a change of subject (resolves L-399)
Conflict: `invalidation.customer_identity` preserves "the context_envelope except priorTransaction", and a carried appointmentType, taxProRef, or officeRef skips its question. A caller routed from Part 4 for their own Tax Pro's callback who switches to booking for a spouse keeps the first owner's type, Tax Pro, and office, and is asked nothing.
Options:
  A. On an identity change, also clear the carried customerRef, appointmentType, taxProRef, and officeRef (JSON and prose). (Recommended)
  B. Keep them, but confirm each one after an identity change.
Footprint: A ≈ 2 edits, +10 words. B ≈ 2 edits, +15 words.
Answer: A

### Q-93 · contact.callbackNumber has no schema (resolves L-404)
Conflict: `scheduler_always` and the §5.2 book_appointment Note require "contact.callbackNumber" on a new-customer phone callback, but no request JSON has `contact`. `newCustomer.phoneNumber` is also captured regardless of method, so the implementer has to guess whether these are two numbers.
Options:
  A. newCustomer.phoneNumber is the callback number; drop contact.callbackNumber (removes a field). (Recommended)
  B. Keep it; the Note says "send top-level contact.callbackNumber".
  C. As B, and add `contact` to a new-customer phone_callback example (new JSON key).
Footprint: A ≈ 2 edits, -8 words. B ≈ 1 edit, +3 words. C ≈ 2 edits, +1 key.
Answer: A

### Q-94 · office_contact and a caller-named office (resolves L-397)
Conflict: Named Office sits under the office_info path. office_contact captures a ZIP only when routedOfficeRef is null. A rollover caller asking for "the receptionist at the Oak Ridge office" (3B) therefore gets the routed office, even though "Routed Office: On either path, the office resolved from the caller's ZIP or name" assumes both paths resolve names.
Options:
  A. Add "or resolve a caller-named office per Named Office" to the §3 triage bullet and office_contact_flow[1]. (Recommended)
  B. Drop "(office_info path)" from the Office Details Logic heading and point to it from the flow.
Footprint: A ≈ 2 edits, +16 words. B ≈ 2 edits, +6 words.
Answer: A

### Q-95 · Complexity screening on a reschedule (resolves L-395)
Conflict: `workflow.reschedule_existing[3]` sends "the higher of the computed floor and the bound appointment's taxProCertLevel", but the reschedule workflow never computes a floor. The gatekeeper item has no scope, so a yes runs the waterfall and can raise the floor above the bound Tax Pro, which empties the same-Tax-Pro rungs.
Options:
  A. On reschedule_existing, take the baseline floor from find_customer silently, with no gatekeeper or waterfall. (Recommended)
  B. Screening runs as it does on a new booking.
  C. Use taxProCertLevel alone.
Footprint: A ≈ 2 edits, +12 words. B ≈ 1 edit, +6 words. C ≈ 1 edit, -6 words.
Answer: A

## Still open (no question slot left)

Answer inline as "L-xxx: A" if you want them settled. Otherwise they stay open in `rounds/FINAL.md`.

- **L-396 · Reschedule ladder with no named Tax Pro.** Rung 3 "same Tax Pro at nearby offices" and the rung 4 trade-off have no Tax Pro when the bound appointment is CDAS. A (Recommended): with no named Tax Pro, rung 3 searches nearby offices for any qualified Tax Pro and rung 4 is skipped. B: rungs 1-2 only.
  Answer: A
- **L-400 · Logistics questions outside a task.** Parts 3 and 4 both claim them, and the Scheduler has no path. A (Recommended): send them to faq_agent in every agent (4 edits, +25 words). B: the Scheduler owns them and returns appointment_details_provided (5 edits, +35 words).
  Answer: A
- **L-402 · outcome_unknown line on cancel and secure-link writes.** The frozen line speaks of "that time" and double-booking. A (Recommended): reword both frozen copies to "confirming that on my end ... so nothing gets done twice". B: speak the system_failure line on cancel and secure-link. C: no change.
  Answer: A
- **L-403 · "method_descriptions only" versus readbacks.** scheduler_never limits method wording to the method_descriptions lexicon, but gate readbacks and 4A/4B say "an in-person appointment". A (Recommended): "When offering or explaining a method, use global_voice_lexicon.method_descriptions." B: add a meetingMethodSpoken readback rule and edit 4A/4B. C: no change.
  Answer: A
