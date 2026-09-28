# Round 3 questions

Write a letter, your own text, "defer", or "not an issue" after each `Answer:`. Then run `/continue`.
These 12 questions cover the one open High (L-170) and the largest Medium clusters. The other open Medium items carry to round 4; the ledger has their summaries.

### Q-25 · Transfer outcomes and reasons (resolves L-170, L-171, L-174, L-194, L-195)
Conflict: The `global_always` transfer-results item returns "the outcome carrying that transferReason", but out_of_scope and automation_blocked have no outcome, and `validation_failed` ("A tool rejects...") overlaps rejected, which maps to automation_blocked. Part 3 `office_info_transfer` and `system_failure` both fit an office lookup failure. A failed `transfer_to_agent` call is "agent_unavailable with no message", but it returns no supportHoursSpoken for that row. `handoff_invalid`, `configuration_missing`, and the §1.4 unregistered-ANI row have no transferReason.
Options:
  A. `transferred_to_human` covers every agent_available transfer whose reason has no outcome of its own (caller_requested, out_of_scope, automation_blocked). `validation_failed` excludes rejected. Delete `office_info_transfer`; Part 3 uses `system_failure`. On a failed call, speak the §1.4 system_failure line and return `transfer_unavailable` with nextAction close and no support hours. `handoff_invalid` and `configuration_missing` carry transferReason system_failure. Unregistered ANI maps to identity_unresolved. (Recommended)
  B. Add outcomes `out_of_scope_transfer` and `automation_blocked` beside `transferred_to_human`. Keep `office_info_transfer`, rewording it as Part 3's system_failure outcome. Failed call, handoff_invalid, and unregistered ANI as in A.
  C. Other: ___
Footprint: A ≈ 8 edits, net +20 words. B ≈ 10 edits, net +60 words.
Answer: A

### Q-26 · Context carried into the Scheduler (resolves L-184, L-178, L-177, L-180)
Conflict: §1.1 says to use a carried appointmentType, taxProRef, and officeRef "without re-asking". But `workflow.schedule_new[1]` still establishes the type, asks about the prior Tax Pro, and resolves the office by entryPoint, so routedOfficeRef could beat the carried officeRef. Handoffs to appointment_scheduler carry no `operation`, and nothing sets it when it arrives null. The Scheduler takes a caller-named Tax Pro as a preference but has no `search_tax_pro_by_name`. A direct "have a Tax Pro call me" fits both phone tax_prep and the callback type.
Options:
  A. A carried appointmentType, taxProRef, or officeRef skips its own question and outranks entryPoint and routedOfficeRef. A null operation with a carried appointmentType means schedule_new; otherwise the Scheduler asks whether to book, change, or cancel. A caller-named Tax Pro, or a callback request with no carried Tax Pro, hands back intent_changed with routingTarget speak_to_tax_pro. (Recommended)
  B. Carried context as in A. Add `search_tax_pro_by_name` to the Scheduler's tools so it resolves named Tax Pros itself. With no carried Tax Pro, a callback request is booked as phone tax_prep.
  C. Other: ___
Footprint: A ≈ 6 edits, net +40 words. B ≈ 7 edits, net +55 words.
Answer: A

### Q-27 · Canceled appointments and who cancels (resolves L-193, L-179)
Conflict: After D-021, `get_customer_appointments` can return status canceled. But its results count only active appointments ("No active future appointments exist."), so a caller whose only appointment is canceled gets none_found and `appointment_already_canceled` cannot fire. Head of Call cancels inline (deterministic flow PA-10 to PA-12), and the Scheduler owns cancel_existing. Nothing says which cancellations reach the Scheduler.
Options:
  A. Results count canceled future appointments too. A canceled-only match returns one_appointment with status canceled, and that triggers `appointment_already_canceled`. none_found means no active or canceled future appointment. The Scheduler cancels only when invoked with operation cancel_existing or when the caller asks mid-booking; Head of Call's inline cancel stays in the flow. (Recommended)
  B. Reverse D-021: delete status canceled and `appointment_already_canceled`, and treat a canceled appointment as none_found. Ownership as in A.
  C. Other: ___
Footprint: A ≈ 4 edits, net +30 words. B ≈ 5 edits, net -40 words.
Answer: A

### Q-28 · A no or an unclear answer at the gate (resolves L-199, L-204, L-191)
Conflict: Only the cancellation gate's "no" maps to an outcome. A no at the booking, reschedule, or DDO gate has no branch. An ambiguous or conditional answer "is not consent", but no rule caps the re-asks or ties them to the no-match count. After not_confirmed, the re-gate reuses the same slot, and the contract doesn't say whether the retry keeps the idempotencyKey.
Options:
  A. After a no at any gate, ask once what to change. A change re-enters negotiation, and a second no returns `customer_declined_options`. An ambiguous answer counts as a no-match: re-ask once, then transfer as clarification_exhausted. The not_confirmed re-gate keeps the same idempotencyKey. (Recommended)
  B. A no at any gate returns `customer_declined_options` at once. Ambiguity as in A. The not_confirmed re-gate takes a new key with suffix -2, as the DDO re-send does.
  C. Other: ___
Footprint: A ≈ 4 edits, net +40 words. B ≈ 4 edits, net +25 words.
Answer: A

### Q-29 · Scheduler loops with no cap (resolves L-201, L-203, L-205, L-165)
Conflict: The Year-Round Office proposal and the three central-line offices have no exit when the caller declines them all. Item 7 re-evaluates on every no_slots, so the peak trade-off can be asked again at each rung after "stay". slot_taken re-searches with no rung scope and no cap. The ZIP reprompt on invalid_location has no attempt cap.
Options:
  A. A caller who declines every proposed office returns `customer_declined_options`. The peak trade-off is asked once per invocation, and "stay" holds until a caller-initiated constraint change. slot_taken re-searches the same rung once; a second slot_taken moves to the next rung. An invalid ZIP counts under MAX_INPUT_ATTEMPTS and transfers as clarification_exhausted. (Recommended)
  B. A caller who declines every proposed office transfers as no_acceptable_availability. Trade-off, slot_taken, and ZIP as in A.
  C. Other: ___
Footprint: A ≈ 5 edits, net +45 words. B ≈ 5 edits, net +40 words.
Answer: A

### Q-30 · Office Information: the open-office branch and phone numbers (resolves L-186, L-185)
Conflict: §3 If OPEN tells the caller the staff is busy, then returns capture_intent, while `terminal_payload_contract` limits capture_intent to calls "where nothing was served". `office_open_unanswered` covers only callers whose open office did not answer, not a caller who asked for the front desk (3C). `global_always` sends every phone-number question to office_information, but the office_info scope lists only hours, address, and directions, and the OPEN branch withholds the number.
Options:
  A. capture_intent means the caller's need was not met. `office_open_unanswered` covers any office_contact caller at an open office. office_info also answers a phone-number question with mainPhoneSpoken for the routed office; the no-number rule applies only to the office_contact OPEN branch. (Recommended)
  B. The OPEN branch returns nextAction leave_message_offer, so the caller who wanted staff hears the message option. The capture_intent definition stays. Phone numbers as in A.
  C. Other: ___
Footprint: A ≈ 5 edits, net +20 words. B ≈ 6 edits, net +15 words.
Answer: B

### Q-31 · Office Information: follow-ups and lookup gaps (resolves L-202, L-206, L-152, L-153)
Conflict: `workflow.office_info_flow[3]` returns right after the blurb. But `closed_for_season` stores yroOfficeRef "to answer follow-up questions", and §3 Location Change expects mid-call office changes. A caller-named office with no officeName match has no branch. The hours_unavailable result has no branch. A null routedOfficeRef on office_contact has no resolution step.
Options:
  A. office_info answers follow-ups, including another office, in the same invocation, then returns `office_info_provided`. No name match: reprompt once for the office name or ZIP, then transfer as system_failure. On hours_unavailable, give the address and say the hours aren't available. office_contact with no routedOfficeRef captures a ZIP, as office_info does. (Recommended)
  B. One answer per invocation: return after the blurb, and Head of Call handles follow-ups through offer_additional_help. Delete the yroOfficeRef follow-up clause and §3 Location Change. Name match, hours_unavailable, and ZIP as in A.
  C. Other: ___
Footprint: A ≈ 6 edits, net +50 words. B ≈ 7 edits, net +10 words.
Answer: A

### Q-32 · Speak to a Tax Pro: exits (resolves L-200, L-175, L-142, L-154, L-173)
Conflict: A caller who declines both the callback and the message has no exit. The unavailable-Tax-Pro path returns leave_message_offer with no transfer tried and no closed office, outside the §1.3 triggers. A generic request with no prior Tax Pro, or an inactive one, has no path. Disambiguation has no exit, and 4C shows a yes/no confirm instead of a location question. Parts 3 and 4 return capture_intent for an unclear intent but name no finalOutcome.
Options:
  A. Add Base outcome `intent_unclear` (nextAction capture_intent, callContained true) for Parts 2 to 4. A caller who declines both options returns `routed_to_message` with leave_message_offer. §1.3 gains "or the requested Tax Pro is unavailable". No or inactive prior Tax Pro follows the by-name inactive path. Ask the location question once; a second miss is no match. Edit 4C to match. (Recommended)
  B. Add Part 4 outcome `tax_pro_options_declined` (offer_additional_help) for a caller who declines both. Delete leave_message_offer from the unavailable path, which offers only the Scheduler. Unclear intent, prior Tax Pro, and disambiguation as in A.
  C. Other: ___
Footprint: A ≈ 8 edits, net +50 words. B ≈ 9 edits, net +45 words.
Answer: B

### Q-33 · Tax questions and requests for a person (resolves L-182, L-196, L-181)
Conflict: §1.2 Tax/Financial Boundary sends every non-loan tax question "to a Tax Pro" with no routingTarget. `global_always` sends "general tax questions" to faq_agent, and non-answers return `no_approved_answer`. After D-012, no path ends in `question_answered`. In the Scheduler, "a request for a person" fits both a barging transfer and a speak_to_tax_pro handback.
Options:
  A. faq_agent takes non-personal tax questions. Personal advice, calculation, and notice questions: in the Scheduler, say the Tax Pro covers it at the appointment; elsewhere, hand back to speak_to_tax_pro. Delete `question_answered`. Only a request for a live agent is barging; a request for a specific or own Tax Pro hands back to speak_to_tax_pro. (Recommended)
  B. Every tax question goes to faq_agent; delete "and the rest to a Tax Pro" from §1.2. Keep `question_answered` for a Part 3 or Part 4 caller whose only need was a knowledge-base question. Person requests as in A.
  C. Other: ___
Footprint: A ≈ 5 edits, net +15 words. B ≈ 4 edits, net +10 words.
Answer: A

### Q-34 · Type or method change: JSON and reschedule (resolves L-098, L-151)
Conflict: §2 State 2 "Type & Method Edge Cases" re-checks method and office eligibility, re-derives the floor, and skips readiness on an accepted channel rung. `invalidation.upstream_change` does none of these (the round 2 fix was reverted). `workflow.reschedule_existing[2]` bars a method change on reschedule with no handler, while §2 State 2 Immutability bars only a type change.
Options:
  A. Rewrite `upstream_change` to carry the eligibility and floor re-check and the channel-rung readiness skip, within 60 words. A method change on reschedule is barred like a type change: preserve the appointment and transfer as automation_blocked, stated in both the prose and the JSON. (Recommended)
  B. upstream_change as in A. Allow a method change on reschedule: delete "or method" from step 3 and add 'method' to the reschedule changing array.
  C. Other: ___
Footprint: A ≈ 4 edits, net +25 words. B ≈ 4 edits, net +20 words.
Answer: A

### Q-35 · Frozen lexicon: "transfer" and an unused line (resolves L-210, L-172)
Conflict: §1.2 allows "transfer" when it refers to a live human agent, but the frozen `prohibited_phrases` bans "transfer you to" in every case. That list also lacks the §1.2 ban on "scheduling department". The frozen `reprompt` line "Just so I don't mix up the year, what year was that?" has had no use since D-024.
Options:
  A. Never say "transfer": delete "(unless referring to a live human agent)" from §1.2. Add "scheduling department" to `prohibited_phrases`. Delete the year reprompt line. (Recommended: no approved line says "transfer")
  B. Allow "transfer" for a live agent: replace "transfer you to" in `prohibited_phrases` with "transfer you to the" + a system or department name. Add "scheduling department", and delete the year line, as in A.
  C. Other: ___
Footprint: A ≈ 3 edits, net -15 words. B ≈ 3 edits, net -5 words.
Answer: B

### Q-36 · Digital drop-off as a rung and when a scenario is chosen (resolves L-190, L-072)
Conflict: The `find_available_slots` rung values include digital_drop_off, but DDO has no slots and skips readiness and availability. `scenario_selection` runs "after readiness returns ready". But the drop-off method (item 2) and keeping the prior Tax Pro (item 8) are chosen at `workflow.schedule_new[1]`, before readiness.
Options:
  A. Accepting a digital_drop_off rung ends the slot search and runs the DDO path (destination gate, then `send_secure_link`). Delete digital_drop_off from the `find_available_slots` rung values. scenario_selection records the step 2 choices (drop-off method, prior Tax Pro), then applies first-match-wins after ready. (Recommended)
  B. Keep digital_drop_off in the rung values as a marker, never sent to `find_available_slots`. Scenario timing as in A.
  C. Other: ___
Footprint: A ≈ 4 edits, net +20 words. B ≈ 3 edits, net +25 words.
Answer: A
