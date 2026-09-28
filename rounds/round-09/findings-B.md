# Round 9 · Lens B findings

Saved by the orchestrator from the reviewer's reply. Reviewer found D-086, D-087, D-089, D-091 to D-094, D-096 to D-099 consistent.

### B-01 · `workflow.schedule_new[1]` still asks "keep the prior Tax Pro" after Part 4
Anchor: §2 State 5 `workflow.schedule_new[1]` (item "2 Type, method, location") vs §2 State 2 Appointment Type Rules > After Part 4 and the `scheduler_always` routed_to_scheduler item
Severity: Medium
Class: Safe
Issue: D-084 says that after a Part 4 `routed_to_scheduler` the Scheduler never asks whether to keep the prior Tax Pro. The After Part 4 prose and the `scheduler_always` item both say "never ask". `workflow.schedule_new[1]` has no exception. It still reads "If a returning client's prior Tax Pro is active, ask whether to keep them".
Fix: in `workflow.schedule_new[1]`:
- Old: `If a returning client's prior Tax Pro is active, ask whether to keep them;`
- New: `Except per the scheduler_always routed_to_scheduler item, if a returning client's prior Tax Pro is active, ask whether to keep them;`
- Net +8 words. The item is already over the 60-word limit (backlog L-417, oscillation guard), so do not trim it here.

### B-02 · Terminal contract leaves officeRef off Part 4's "another Tax Pro" handoff
Anchor: §1.5 `terminal_payload_contract` (taxProRef and officeRef clause) vs §4 State 2 `agent_specific_outcomes.routed_to_scheduler` and §4 No Matches / Inactive
Severity: Medium
Class: Safe
Issue: D-085 wrote "taxProRef when handing off to leave a message or to appointment_scheduler for a callback, and officeRef on either handoff". "Either" names only the message and callback handoffs. The another-Tax-Pro handoff (`routed_to_scheduler`, appointmentType null) is a third handoff. D-040 settled that it carries officeRef when known, and Part 4 says so. Part 1 beats Part 4 under C-1.
Fix: in `terminal_payload_contract`:
- Old: `and officeRef on either handoff.`
- New: `and officeRef when known on those handoffs and on routed_to_scheduler for another Tax Pro.`
- Net +9 words. The string is already over the JSON limit (backlog L-034, L-251).

### B-03 · §2 Complexity "Reschedule" bullet omits the D-095 raise
Anchor: §2 State 2 Complexity Matching & Tax Pro Rating Floor > Reschedule vs §2 State 5 `workflow.reschedule_existing[3]`
Severity: Medium
Class: Safe
Issue: D-095 sets the reschedule floor to the silent inherited baseline "raised to the bound appointment's taxProCertLevel". The JSON step 4 says this. The prose bullet says only "Use the baseline silently, with no gatekeeper or waterfall". Prose beats JSON inside a part (C-1). Apply together with B-04, which may narrow this sentence.
Fix: in §2 Complexity Matching:
- Old: `- **Reschedule:** Use the baseline silently, with no gatekeeper or waterfall.`
- New: `- **Reschedule:** Use the baseline silently, raised to the bound appointment's taxProCertLevel, with no gatekeeper or waterfall.`
- Net +6 words.

### B-04 · The D-095 reschedule floor collides with the fixed-floor types
Anchor: §2 State 5 `workflow.reschedule_existing[3]` and the `scheduler_always` floor items vs §2 State 2 Appointment Type Rules table (emerald_advance, tax_notice_service and callback rows; tax_prep row for physical_drop_off)
Severity: Medium
Class: Human
Issue: D-095 sets the reschedule floor to the baseline raised to the bound appointment's `taxProCertLevel`, with no qualifier by type. The type rules say emerald_advance, tax_notice_service and callback always send `taxProRatingFloor` 1 and skip screening. `scheduler_always` sends null on physical_drop_off. A physical_drop_off appointment has no Tax Pro, so it has no cert level to raise to. Type is immutable on reschedule, so it is unclear whether floor 1 or the raised baseline applies.
Fix: Options:
A. (Recommended) The type floor wins on reschedule. emerald_advance, tax_notice_service and callback send 1, and physical_drop_off sends null. The baseline and cert-level raise apply only to tax_prep and tax_extension. 2 edits, about +14 words. Fold B-03's wording into the same bullet.
B. The reschedule floor wins for every type except physical_drop_off, which stays null. Scope the "send 1" rows and the matching `scheduler_always` item to schedule_new. About 5 edits, roughly +10 words.
C. Leave the rules and add one sentence saying reschedule ignores the type floor rows. 1 edit, about +10 words.

Summary: 4 findings. Critical 0, High 0, Medium 4, Low 0. Safe 3 (B-01, B-02, B-03), Human 1 (B-04).
