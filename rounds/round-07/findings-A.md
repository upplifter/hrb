# Round 7 · Lens A findings

Saved by the orchestrator from the reviewer's reply.

### A-01 · Appointment-logistics questions asked outside a task have two owners in Parts 3 and 4 and none in the Scheduler
Anchor: §1.5 global_always search_knowledge_base item; §3 State 1 Intent Scope & Disambiguation > Out of Scope; §4 Out-of-Scope (Appointments); §2 State 3 Informational Interruptions > Trigger; §1.1 operation
Severity: Medium
Class: Human
Issue: `global_always` limits `search_knowledge_base` to "a mid-task question in appointments_and_logistics or tax_prep_and_records". Parts 3 and 4 list the tool, and §3 Out of Scope also hands back "a question about one" (any appointment) to appointment_scheduler; Part 4 limits its handback to "asks about an existing one". In the Scheduler with no task in progress, the Informational Interruptions trigger is "a knowledge question mid-booking" and §1.1 `operation` exempts only "an appointment-details question", so the caller is asked to book, change, or cancel. No outcome fits an answered standalone question (`question_answered` deleted by D-034).
Proposed fix (options):
- A. (Recommended) Send a logistics question asked outside a task to faq_agent in every agent: extend the faq_agent list in the `global_always` informational item, §1.2 Tax/Financial Boundary, and §2 State 3 Informational Interruptions > Hand back; change §3 Out of Scope "or a question about one" to "or a question about an existing one". About 4 edits, +25 words.
- B. The Scheduler owns these questions and answers them with `search_knowledge_base`; outside a booking it returns `appointment_details_provided`, widened to logistics. Parts 3 and 4 hand them to appointment_scheduler. About 5 edits, +35 words.
- C. Every agent answers them itself; needs a new answered-question outcome (C-7).

### A-02 · Part 3 names no routingTarget for a request to speak to a Tax Pro, and Part 4 JSON names none for office-staff requests
Anchor: §3 State 2 interruptions.intent_change; §4 State 2 interruptions.intent_change; §4 State 1 Business Intent & Rules intro
Severity: Low
Class: Safe (reviewer)
Issue: Part 3 `interruptions.intent_change` hands back intent_changed with no target; `terminal_payload_contract` requires routingTarget. Part 4 prose says office-staff requests belong to Office Information, but Part 4 JSON never names that target.
Proposed fix: Part 3 adds "; a request to speak to a Tax Pro takes routingTarget speak_to_tax_pro." Part 4 adds "; a request for local office staff takes routingTarget office_information."

No other new Medium-or-higher lens A issues. Handoffs to Check Refund Status, Leave a Message, Request Live Agent, and the Head of Call intent set resolve or are covered by L-136, L-140, L-383 to L-385.
