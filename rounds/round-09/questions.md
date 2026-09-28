# Round 9 questions

Write a letter, your own text, "defer", or "not an issue" after each `Answer:`. Then run `/continue`.
Round 9 of 10 under C-12. These 6 questions cover every new Medium-or-higher Human item from round 9 (L-438 to L-444), including one High. Most come from gaps the round 8 decisions left open.

### Q-96 · Reschedule floor for types with a fixed floor (resolves L-438, High)
Conflict: `workflow.reschedule_existing[3]` (D-095) sends the higher of the inherited baseline and the bound appointment's taxProCertLevel on every reschedule. `scheduler_always`, the §2 type table, and §5.2 Callbacks send floor 1 on emerald_advance, tax_notice_service, and callback, and null on Physical Drop-Off, with no operation limit. A callback reschedule for a complexity-4 client gets 4 under one rule and 1 under the other.
Options:
  A. The type floor stands on a reschedule. Step 4: "the higher of the inherited baseline floor (1 on emerald_advance, tax_notice_service, and callback; null on physical_drop_off), taken silently"; §2 Reschedule bullet adds "except where the type table sets the floor". (Recommended: keeps pre-D-095 behavior)
  B. The inherited baseline applies to every reschedule. Scope the fixed-floor item, the type-table rows, and §5.2 Callbacks to schedule_new.
Footprint: A ≈ 2 edits, +18 words. B ≈ 3 to 5 edits, +10 words, and fewer Tax Pros qualify on these reschedules.
Answer:

### Q-97 · Which handoffs carry officeRef (resolves L-439)
Conflict: D-085 wrote "taxProRef when handing off to leave a message or to appointment_scheduler for a callback, and officeRef on either handoff" into `terminal_payload_contract`. Literally, "either" names only the message and callback handoffs, but §4 `routed_to_scheduler` also carries officeRef on the another-Tax-Pro handoff (D-040). Part 1 wins under C-1.
Options:
  A. "... and officeRef, when known, on a message handoff or any routed_to_scheduler." (Recommended: matches D-040 and the round 8 intent)
  B. "... and officeRef on a message handoff or any handoff to appointment_scheduler." Adds carrying on Part 3 and post-commit intent_changed handoffs, which then skip the office question.
Footprint: A ≈ 1 edit, +7 words. B ≈ 1 edit, +6 words.
Answer:

### Q-98 · After Part 4, a Tax Pro named by the caller (resolves L-440)
Conflict: After a Part 4 routed_to_scheduler, the caller's own or the Part 4-named Tax Pro gets the D-081 statement, and any other named Tax Pro hands back to speak_to_tax_pro. After D-085 the another-Tax-Pro handoff carries no taxProRef, so the Scheduler cannot tell which Tax Pro Part 4 named. A wrong handback loops the caller back to Part 4.
Options:
  A. After Part 4, treat any named Tax Pro like the caller's own: one statement that this booking is with another Tax Pro, then booking continues. Edit the After Part 4 sub-bullet and the scheduler_always routed_to_scheduler item. (Recommended: smallest edit, -4 words)
  B. Carry the Part 4-named taxProRef on the another-Tax-Pro handoff for recognition only, never as a booking constraint. Partly reverses D-085.
Footprint: A ≈ 2 edits, -4 words; changes what the caller hears for a third named Tax Pro. B ≈ 4 edits, +20 words.
Answer:

### Q-99 · Switching whose appointment it is (resolves L-441)
Conflict: D-092 clears the carried customerRef, appointmentType, taxProRef, and officeRef on an identity change (name, DOB, or last 4 SSN). With a carried customerRef the identity questions are skipped, so when the caller switches to a spouse's appointment, the spouse's details are a first capture, not a change. It is unclear whether the switch clears the carried values.
Options:
  A. Add the transaction subject to the trigger. Prose: "..., Last 4 SSN, or the transaction subject." JSON: "A change to any one, or to transactionSubject, wipes STATE.* completely". (Recommended)
  B. On a subject change, clear only priorTransaction and the four carried values, and keep the rest of STATE.
Footprint: A ≈ 2 edits, +8 words; the caller is asked the type again after a switch. B ≈ 2 edits, +30 words.
Answer:

### Q-100 · A rejected Tax Pro comes back (resolves L-442, L-443)
Conflict: Under D-090, rejecting the proposed prior Tax Pro while keeping the office re-selects returning_tax_pro_unavailable. The "keep" choice from schedule_new[1] is never cleared, so the next caller-initiated change re-selects returning_same_tax_pro and offers the same Tax Pro again. Separately, find_available_slots has no way to exclude a Tax Pro, and scheduler_never forbids filtering, so the widened search can return the rejected Tax Pro's other times.
Options:
  A. A rejection lasts for the call. partial_acceptance adds "and records the prior Tax Pro as not kept; never offer that Tax Pro again"; scheduler_never allows skipping slots with a Tax Pro rejected per partial_acceptance. (Recommended)
  B. As A, but instead of skipping slots, add a request field `excludeTaxProRefs` to find_available_slots and send the rejected taxProRef (new field, C-7).
  C. A rejection holds only until the next caller-initiated change; no filtering.
Footprint: A ≈ 2 edits, +26 words. B ≈ 3 edits, +18 words plus a field. C ≈ 1 edit, +6 words.
Answer:

### Q-101 · "Request to speak to" in Tax Pro Requests (resolves L-444)
Conflict: L-252 (round 4) set the Tax Pro Requests rule to "A request to speak to a specific or own Tax Pro", keeping D-034's split between asking for a person and booking with them. The round 7 decided edit (for D-081) dropped "to speak to" in prose and JSON with no decision naming it. Now a returning client who wants to book with their own Tax Pro matches both this handback and scenario_selection item 8. The anchor has been edited in 3 earlier rounds, so the guard sends this to you.
Options:
  A. Restore "to speak to" in the prose bullet and in interruptions.intent_change. (Recommended: restores L-252)
  B. Keep the current wording; a booking request for the own Tax Pro hands back to speak_to_tax_pro.
Footprint: A ≈ 2 edits, +6 words. B ≈ 0 edits; changes what a returning caller experiences.
Answer:
