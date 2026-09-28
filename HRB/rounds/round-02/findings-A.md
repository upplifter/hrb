- anchor: §5.2 find_offices_near
  also: §1.1 The Head of Call Envelope (routedOfficeRef); §2 State 5 scheduler_always find_offices_near result item
  severity: Medium
  claim: After D-010, Head of Call resolves the dialed number, but find_offices_near still resolves DNIS and returns invalid_dnis, so two owners resolve the rollover office.
  evidence: "Office that Head of Call resolved from dialedOfficeNumber." | "Resolves the initial retail office or returns nearby offices." | "invalid_dnis | Rollover DNIS did not map to an active office." | "If find_offices_near returns invalid_location or invalid_dnis, reprompt for a valid ZIP"
  class: human
  decision: dnis-resolution-owner

- anchor: §1.1 The Head of Call Envelope (customerRef, customerStatus)
  also: §1.5 context_envelope.customerRef; §2 State 1 Authentication Logic > State Persistence
  severity: Medium
  claim: The envelope trusts identity only "from a prior agent", while Head of Call authenticates callers and passes UCID and Authentication Status, so no rule says whether Head of Call identity skips find_customer.
  evidence: "Authenticated identity from a prior agent." | "Data To Pass: UCID · Customer Status · Utterance · Authentication Status"
  class: human
  decision: head-of-call-identity-trust

- anchor: §2 State 5 objective
  also: §1.1 The Head of Call Envelope (operation); §1.5 context_envelope.operation
  severity: Medium
  claim: Head of Call routes Confirm Appointment to the Appointment Scheduling flow, but the Scheduler has no confirm operation and no rule to hand it back.
  evidence: "Intent = Confirm Appointment?" | "Appointment Scheduling flow (cascade)" | "at most one schedule_new, reschedule_existing, cancel_existing, or send_secure_link transaction"
  class: human
  decision: confirm-appointment-owner

- anchor: §5.1 search_knowledge_base (KB results)
  also: §1.5 global_always search_knowledge_base item; §1.5 terminal_payload_contract routingTarget
  severity: Medium
  claim: A requires_tax_pro result "routes to a Tax Pro" with no owner, routingTarget, or outcome, and no rule says whether a mid-booking Scheduler suspends or abandons the booking.
  evidence: "requires_tax_pro routes to a Tax Pro."
  class: human
  decision: requires-tax-pro-handler

- anchor: §1.2 Hours: One Source, Spoken Once
  also: §4 State 2 agent_specific_tools; §1.5 global_always search_knowledge_base item
  severity: Medium
  claim: After D-012, only the Scheduler hands office hours and phone questions to office_information, so the Speak to a Tax Pro agent, which lacks the Part 3 tools, has no owner for them.
  evidence: "The Scheduler hands these questions back with routingTarget office_information." | "Never answer office hours or phone numbers from search_knowledge_base."
  class: human
  decision: tax-pro-agent-hours-handback

- anchor: §4 Intent Scope & Out-of-Scope Rerouting > Speak to Tax Pro (Generic)
  also: §4 Business Intent & Rules (intro); §3 Intent Scope & Disambiguation > office_contact
  severity: Medium
  claim: Part 4 claims requests for an "office associate" while the same section and Part 3 give local office staff to Office Information, so office-staff requests have two owners.
  evidence: "speak with a tax advisor, preparer, or office associate generally" | "Requests for local office staff belong to the Office Information Agent."
  class: human
  decision: office-associate-owner

- anchor: §4 Intent Scope & Out-of-Scope Rerouting > Out-of-Scope (New Appointment)
  also: §4 Fulfillment Priority step 4; §2 State 2 Appointment Type Rules (tax_prep row)
  severity: Medium
  claim: Part 4 routes only in-person or virtual tax prep requests as new appointments, so a phone tax_prep request could go either as a new appointment or as a callback-type route_intent.
  evidence: "If the caller requests a new in-person or virtual tax prep session" | "In-person, Phone, Virtual, DDO, Physical Drop-Off"
  class: human
  decision: phone-appointment-vs-callback

- anchor: §4 Tax Pro Lookup & Disambiguation > Generic Request
  also: §4 State 2 workflow.speak_to_tp_generic[3]
  severity: Medium
  claim: The generic path covers only a caller with an active prior Tax Pro, yet the workflow offers a Tax Pro callback and message to every caller, with no path for a caller with no or an inactive prior Tax Pro.
  evidence: "If active, state the options for reaching them." | "4. State the callback and message options and mention the Online Message Center for Tax Pro Review."
  class: human
  decision: generic-no-tax-pro-path

- anchor: §4 Intent Scope & Out-of-Scope Rerouting > Out-of-Scope (FAQ Agent)
  also: §1.5 global_always informational-question item
  severity: Medium
  claim: Part 4 sends password resets and income tax course questions to faq_agent, but the Base JSON names only login, account, and general tax, so the Scheduler and Office Information have no target for income tax course questions.
  evidence: "password resets, account access, or income tax course information" | "faq_agent for login, account, or general tax questions."
  class: human
  decision: itc-questions-target

- anchor: §2 State 2 Digital Drop-Off (DDO) Rules > Rescheduling
  also: §2 State 5 workflow.reschedule_existing[1]
  severity: Medium
  claim: A DDO change needs a new link "in a separate invocation", but no rule says which agent or operation starts it, and reschedule_existing would find no appointment and transfer.
  evidence: "A requested change requires sending a new link in a separate invocation."
  class: human
  decision: ddo-change-handling

- anchor: §2 State 5 scheduler_always callback item
  also: §4 State 2 tax_pro_always[0]; §1.5 terminal_payload_contract
  severity: Low
  claim: Part 4 elicits the call reason before its callback handoff, but no payload field carries it, so the Scheduler asks the caller for it again for appointmentNotes.
  evidence: "Elicit the reason for the call first." | "On callback, capture the reason for the call in appointmentNotes"
  class: human
  decision: callback-reason-carry
