- anchor: Part 2 State 5 agent_specific_tools.send_secure_link
  also: Part 2 State 5 objective | §1.5 terminal_payload_contract | Part 2 State 5 agent_specific_outcomes | §5.2 send_secure_link
  severity: Critical
  claim: F-01 still holds: the Scheduler executes a DDO write that sits outside its three-operation objective, has no outcome, no idempotency key, and no path for a net-new caller without customerRef.
  evidence: "complete at most one schedule_new, reschedule_existing or cancel_existing retail appointment transaction" | "For digital drop-off, execute send_secure_link instead of book_appointment." | "For new clients, omit customerRef and send the newCustomer object." | "Generate idempotencyKey as interactionId-slotRef for booking"
  class: human
  decision: ddo-write-ownership-outcome-and-new-customer-contract

- anchor: Part 2 State 2 Digital Drop-Off (DDO) Rules
  also: Part 2 State 5 scheduler_always | Part 2 State 5 invalidation.ladder_state | §5.2 send_secure_link
  severity: High
  claim: F-02 still holds: every write requires an explicit yes, but the DDO rules only confirm the destination, and the send_secure_link request carries no confirmation evidence.
  evidence: "Capture and confirm the secure-link destination (SMS or Email)." | "Require an explicit spoken yes immediately before any write." | "other than a method change made by accepting a channel rung"
  class: human
  decision: ddo-consent-contract

- anchor: Part 2 State 5 agent_specific_tools.find_available_cdas_slots
  also: §5.2 check_search_readiness | §5.2 find_available_cdas_slots | Part 4 State 1 Fulfillment: CDAS Callback Appointment | Part 4 State 2 objective
  severity: High
  claim: F-03 still holds: callback slot search has two tools with different contracts, and no Scheduler workflow step uses find_available_cdas_slots.
  evidence: "Searches Appointment Manager for 15-minute Callback Appointment (CDAS) slots" | "For CDAS callbacks, send appointmentType = callback; appointmentMethod, taxProRatingFloor, and timeWindow may be null." | "triages the request but does not book the calendar slot"
  class: human
  decision: cdas-search-tool-owner

- anchor: Part 2 State 5 broadening.scenario_selection
  also: Part 2 State 5 broadening.ladders.new_client | Part 2 State 2 Appointment Type Rules (type table, callback row) | Part 2 State 3 Ladders
  severity: High
  claim: F-04 still holds: scenario_selection has no callback entry, so a callback falls through to new_client, whose rungs offer digital drop-off and nearby offices that the callback type does not permit.
  evidence: "callback | phone_callback | 15-minute CDAS callback." | "10 Otherwise: new_client."
  class: human
  decision: callback-scenario-and-ladder

- anchor: §1.5 terminal_payload_contract
  also: Part 4 State 2 tax_pro_always | Part 4 State 1 Fulfillment: CDAS Callback Appointment | Part 2 State 5 scheduler_always (callback reason)
  severity: High
  claim: F-05 still holds: Part 4's callback handback carries appointmentType, which the terminal contract does not define, and has no slot for the elicited reason, taxProRef, or officeRef.
  evidence: "return route_intent with routingTarget set to appointment_scheduler and appointmentType set to callback" | "On route_intent include routingTarget (refund_status, faq_agent, appointment_scheduler, tax_prep, or named destination)." | "taxProRef and officeRef when routing to leave a message"
  class: human
  decision: callback-handback-payload-fields

- anchor: Part 4 State 2 tax_pro_always (MyBlock)
  also: Part 4 State 1 Fulfillment Priority | Part 4 Mini-Dialogues 4A, 4E | Part 4 State 2 workflow step 4/5 | §1.2 Zero Web Deflection & Prohibited Speech | Part 4 State 2 tax_pro_never
  severity: High
  claim: F-06 still holds: Part 4 requires an app-name mention that the Part 1 zero-web-deflection rule forbids and whose only exception is DDO.
  evidence: "Never speak a URL, website, portal, or app name." | "Mention MyBlock ('For your convenience, you can also message your tax pro anytime through the MyBlock app')."
  class: human
  decision: myblock-mention-vs-zero-web-deflection

- anchor: §1.5 global_outcomes.customer_abandoned
  also: §1.2 Input Exhaustion & Silence > Abandonment
  severity: High
  claim: F-10 still holds in part: the §1.2 prose now says an unanswered gate terminates, but global_outcomes.customer_abandoned still says it transfers.
  evidence: "An unanswered gate is not abandonment, it runs the No-Input Rule, then terminates." | "an unanswered gate runs the reprompt rule, then transfers."
  class: safe
  fix: In global_outcomes.customer_abandoned, replace "runs the reprompt rule, then transfers" with "runs the no-input rule, then terminates".

- anchor: Part 3 State 2 office_never
  also: Part 3 State 1 Office Contact Triage | Part 3 Mini-Dialogue 3C | Part 3 State 2 agent_specific_tools.transfer_to_agent | §1.4 Caller-Initiated Barging row
  severity: Medium
  claim: F-07 still holds: Part 3 handles local-desk requests but lacks Part 4's prohibition on live transfers to local desks, and "local office contact" is never defined against barging.
  evidence: "Never perform live phone transfers to local office desks or individual Tax Professionals." | "Transfer me to someone at the front desk." | "Caller-Initiated Barging (explicit central live-agent request, not local office contact)"
  class: human
  decision: local-office-contact-vs-barging-owner

- anchor: Part 2 State 5 agent_specific_tools.search_knowledge_base
  also: Part 3 State 2 agent_specific_tools.search_knowledge_base | Part 4 State 2 agent_specific_tools.search_knowledge_base | interruptions.informational_question (all three agents) | Part 4 State 1 Out-of-Scope (FAQ Agent)
  severity: Medium
  claim: F-08 still holds: every agent may answer FAQ-scope questions from the knowledge base, and only Part 4 routes them to faq_agent.
  evidence: "If the elicited reason is general tax questions, login difficulty, MyBlock credential issues, password resets, account access" | "call search_knowledge_base, answer in one brief turn" | "Acceptable category enums: digital_account_support, financial_products, identity_and_fraud, tax_prep_and_records"
  class: human
  decision: kb-category-scope-per-agent

- anchor: Part 2 State 5 agent_specific_tools.search_knowledge_base
  also: Part 3 State 1 Office Contact Triage | §1.2 Hours: One Source, Spoken Once | §1.5 terminal_payload_contract (routingTarget)
  severity: Medium
  claim: F-09 still holds: the Scheduler can answer office hours or phone questions from knowledge-base categories, while office facts come from Part 3 tools, and routingTarget has no office-information value.
  evidence: "Never invent hours from memory." | "Relies strictly on `check_office_open_status`" | "On route_intent include routingTarget (refund_status, faq_agent, appointment_scheduler, tax_prep, or named destination)."
  class: human
  decision: office-facts-source-and-route

- anchor: §1.5 global_never
  also: Part 2 State 5 scheduler_never | Part 2 State 5 closure.re_entry | Part 2 State 5 interruptions.cancel_said | Part 3 State 2 office_never | Part 4 State 2 tax_pro_never
  severity: Medium
  claim: F-11 still holds: no rule bars tool calls after an agent decides to hand back or commits; the only limit is one transaction per invocation.
  evidence: "One invocation commits at most one transaction." | "return exactly one terminal payload" | "close the committed transaction normally and hand back intent_changed rather than starting a second transaction here"
  class: human
  decision: post-handback-tool-lock

- anchor: §1.5 terminal_payload_contract (intent)
  also: Part 3 State 1 Intent Scope & Disambiguation | Part 4 State 2 tax_pro_always (unclear intent)
  severity: Medium
  claim: F-12 still holds: the contract requires resolving unclear_intent, but the intent enum omits it, no owner is named, and Parts 3 and 4 resolve unclear intent differently.
  evidence: "Resolve unclear_intent before return." | "intent (schedule_appointment, office_info, office_contact, speak_to_tax_pro, or informational)" | "If intent is unclear, ask whether the caller wants a callback appointment" | "If unresolved after one reprompt, transfer or route to leave a message."
  class: human
  decision: unclear-intent-owner

- anchor: Part 3 State 2 agent_specific_outcomes.office_contact_triage_complete
  also: Part 3 State 1 Office Contact Triage > If CLOSED | Part 3 State 2 office_always | Part 3 State 2 workflow.office_contact_flow step 4 | Part 3 Mini-Dialogue 3B
  severity: Medium
  claim: F-13 still holds: after giving a closed office's hours and phone number, Part 3 always returns leave_message_offer, whether or not the caller's need is met.
  evidence: "provide the main line number, then stop speaking and return nextAction = leave_message_offer." | "Caller received office contact details for a closed office or explicitly requested a message."
  class: human
  decision: closed-office-contact-next-action

- anchor: Part 2 State 5 scheduler_always (callback)
  also: Part 2 State 2 Appointment Type Rules (type table, callback row) | §1.5 global_never | §1.3 Leave-a-Message Ownership | §5.2 book_appointment request
  severity: Medium
  claim: F-14 still holds: the Scheduler captures the caller's reason into appointmentNotes, while agents never capture message content, and nothing separates the two.
  evidence: "On callback, capture the reason for the call in appointmentNotes." | "never capture message content" | "Received IRS letter CP2000"
  class: human
  decision: appointment-notes-vs-message-content

- anchor: Part 3 State 2 office_always (closed_for_season)
  also: Part 2 State 3 Office Resolution > Off-Season Closure | Part 2 State 5 scheduler_always (off-season) | Part 3 State 1 Office Details Logic > Off-Season Closure | §5.3 get_office_details
  severity: Medium
  claim: F-15 still holds: two agents propose a Year-Round Office from two tools, and get_office_details returns no acceptsAppointmentType to check eligibility.
  evidence: "call find_offices_near with isYearRoundOffice true to propose the nearest Year-Round Office." | "explicitly state the closure, offer yroOfficeAddressSpoken, and store yroOfficeRef to answer follow-up questions." | "Never propose, select or broaden to an office returning acceptsAppointmentType false for that type."
  class: human
  decision: yro-proposal-owner

- anchor: Part 4 State 2 agent_specific_tools.find_customer
  also: Part 4 State 2 tax_pro_always | Part 4 State 2 workflow.speak_to_tp_generic step 3 | Part 2 State 1 Authentication Logic
  severity: Medium
  claim: F-16 still holds: Part 4 runs find_customer authentication without the Scheduler's multiple_matches, no_match, and authentication_failed handling.
  evidence: "Disclose a prior-year or assigned Tax Pro only after find_customer resolves the owner" | "Authenticate the owner before disclosing an assigned or prior-year Tax Pro."
  class: human
  decision: authentication-owner

- anchor: Part 4 State 2 agent_specific_outcomes.routed_to_message
  also: Part 4 State 1 Fulfillment: CDAS Callback Appointment | Part 4 State 2 agent_specific_tools
  severity: Medium
  claim: F-17 still holds: routed_to_message fires when no callback slots are available, but Part 4 holds no slot-search tool and does not book callbacks.
  evidence: "Caller opted to leave a message or no callback slots were available." | "triages the request but does not book the calendar slot"
  class: human
  decision: routed-to-message-availability-clause

- anchor: Part 3 State 2 agent_specific_tools.search_knowledge_base
  also: Part 3 State 2 objective | Part 3 State 2 interruptions.informational_question | §5.1 search_knowledge_base (Category Enums)
  severity: Medium
  claim: F-18 still holds: the Office Information agent may query all knowledge-base categories, although its objective covers only office facts.
  evidence: "Answer questions about physical office locations, operating hours, landmark directions, and local office contact options." | "Must be one of digital_account_support, financial_products, identity_and_fraud, tax_prep_and_records"
  class: human
  decision: office-info-kb-scope

- anchor: Part 3 State 2 agent_specific_tools.transfer_to_agent
  also: Part 3 State 2 office_never | Part 3 State 2 agent_specific_outcomes.office_info_transfer | Part 2 State 5 agent_specific_tools.transfer_to_agent
  severity: Medium
  claim: F-19 still holds: Part 3's transfer_to_agent entry gives no local-desk prohibition and no knownSoFar mapping, which only the Scheduler entry has.
  evidence: "Use on unresolved intent or office lookup failure." | "Map your current state to knownSoFar keys like officeName, dateSpoken, and meetingMethodChosen."
  class: human
  decision: office-info-transfer-contract

- anchor: Part 2 State 5 broadening.ladders.extension
  also: Part 2 State 3 Ladders (Extension row) | Part 2 State 5 scheduler_always (tax_extension) | §5.2 find_available_slots rung note | §1.5 terminal_payload_contract (routingTarget)
  severity: Medium
  claim: F-20 still holds: the extension rung offers a live-agent transfer for self-filing support that no agent owns and no routingTarget or transferReason names, and scheduler_always omits self-filing.
  evidence: "or transfer them to a live agent for self-filing support" | "Self-filing is a handback, not a slot-search rung." | "its final rung offers follow-up tax_prep"
  class: human
  decision: self-filing-support-owner

- anchor: §1.5 terminal_payload_contract (nextAction)
  also: Part 3 State 1 Office Contact Triage > If OPEN | Part 3 State 2 agent_specific_outcomes.office_open_unanswered | Part 2 State 5 closure.principle
  severity: Medium
  claim: F-21 still holds: capture_intent is listed as a nextAction but never defined, and it overlaps the Head of Call's additional-help question.
  evidence: "offer_additional_help, capture_intent, end_call, or none" | "so the Head of Call flow can ask how the system can help them today" | "the Head of Call flow owns the close, the additional-help question, the transfer node"
  class: human
  decision: capture-intent-definition

- anchor: Part 2 State 5 interruptions.intent_change
  also: Part 3 State 2 interruptions.intent_change | Part 4 State 1 Out-of-Scope (Refund Status) | Part 2 State 5 scheduler_never
  severity: Medium
  claim: F-22 still holds: only Part 4 routes refund-status questions to refund_status, while the Scheduler and Office Information agents have no such rule and can answer from the knowledge base.
  evidence: "transition immediately to the deterministic Refund Status Flow via intent_changed with routingTarget = refund_status" | "If the caller moves to something outside scheduling that is neither a cancellation nor a request for a person"
  class: human
  decision: refund-status-routing-all-agents

- anchor: Part 2 State 5 objective
  also: Part 2 State 5 broadening.ladders.returning_tax_pro_unavailable | Part 2 State 3 Ladders | §5.2 find_available_slots rung note
  severity: Medium
  claim: F-23 still holds: the objective anchors every type to a specific office, while a ladder rung books a regional virtual Tax Pro with no defined office for readback.
  evidence: "Every type is booked against a specific office." | "virtual with a qualified regional Tax Pro, searchScope regional" | "searchScope is office, nearby, or regional (virtual rung only)."
  class: human
  decision: regional-virtual-office-anchor

- anchor: Part 2 State 5 broadening.scenario_selection
  also: Part 2 State 5 workflow.schedule_new step 3 | Part 2 State 5 agent_specific_tools.check_search_readiness
  severity: Medium
  claim: F-24 still holds: scenario selection runs only after readiness, yet item 2 asks the drop-off form, which decides DDO, and DDO skips readiness.
  evidence: "First match wins after readiness returns ready" | "where the caller has not said in the office or by secure upload link, ask" | "Skip readiness and availability only on a digital drop-off."
  class: human
  decision: drop-off-question-timing

- anchor: Part 3 State 1 Office Details Logic > By-Appointment-Only
  also: Part 3 State 2 office_always (by_appointment_only) | Part 3 Mini-Dialogue 3D
  severity: Medium
  claim: F-25 still holds: on a by-appointment-only office, Part 3 routes to the Scheduler even though the caller never asked to book.
  evidence: "Do not ask if they want to book one. Stop speaking and return nextAction = route_intent" | "Can I walk into the Westport office tomorrow morning?"
  class: human
  decision: by-appointment-only-next-action

- anchor: Part 3 State 2 office_never (cross-office phone)
  also: Part 3 State 1 Office Contact Triage > Cross-Office Restriction | Part 3 State 2 office_always (closed_for_season) | §5.2 find_offices_near note
  severity: Medium
  claim: F-26 still holds: the phone restriction names two referents ("currently routed" and "primary routed" office), routedOfficeRef is null on central-line calls, and a stored yroOfficeRef has no stated status.
  evidence: "Direct phone numbers are restricted to the currently routed office (officeRef)." | "Never provide direct transfer numbers for offices other than the primary routed office" | "routedOfficeRef is populated on rollover, null on central-line searches."
  class: human
  decision: restricted-office-referent

- anchor: Part 2 State 5 scheduler_always (tool results)
  also: §5.2 book_appointment Outcome Results | §5.2 cancel_appointment Outcome Results
  severity: Medium
  claim: F-27 still holds: not_confirmed triggers a re-gate with no attempt limit and no exit outcome.
  evidence: "On not_confirmed, re-gate;"
  class: human
  decision: re-gate-limit

- anchor: Part 2 State 5 scheduler_always (efile_rejection_retail)
  also: §1.1 entryReason | Part 2 State 5 scheduler_always (appointment type) | Part 2 State 3 Readiness & Availability > Tax Pro Trade-off
  severity: Medium
  claim: F-28 still holds: the efile entry opens on the booking without saying whether to ask the type, which may never be inferred from the entry point, and it places the trade-off outside a ladder step.
  evidence: "When entryReason is efile_rejection_retail, open on the booking, never re-ask the intent" | "Never infer it from the entry point, the season or the caller's history." | "only at the ladder step that drops the Tax Pro preference" | "otherwise apply the Tax Pro trade-off"
  class: human
  decision: efile-entry-type-and-trade-off
