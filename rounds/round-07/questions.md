# Round 7 questions

Write a letter, your own text, "defer", or "not an issue" after each `Answer:`. Then run `/continue`.
These 12 questions cover the round 7 High (D-01), the 11 carried groups from rounds 1-6, and one new Medium bundled with L-146. Ten new round 7 Mediums carry to round 8 (L-395 to L-404; options in findings-A to findings-E). Round 8 is the last round under C-12. To finish sooner, you may answer any of them now as "L-xxx: A".

### Q-72 · Reschedule has no refs for the bound appointment (resolves L-393)
Conflict: `workflow.reschedule_existing[3]` preserves unchanged constraints and calls `check_search_readiness`, which needs officeRef, and the changing array compares officeRef and taxProRef. §5.2 `get_customer_appointments` returns only officeName, taxProName, dateSpoken, and timeSpoken, so the bound office, Tax Pro, and time (requestedTimeSource existing_appointment) cannot be filled.
Options:
  A. Add officeRef, taxProRef (null with no named Tax Pro), date, and requestedTime to each appointment in the §5.2 Response JSON. (Recommended: fills every use)
  B. Add only officeRef and taxProRef; drop requestedTimeSource existing_appointment.
  C. Add appointmentRef to the check_search_readiness request; the tool resolves the bound constraints.
Footprint: A ≈ 1 JSON edit, +4 keys. B ≈ 3 edits, +2 keys. C ≈ 3 edits, +1 field.
Answer: A

### Q-73 · Tax Pro trade-off points (resolves L-074, L-075)
Conflict: §2 State 3 Tax Pro Trade-off asks "only at these two points" (the rung that drops the Tax Pro; before a Peak Capacity switch). `invalidation.partial_acceptance` asks it a third time when the caller rejects a proposed Tax Pro but keeps the office. The `scheduler_always` efile_rejection_retail item says "otherwise apply the Tax Pro trade-off" with no prior Tax Pro, so [Name] is empty.
Options:
  A. Add partial rejection as a third point in the prose list; the efile item reads "otherwise follow workflow.schedule_new". (Recommended: matches the JSON)
  B. Keep two points; partial_acceptance widens to eligible Tax Pros without asking; the efile item as in A.
Footprint: A ≈ 2 edits, net +8 words. B ≈ 2 edits, net -8 words.
Answer: B

### Q-74 · Off-season line in Part 3 (resolves L-080)
Conflict: The frozen §1.4 Off-season line names [officeName] twice and asks "Would that work?", a booking question. §3 Off-Season Closure states the closure and offers the Year-Round Office address, and Part 3 never books.
Options:
  A. Scope the §1.4 Path cell to "Off-season office closure (Scheduler)"; Part 3 keeps its own wording. (Recommended: no frozen line changes)
  B. Part 3 speaks the frozen line with the address; a yes hands back intent_changed to appointment_scheduler.
Footprint: A ≈ 1 edit, +1 word. B ≈ 3 edits, net +20 words.
Answer: A

### Q-75 · §1.4 lines with no lexicon copy (resolves L-089)
Conflict: Under C-2 (mirror), five §1.4 lines have no copy in `global_voice_lexicon.empathy`: Unregistered ANI or third-party blocked, agent_available, the two agent_unavailable lines, and Repeat or slow-down. The runtime prompt never sees them.
Options:
  A. Append the five lines to global_voice_lexicon.empathy, each with its path tag. (Recommended)
  B. Not an issue; the runtime reads §1.4.
Footprint: A ≈ 1 JSON edit, +75 words (over the 1% round budget unless offset). B: none.
Answer: A. It's ok to go over budget here.

### Q-76 · Confirm Appointment requests (resolves L-136)
Conflict: The flow spec's Head of Call routes "Confirm Appointment" to the Scheduler or confirms inline (PA-20). The Scheduler has no confirm operation; §1.1 `operation` asks "which of the three".
Options:
  A. A confirm request that reaches the Scheduler is an appointment-details question and returns appointment_details_provided. (Recommended: no new operation)
  B. Not an issue; Head of Call confirms inline.
Footprint: A ≈ 2 edits, +12 words. B: none.
Answer: B

### Q-77 · "Office associate" has two owners (resolves L-140)
Conflict: §4 Speak to Tax Pro (Generic) covers "a tax advisor, preparer, or office associate", while Part 3 office_contact owns local office staff and Part 4 prose says office-staff requests belong to Office Information.
Options:
  A. Delete "or office associate" from §4 Generic. (Recommended: smallest edit)
  B. Replace it with "tax associate".
Footprint: A ≈ 1 edit, -2 words. B ≈ 1 edit, 0 words.
Answer: A

### Q-78 · Readiness conflict signals and cap (resolves L-146, L-394)
Conflict: On any readiness conflict the Scheduler speaks the past-date line (§1.4, `check_search_readiness` entry), though conflict also covers closed tax_extension and emerald_advance windows. Repeated needs_more or conflict on recognizable answers has no cap, since the No-Match Rule counts only unrecognized input.
Options:
  A. Speak the past-date line only when issue is a past date; a closed window follows the type row (tax_extension offers tax_prep; emerald_advance states it is not available now and returns customer_declined_options). A second consecutive conflict, or needs_more for the same askFor item, counts as a no-match, then transfers as clarification_exhausted. (Recommended)
  B. Add readiness result window_closed (new enum value) and keep the cap as in A.
  C. Cap only: A's cap rule, no closed-window change.
Footprint: A ≈ 3 edits, net +35 words. B ≈ 4 edits, +1 enum, +40 words. C ≈ 1 edit, +20 words.
Answer: A

### Q-79 · taxProPreference.source has no enum (resolves L-162)
Conflict: §5.2 `check_search_readiness` sends taxProPreference.source ("caller_stated") and returns taxProSource, but no enum lists the values; the Scheduler also carries a prior Tax Pro, a Part 4 taxProRef, and an existing appointment's Tax Pro.
Options:
  A. Define source as caller_stated, prior_tax_pro, carried, or existing_appointment in a Note line. (Recommended)
  B. Delete source and taxProSource.
Footprint: A ≈ 1 edit, +12 words. B ≈ 3 edits, -2 fields.
Answer: A

### Q-80 · New customer's name readback (resolves L-164)
Conflict: §1.2 Confirmed at capture reads back only raw data the system cannot verify; Mini-Dialogue 1A captures a new customer's name after no_match with no readback, although nothing verifies it before book_appointment.
Options:
  A. First-party names are never read back (§1.2 stands; no edit). (Recommended)
  B. Read the new customer's name back once after no_match; 1A adds the readback.
Footprint: A: none. B ≈ 3 edits, +20 words.
Answer: A

### Q-81 · Re-asking for the named Tax Pro after routed_to_scheduler (resolves L-383)
Conflict: §2 State 2 After Part 4 says "state once that they aren't available and continue booking". After D-061 the caller may have come for another Tax Pro because only a callback could be booked with theirs, so "aren't available" can be false, and a request for the named (non-own) Tax Pro still returns intent_changed to speak_to_tax_pro, looping back to Part 4.
Options:
  A. After routed_to_scheduler, a request for the caller's own or the named Tax Pro gets one statement that this booking is with another Tax Pro, then booking continues; a second request returns customer_declined_options; never hand back. (Recommended)
  B. Keep "aren't available" for the own Tax Pro only; a named Tax Pro follows the same rule.
Footprint: A ≈ 3 edits, net +10 words. B ≈ 2 edits, +8 words.
Answer: A

### Q-82 · Message request naming no recipient in the Scheduler (resolves L-384)
Conflict: D-067 routes a Scheduler message request to speak_to_tax_pro when it names a Tax Pro, or office_information when it names office staff. A request that names neither has no rule.
Options:
  A. Ask once whether the message is for their tax professional or the office, then route per D-067; an unclear answer follows the No-Match Rule. (Recommended)
  B. Default to speak_to_tax_pro.
Footprint: A ≈ 2 edits, +18 words. B ≈ 2 edits, +8 words.
Answer: B

### Q-83 · Callback reason on a routed tax_prep phone callback (resolves L-385)
Conflict: The type table captures a one-phrase reason in appointmentNotes on callback, and §5.2 says "appointmentNotes is null except on callback". §2 After Part 4 books a Part 4 callback request as a tax_prep phone_callback, so it is unclear whether that booking carries the reason.
Options:
  A. Capture the one-phrase reason on any phone_callback; the Note reads "null except on a phone_callback". (Recommended)
  B. Only appointmentType callback carries it; a tax_prep phone_callback sends null.
Footprint: A ≈ 2 edits, +3 words. B ≈ 1 edit, +6 words.
Answer: A
