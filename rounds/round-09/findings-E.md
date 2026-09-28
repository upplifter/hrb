# Round 9 · Lens E findings

Saved by the orchestrator from the reviewer's reply. Reviewer found D-084, D-086, D-088, D-089, D-091 to D-094, D-096, D-098, D-099 consistent between prose and JSON; both frozen `outcome_unknown` copies identical; all `workflow.*[n]` and key-path pointers resolve.

### E-01 · Prose "Reschedule" floor omits the D-095 raise
Anchor: §2 State 2 Complexity Matching & Tax Pro Rating Floor > Reschedule; `workflow.reschedule_existing[3]`
Severity: Medium
Class: Safe
Issue: D-095 sets the reschedule floor to the inherited baseline "raised to the bound appointment's taxProCertLevel". JSON says so. The prose bullet says only "Use the baseline silently".
Fix (Reschedule bullet):
- Old: `- **Reschedule:** Use the baseline silently, with no gatekeeper or waterfall.`
- New: `- **Reschedule:** Use the inherited baseline silently, with no gatekeeper or waterfall, raised to the bound appointment's taxProCertLevel.`
- Net +7 words. (Duplicate of B-03.)

### E-02 · Rejected Tax Pro with the office kept has no prose rule (D-074, D-090)
Anchor: §2 State 3 Availability > Tax Pro Trade-off; `invalidation.partial_acceptance`
Severity: Medium
Class: Safe
Issue: `invalidation.partial_acceptance` carries D-074 (widen to eligible Tax Pros without asking the trade-off) and D-090 (caller-initiated change; `returning_same_tax_pro` re-selects `returning_tax_pro_unavailable` at that office). No prose section states either. The prose says only that the trade-off is asked "only at these two points".
Fix: add one bullet in §2 State 3 directly after the Tax Pro Trade-off sub-bullets. JSON unchanged.
- New: `- **Rejected Tax Pro, office kept:** Clear the Tax Pro and dependent slots without asking the trade-off. Treat it as a caller-initiated change; Returning, Same Tax Pro re-selects Returning, Tax Pro Unavailable at that office.`
- 34 words, 2 sentences. Net +34 words, no deletion available.

### E-03 · `office_never[0]` sends every appointment question to the Scheduler (D-097)
Anchor: §3 State 2 `office_never[0]`; `global_always` informational item
Severity: Medium
Class: Safe
Issue: D-097 sends an out-of-task `appointments_and_logistics` question to `faq_agent` in every agent. Part 3 hands only questions about an existing appointment to `appointment_scheduler`, and the §3 Out of Scope prose says "a question about an existing one". `office_never[0]` says "answer questions about them".
Fix (`office_never[0]`):
- Old: `Never schedule, reschedule, or cancel appointments or answer questions about them. Hand back intent_changed to appointment_scheduler immediately.`
- New: `Never schedule, reschedule, or cancel appointments or answer questions about an existing one. Hand back intent_changed to appointment_scheduler immediately.`
- Net +2 words.

### E-04 · D-087 "promises no person" still lets path-bound lines act as a free acknowledgment
Anchor: §1.5 `global_always` empathy item; `global_voice_lexicon.empathy`
Severity: Medium
Class: Human (two plausible readings; touches frozen text if fixed by tags)
Issue: The item allows any empathy line that "promises no person" as a free acknowledgment. Several path-bound lines promise no person: "Ah, that time just got booked", "Good catch, let me fix that", "That date's already gone by...", the off-season closure line, "I'm sorry, I don't have anyone available right now", and "Today's fully booked..." (tagged "Only on office_at_capacity"). Read literally, a builder may use them as a generic acknowledgment.
Fix: Options:
1. (Recommended) Tag the three general lines in `global_voice_lexicon.empathy` with "(General acknowledgment.)": "I'm sorry, let me fix that.", "I understand, let's find you the soonest we can.", "That's frustrating, I get it. Let's see what we can do." Change the `global_always` item to "with a global_voice_lexicon.empathy line tagged general acknowledgment when the moment calls for it, and add no facts. Speak every other empathy line only on its own path." 4 edits (3 frozen tags, needs a decision under C-8, plus 1 JSON item), about +11 words.
2. Name the lines by position: "with one of the first three global_voice_lexicon.empathy lines". 1 edit, about +1 word. Breaks if reordered.
3. Leave as is.

### E-05 · Reschedule floor formula vs the type-specific floors
Anchor: `workflow.reschedule_existing[3]`; `scheduler_always` floor items; §2 State 2 Appointment Type Rules table; Complexity Matching > Reschedule
Severity: Medium
Class: Human (two plausible readings)
Issue: D-095 makes the floor on every `reschedule_existing` the higher of the inherited baseline and the bound `taxProCertLevel`. The type rules say emerald_advance, tax_notice_service and callback skip complexity screening and send floor 1. Type is immutable on reschedule, so those types reach `reschedule_existing`. The physical_drop_off null is already carved out in `scheduler_always`. (Same conflict as B-04.)
Fix: Options:
1. (Recommended) Type rules win: on a reschedule of emerald_advance, tax_notice_service or callback the floor is 1, raised to the bound `taxProCertLevel` where one exists. The baseline formula applies to tax_prep and tax_extension only. 2 edits, about +12 words.
2. The baseline formula wins on every reschedule except physical_drop_off, stated once in the `scheduler_always` floor-pass item. 1 edit, about +8 words.
3. Leave as is.

### E-06 · Tax Pro Requests lost "to speak to" (L-252 regression)
Anchor: §2 State 2 Appointment Type Rules > Tax Pro Requests; `interruptions.intent_change`
Severity: Medium
Class: Human (oscillation guard: anchor edited in rounds 4, 7 and 8; at the 35-word limit)
Issue: Round 4 (L-252) changed the prose to "A request to speak to a specific or own Tax Pro" so a returning client who keeps the prior Tax Pro is not handed back. The round 7 rewrite dropped "to speak to". Prose and JSON now say "Requests for a specific or own Tax Pro ... return intent_changed to speak_to_tax_pro". That conflicts with `schedule_new[1]` (ask whether to keep the prior Tax Pro), `scenario_selection` item 8 ("asks for the prior Tax Pro") and dialogue 3B. Only the After Part 4 exception is carved out.
Fix: Options:
1. (Recommended) Restore the qualifier. Prose: `**Tax Pro Requests:** A request to speak to a specific or own Tax Pro, a named Tax Pro neither prior nor carried, or a callback without carried taxProRef returns intent_changed to speak_to_tax_pro, except per After Part 4.` JSON `intent_change`: "A request for a specific or own Tax Pro" becomes "A request to speak to a specific or own Tax Pro". 2 edits. Prose bullet reaches 37 words (one lint WARN). Net +2 words each.
2. Same fix, with the prose bullet split in two. 3 edits, about +4 words.
3. Leave as is, and state in `scenario_selection` item 8 that a keep-the-prior-Tax-Pro answer is not a Tax Pro request.

### E-07 · §4 Out-of-Scope (FAQ Agent) omits out-of-task appointment logistics (D-097)
Anchor: §4 State 1 Intent Scope & Out-of-Scope Rerouting > Out-of-Scope (FAQ Agent)
Severity: Low
Class: Safe
Issue: `global_always`, §1.2 and §2 Informational Interruptions route out-of-task logistics to `faq_agent`. Part 4's own faq_agent list does not.
Fix:
- Old: `income tax course, loan, fee, or penalty question`
- New: `income tax course, loan, fee, penalty, or out-of-task appointment-logistics question`
- Net +2 words. The bullet is 35 words after the edit.

### E-08 · "officeRef on either handoff" reads as two handoffs, not the another-Tax-Pro handoff
Anchor: §1.5 `terminal_payload_contract` (taxProRef and officeRef clause); §4 `agent_specific_outcomes.routed_to_scheduler`
Severity: Low
Class: Human (Part 1 outranks Part 4, both readings plausible)
Issue: "officeRef on either handoff" names the message and callback handoffs. Part 4 `routed_to_scheduler` carries officeRef "only when known" for another Tax Pro. Under C-1 the narrower Part 1 reading could win. (Same as B-02, which is Safe under D-040.)
Fix: Options:
1. (Recommended) Change "officeRef on either handoff" to "officeRef on any handoff". 1 edit, net 0 words.
2. Leave as is.

Summary: 8 findings. Critical 0, High 0, Medium 6 (E-01 to E-06), Low 2 (E-07, E-08). Safe 4 (E-01, E-02, E-03, E-07), Human 4 (E-04, E-05, E-06, E-08).
