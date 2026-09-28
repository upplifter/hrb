# Round 6 questions

Write a letter, your own text, "defer", or "not an issue" after each `Answer:`. Then run `/continue`.
These 12 questions cover the 9 new Human Mediums from round 6 and the 8 highest-impact carried items. Eight more questions on older carried items (L-074, L-075, L-080, L-089, L-136, L-140, L-146, L-162, L-164) have drafted options in `findings-R.md` and go into round 7. To finish sooner, you may answer any of them now as "L-xxx: A".

### Q-60 · Booking with a named Tax Pro who is not the caller's own (resolves L-369)
Conflict: The Scheduler hands a named, non-prior, non-carried Tax Pro to speak_to_tax_pro (§2 State 2 Tax Pro Requests). Part 4 sends any non-callback booking back to appointment_scheduler (tax_pro_always callback item) without saying to carry taxProRef. Without taxProRef the caller loops. With it, scenario_selection honors only a prior Tax Pro (item 8), so the Tax Pro is silently dropped.
Options:
  A. Part 4 states once that it can book only a callback with that Tax Pro. It offers the callback, the message, or another qualified Tax Pro (routed_to_scheduler, appointmentType null) and never returns intent_changed for this request. (Recommended: no new scenario)
  B. Part 4 carries taxProRef and officeRef on the handback. The Scheduler treats a carried non-prior taxProRef like returning_same_tax_pro at the carried office.
  C. The Scheduler asks once whether any qualified Tax Pro is fine. A no returns customer_declined_options, and the request is never handed back.
Footprint: A ≈ 3 edits, net +25 words. B ≈ 4 edits, net +35 words. C ≈ 3 edits, net +20 words.
Answer:

### Q-61 · By-appointment-only office (resolves L-081, L-370)
Conflict: §3 By-Appointment-Only returns nextAction route_intent to appointment_scheduler, but no Part 3 outcome carries route_intent, and in 3D the caller never asked to book. office_contact_flow[1] applies the same rule, so a caller who wants the receptionist or a message is sent to booking.
Options:
  A. On office_info, return intent_changed with routingTarget appointment_scheduler. On office_contact, state that the office is appointment-only and continue to `check_office_open_status`. (Recommended)
  B. On office_info, return office_info_provided with no route. On office_contact, return office_contact_triage_complete with nextAction leave_message_offer, as D-053 does for closed_for_season.
  C. Other: ___
Footprint: A ≈ 4 edits (incl. 3D System line), net +15 words. B ≈ 4 edits, net +10 words.
Answer:

### Q-62 · Ladder after a rejected last-served office (resolves L-371)
Conflict: After the caller rejects the last-served office, D-048 moves to same_tax_pro_nearby_offices (rung 3). Rung 5, "any_qualified_tax_pro at that office", then offers the rejected office again. §2 State 3 Declined Offices also returns customer_declined_options once every proposed office is declined, while the ladder says to move on to rung 4.
Options:
  A. After a rejected last-served office, rung 5 is exhausted. Declining every rung 3 office moves to rung 4, and Declined Offices applies only to the office-resolution step. (Recommended)
  B. Rung 5 runs at the office the caller accepts on rung 3, or else at the office resolved by entryPoint.
  C. Declining every rung 3 office returns customer_declined_options, which ends the ladder.
Footprint: A ≈ 3 edits, net +25 words. B ≈ 2 edits, net +20 words. C ≈ 1 edit, net +10 words.
Answer:

### Q-63 · Peak switch after "stay" (resolves L-372)
Conflict: scenario_selection item 7 asks the peak trade-off "once per invocation", and "stay" holds only "until a caller-initiated constraint change". After such a change, item 7 fires again but the question can't be re-asked. The agent must either drop the Tax Pro silently or keep the ladder with no rule that says so.
Options:
  A. "Stay" holds for the whole invocation. Item 7 never switches returning_same_tax_pro after a stay. (Recommended: smallest edit)
  B. A caller-initiated constraint change allows one more trade-off question.
  C. Other: ___
Footprint: A ≈ 2 edits, net -5 words. B ≈ 2 edits, net +5 words.
Answer:

### Q-64 · Scope of the automation flags (resolves L-375)
Conflict: The scheduler_always too_many item and §5.2 Automation Flags transfer on isCancelable false or isReschedulable false regardless of operation. The prose Appointment Details bullet transfers only on too_many. So a details question, a reschedule of a non-cancelable appointment, or a flag on an unbound appointment each has two readings.
Options:
  A. isReschedulable false blocks only reschedule_existing, and isCancelable false blocks only cancel_existing. Each checks only the bound appointment, and details questions ignore both. (Recommended)
  B. Keep the flags unscoped on reschedule and cancel, and exempt only details questions.
  C. Leave the flags unscoped, and add the flag transfer to the Appointment Details bullet.
Footprint: A ≈ 3 edits, net +20 words. B ≈ 2 edits, net +8 words. C ≈ 1 edit, net +8 words.
Answer:

### Q-65 · Which agents offer a message for a closed office (resolves L-376)
Conflict: §1.3 and the global_always leave-message item return leave_message_offer when "the target office is closed, busy, or hours_unavailable", with no scope. Part 1 wins (C-1), which would override the Scheduler's Year-Round Office proposal and the office_info closed_for_season answer. D-023, D-045 and D-053 were all about office_contact.
Options:
  A. Scope the closed, busy, and hours_unavailable trigger to the office_contact path in §1.3 and global_always. (Recommended: keeps current agent behavior)
  B. Keep it for every agent. The Scheduler and office_info then return leave_message_offer for a closed office instead of their current paths.
  C. Other: ___
Footprint: A ≈ 2 edits, net +6 words. B ≈ 4 edits, net +20 words.
Answer:

### Q-66 · A message request inside the Scheduler (resolves L-377)
Conflict: §1.3 says an explicit message request returns nextAction leave_message. The Scheduler and the Base JSON have no outcome that carries it outside transfer_unavailable, and no routingTarget is a message destination. "Can I just leave Sarah a message?" mid-booking has no valid payload.
Options:
  A. In the Scheduler, a message request hands back intent_changed: speak_to_tax_pro if it names a Tax Pro, office_information if it names office staff. Those agents return their own message outcomes. (Recommended: no new outcome)
  B. Add a Base outcome `message_requested` (transactionOccurred false, or true after a commit; callContained true; nextAction leave_message) for any agent without its own.
  C. Other: ___
Footprint: A ≈ 2 edits, net +25 words. B ≈ 3 edits, net +35 words, adds one outcome.
Answer:

### Q-67 · Where no_acceptable_availability carries the constraints (resolves L-378)
Conflict: no_acceptable_availability says "carry the agreed constraints plus the scenario and exhausted rungs". The terminal contract has scenario and exhaustedRungs but no constraints field. The §5.1 transfer_to_agent request has `knownSoFar` (dateSpoken, timeWindow, officeName, meetingMethodChosen).
Options:
  A. Map the agreed constraints to transfer_to_agent `knownSoFar`, and carry scenario and exhaustedRungs in the payload. (Recommended: no new field)
  B. State the agreed constraints in interactionSummary.
  C. Add a constraints field to the terminal contract.
Footprint: A ≈ 1 edit, net +4 words. B ≈ 1 edit, net +2 words. C ≈ 2 edits, net +15 words, adds a field.
Answer:

### Q-68 · office_not_found on an office the caller did not give (resolves L-379)
Conflict: get_office_details returns office_not_found for an unmatched officeRef. Part 3 handles it only on a caller-given ZIP (D-044, D-056). It has no rule for routedOfficeRef, an officeRef matched from nearbyOffices, or yroOfficeRef.
Options:
  A. Treat it as an office lookup failure: transfer as system_failure. (Recommended: smallest edit)
  B. On routedOfficeRef, return handoff_invalid. On a matched or Year-Round officeRef, transfer as system_failure.
  C. Ignore the officeRef, capture a ZIP, and apply the caller-given ZIP rule.
Footprint: A ≈ 2 edits, net +12 words. B ≈ 2 edits, net +20 words. C ≈ 2 edits, net +15 words.
Answer:

### Q-69 · find_customer no_match outside a new booking (resolves L-084, L-150)
Conflict: §2 State 1 treats no_match as a new customer. No step covers no_match on reschedule_existing, cancel_existing, or an appointment-details question. Part 4 (tax_pro_always, speak_to_tp_generic step 3) covers third-party and authentication failure only, not a first-party no_match.
Options:
  A. In the Scheduler, no_match on reschedule, cancel, or a details question transfers as identity_unresolved with the §1.4 "Authentication failed" line. In Part 4, a first-party no_match follows the no-prior-Tax-Pro path and offers only the Scheduler. (Recommended)
  B. Everywhere, re-capture name and date of birth once. A second no_match transfers as identity_unresolved.
  C. Other: ___
Footprint: A ≈ 2 edits, net +30 words. B ≈ 2 edits, net +30 words.
Answer:

### Q-70 · Carried identity and profile data (resolves L-085, L-135)
Conflict: §1.1 customerRef trusts only an identity "from a prior agent". The flow spec leaves open whether Head of Call identification counts. Skipping find_customer (§1.1, scheduler_always customerRef item; Part 4 step 3 always calls it) leaves no source for priorTaxProStatus, clientComplexity, or lastFiledYear.
Options:
  A. Head of Call identity never fills customerRef (§1.1 unchanged). A carried customerRef skips the identity questions, but find_customer still runs with customerRef alone to read the profile. (Recommended: smallest edit)
  B. As A, and Head of Call also fills customerRef when its flow marks the caller authenticated. §1.1 and context_envelope say so.
  C. Other: ___
Footprint: A ≈ 4 edits, net +25 words (one request field in §5.2 find_customer). B ≈ 6 edits, net +40 words.
Answer:

### Q-71 · Callback notes and phone fields on book_appointment (resolves L-090, L-160, L-163)
Conflict: The scheduler_always callback item captures "the reason for the call in appointmentNotes". global_never bans capturing "message content", and Part 1 wins. The §5.2 existing-customer example sends appointmentNotes with notice content on a tax_prep booking. It also sends a top-level phoneNumber that no rule defines, and contact.callbackNumber, which §5.2 requires only for new customers.
Options:
  A. appointmentNotes holds only a callback's reason as one short phrase, and that is not message content. The example sets appointmentNotes to null and drops phoneNumber and contact. (Recommended: keeps current capture)
  B. As A, but every phone_callback sends contact.callbackNumber: the profile number for an existing customer unless the caller gives another, read back at capture.
  C. Other: ___
Footprint: A ≈ 3 edits, net -10 words. B ≈ 4 edits, net +20 words.
Answer:
