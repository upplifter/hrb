# Round 2 questions

Write a letter, your own text, "defer", or "not an issue" after each `Answer:`. Then run `/continue`.
The 12 questions cover every High item. The remaining Medium items (L-072 to L-091 not listed below, and L-134 to L-165 not listed below) carry to round 3; the ledger has their summaries.

### Q-13 · Recovery line before or after transfer_to_agent (resolves L-129)
Conflict: §2 State 1 Authentication Logic and the `scheduler_always` unregistered-ANI item speak the recovery line ("Let me get you to someone...") and then call `transfer_to_agent`. `global_always` requires the call before any promise of a person, and D-007 settled that order only for outcome_unknown. On agent_unavailable, the caller has already heard a person promised.
Options:
  A. Use the D-007 order for every transfer: call `transfer_to_agent` first. On agent_available, speak the path's §1.4 recovery line. On agent_unavailable, speak only the matching agent_unavailable row. (Recommended: one rule for every transfer)
  B. Keep the current order for recovery lines. Narrow `global_always` so a §1.4 recovery line may precede the call. On agent_unavailable, speak the agent_unavailable row after it.
  C. Other: ___
Footprint: A ≈ 5 edits, net +10 words. B ≈ 3 edits, net +15 words.
Answer: A

### Q-14 · Which finalOutcome a transfer returns (resolves L-130, L-131, L-157, L-158)
Conflict: After a reason transfer (e.g., system_failure), agent_available matches both `transferred_to_human` and the reason outcome. agent_unavailable matches `transfer_unavailable`, while the reason outcome fixes nextAction transfer. `outcome_unknown` fixes callContained false even on a message handback, against the D-005 definition. Several triggers (none_nearby, a type change on reschedule, rejected, change_not_allowed, office lookup failure) have no transferReason, and not_cancelable fits both validation_failed and automation_blocked. A failed `transfer_to_agent` call returns only `issue`, with no handler.
Options:
  A. On agent_available, return the reason outcome (`transferred_to_human` only for caller_requested). On agent_unavailable, return `transfer_unavailable` carrying transferReason, except `outcome_unknown`, which keeps its name and takes nextAction and callContained from `transfer_unavailable`. Map none_nearby to no_acceptable_availability; type change, rejected, change_not_allowed, and not_cancelable to automation_blocked; office lookup failure to system_failure. Treat a failed transfer call as agent_unavailable with no message. (Recommended)
  B. Always return `transferred_to_human` or `transfer_unavailable`. Delete the reason outcomes from `global_outcomes`; their reasons live only in transferReason. Mapping and failed-call handling as in A.
  C. Other: ___
Footprint: A ≈ 10 edits, net +40 words. B ≈ 12 edits, net -120 words.
Answer: A

### Q-15 · Keeping the Tax Pro across an office change (resolves L-132, L-145, L-147)
Conflict: §2 State 3 Dynamic State Invalidation: Location & Time and `invalidation.upstream_change` purge the Tax Pro on any location change, but the `same_tax_pro_nearby_offices` rung (returning_same_tax_pro, reschedule) changes the office to keep the Tax Pro. `scenario_selection` item 7 switches returning_same_tax_pro to peak_capacity, which offers any Tax Pro at three offices with no trade-off. A none_nearby result on a nearby-office rung transfers the caller and skips the later rungs.
Options:
  A. Accepting `same_tax_pro_nearby_offices` keeps taxProRef; every other location change still purges it. Before item 7 switches returning_same_tax_pro to peak_capacity, ask the Tax Pro trade-off; on "stay", keep the returning_same_tax_pro ladder. none_nearby on a nearby-office rung exhausts that rung and moves to the next; at the first office lookup it still transfers. (Recommended)
  B. As A, but item 7 never applies to returning_same_tax_pro, so no trade-off is asked at peak.
  C. Other: ___
Footprint: A ≈ 6 edits, net +45 words. B ≈ 5 edits, net +30 words.
Answer: A

### Q-16 · Digital drop-off gaps after D-001 (resolves L-094, L-133, L-144, L-156, L-166)
Conflict: `send_secure_link` accepts `newCustomer`, but `scheduler_never` says only `book_appointment` creates a profile. The tax_notice DDO fallback must "send all five notice values", but `send_secure_link` has no `taxNoticeDetails` field. `workflow.schedule_new` step 5 offers a text confirmation and the full readback on DDO too. `send_secure_link` has no outcome_unknown result, so D-007 cannot fire. §2 State 2 DDO Rules > Rescheduling needs "a new link in a separate invocation" with no owner.
Options:
  A. `send_secure_link` creates the profile at commit, as `book_appointment` does (edit `scheduler_never`). Add `taxNoticeDetails` to the `send_secure_link` request. On DDO, skip the text offer; the destination readback is the whole gate. Add result outcome_unknown to `send_secure_link`. A DDO change request is a new schedule_new DDO send in the Scheduler. (Recommended)
  B. `send_secure_link` never creates a profile; `newCustomer` only identifies the caller. Drop the notice values on the DDO fallback. Gate, outcome_unknown, and DDO change as in A.
  C. Other: ___
Footprint: A ≈ 8 edits, net +35 words. B ≈ 7 edits, net -5 words.
Answer: A

### Q-17 · Tax Pro and office context on the handoff to the Scheduler (resolves L-095, L-141, L-159)
Conflict: After D-004, Part 4 carries `taxProRef` and `officeRef` on route_intent, but §1.1 and `context_envelope` gained only `appointmentType`, so `ladders.callback` "with the carried Tax Pro" has no source. D-003 makes every callback CDAS, so the `scheduler_always` CDAS phrasing hides the carried Tax Pro's name. §4 Out-of-Scope (New Appointment) covers only in-person or virtual tax prep, so a phone tax_prep request fits both a new appointment and a callback.
Options:
  A. Add `taxProRef` and `officeRef` to §1.1 and `context_envelope` as "set by a prior agent's handoff; use without re-asking". Speak the carried Tax Pro's name on a callback slot; CDAS phrasing applies only when no Tax Pro is carried. Any new tax_prep request, in any method, goes to appointment_scheduler as a new appointment; callback is only for reaching a confirmed Tax Pro. (Recommended)
  B. Carry the Tax Pro in `knownPreferences.preferredTaxPro` and the office in `routedOfficeRef`, adding no envelope field. Phrasing and phone tax_prep as in A.
  C. Other: ___
Footprint: A ≈ 5 edits, net +30 words. B ≈ 4 edits, net +15 words.
Answer: A

### Q-18 · Extension ladder exits (resolves L-096, L-148, L-149)
Conflict: §2 State 2 Tax Extension commits the extension, then returns route_intent when the caller also wants tax prep. The `scheduler_always` tax_extension item ties route_intent only to the ladder's final self-filing rung. On that rung, nothing picks the tax_prep handback over the support transfer, "close the extension transaction" refers to nothing committed, a caller who wants neither has no exit, and no finalOutcome is named. `sourceUtterance` is set to a scripted string, not the caller's words.
Options:
  A. Keep both paths. On the self-filing rung, ask one either-or: a tax_prep appointment or help with self-filing. tax_prep returns `intent_changed` with routingTarget appointment_scheduler; self-filing help calls `transfer_to_agent` (out_of_scope); neither returns `customer_declined_options`. Carry the caller's own words as sourceUtterance. Add the committed-extension path to the JSON item. (Recommended)
  B. As A, but delete the committed-extension-plus-tax-prep path from §2 State 2, so only the self-filing rung hands back for tax_prep.
  C. Other: ___
Footprint: A ≈ 5 edits, net +10 words. B ≈ 5 edits, net -20 words.
Answer: A

### Q-19 · capture_intent and unclear_intent (resolves L-069, L-070, L-071)
Conflict: nextAction `capture_intent` is listed in `terminal_payload_contract` but never defined, and it overlaps `offer_additional_help`. The contract says "Resolve unclear_intent before return" with no owner or enum value. §3 Intent Scope > unclear_intent says "transfer or route to leave a message" with no rule to choose, and Part 4 asks whether the caller wants a callback.
Options:
  A. Define `capture_intent` as "Head of Call re-asks the caller's need; use only when nothing was served". Each agent reprompts an unclear intent once, then returns `capture_intent`. Delete "Resolve unclear_intent before return" and the Part 3 transfer-or-message clause. (Recommended)
  B. Delete `capture_intent`; the Part 3 OPEN branch returns `offer_additional_help`. An intent still unclear after one reprompt calls `transfer_to_agent` with clarification_exhausted in every agent.
  C. Other: ___
Footprint: A ≈ 5 edits, net +15 words. B ≈ 6 edits, net -10 words.
Answer: A

### Q-20 · Write result handling (resolves L-073, L-092, L-093)
Conflict: The `scheduler_always` tool-result item re-gates on not_confirmed with no cap or exit. No tool result triggers `appointment_already_canceled`, though `closure.continuation_context` says a reference that "comes back canceled" is handled that way. §5.2 reschedule_appointment lists no not_confirmed or rejected result, though the Scheduler handles both.
Options:
  A. Re-gate once on not_confirmed; a second not_confirmed transfers as validation_failed. Add status canceled to `get_customer_appointments`, which triggers `appointment_already_canceled` on cancel_existing. Add not_confirmed and rejected to the reschedule_appointment results. (Recommended)
  B. Treat not_confirmed as validation_failed with no re-gate. Delete `appointment_already_canceled` and the continuation_context clause; a canceled reference is handled as none_found. Reschedule results as in A.
  C. Other: ___
Footprint: A ≈ 5 edits, net +25 words. B ≈ 5 edits, net -40 words.
Answer: A

### Q-21 · Consent after an interruption or correction (resolves L-076, L-155)
Conflict: `interruptions.informational_question` lets a yes given before an interruption stand, while `scheduler_always` requires an explicit yes "immediately before any write". The mid-gate correction rule (§2 State 4 The Pre-Commit Gate, `scheduler_always`) re-runs readiness and search for every correction, including a text-destination fix that `invalidation.text_confirmation` treats as outside the scheduling constraints.
Options:
  A. Any interruption after the yes voids it: re-read the gate and ask again before the write. A text-destination correction updates only the destination and re-reads the gate, with no readiness or search. (Recommended)
  B. A yes survives an informational interruption when nothing changed; add that exception to the "immediately before any write" rule. Text-destination correction as in A.
  C. Other: ___
Footprint: A ≈ 4 edits, net +5 words. B ≈ 3 edits, net +20 words.
Answer: A

### Q-22 · Who offers a message (resolves L-082, L-083)
Conflict: §1.3 Leave-a-Message Ownership returns `leave_message_offer` only when a transfer is unavailable, and gives the offer to the deterministic flow. §3 Office Contact Triage > If CLOSED returns `leave_message_offer` with no transfer tried. §4 Fulfillment Priority step 1 and dialogue 4A have the agent speak the message option itself.
Options:
  A. Widen §1.3: `leave_message_offer` also applies when the caller's target office is closed, and Part 4 may name the message option among its fulfillment choices. (Recommended: matches current Part 3 and Part 4 behavior)
  B. Keep §1.3 as written. Part 3 If CLOSED returns `offer_additional_help`, and Part 4 offers only the callback, returning `leave_message` when the caller asks for a message.
  C. Other: ___
Footprint: A ≈ 3 edits, net +20 words. B ≈ 6 edits, net -15 words.
Answer: A

### Q-23 · DOB repair, PII payloads, and tax-advice bans (resolves L-086, L-087, L-088)
Conflict: §2 State 1 New Customer DOB Check re-asks the year after no_match, while `global_always` says date of birth never receives a confirmation turn. §1.2 Data Sanitization exempts only `find_customer` payloads, but `book_appointment` and `send_secure_link` `newCustomer` also carry dateOfBirth and ssnLast4. `global_never` omits the §1.2 bans on interpreting notices and quoting loan terms, fees, or penalties.
Options:
  A. The year re-ask is a repair, not a confirmation; name it as an exception in `global_always`. Extend the sanitization exception to the `newCustomer` payloads of `book_appointment` and `send_secure_link`. Add the notice, loan-term, fee, and penalty bans to `global_never`. (Recommended)
  B. Delete the year re-ask (§2 State 1 bullet and the last 1A Agent turn). Payload exception and `global_never` as in A.
  C. Other: ___
Footprint: A ≈ 4 edits, net +25 words. B ≈ 5 edits, net +5 words.
Answer: B

### Q-24 · Knowledge base results and question routing (resolves L-097, L-137, L-138, L-139, L-143)
Conflict: §5.1 search_knowledge_base says requires_tax_pro "routes to a Tax Pro" with no owner, and no result maps to `no_approved_answer`. `global_always` says to ignore followUpTopics, while Part 5 builds the clarification_needed path from them. `scheduler_never` answers loan, fee, and penalty questions from the knowledge base, which D-012 limits to two categories. Income tax course and password questions have a target only in Part 4, and the Speak to a Tax Pro agent has no owner for office hours.
Options:
  A. On clarification_needed, ask once from followUpTopics and send the choice as clarifier. On requires_tax_pro in the Scheduler, say the Tax Pro covers it at the appointment and resume; elsewhere return `no_approved_answer`. Any other non-answer returns `no_approved_answer`. Loan, fee, penalty, income tax course, and password questions go to faq_agent in every agent. Every agent hands office hours and phone questions to office_information. (Recommended)
  B. Never use clarification: delete the clarifier path from Part 5. requires_tax_pro and every other non-answer return `no_approved_answer`. Routing as in A.
  C. Other: ___
Footprint: A ≈ 7 edits, net +30 words. B ≈ 7 edits, net -20 words.
Answer: A
