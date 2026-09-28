# Round 9 · Lens F findings

Saved by the orchestrator from the reviewer's reply. Reviewed and not raised: the 27 dup_mirror WARNs (prose/JSON mirrors under C-2 A or frozen text); length WARNs already in the backlog (terminal_payload_contract, workflow.schedule_new[1], closure.line_patterns, find_available_slots, Ladders table cells); the frozen `should` line; the D-006 `online` exception; anchors held by the oscillation guard (context_envelope.taxProRef/officeRef, speak_to_tp_generic[2], §1.4 agent_unavailable row, Part 5 Conventions en dash).

### F-01 · Reschedule floor in prose omits the D-095 raise
Anchor: §2 State 2 Complexity Matching & Tax Pro Rating Floor > Reschedule bullet; `workflow.reschedule_existing[3]`
Severity: Medium
Class: Safe
Fix: Old `- **Reschedule:** Use the baseline silently, with no gatekeeper or waterfall.` New `- **Reschedule:** Use the baseline silently, with no gatekeeper or waterfall, raised to the bound appointment's taxProCertLevel.` Net +6. (Duplicate of B-03, C-02, E-01.)

### F-02 · Part 3 `office_never[0]` still bars every appointment question after D-097
Anchor: §3 State 2 `office_never[0]`
Severity: Medium
Class: Safe
Fix: Old `answer questions about them.` New `answer questions about an existing one.` Net +2. (Duplicate of E-03.)

### F-03 · faq_agent lists miss D-097's logistics topic, with three spellings
Anchor: §4 Intent Scope > Out-of-Scope (FAQ Agent); §2 State 3 Informational Interruptions > Hand back
Severity: Low
Class: Safe
Fix: (§4) Old `loan, fee, or penalty question, immediately hand back` New `loan, fee, penalty, or out-of-task appointment-logistics question, immediately hand back`. (§2) Old `non-personal tax, and out-of-task logistics questions to faq_agent;` New `non-personal tax, and out-of-task appointment-logistics questions to faq_agent;`. Net +3. (Overlaps E-07.)

### F-04 · D-087 leaves "free" empathy lines undefined
Anchor: §1.5 `global_always[2]` (empathy item); `global_voice_lexicon.empathy`
Severity: Medium
Class: Human
Issue: The item allows "a line that promises no person" as a free acknowledgment. Many path-bound lines also promise no person; three carry facts or ask a question. Only the first three lexicon lines are clearly free. The lexicon is frozen (C-8), so tags need a decision. (Same as E-04.)
Options: A. (Recommended) Tag the three free lines, e.g. "(Any moment.)", and have the item name that tag. About 4 edits, +10 words. B. Say "one of the first three global_voice_lexicon.empathy lines". 1 edit, +3 words; fragile. C. Leave as is.

### F-05 · Write-tool entries repeat the explicit-yes gate and the no-text rule
Anchor: §2 State 5 `agent_specific_tools.book_appointment`, `reschedule_appointment`, `cancel_appointment`, `send_secure_link`
Severity: Low
Class: Human (touches consent)
Issue: `scheduler_always[1]` already requires an explicit yes "immediately before any write, including send_secure_link". Four tool entries repeat "and an explicit yes". `cancel_appointment` also says "Send no text confirmation", which repeats two other items.
Options: A. Delete the repeats, 4 edits, -20 words. B. (Chosen by orchestrator) Keep them as a deliberate consent echo; 0 edits.

### F-06 · Part 5 Callbacks bullet repeats the type table and `scheduler_always`
Anchor: §5.2 check_search_readiness > Callbacks bullet
Severity: Low
Class: Safe
Fix: Old `- **Callbacks:** Send appointmentType callback, appointmentMethod phone_callback, and taxProRatingFloor 1; timeWindow may be null.` New `- **Callbacks:** timeWindow may be null.` Net -8.

### F-07 · `persona_translation` repeats `prohibited_phrases`
Anchor: §1.5 `global_voice_lexicon.persona_translation`
Severity: Low
Class: Safe
Fix: Old `Avoid 'please provide', 'in order to', 'proceeding with', 'your request has been', 'I will now'.` New `Avoid 'proceeding with' and 'your request has been'.` Net -7.

### F-08 · State 1 third-party bullet repeats the §1.2 name-confirm rule
Anchor: §2 State 1 Authentication Logic > Third-Party
Severity: Low
Class: Safe
Fix: Old `...using First Name, Last Name, DOB, and Last 4 SSN. Confirm the owner's name at capture.` New `...using First Name, Last Name, DOB, and Last 4 SSN.` Net -6. (Orchestrator note: D-086 says the §2 Third-Party prose mirror stays unchanged under C-2 A; verify before applying.)

### F-09 · `none_nearby` meaning uses an unquantified hedge
Anchor: §5.2 find_offices_near > Outcome Results
Severity: Low
Class: Safe
Fix: Old `| none_nearby | Valid location, but no office serves it within a reasonable distance. |` New `| none_nearby | Valid location, but no office serves it. |` Net -4.

### F-10 · Part 2 JSON pointers mix 0-based indexes and 1-based step labels
Anchor: §2 State 5 `workflow.reschedule_existing[4]`; `workflow.cancel_existing[1]`; `broadening.scenario_selection[0]`
Severity: Low
Class: Safe
Fix: Old `Handle a no per workflow.schedule_new[4].` New `Handle a no per workflow.schedule_new step 5.` Old `Retrieve and bind per workflow.reschedule_existing[1]` New `... step 2`. Old `at workflow.schedule_new[1].` New `at workflow.schedule_new step 2.` Net +6. (Orchestrator note: the spec now uses `workflow.x[n]` pointers everywhere and other rounds standardized on them; low value, likely skip.)

### F-11 · Scheduler `transfer_to_agent` entry points to "above"
Anchor: §2 State 5 `agent_specific_tools.transfer_to_agent`
Severity: Low
Class: Safe
Fix: Old `"Call on the transfer conditions defined above."` New `"Call per global_always and scheduler_always transfer conditions."` Net 0.

### F-12 · "Principles" subhead is not bold
Anchor: §2 State 3 Search Broadening Ladder > Principles
Severity: Low
Class: Safe
Fix: Old `Principles` New `**Principles**` Net 0.

Summary: 12 findings (0 Critical, 0 High, 3 Medium, 9 Low). 10 Safe, 2 Human (F-04, F-05).
