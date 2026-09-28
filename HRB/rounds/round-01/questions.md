# Round 1 questions

Write a letter, your own text, "defer", or "not an issue" after each `Answer:`. Then run `/continue`.
24 more Human items (L-069 to L-093) carry to round 2. The ledger has their summaries.

### Q-01 · Digital Drop-Off fulfillment contract (resolves L-036, L-037, L-038)
Conflict: The Scheduler calls `send_secure_link`, but §2 State 5 `objective` covers only the three appointment operations, and no outcome, idempotencyKey, or confirmation object exists for it. The request needs `customerRef`, which a new caller lacks (§5.2 send_secure_link). §2 DDO Rules confirm only the destination, while `scheduler_always` requires an explicit yes before any write, and `delivery_failed` has no path.
Options:
  A. DDO is a gated write. Add it to the objective. Read back the destination and require an explicit yes. Add `idempotencyKey` and `confirmation` to the request, and accept `newCustomer` when `customerRef` is absent. Add outcome `ddo_link_sent`. On `delivery_failed`, re-capture the destination once, then transfer as `system_failure`. (Recommended: matches the "every write" gate)
  B. DDO is fulfillment, not a write. Destination confirmation at capture is the consent. No idempotencyKey or confirmation object. The request sends `customerRef` or the captured contact. Add outcome `ddo_link_sent`. `delivery_failed` transfers as `system_failure`.
  C. Other: ___
Footprint: A ≈ 8 edits, net +70 words. B ≈ 6 edits, net +45 words.
Answer: A

### Q-02 · Callback slot search and ladder (resolves L-039, L-040, L-041, L-042)
Conflict: `find_available_cdas_slots` is in the Scheduler's tools, but no workflow step calls it, while the §5.2 check_search_readiness note sends callbacks through readiness and `find_available_slots` with a null method and floor (the floor is mandatory per `scheduler_always`). `broadening.scenario_selection` has no callback entry, so a callback falls to `new_client`, whose rungs offer DDO and nearby offices.
Options:
  A. Callbacks use `find_available_cdas_slots` only and skip readiness. Delete the callback sentence from the readiness note. Add scenario `callback` with rungs `time_window` and `date_window` only. (Recommended: smallest contract change)
  B. Callbacks use readiness and `find_available_slots`. Delete `find_available_cdas_slots` from the Scheduler tools and Part 5. Add scenario `callback` as in A, with `phone_callback` as the method and floor 1.
  C. Other: ___
Also answer: "CDAS" now means both the callback appointment and any slot with no named Tax Pro (§2 State 3 CDAS). Should it mean (i) callbacks only, with the unnamed slot described another way, or (ii) both, defined once in Part 5 Conventions?
Footprint: A ≈ 7 edits, net +30 words. B ≈ 6 edits, net -80 words.
Answer: B. , ii

### Q-03 · Tax Pro to Scheduler handoff context (resolves L-043, L-044, L-045)
Conflict: Part 4 returns `route_intent` with `appointmentType` callback and a confirmed Tax Pro, but `terminal_payload_contract` and `context_envelope` carry neither, so the Scheduler must re-ask. `routed_to_message` fires when "no callback slots were available", which Part 4 cannot observe. The inactive-Tax-Pro route to the Scheduler (§4 No Matches / Inactive) names no type or outcome.
Options:
  A. Carry `appointmentType`, `taxProRef`, and `officeRef` on `route_intent` to `appointment_scheduler`, and add `appointmentType` to `context_envelope`. Delete "or no callback slots were available". The inactive-Tax-Pro route uses `routed_to_scheduler` with `appointmentType` null. (Recommended)
  B. Pass nothing new; the Scheduler re-asks type and Tax Pro. Delete the no-slots clause. The inactive-Tax-Pro route uses `routed_to_scheduler`.
  C. Other: ___
Footprint: A ≈ 6 edits, net +35 words. B ≈ 3 edits, net -10 words.
Answer: A

### Q-04 · Terminal payload completeness (resolves L-046, L-047, L-048, L-049)
Conflict: Outcomes carry `appointmentType`, `appointmentRef`, `transferReason`, `supportHoursSpoken`, and `sourceUtterance`, which `terminal_payload_contract` never lists. Several outcomes omit the mandatory `transactionOccurred`, `callContained`, or `intent`. `callContained` is undefined: it is true for leave_message in Parts 3-4 but false in `transfer_unavailable`. `transferReason` has no enum.
Options:
  A. List every carried field in the contract. Define `callContained` as true when no live human is needed, so message handbacks are true. Fill each outcome's missing mandatory values. Build a `transferReason` enum from values the spec already uses, plus `caller_requested` and `automation_blocked`. (Recommended)
  B. As A, but `callContained` is false for any handback that leaves the agent for a transfer, message, or `capture_intent`.
  C. Other: ___
Footprint: either ≈ 12 edits, net +90 words.
Answer: A

### Q-05 · MyBlock mention (resolves L-050)
Conflict: §4 Fulfillment Priority step 2, `tax_pro_always`, both Part 4 workflows, and dialogues 4A and 4E require "you can also message your tax pro anytime through the MyBlock app". §1.2 Zero Web Deflection forbids any app name, with DDO as the only exception. The sentence also makes the 4A and 4E turns four sentences long.
Options:
  A. Delete the MyBlock mention everywhere in Part 4, including the frozen 4A and 4E Agent lines. (Recommended: Part 1 wins under C-1)
  B. Add MyBlock messaging as a second named exception in §1.2 and `global_never`. Keep Part 4, and cut the 4A and 4E turns to three sentences.
  C. Other: ___
Footprint: A ≈ 6 edits, net -60 words. B ≈ 4 edits, net +20 words.
Answer: B. It's known as "Online Message Center for Tax Pro Review"

### Q-06 · outcome_unknown handoff (resolves L-051)
Conflict: §2 State 4 Indeterminate Writes says to hand back at once, and `global_outcomes.outcome_unknown` uses nextAction transfer. The §1.4 line promises a person, and `global_always` says to call `transfer_to_agent` before promising a person. If `transfer_to_agent` returns agent_unavailable, no outcome keeps `idempotencyKey`.
Options:
  A. On outcome_unknown, call `transfer_to_agent` with `transferReason` outcome_unknown and `idempotencyKey` (as the §5.1 example shows). On agent_available, speak the §1.4 outcome_unknown line. On agent_unavailable, speak the matching agent_unavailable line. Return `outcome_unknown` with `idempotencyKey` either way. (Recommended)
  B. Never call `transfer_to_agent` on outcome_unknown. Speak the §1.4 line, return the payload with nextAction transfer, and let Head of Call transfer.
  C. Other: ___
Footprint: A ≈ 4 edits, net +30 words. B ≈ 2 edits, net +10 words.
Answer: A

### Q-07 · Ladder progress and exhaustion (resolves L-052, L-053)
Conflict: `invalidation.ladder_state` resets the ladder on any scheduling-constraint change except a method change from a channel rung. Accepting a time, date, office, or Tax Pro rung is such a change, so the ladder restarts at the primary offer. After every rung is declined, both `customer_declined_options` (contained close) and `no_acceptable_availability` (transfer) match.
Options:
  A. A change made by accepting any rung does not reset the ladder; only a caller-initiated constraint change does. When every rung is declined, return `no_acceptable_availability`. `customer_declined_options` covers a caller who stops before the ladder is exhausted or declines the cancellation gate. (Recommended)
  B. Same reset fix as A, but exhaustion returns `customer_declined_options` (contained, no transfer). `no_acceptable_availability` applies only when the caller asks for a person.
  C. Other: ___
Footprint: A ≈ 3 edits, net +10 words. B ≈ 3 edits, net +15 words.
Answer: A

### Q-08 · Peak capacity scope (resolves L-054)
Conflict: `broadening.scenario_selection` item 7 switches any scenario to `peak_capacity` on office_at_capacity at peak. Its rungs offer virtual and DDO, which emerald_advance (in person only), reschedule (method fixed), physical drop-off, and tax_notice ladders do not allow.
Options:
  A. Item 7 applies only to `new_client`, `returning_same_tax_pro`, `returning_tax_pro_unavailable`, and `same_day` on schedule_new. Other scenarios keep their own ladders. (Recommended)
  B. Item 7 applies to all scenarios, but peak rungs skip any method that the type or operation forbids.
  C. Other: ___
Footprint: either ≈ 2 edits, net +15 words.
Answer: A

### Q-09 · Office reference for Office Information and Tax Pro agents (resolves L-055, L-056)
Conflict: Parts 3 and 4 use `routedOfficeRef`, but the envelope carries only `dialedOfficeNumber`, and only the Scheduler's `find_offices_near` resolves one to the other. `get_office_details` accepts only `officeRef` or `postalCode`, so a caller-named office ("the Oak Ridge office") cannot be resolved.
Options:
  A. Head of Call resolves the dialed number and passes `routedOfficeRef` in the envelope to every agent (§1.1 and `context_envelope`). Office Information resolves a named office by capturing a ZIP and matching `officeName` in the `get_office_details` `nearbyOffices` list. (Recommended)
  B. Give the Office Information and Tax Pro agents `find_offices_near` for both rollover resolution and named-office lookup.
  C. Other: ___
Footprint: A ≈ 4 edits, net +40 words. B ≈ 5 edits, net +45 words.
Answer: A

### Q-10 · Routing targets and out-of-scope handbacks (resolves L-057, L-058, L-059, L-060)
Conflict: `routingTarget` lists `tax_prep` and "named destination" but has no value for the Office Information or Tax Pro agents. Open claim, Tax Pro Review, and readiness `out_of_scope` hand back with no target. The extension ladder's self-filing support transfer has no owner, and its tax_prep follow-up uses `intent_changed` inside the Scheduler's own scope. `appointment_requested` is never emitted and overlaps `intent_changed`.
Options:
  A. Set `routingTarget` to refund_status, faq_agent, appointment_scheduler, office_information, or speak_to_tax_pro. Open claim, Tax Pro Review, `out_of_scope`, and self-filing support call `transfer_to_agent` with `transferReason` out_of_scope. The tax_prep follow-up returns `route_intent` to appointment_scheduler. Delete `appointment_requested`. (Recommended)
  B. As A, but keep `appointment_requested` for scheduling handbacks from Parts 3 and 4, and use `intent_changed` only for other targets.
  C. Other: ___
Footprint: A ≈ 9 edits, net -20 words. B ≈ 10 edits, net -5 words.
Answer: A

### Q-11 · Informational questions across agents (resolves L-061, L-062, L-063, L-064)
Conflict: Every agent answers informational questions with `search_knowledge_base` in all categories. Part 4 alone routes general tax, login, and account questions to `faq_agent` and refund status to `refund_status`. §1.2 Hours: One Source names no source, so the Scheduler may answer office hours from the knowledge base.
Options:
  A. Apply Part 4's routing in all agents: refund status goes to `refund_status`, and login, account, and general tax questions go to `faq_agent`. `search_knowledge_base` answers only mid-task questions in `appointments_and_logistics` and `tax_prep_and_records`. Office hours and phone numbers come only from the Part 3 tools; the Scheduler hands them back to office_information. (Recommended)
  B. Keep `search_knowledge_base` in all agents for all categories. Part 4's routing applies only to the reason elicited at the start of a Part 4 call. Name `get_office_details` as the hours source.
  C. Other: ___
Footprint: A ≈ 8 edits, net +30 words. B ≈ 3 edits, net +15 words.
Answer: A

### Q-12 · Live-agent requests and local-desk contact (resolves L-065, L-066, L-067, L-068)
Conflict: Every agent calls `transfer_to_agent` on an explicit live-agent request (§1.4 barging row). The flow spec's universal rule sends "agent", a synonym, or DTMF 0 from any node in any flow to the Request Live Agent flow (`deterministic_flows/HRB-Future-IVA-Deterministic-Flow-Spec.md`, §4). The frozen barging row has the agent state support hours and offer a message on agent_unavailable, while the next row gives both to the deterministic flow. Part 3 handles "front desk" requests but lacks Part 4's no-live-transfer-to-local-desk rule and the `knownSoFar` mapping.
Options:
  A. Agents keep `transfer_to_agent` for explicit central live-agent requests (this round moved that rule into `global_always`). Edit the frozen barging row to use the two agent_unavailable rows as written. Move the no-local-desk-transfer rule to `global_never`, and keep the `knownSoFar` mapping only in §5.1 transfer_to_agent. (Recommended)
  B. Agents stop and return nextAction transfer with no tool call, so the Request Live Agent flow handles the request. Other changes as in A.
  C. Other: ___
Footprint: A ≈ 6 edits, net -20 words. B ≈ 10 edits, net -30 words.
Answer: A
