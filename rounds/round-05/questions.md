# Round 5 questions

Write a letter, your own text, "defer", or "not an issue" after each `Answer:`. Then run `/continue`.
These 11 questions cover every open Medium from round 5 and the four gaps found while verifying round 4 (L-322 to L-325). Older carried Human items (L-074 to L-192) stay in the ledger.

### Q-49 · Part 4's "another Tax Pro" handoff into the Scheduler (resolves L-357, L-358, L-360)
Conflict: The D-040 rule "If priorTransaction is routed_to_scheduler, book a callback request as a tax_prep phone_callback appointment" has no scope. It also matches Part 4's normal callback handoff, which carries appointmentType callback (§1.1 says a carried type outranks). The another-Tax-Pro handoff sets no operation, so the Scheduler asks "book, change, or cancel" after the caller already chose to book (§1.1 operation). It can also ask to keep a prior Tax Pro whom Part 4 just found unavailable (workflow.schedule_new[1], scenario_selection item 8).
Options:
  A. The rule applies only when priorTransaction.finalOutcome is routed_to_scheduler and no appointmentType is carried. That handoff means operation schedule_new, skips the keep-prior-Tax-Pro question, and selects returning_tax_pro_unavailable for a returning client. (Recommended)
  B. As A, but the Scheduler still asks whether to keep the prior Tax Pro.
  C. Other: ___
Footprint: A ≈ 5 edits (§1.1 operation row, context_envelope.operation, After Part 4 bullet, scheduler_always item, scenario_selection item 9), net +35 words. B ≈ 4 edits, net +25 words.
Answer:

### Q-50 · Own Tax Pro request after Part 4 sent the caller to the Scheduler (resolves L-359)
Conflict: After Part 4 routes a caller whose Tax Pro is unavailable, a request in the Scheduler for "my own Tax Pro" still hands back intent_changed to speak_to_tax_pro (§2 State 2 Tax Pro Requests, interruptions.intent_change). Part 4 then finds the Tax Pro unavailable again and routes back, with no limit.
Options:
  A. After a Part 4 routed_to_scheduler, state once that the Tax Pro isn't available and continue booking. A second request returns customer_declined_options. (Recommended)
  B. After a Part 4 routed_to_scheduler, such a request returns customer_declined_options at once.
  C. Other: ___
Footprint: A ≈ 3 edits, net +30 words. B ≈ 3 edits, net +20 words.
Answer:

### Q-51 · Which handbacks set the next agent's carried values (resolves L-361)
Conflict: terminal_payload_contract carries appointmentType, and carries taxProRef and officeRef "when handing off ... to appointment_scheduler". §1.1 treats any such value "set by a prior agent's handoff" as carried, so it skips its question and outranks everything. So Part 4's another-Tax-Pro handoff would carry the unavailable Tax Pro. A post-commit cancel handback (D-041) would carry the booked type, and a carried type means schedule_new. The extension follow-up (D-019) would carry tax_extension instead of tax_prep.
Options:
  A. Only Part 4's callback handoff sets taxProRef and officeRef for the next agent. The another-Tax-Pro handoff sets only officeRef, when known. The Scheduler's intent_changed handbacks carry the committed reference and sourceUtterance but no appointmentType, except that the extension follow-up carries appointmentType tax_prep. (Recommended)
  B. Keep the contract, and Head of Call decides which terminal fields it copies into the next envelope. Edit §1.1 to say the carried values come from Head of Call.
  C. Other: ___
Footprint: A ≈ 4 edits, net +30 words. B ≈ 2 edits, net +10 words, and moves a mapping into Head of Call (outside this spec).
Answer:

### Q-52 · office_contact at a seasonally closed office (resolves L-362)
Conflict: D-045 makes office_contact run the office_info seasonalStatus check first. On closed_for_season the rule only says "state the closure and offer yroOfficeAddressSpoken". It does not say whether `check_office_open_status` still runs, whether a main line is given, or which outcome returns.
Options:
  A. After the closure and Year-Round Office address, return office_contact_triage_complete with nextAction leave_message_offer. Skip `check_office_open_status` and give no phone number. (Recommended)
  B. Make the Year-Round Office the routed office and continue the office_contact flow for it (open status, main line, message offer).
  C. Other: ___
Footprint: A ≈ 3 edits, net +25 words. B ≈ 4 edits, net +30 words.
Answer:

### Q-53 · Appointment-details questions (resolves L-324, L-363, L-364)
Conflict: D-049 lets the Scheduler answer "when is my appointment?", but:
- The path has no finalOutcome, so the contract cannot validate.
- It sits under a "mid-booking" trigger yet ends the invocation.
- It has no handling for none_found, several_appointments, too_many, or a canceled status.
- Parts 3 and 4 route only schedule, reschedule, or cancel, so this question has no routingTarget there.
Options:
  A. Add Scheduler outcome `appointment_details_provided` (transactionOccurred false, callContained true, nextAction offer_additional_help, intent schedule_appointment). Mid-booking, answer and resume per interruptions.informational_question.
    - none_found: say nothing is on file.
    - several_appointments: read each date, time, and office.
    - too_many: transfer per the existing rule.
    - Canceled appointment: say it is canceled.
    Parts 3 and 4 hand these questions to appointment_scheduler. (Recommended)
  B. As A, but reuse offer_additional_help with no new outcome, and set finalOutcome to the nearest existing outcome (customer_declined_options).
  C. Other: ___
Footprint: A ≈ 7 edits, net +70 words, adds one outcome. B ≈ 6 edits, net +50 words.
Answer:

### Q-54 · What is left of intent_unclear (resolves L-325, L-365)
Conflict: D-042 deleted intent_unclear. After that, no outcome uses nextAction capture_intent, which is still defined in the contract. In Part 3, an unresolved "hours and address" or "speaking to the office staff" choice ends in clarification_exhausted, but the mandatory `intent` has no value, because neither office_info nor office_contact was established.
Options:
  A. Delete capture_intent from the nextAction enum and its definition. An unresolved Part 3 intent carries intent office_info. (Recommended)
  B. Keep capture_intent for Head of Call's use. An unresolved Part 3 intent omits `intent` on this outcome only.
  C. Other: ___
Footprint: A ≈ 3 edits, net -25 words. B ≈ 2 edits, net +12 words.
Answer:

### Q-55 · Transfer reason for a caller-named office with no match (resolves L-322)
Conflict: §3 No Name Match transfers as system_failure after one reprompt. D-044 made office_not_found on a caller-given ZIP a no-match (clarification_exhausted) and limited "lookup failure" to tool errors, while system_failure means "a tool failed".
Options:
  A. A name no-match is also a no-match: reprompt once, then transfer as clarification_exhausted. Merge it with the ZIP Not Found bullet. (Recommended: one rule, net words down)
  B. Keep system_failure for a name no-match.
  C. Other: ___
Footprint: A ≈ 3 edits, net -15 words. B 0 edits.
Answer:

### Q-56 · requires_tax_pro inside the Speak to a Tax Pro agent (resolves L-323)
Conflict: D-046 hands requires_tax_pro back to speak_to_tax_pro outside the Scheduler. Part 4 is that agent, so the spec applies it only in office_information. In Part 4, a KB requires_tax_pro answer falls to "any other non-answer returns no_approved_answer", which ends a caller who is trying to reach a Tax Pro.
Options:
  A. In Part 4, requires_tax_pro continues the workflow: state the options for reaching the Tax Pro per tax_pro_always. (Recommended)
  B. Keep no_approved_answer in Part 4.
  C. Other: ___
Footprint: A ≈ 2 edits, net +15 words. B 0 edits.
Answer:

### Q-57 · Changing a digital drop-off (resolves L-366)
Conflict: The DDO rule "Handle a requested change as a new schedule_new DDO send" reads as a second send in the same invocation. That send has no key: ddo-1 deduplicates, and ddo-2 is the delivery_failed re-send. D-041 hands a post-commit change back with "the committed reference", but a DDO send has none. In the next invocation, a "change" answer sets reschedule_existing, and retrieval of the DDO ends in none_found and a transfer.
Options:
  A. A change after ddo_link_sent hands back per D-041 with no reference. At the null-operation question, a change to a digital drop-off sets operation schedule_new with method digital_drop_off. (Recommended)
  B. Allow one destination change in the same invocation, re-gated and sent with a new key format `interactionId-ddo-change`.
  C. Other: ___
Footprint: A ≈ 3 edits, net +20 words. B ≈ 4 edits, net +30 words, adds a key format.
Answer:

### Q-58 · Switching between book, change, and cancel before a commit (resolves L-367)
Conflict: Before a commit, only a switch to cancel is defined (interruptions.cancel_said). If a caller at the cancellation gate says "no, move it instead", the switch hits "A no leaves it untouched" and returns customer_declined_options. A caller mid-reschedule who wants a new booking instead has no path either.
Options:
  A. A pre-commit switch between schedule_new, reschedule_existing, and cancel_existing restarts the new workflow in the same invocation, keeping authentication, as cancel_said does. (Recommended)
  B. A pre-commit switch hands back intent_changed with routingTarget appointment_scheduler and the new operation's sourceUtterance.
  C. Other: ___
Footprint: A ≈ 3 edits (merge into cancel_said), net +15 words. B ≈ 3 edits, net +20 words.
Answer:

### Q-59 · Declining the tax_prep offer when the extension window is closed (resolves L-368)
Conflict: On tax_extension with the filing window closed, the Scheduler offers a tax_prep appointment instead (§2 State 2 table, scheduler_always tax_extension item). A caller who declines has no outcome: no ladder has started, and customer_declined_options does not list this case.
Options:
  A. Add "declines the tax_prep offer from a closed extension window" to customer_declined_options. (Recommended)
  B. A decline hands back intent_changed with routingTarget faq_agent for general extension questions.
  C. Other: ___
Footprint: A ≈ 2 edits, net +10 words. B ≈ 2 edits, net +12 words.
Answer:
