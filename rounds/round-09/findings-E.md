# Round 9 · Lens E findings

Saved by the orchestrator from the reviewer's reply.

### E-01 · office_never still sends every appointment question to the Scheduler after D-097
Anchor: §3 State 2 office_never[0]; §3 Intent Scope & Disambiguation > Out of Scope; global_always informational item
Severity: Medium
Class: Safe
Issue: D-097 says Part 3 hands only questions about an existing appointment to appointment_scheduler; out-of-task logistics questions go to faq_agent. §3 Out of Scope prose and global_always were updated; office_never[0] still sends any question "about them" to appointment_scheduler, giving general logistics questions two owners.
Fix: Old: "Never schedule, reschedule, or cancel appointments or answer questions about them. Hand back intent_changed to appointment_scheduler immediately."
New: "Never schedule, reschedule, or cancel appointments or answer questions about an existing one. Hand back intent_changed to appointment_scheduler immediately."
Footprint: 1 edit, +2 net words.

### E-02 · The Reschedule floor prose leaves out the bound appointment's taxProCertLevel
Anchor: §2 State 2 Complexity Matching & Tax Pro Rating Floor > Reschedule; workflow.reschedule_existing[3]; scheduler_always floor-pass item
Severity: Medium
Class: Safe
Issue: D-095 sets the reschedule floor to the inherited baseline raised to the bound appointment's taxProCertLevel. The JSON has both parts; the prose bullet says only "Use the baseline silently". Under C-1 prose wins and drops the raise.
Fix: Old: "- **Reschedule:** Use the baseline silently, with no gatekeeper or waterfall."
New: "- **Reschedule:** Use the baseline silently, with no gatekeeper or waterfall, raised to the bound appointment's taxProCertLevel."
Footprint: 1 edit, +6 net words.

### E-03 · schedule_new[1] still asks the keep-prior-Tax-Pro question with no Part 4 exception
Anchor: workflow.schedule_new[1]; scheduler_always routed_to_scheduler item; §2 State 2 After Part 4
Severity: Low
Class: Safe (held by oscillation guard with L-417)
Issue: D-084 says never ask whether to keep the prior Tax Pro after a Part 4 routed_to_scheduler. Prose and the routed item say so; schedule_new[1] has no exception. The specific item governs, so this is a clarity gap. Round 8 verify left it for the L-417 guard.
Fix: With L-417: Old: "If a returning client's prior Tax Pro is active, ask whether to keep them;" New: "If a returning client's prior Tax Pro is active, ask whether to keep them, except after a Part 4 routed_to_scheduler;" paired with an offsetting trim.
Footprint: 1 edit, +7 words before trim.

Other checks (no finding): D-085 to D-094, D-096, D-098, D-099 match across prose, JSON, Part 5, and dialogues. contact.callbackNumber no longer appears. Both frozen outcome_unknown copies are identical.

Summary: 3 findings (0 Critical, 0 High, 2 Medium, 1 Low).
