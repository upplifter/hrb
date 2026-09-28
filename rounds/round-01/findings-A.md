- anchor: §State 5 objective
  also: §State 5 agent_specific_outcomes; §State 2 Digital Drop-Off (DDO) Rules; §5.2 send_secure_link
  severity: High
  claim: The Scheduler executes the DDO `send_secure_link` write, but its objective covers only the three appointment operations and no outcome covers `link_sent` or `delivery_failed`, so a DDO call has no valid `finalOutcome`.
  evidence: "complete at most one schedule_new, reschedule_existing or cancel_existing retail appointment transaction" | "For digital drop-off, execute send_secure_link instead of book_appointment" | "DDO is a fulfillment action, not a calendar appointment"
  class: human
  decision: ddo-objective-and-outcome

- anchor: §State 5 agent_specific_tools.find_available_cdas_slots
  also: §5.2 find_available_cdas_slots; §5.2 check_search_readiness note
  severity: High
  claim: Two tools own callback slot search: `find_available_cdas_slots` is in the Scheduler tool list but no workflow step calls it, while Part 5 routes `callback` through readiness and `find_available_slots`.
  evidence: "Searches Appointment Manager for 15-minute Callback Appointment (CDAS) slots" | "For CDAS callbacks, send appointmentType = callback"
  class: human
  decision: cdas-search-tool-owner

- anchor: §4 State 2 tax_pro_always
  also: §1.5 terminal_payload_contract; §1.1 knownPreferences
  severity: Medium
  claim: The Tax Pro agent hands off a callback with `appointmentType` and a confirmed Tax Pro, but the terminal payload carries neither on `route_intent` and the envelope has no field to receive them, so the Scheduler must re-ask both.
  evidence: "return route_intent with routingTarget set to appointment_scheduler and appointmentType set to callback" | "taxProRef and officeRef when routing to leave a message"
  class: human
  decision: callback-handoff-context

- anchor: §1.4 Caller-Initiated Barging
  also: §State 5 agent_specific_tools.transfer_to_agent; §4 State 2 agent_specific_tools.transfer_to_agent; §3 State 2 agent_specific_tools.transfer_to_agent
  severity: Medium
  claim: Every agent handles a caller's live-agent request in-agent with `transfer_to_agent`, while the Request Live Agent flow diagram claims that request from any flow, so the capability has two owners.
  evidence: "Call this tool immediately when the caller explicitly requests a live agent (barging)" | "Caller-Initiated Barging (explicit central live-agent request, not local office contact)"
  class: human
  decision: live-agent-request-owner

- anchor: §4 State 2 agent_specific_outcomes.routed_to_message
  also: §4 Fulfillment: CDAS Callback Appointment; §4 Mini-Dialogues 4C
  severity: Medium
  claim: The outcome triggers on "no callback slots", but the Tax Pro agent holds no slot-search tool and never books, so it cannot observe callback availability.
  evidence: "Caller opted to leave a message or no callback slots were available" | "does not book the calendar slot" | "I can check Paul's calendar for a callback"
  class: human
  decision: tax-pro-callback-availability-owner

- anchor: §4 State 2 tax_pro_always
  also: §4 State 2 workflow.speak_to_tp_generic; §4 State 2 agent_specific_tools.find_customer; §State 5 scheduler_always
  severity: Medium
  claim: The Tax Pro agent runs authentication, but its objective omits it and the capture rules (four values, name confirmation, `customerRef` skip) live only in the Scheduler JSON it does not inherit.
  evidence: "Disclose a prior-year or assigned Tax Pro only after find_customer resolves the owner" | "Resolve the owner through find_customer" | "Assist callers in reaching their assigned or named Tax Professional"
  class: human
  decision: authentication-owner

- anchor: §1.5 terminal_payload_contract
  also: §1.5 global_outcomes.intent_changed; §State 5 interruptions.intent_change; §3 State 2 interruptions.intent_change
  severity: Medium
  claim: The `routingTarget` list includes `tax_prep`, which names no agent or flow, and an open "named destination", while no value exists for the Office Information or Tax Pro agents.
  evidence: "refund_status, faq_agent, appointment_scheduler, tax_prep, or named destination" | "Caller moves outside the current agent's scope"
  class: human
  decision: routing-target-enum

- anchor: §State 5 broadening.scenario_selection
  also: §5.2 check_search_readiness note
  severity: Medium
  claim: Open claims, Tax Pro Review, and other specialized services are handed back with no `routingTarget`, and no agent or flow owns them.
  evidence: "Open claim, Tax Pro Review or another specialized service: never schedule or broaden; hand back intent_changed with sourceUtterance"
  class: human
  decision: specialized-service-owner

- anchor: §State 5 broadening.ladders.extension
  also: §State 3 Ladders > Extension; §State 2 Tax Notice Services Guardrails > Tax Extension
  severity: Medium
  claim: The extension rung offers self-filing support that no agent or flow owns, sends the transfer outside `transfer_to_agent`'s system-initiated scope, and uses `intent_changed` for a booking inside the Scheduler's own scope.
  evidence: "or transfer them to a live agent for self-filing support" | "Call transfer_to_agent only for system-initiated escalations" | "Caller moves outside the current agent's scope"
  class: human
  decision: self-filing-owner

- anchor: §4 Intent Scope & Out-of-Scope Rerouting > Out-of-Scope (FAQ Agent)
  also: §State 5 interruptions.informational_question; §3 State 2 interruptions.informational_question; §4 State 2 interruptions.informational_question; §5.1 search_knowledge_base
  severity: Medium
  claim: The FAQ Agent owns general tax and login questions, but every agent answers the same questions in-agent through `search_knowledge_base`, so the capability has two owners.
  evidence: "transition immediately to the FAQ Agent via intent_changed with routingTarget = faq_agent" | "call search_knowledge_base, answer in one brief turn"
  class: human
  decision: kb-vs-faq-boundary

- anchor: §1.2 Hours: One Source, Spoken Once
  also: §State 5 interruptions.informational_question; §3 Office Details Logic
  severity: Medium
  claim: The rule promises one source for hours but names none, so the Scheduler may answer office hours from `search_knowledge_base` while the Office Information Agent owns them through `get_office_details`.
  evidence: "Hours: One Source, Spoken Once" | "Never invent hours from memory" | "call search_knowledge_base, answer in one brief turn"
  class: human
  decision: office-hours-owner

- anchor: §3 Office Details Logic > By-Appointment-Only
  also: §3 State 2 office_always; §3 State 2 agent_specific_outcomes
  severity: Medium
  claim: The Office Information Agent routes to the Scheduler without the caller asking to book, and none of its outcomes carries `route_intent`, so the handback has no `finalOutcome`.
  evidence: "Do not ask if they want to book one" | "Stop speaking and return nextAction = route_intent with routingTarget = appointment_scheduler"
  class: human
  decision: by-appointment-only-handback

- anchor: §4 Tax Pro Lookup & Disambiguation > No Matches / Inactive
  also: §4 State 2 tax_pro_always; §4 State 2 agent_specific_outcomes.routed_to_scheduler
  severity: Medium
  claim: The route to the Scheduler for another Tax Pro names no appointment type, and the only scheduler outcome covers a callback, so this handback has no defined outcome or type.
  evidence: "Offer to route to the Appointment Scheduler for another qualified Tax Pro at that location" | "Caller opted for a callback appointment"
  class: human
  decision: inactive-tax-pro-handback

- anchor: §3 State 2 workflow.office_info_flow
  also: §3 Dynamic State Invalidation: Location Change; §5.3 get_office_details
  severity: Medium
  claim: Callers name offices, but `get_office_details` accepts only `officeRef` or `postalCode` and the agent holds no office-lookup tool, so resolving a named office has no owner.
  evidence: "Call get_office_details using the routed officeRef or captured ZIP" | "The caller asks about a different office or ZIP mid-call"
  class: human
  decision: office-name-resolution

- anchor: §4 State 2 agent_specific_tools.transfer_to_agent
  severity: Low
  claim: The Tax Pro agent holds no write tool, so the indeterminate-write transfer trigger names a capability outside its scope.
  evidence: "Use on third-party or authentication failure, or an indeterminate write"
  class: safe
  fix: Delete ", or an indeterminate write" from `agent_specific_tools.transfer_to_agent` in the Tax Pro JSON.
