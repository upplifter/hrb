# Round 9 · Lens A findings

Saved by the orchestrator from the reviewer's reply.

### A-01 · Part 4 callback and message handoffs never say which office officeRef is
Anchor: §4 Fulfillment: CDAS Callback Appointment > Handoff; §4 Fulfillment: Leave a Message > Handoff; §4 State 2 `tax_pro_always` callback item; §4 `agent_specific_outcomes.routed_to_scheduler`; §1.5 `terminal_payload_contract` (taxProRef and officeRef clause)
Severity: Medium
Class: Human
Issue: Part 4 hands back "the confirmed taxProRef and officeRef" on a callback and "any known ... officeRef" on a message. Nothing names the source. Four values fit: `routedOfficeRef` (the dialed field office), `find_customer` `priorOfficeRef`, `search_tax_pro_by_name` `primaryOfficeId`, or an office matched from a captured ZIP. In the Scheduler a carried officeRef outranks entryPoint and routedOfficeRef, and the callback ladder searches "callback slots at the selected office, with the carried Tax Pro". If the dialed office is carried and the Tax Pro works elsewhere, no slots come back and the call ends in `no_acceptable_availability`. `routed_to_scheduler` for another Tax Pro also carries officeRef "only when known", from the same unnamed source.
Fix: Options:
A. (Recommended) Name the source once in prose and once in JSON. Prose: add a §4 Fulfillment Priority step 5: "officeRef: the Tax Pro's primaryOfficeId on a by-name request, priorOfficeRef for the prior Tax Pro, routedOfficeRef for another Tax Pro; null when none applies." JSON: add the same sentence to `tax_pro_always[6]`, and change `routed_to_scheduler` "with officeRef only when known" to "with officeRef per tax_pro_always". 3 edits, about +40 words; trim the "confirmed" qualifier in both Handoff bullets to offset.
B. Do not carry officeRef on a callback; the Scheduler resolves the office by entryPoint. 4 edits, about -15 words. Fails when the Tax Pro does not work at the resolved office.
C. Carry `routedOfficeRef` when present, otherwise the Tax Pro's office. Same footprint as A. Same failure as B on rollover calls.

### A-02 · A caller who rejects the carried Tax Pro on a callback has no owner
Anchor: §2 State 5 `invalidation.partial_acceptance`; `broadening.ladders.callback`; §2 State 2 Appointment Type Rules > Tax Pro Requests
Severity: Medium
Class: Human
Issue: D-090 makes rejecting a proposed Tax Pro while keeping the office a caller-initiated change. `partial_acceptance` clears taxProRef and restarts "at its primary offer". The callback primary is "Callback slots at the selected office, with the carried Tax Pro", and that value was just cleared. Tax Pro Requests hands "a callback without carried taxProRef" back to speak_to_tax_pro, and D-018 says a callback only reaches a confirmed Tax Pro. `partial_acceptance` instead restarts the callback ladder, which would book a callback with no Tax Pro.
Fix: Options:
A. (Recommended) Append to `invalidation.partial_acceptance`: "On callback, hand back intent_changed with routingTarget speak_to_tax_pro." 1 JSON edit, about +12 words. Follows Tax Pro Requests.
B. Return `customer_declined_options`. Append "On callback, return customer_declined_options." and add the case to that outcome. 2 edits, about +18 words. No path to another Tax Pro.
C. Book a CDAS callback with any qualified Tax Pro. 2 edits, about +15 words. Reverses D-018.

### A-03 · A logistics question has two owners in Parts 3 and 4, and "mid-task" is undefined
Anchor: §1.5 `global_always` search_knowledge_base item, informational-question item, and followUpTopics item; §3 State 2 `agent_specific_tools.search_knowledge_base`; §4 State 2 `agent_specific_tools.search_knowledge_base`; §2 State 3 Informational Interruptions
Severity: Medium
Class: Human
Issue: `global_always` tells every agent to answer a "mid-task" appointments_and_logistics or tax_prep_and_records question with `search_knowledge_base`. It also sends an "out-of-task appointments_and_logistics" question to faq_agent (D-097). Neither term is defined. In the Scheduler, "mid-booking" is the only trigger, so a question at the null-operation question, during cancel_existing, or during an appointment-details answer is unclear. In Parts 3 and 4 "What should I bring?" is tax_prep_and_records, so it is KB when mid-task and faq_agent when out-of-task. Parts 3 and 4 still list `search_knowledge_base`, and `global_always` has an office_information-only requires_tax_pro clause that presumes Part 3 queries the KB.
Fix: Options:
A. (Recommended) Scope the KB to the Scheduler. In the `global_always` KB item, replace "only for a mid-task question in" with "only for a question asked during a Scheduler booking or reschedule in". Delete `search_knowledge_base` from Part 3 and Part 4 `agent_specific_tools`. Delete the office_information requires_tax_pro sentence from the followUpTopics item. 4 edits, about -25 words; removes a tool from two agents.
B. Keep the KB in all agents and define the term once: "A question is mid-task when it is about the appointment being booked, changed, or canceled, or about the caller's current office or Tax Pro request; every other one is out-of-task." 1 edit, about +30 words.

Summary: 3 findings (0 Critical, 0 High, 3 Medium, 0 Low). 0 Safe, 3 Human.
