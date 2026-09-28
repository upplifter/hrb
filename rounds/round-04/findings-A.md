# Round 4 findings, lens A (Scope and ownership)

Saved by the orchestrator from the reviewer's reply (write blocked).

### A-01 · Message offer and support hours are owned by a flow that has neither
Anchor: §1.3 Leave-a-Message Ownership; §1.4 "agent_unavailable, message available" row; §2 State 5 closure.line_patterns (handoff_unavailable)
Severity: High
Class: Human (moves ownership between the spec and a deterministic flow)
Issue: "The deterministic Leave a Message flow owns the offer where still needed" and "The deterministic flow provides support hours and offers the message option." The Leave a Message flow (deterministic spec §5.2) starts at LM-01/LM-02 with recipient identification and has no offer or support-hours prompt; Head of Call (§2.7) has no node for nextAction leave_message_offer.
Proposed fix: Decide who speaks the offer and support hours on leave_message_offer, then align §1.3, the §1.4 row, and closure.line_patterns.

### A-02 · Callback with no Tax Pro loops between Part 4 and the Scheduler
Anchor: §4 No Matches / Inactive; tax_pro_always unavailable item; §2 State 2 Appointment Type Rules > Tax Pro Requests; §2 State 5 interruptions.intent_change
Severity: High
Class: Human
Issue: Part 4 sends a caller with no active Tax Pro to the Scheduler "for another qualified Tax Pro (routed_to_scheduler, appointmentType null)". In the Scheduler, "a callback with no carried taxProRef hands back intent_changed to speak_to_tax_pro", so a caller who keeps asking for a call back bounces between agents with no bound.
Proposed fix: Name one terminal owner for a callback request with no reachable Tax Pro, and bar a return to the sending agent.

### A-03 · "Own Tax Pro" requests have two owners in the Scheduler
Anchor: §2 State 2 Appointment Type Rules > Tax Pro Requests; §2 State 5 broadening.scenario_selection item 8; workflow.schedule_new[1]; interruptions.intent_change
Severity: High
Class: Human (reviewer); orchestrator: see triage
Issue: Prose says "A request for a specific or own Tax Pro ... hands back intent_changed to speak_to_tax_pro", while item 8 books "Returning client who asks for the prior Tax Pro" as returning_same_tax_pro. The JSON mirror says "A request to speak to a specific or their own Tax Pro". Under C-1 the prose would remove returning_same_tax_pro.
Proposed fix: Limit the prose handback to a request to speak to a Tax Pro, matching interruptions.intent_change.

### A-04 · The Scheduler captures a Tax Pro preference it cannot own
Anchor: §1.1 knownPreferences; §1.5 context_envelope.knownPreferences; §2 State 5 workflow.schedule_new[2]
Severity: Medium
Class: Human
Issue: "preferredTaxPro and preferredDate are starting points only" and schedule_new[2] "Capture the ... Tax Pro preference", but a caller-named Tax Pro other than the prior or carried one hands back to speak_to_tax_pro (D-027), and the Scheduler cannot resolve a name.
Proposed fix: A preferredTaxPro other than the prior or carried Tax Pro follows the Tax Pro Requests handback; limit step 3's "Tax Pro preference" to the prior-Tax-Pro choice.

### A-05 · Identity/fraud and contact-directory questions have no owner
Anchor: §1.5 global_always informational item; §5.1 search_knowledge_base > Category Enums
Severity: Medium
Class: Human
Issue: The tool accepts identity_and_fraud and contact_directories, but "Agents send only appointments_and_logistics or tax_prep_and_records", and the informational item names no target for identity-theft, fraud, or other-department phone questions.
Proposed fix: Assign identity/fraud and non-office contact questions to a routingTarget or a transfer_to_agent reason.

### A-06 · tax_prep_and_records questions have two owners
Anchor: §1.5 global_always KB item and informational item; §2 State 3 Informational Interruptions
Severity: Medium
Class: Human
Issue: The KB item answers "a mid-task question in appointments_and_logistics or tax_prep_and_records" in-agent, while "non-personal tax questions" go to faq_agent. "Do I need my 1099s?" fits both.
Proposed fix: Define the boundary once (e.g., tax_prep_and_records covers only what to bring or prepare for the appointment).

### A-07 · Rescheduling a callback or physical drop-off uses the wrong ladder
Anchor: §2 State 5 broadening.scenario_selection items 2-4; broadening.ladders.reschedule; §2 State 3 Ladders (Rescheduling row)
Severity: Medium
Class: Human
Issue: Item 3 matches every reschedule first, and the reschedule ladder offers "same_tax_pro_nearby_offices" and "any_qualified_tax_pro", which contradict a callback ("only reaches a confirmed Tax Pro") and a physical drop-off ("with no Tax Pro named").
Proposed fix: Give callback and physical_drop_off reschedules the time and date rungs only, in scenario_selection and the State 3 table.

### A-08 · Part 4 names no target for non-tax_prep appointment requests
Anchor: §4 Out-of-Scope (New Appointment); tax_pro_always callback item; §4 State 2 interruptions.intent_change
Severity: Medium
Class: Human
Issue: Part 4 routes only "a new tax prep appointment in any method" to appointment_scheduler; reschedule, cancel, and other types fall to intent_change, which names no routingTarget. Part 3 covers "any request to schedule, reschedule, or cancel".
Proposed fix: Route any appointment request in Part 4 to appointment_scheduler, matching Part 3.

### A-09 · Refund-status TRANSFER handoff to the Scheduler has no entry context
Anchor: §1.1 entryReason; §1.5 context_envelope.entryReason
Severity: Medium
Class: Human
Issue: Check Refund Status sends C-22 (efile_rejection_retail) and C-28 (TaxReturnStatus 13-00, 13-02, 14-00, "Status = TRANSFER") to the Scheduler; §1.1 defines entry behavior only for efile_rejection_retail.
Proposed fix: Name the entryReason for C-28 and its opening rule, or treat it as a null-operation entry.

### A-10 · Appointment-details questions have no owner
Anchor: §2 State 5 objective; agent_specific_tools.get_customer_appointments; §1.5 global_always informational item
Severity: Medium
Class: Human
Issue: get_customer_appointments runs "on reschedule_existing and cancel_existing only"; no agent answers "when is my appointment?" and the informational item names no target.
Proposed fix: Assign appointment-details questions to the Scheduler (read-only after authentication) or a named handback target.

### A-11 · Part 4 objective omits two of its outcomes
Anchor: §4 State 2 objective
Severity: Low
Class: Safe. Extend the objective to cover the D-033 paths already defined.
Issue: The objective names only leave_message and the CDAS callback; it omits routed_to_scheduler for another Tax Pro and tax_pro_options_declined.
Proposed fix: Add "or, when the Tax Pro is unavailable, to the Scheduler for another Tax Pro", and trim "15-minute CDAS" to offset.
