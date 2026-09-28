- anchor: §2 State 5 workflow.schedule_new[2]; §5.2 check_search_readiness taxProPreference
  also: §2 State 3 Readiness & Availability > CDAS phrasing; §1.1 knownPreferences; §4 State 2 agent_specific_tools.search_tax_pro_by_name
  severity: Medium
  claim: The Scheduler captures a caller-named Tax Pro preference and sends a taxProRef, but only the Part 4 agent owns search_tax_pro_by_name, so nothing resolves a spoken name to a ref in the Scheduler.
  evidence: "Tax Pro preference, method-specific contact detail" | "unless the caller explicitly requested that specific Tax Pro by name" | "preferredTaxPro and preferredDate are starting points only"
  class: human
  decision: scheduler-named-tax-pro-resolution

- anchor: §1.1 operation; §1.5 context_envelope.operation
  also: §4 Fulfillment: CDAS Callback Appointment > Handoff; §3 Intent Scope & Disambiguation > Out of Scope; §2 State 5 interruptions.cancel_said
  severity: Medium
  claim: Every Scheduler workflow is keyed on operation, but route_intent and intent_changed handoffs to appointment_scheduler carry no operation, and no rule says who sets it when the envelope arrives null.
  evidence: "or null outside scheduling" | "nextAction = route_intent, routingTarget = appointment_scheduler, appointmentType = callback" | "switch to the cancel_existing workflow in full"
  class: human
  decision: operation-owner-on-scheduler-handoff

- anchor: §2 State 5 objective
  also: §2 State 5 closure.continuation_context; deterministic_flows Head of Call §2.5 PA-10 to PA-12
  severity: Medium
  claim: Cancellation has two owners, since Head of Call cancels inline while the Scheduler owns cancel_existing, and the spec never states which cancellations reach the Scheduler (distinct from L-136, which covers Confirm).
  evidence: "complete at most one schedule_new, reschedule_existing, cancel_existing, or send_secure_link transaction" | "Okay, I've cancelled that appointment for you." | "a reference that comes back canceled is handled as already canceled"
  class: human
  decision: cancel-owner-head-of-call-vs-scheduler

- anchor: §2 State 2 Appointment Type Rules (callback row)
  also: §2 State 3 Ladders (Callback row); §2 State 5 broadening.ladders.callback.primary; §4 Intent Scope > Out-of-Scope (New Appointment)
  severity: Medium
  claim: A caller who asks the Scheduler directly for a Tax Pro to call them fits both tax_prep by phone and the callback type, because Part 4 limits callback to a confirmed Tax Pro while the Scheduler books callbacks with no carried Tax Pro.
  evidence: "A callback only reaches a confirmed Tax Pro." | "with the carried Tax Pro when present" | "15-minute CDAS callback. Capture the reason for the call in appointmentNotes."
  class: human
  decision: callback-type-entry-in-scheduler

- anchor: §2 State 5 interruptions.intent_change
  also: §1.5 global_always (transfer_to_agent item); §4 Intent Scope > Speak to Tax Pro (Generic)
  severity: Medium
  claim: "A request for a person" in the Scheduler fits both a barging live-agent transfer and a hand-back to speak_to_tax_pro when the caller asks mid-booking to talk to a Tax Pro.
  evidence: "that is neither a cancellation nor a request for a person" | "or an explicit caller request for a live agent (barging)"
  class: human
  decision: scheduler-person-request-owner

- anchor: §1.2 PII & IRS Sec. 7216 Compliance > Tax/Financial Boundary
  also: §1.5 global_always (informational question item)
  severity: Medium
  claim: §1.2 sends every non-loan tax question "to a Tax Pro" with no routingTarget, while global_always sends general tax questions to faq_agent, so personalized advice and notice questions have two owners.
  evidence: "Hand loan, fee, and penalty questions to faq_agent, and the rest to a Tax Pro." | "faq_agent for login, password, account, income tax course, loan, fee, penalty, or general tax questions"
  class: human
  decision: tax-advice-question-owner

- anchor: §4 State 2 objective
  also: §4 State 1 Business Intent & Rules (intro paragraph)
  severity: Low
  claim: The Part 4 objective and intro make the agent the owner of Work Center messaging and send refund queries to "specialized agents", while §1.3 gives messaging to the Leave a Message flow and refund_status is a flow.
  evidence: "via asynchronous Work Center messaging" | "rerouting refund and login queries to specialized agents" | "Route to asynchronous Work Center messaging or 15-minute CDAS callback appointments."
  class: safe
  fix: Replace "via asynchronous Work Center messaging" and "Route to asynchronous Work Center messaging" with a leave_message handback per §1.3, and "to specialized agents" with "per global_always".
