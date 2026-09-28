# Round 4 questions

Write a letter, your own text, "defer", or "not an issue" after each `Answer:`. Then run `/continue`.
These 12 questions cover the three open Highs (L-288, L-289, L-290), the seven Medium gaps left by round 3's decisions (L-238 to L-244), and every new round 4 Medium. Older carried Human items (L-074 to L-192) stay in the ledger for round 5.

### Q-37 · Idempotency keys on a second invocation (resolves L-288)
Conflict: `closure.re_entry` requires "a fresh idempotency key namespace", but every key format starts with interactionId, which §1.1 defines per session (e.g., `interactionId-ddo-1`). A DDO change in a later invocation of the same call (D-017) rebuilds `interactionId-ddo-1`, so the backend can deduplicate the new send and the agent still reports ddo_link_sent.
Options:
  A. Add an invocation counter to every key: `interactionId-N-...`, where N is the Scheduler invocation number in the call, starting at 1. Delete "fresh idempotency key namespace" from re_entry. (Recommended)
  B. Keep the formats, and state that Head of Call issues a new interactionId for each agent invocation. Edit the §1.1 interactionId row to match.
  C. Other: ___
Footprint: A ≈ 3 edits (idempotency item, re_entry, §5.2 examples), net +10 words. B ≈ 3 edits, net +10 words, and changes a Head of Call contract.
Answer: B

### Q-38 · Who offers the message and speaks support hours (resolves L-289, L-320)
Conflict: §1.3 and the §1.4 "agent_unavailable, message available" row say "The deterministic flow provides support hours and offers the message option." The Leave a Message flow starts at LM-01/LM-02 with recipient identification and has no offer or support-hours prompt, and Head of Call has no node for nextAction leave_message_offer. On this path nobody offers the message.
Options:
  A. The agent offers it: on leave_message_offer, speak one approved offer line (new frozen line approved by this decision), then return leave_message on a yes and offer_additional_help on a no. Support hours are spoken only on the no-message row, as today. §1.3 and the §1.4 row change to match. (Recommended: keeps the flows untouched)
  B. Head of Call owns it: the spec keeps returning leave_message_offer, and a Head of Call node (outside this spec, C-11) speaks the offer and hours. The spec edits only the §1.4 row to name Head of Call instead of "the deterministic flow".
  C. Other: ___
Footprint: A ≈ 6 edits, net +40 words, adds one approved line. B ≈ 2 edits, net 0 words, but needs a flow change outside this spec.
Answer: B

### Q-39 · Unavailable Tax Pro: callbacks and exits in Part 4 (resolves L-290, L-239, L-244, L-298)
Conflict: Part 4 sends a caller with no active Tax Pro to the Scheduler for another Tax Pro. There, "a callback with no carried taxProRef hands back intent_changed to speak_to_tax_pro", so a caller who keeps asking for a call back bounces between the agents. A caller who declines the Scheduler offer has no outcome. A generic caller with no prior Tax Pro hears "they are unavailable" with no one to name. The generic path checks activeStatus and takingAppointmentsInd, which find_customer does not return, and routed_to_scheduler needs an officeRef the path never resolves.
Options:
  A. The Scheduler owns the callback for another Tax Pro: a callback request arriving with `routed_to_scheduler` from Part 4 books a phone tax_prep appointment and never hands back. A caller who declines the Scheduler offer returns `tax_pro_options_declined`. With no prior Tax Pro, skip the "unavailable" line and offer the Scheduler directly. The generic path reads priorTaxProStatus only. routed_to_scheduler carries officeRef only when known; otherwise the Scheduler resolves the office. (Recommended)
  B. Part 4 owns it: Part 4 never sends a callback request to the Scheduler without a confirmed Tax Pro; it returns `tax_pro_options_declined` instead. Declined offer, no prior Tax Pro, status fields, and officeRef as in A.
  C. Other: ___
Footprint: A ≈ 7 edits, net +45 words. B ≈ 6 edits, net +30 words.
Answer: A

### Q-40 · Cancel and change requests inside the Scheduler (resolves L-240, L-241, L-291, L-292, L-302)
Conflict: With a null operation, the Scheduler asks book, change, or cancel (D-027), but D-028 lets it cancel only on operation cancel_existing or a mid-booking request. `cancel_said` cancels whenever the caller wants to cancel "before any commit", including during reschedule, and "no, cancel that" at a booking gate matches both cancel_said and the gate-no rule (D-029). After a commit, cancel_said hands back intent_changed with no routingTarget. A change request after commit has no path. On reschedule_existing, a canceled appointment in the results has no rule.
Options:
  A. A "cancel" answer to the operation question sets operation cancel_existing. cancel_said applies only to an existing appointment; "cancel this booking" at a gate is a gate no. A cancel or change request after commit hands back intent_changed with routingTarget appointment_scheduler and the committed reference. On reschedule_existing, a canceled appointment is not offered; a canceled-only match returns appointment_already_canceled. (Recommended)
  B. As A, but a cancel or change request after commit returns offer_additional_help, and Head of Call's inline cancel handles it (D-028).
  C. Other: ___
Footprint: A ≈ 6 edits, net +35 words. B ≈ 6 edits, net +30 words.
Answer: A

### Q-41 · What intent_unclear means (resolves L-293, L-294, L-295, L-296)
Conflict: The contract says "Reprompt an unclear intent once, then return intent_unclear" (no transfer), while §1.2 says a second no-match transfers as clarification_exhausted, and nothing separates the two. intent_unclear carries no intent value where Part 3 cannot tell office_info from office_contact. It always sets capture_intent, which the contract allows "only when nothing was served", yet Part 3 answers follow-ups after serving. `informational` is now used only by no_approved_answer, which always interrupts another intent.
Options:
  A. An unclear intent is an answer that names no in-scope need; an answer to a closed question the agent cannot map is a no-match. intent_unclear carries the intent the agent was invoked for. After a served answer, an unclear follow-up returns the served outcome instead. Delete `informational` from the intent enum; no_approved_answer carries the served intent. (Recommended)
  B. Every unresolved intent answer is a no-match, ending in clarification_exhausted; delete `intent_unclear`. Delete `informational` as in A.
  C. Other: ___
Footprint: A ≈ 5 edits, net +35 words. B ≈ 6 edits, net -20 words, reverses D-033's intent_unclear.
Answer: B

### Q-42 · Transfer and abandonment edge cases (resolves L-242, L-297, L-315, L-316)
Conflict: After D-026, a failed transfer call speaks the system_failure line ("Let me get you to a person") and then closes with no person. A failed call on the outcome_unknown path returns transfer_unavailable, losing outcome_unknown and its idempotencyKey. handoff_invalid and configuration_missing carry transferReason system_failure but also "Say nothing, hand back immediately", so it is unclear whether they call transfer_to_agent. customer_abandoned always sets transactionOccurred false, even after a committed write.
Options:
  A. A failed call speaks the §1.4 "agent_unavailable, no message" line without support hours (edit of that frozen row approved by this decision). A failed call on outcome_unknown keeps outcome_unknown and idempotencyKey. handoff_invalid and configuration_missing never call transfer_to_agent; they hand back with nextAction transfer. customer_abandoned after a commit sets transactionOccurred true and carries the committed reference. (Recommended)
  B. As A, but a failed call speaks nothing and returns transfer_unavailable with nextAction transfer, so Head of Call retries the transfer.
  C. Other: ___
Footprint: A ≈ 7 edits, net +30 words. B ≈ 6 edits, net +20 words.
Answer: B

### Q-43 · Office Information: resolving the office (resolves L-243, L-299, L-304)
Conflict: "Routed office" is undefined when routedOfficeRef is null, so after the D-032 ZIP capture the CLOSED branch speaks a number office_never forbids. A mistyped caller ZIP returns office_not_found, which counts as an "office lookup failure" and transfers at once as system_failure, while the Scheduler reprompts the same input. The named-office match looks only in nearbyOffices, so naming the office the ZIP resolves to (the top-level office) is a false no-match.
Options:
  A. The office resolved from a caller's ZIP or name becomes the routed office for the rest of the invocation. office_not_found on a caller-given ZIP is a no-match: reprompt once, then transfer as clarification_exhausted; only a tool error is a lookup failure. Match officeName against the top-level office and nearbyOffices. (Recommended)
  B. As A, but the phone number is spoken only for the office Head of Call routed, never for a ZIP-resolved office.
  C. Other: ___
Footprint: A ≈ 5 edits, net +30 words. B ≈ 6 edits, net +35 words.
Answer: A

### Q-44 · Office Information: office_contact branches and ending (resolves L-238, L-305, L-303)
Conflict: On hours_unavailable in office_contact, the agent gives the address but names no outcome or nextAction. office_contact_flow skips the seasonalStatus check, so a closed_for_season office takes the CLOSED branch and the caller hears no Year-Round Office. office_info answers follow-ups in the same invocation, but §1.3 bans "Anything else?", so nothing ends the invocation; silence runs the No-Input Rule and ends as consecutive_silence.
Options:
  A. hours_unavailable returns office_contact_triage_complete with nextAction leave_message_offer. office_contact runs the same seasonalStatus check as office_info first. office_info returns office_info_provided at the first silence after an answer, exempt from the robocall path. (Recommended)
  B. hours_unavailable transfers as system_failure. Seasonal check and ending as in A.
  C. Other: ___
Footprint: A ≈ 5 edits, net +35 words. B ≈ 5 edits, net +30 words.
Answer: A

### Q-45 · Knowledge questions: who answers what (resolves L-300, L-309, L-310, L-317, L-246)
Conflict: A KB non-answer mid-booking returns no_approved_answer, which is terminal, while informational_question says to resume. D-025 returns no_approved_answer for requires_tax_pro outside the Scheduler, while D-034 hands personal questions there to speak_to_tax_pro. "Do I need my 1099s?" fits both the in-agent tax_prep_and_records search and faq_agent. Identity-theft, fraud, and other-department phone questions have no owner. The Scheduler says "the Tax Pro covers it at the appointment" even on cancel, digital drop-off, and physical drop-off paths.
Options:
  A. In the Scheduler, a KB non-answer says it has no answer and resumes; elsewhere it returns no_approved_answer. requires_tax_pro outside the Scheduler hands back to speak_to_tax_pro (D-034 wins). tax_prep_and_records covers only what to bring or prepare for the appointment. Identity, fraud, and other-department questions call transfer_to_agent with out_of_scope. On cancel and drop-off paths, a personal question hands back to speak_to_tax_pro. (Recommended)
  B. As A, but identity, fraud, and other-department questions route to faq_agent.
  C. Other: ___
Footprint: A ≈ 7 edits, net +30 words. B ≈ 7 edits, net +25 words.
Answer: A

### Q-46 · Part 4: single match and appointment requests (resolves L-306, L-312)
Conflict: "1 Match: Confirm the Tax Pro" can mean a spoken confirm turn, which §1.2 Confirmation Strategy allows only for unverifiable data, or an internal check; if spoken, a caller "no" has no branch. Part 4 routes only a new tax_prep appointment to appointment_scheduler; reschedule, cancel, and other types fall to intent_change, which names no routingTarget, while Part 3 routes "any request to schedule, reschedule, or cancel".
Options:
  A. Treat a single match as confirmed by consequence: name the Tax Pro in the next turn, and a caller correction follows No Matches / Inactive. Route any appointment request in Part 4 to appointment_scheduler, matching Part 3. (Recommended)
  B. Speak a confirm turn for a single match; a "no" follows No Matches / Inactive. Appointment routing as in A.
  C. Other: ___
Footprint: A ≈ 4 edits, net +15 words. B ≈ 4 edits, net +20 words.
Answer: A

### Q-47 · Scheduler office and ladder paths (resolves L-307, L-311, L-301)
Conflict: A returning caller who keeps their Tax Pro but rejects the last-served office has no path to same_tax_pro_nearby_offices, so declining it ends in customer_declined_options. Every reschedule uses the reschedule ladder, whose Tax Pro and nearby-office rungs contradict a callback ("only reaches a confirmed Tax Pro") and a physical drop-off ("no Tax Pro named"). On invalid_constraints the agent re-runs readiness with no cap, and the rule sits in the find_offices_near item.
Options:
  A. A rejected last-served office moves to the same_tax_pro_nearby_offices rung. Callback and physical_drop_off reschedules use only the time and date rungs. invalid_constraints re-runs readiness once; a second transfers as system_failure. Move the rule to the find_available_slots entry. (Recommended)
  B. A rejected last-served office asks the Tax Pro trade-off and continues on the new_client ladder. Reschedule ladder and invalid_constraints as in A.
  C. Other: ___
Footprint: A ≈ 5 edits, net +30 words. B ≈ 5 edits, net +30 words.
Answer: A

### Q-48 · Scheduler entry context (resolves L-308, L-313, L-314)
Conflict: The Scheduler captures a "Tax Pro preference" and reads preferredTaxPro, but after D-027 it cannot resolve a named Tax Pro. Check Refund Status sends a second path (C-28, TaxReturnStatus 13-00, 13-02, or 14-00) to the Scheduler with no entryReason, while §1.1 defines entry behavior only for efile_rejection_retail. No agent answers "when is my appointment?": get_customer_appointments runs only on reschedule and cancel.
Options:
  A. A preferredTaxPro other than the prior or carried Tax Pro follows the Tax Pro Requests handback, and step 3 captures only the prior-Tax-Pro choice. The C-28 handoff is a null-operation entry (no new entryReason). The Scheduler answers appointment-details questions read-only after authentication, via get_customer_appointments, and returns offer_additional_help. (Recommended)
  B. Preferences and C-28 as in A. Appointment-details questions call transfer_to_agent with out_of_scope.
  C. Other: ___
Footprint: A ≈ 5 edits, net +35 words, adds one read path. B ≈ 4 edits, net +20 words.
Answer: A
