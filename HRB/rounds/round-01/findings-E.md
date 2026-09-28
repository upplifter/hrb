- anchor: §1.5 global_outcomes.customer_abandoned
  also: §1.2 Input Exhaustion & Silence > Abandonment
  severity: High
  claim: The prose says an unanswered gate runs the No-Input Rule and terminates, while the JSON says it runs the reprompt rule and transfers.
  evidence: "it runs the No-Input Rule, then terminates" | "an unanswered gate runs the reprompt rule, then transfers"
  class: safe
  fix: In customer_abandoned, replace "runs the reprompt rule, then transfers" with "runs the no-input rule, then terminates".

- anchor: §1.5 global_always (transfer_to_agent item)
  also: §1.4 Caller-Initiated Barging row; Part 5 transfer_to_agent; each agent's agent_specific_tools.transfer_to_agent
  severity: High
  claim: Base JSON limits transfer_to_agent to system-initiated escalations, but §1.4, Part 5, and every agent block call it on a caller's explicit live-agent request.
  evidence: "Call transfer_to_agent only for system-initiated escalations" | "Caller-Initiated Barging (explicit central live-agent request" | "when the caller explicitly requests a live agent (barging)"
  class: safe
  fix: After the e.g. list, add "or an explicit caller request for a live agent (barging)" to the "only for" clause.

- anchor: §1.4 Approved Recovery Lines > Caller-Initiated Barging row
  also: §1.4 agent_unavailable, message available row; Part 2 State 5 closure.line_patterns; Part 4 State 2 tax_pro_never
  severity: Medium
  claim: The barging row has the agent state support hours and offer a message on agent_unavailable, while the adjacent row and the JSON hand both to the deterministic flow.
  evidence: "stating support hours and offering a message if applicable" | "The deterministic flow provides support hours" | "let the deterministic flow speak support hours and offer the message"
  class: human
  decision: barging-unavailable-line-frozen

- anchor: §1.5 global_outcomes.transfer_unavailable
  also: §1.4 agent_unavailable, no message row; Part 2 State 5 closure.line_patterns.handoff_unavailable
  severity: Medium
  claim: The JSON outcome says to state only the unavailable outcome, while §1.4 has the agent speak support hours and invite a call back when no message is available.
  evidence: "State only the unavailable outcome if a spoken seam is required, then stop speaking." | "Our team picks up [supportHoursSpoken], so give us a call back then."
  class: safe
  fix: Replace that sentence with "When leaveMessageAvailable is false, speak supportHoursSpoken and invite a call back; otherwise state only the unavailable outcome. Then stop speaking."

- anchor: §1.5 global_never (tax advice item)
  also: §1.2 PII & IRS Sec. 7216 Compliance > Tax/Financial Boundary
  severity: Medium
  claim: The Base JSON leaves out the prose bans on interpreting notices and quoting loan terms, fees, or penalties, and the route to a Tax Pro or search_knowledge_base, so the Office Information prompt lacks them.
  evidence: "interpret notices, or quote loan terms, fees, or penalties" | "Never give personalized tax advice, tax calculations, or interpretations of tax law."
  class: human
  decision: base-json-tax-boundary-scope

- anchor: §1.2 PII & IRS Sec. 7216 Compliance > Data Sanitization
  also: Part 5 book_appointment Request JSON (New Customer); Part 2 State 5 scheduler_never
  severity: Medium
  claim: The prose exempts only find_customer payloads from DOB and SSN redaction, but the new-customer book_appointment request also carries dateOfBirth and ssnLast4.
  evidence: "Exception: find_customer request payloads require these fields for authentication." | "only book_appointment may create the profile at commit"
  class: human
  decision: pii-exception-book-appointment

- anchor: Part 2 State 5 workflow.schedule_new (step 2)
  also: §1.1 entryPoint; Part 2 State 5 scheduler_always (rollover item)
  severity: Medium
  claim: §1.1 lets the prior office win over the rollover office in the same-Tax-Pro scenario, but the JSON proposes the last-served office and then still proposes the rollover office.
  evidence: "Wins over prior office, except in the returning-client same-Tax-Pro scenario." | "proposes the office where they were last served, then branch on entryPoint" | "On a rollover, resolve the dialed number to routedOfficeRef and propose that office"
  class: safe
  fix: In step 2 change "then branch on entryPoint" to "otherwise branch on entryPoint", and prefix the scheduler_always rollover item with "Unless returning_same_tax_pro is selected,".

- anchor: Part 2 State 3 Readiness & Availability > Tax Pro Trade-off
  also: Part 2 State 5 invalidation.partial_acceptance; Part 2 State 5 scheduler_always (efile_rejection_retail item)
  severity: Medium
  claim: The prose allows the trade-off question only at the ladder rung that drops the Tax Pro, while the JSON also asks it on partial acceptance and on e-file rejection with no prior Tax Pro.
  evidence: "only at the ladder step that drops the Tax Pro preference" | "but keeps the office, ask the Tax Pro trade-off first" | "otherwise apply the Tax Pro trade-off"
  class: human
  decision: tax-pro-trade-off-trigger-points

- anchor: Part 4 State 2 interruptions.informational_question
  also: Part 4 State 1 Intent Scope & Out-of-Scope Rerouting > Out-of-Scope (FAQ Agent); Part 4 State 2 objective
  severity: Medium
  claim: The prose routes general tax questions and login issues to the FAQ Agent, but the Tax Pro JSON answers informational questions through search_knowledge_base and lists no FAQ Agent triggers.
  evidence: "If the elicited reason is general tax questions, login difficulty" | "call search_knowledge_base, answer in one brief turn" | "rerouting refund and login queries to specialized agents"
  class: human
  decision: tax-pro-faq-vs-kb-ownership

- anchor: Part 4 State 2 agent_specific_outcomes.routed_to_message
  also: Part 4 State 1 Fulfillment: CDAS Callback Appointment
  severity: Medium
  claim: The outcome covers a case where no callback slots were available, but the prose says this agent never searches or books callback slots and hands callbacks to the Scheduler.
  evidence: "Caller opted to leave a message or no callback slots were available." | "triages the request but does not book the calendar slot"
  class: human
  decision: tax-pro-callback-slot-check

- anchor: §1.5 global_voice_lexicon
  also: §1.4 Approved Recovery Lines (agent_available, agent_unavailable rows, Repeat or slow-down, Same-Day row)
  severity: Medium
  claim: Under the C-2 mirror policy, several §1.4 approved lines have no JSON copy, so the runtime prompt carries no approved handoff, unavailable, or repeat line.
  evidence: "I've got someone who can take it from here, [waitTimeSpoken]." | "handoff_confirmed: one short handoff line, only after agent_available."
  class: human
  decision: mirror-missing-approved-lines-frozen

- anchor: Part 5 check_search_readiness (Note)
  also: Part 2 State 2 Appointment Type table > callback; Part 2 State 5 scheduler_always (taxProRatingFloor item)
  severity: Medium
  claim: Part 5 allows a null method and rating floor on callbacks, but the prose sets the callback method to phone_callback and the JSON exempts only physical_drop_off from the mandatory floor.
  evidence: "| callback | phone_callback | 15-minute CDAS callback." | "appointmentMethod, taxProRatingFloor, and timeWindow may be null" | "Treat it as a mandatory eligibility filter, except on physical_drop_off"
  class: human
  decision: callback-method-and-floor

- anchor: Part 3 State 2 agent_specific_tools.transfer_to_agent
  also: Part 3 State 1 Intent Scope & Disambiguation > unclear_intent; Part 3 State 2 agent_specific_outcomes.office_info_transfer
  severity: Medium
  claim: On unresolved intent the prose allows a transfer or a leave-a-message handback, while the JSON allows only a transfer.
  evidence: "If unresolved after one reprompt, transfer or route to leave a message." | "Use on unresolved intent or office lookup failure." | "Unresolved office intent or lookup failure."
  class: human
  decision: office-unclear-intent-exit

- anchor: Part 3 State 2 office_never (direct numbers item)
  also: Part 3 State 1 Office Contact Triage > Cross-Office Restriction; Part 3 State 1 Dynamic State Invalidation: Location Change
  severity: Medium
  claim: The prose ties direct numbers to officeRef, which a location change replaces, while the JSON ties them to the routed office and has no location-change invalidation.
  evidence: "Direct phone numbers are restricted to the currently routed office (officeRef)." | "Purge officeRef and cached office details." | "Never provide direct transfer numbers for offices other than the primary routed office"
  class: human
  decision: office-direct-number-scope

- anchor: Part 2 State 5 workflow.reschedule_existing (step 3)
  also: Part 2 State 2 Appointment Type Rules > Immutability
  severity: Medium
  claim: The prose makes appointment type immutable on reschedule and transfers on request, but the JSON names only the method and gives no action.
  evidence: "Type cannot be changed on a reschedule. If requested, preserve the appointment and call `transfer_to_agent`." | "never change the appointment method through reschedule"
  class: safe
  fix: In step 3, replace "never change the appointment method through reschedule" with "never change the appointment type or method through reschedule; on a type change request, preserve the appointment and call transfer_to_agent".
