# Round 9 · Lens D findings

Saved by the orchestrator from the reviewer's reply. Reviewer checked and found holding: After Part 4 (prose and JSON), D-085, D-086, D-088, D-089/D-078 conflict cap, D-090, D-091, D-093, D-094, D-096, D-097, D-098; all cross-references and `workflow.*[n]` indexes resolve.

### D-01 · Post-commit transfer outcomes report transactionOccurred false
Anchor: §1.5 `terminal_payload_contract` ("Where an outcome states no value, transactionOccurred is false"); `global_outcomes.transferred_to_human`; `global_outcomes.transfer_unavailable`
Severity: Medium
Class: Human
Issue: D-043 fixed `customer_abandoned` so a drop after a commit reports transactionOccurred true with the committed reference. The other post-commit exits were not fixed. After `book_appointment` returns booked, the caller may barge or ask an identity-theft or fraud question during the post-commit readback, and the agent transfers. `transferred_to_human` states no transactionOccurred value, so the contract default gives false. `transfer_unavailable` states "transactionOccurred false" outright. Head of Call would see a committed booking as none.
Fix: Options:
A. (Recommended) In `terminal_payload_contract`, replace "Where an outcome states no value, transactionOccurred is false and intent is the intent the agent is serving." with "After a commit, every outcome sets transactionOccurred true and carries the committed reference. Otherwise, where an outcome states no value, transactionOccurred is false. Where an outcome states no intent, intent is the intent the agent is serving." In `transfer_unavailable`, replace "transactionOccurred false;" with "transactionOccurred per the contract;". 2 edits, +18 words.
B. Edit only `transferred_to_human` and `transfer_unavailable`: "transactionOccurred true with the committed reference after a commit, else false". 2 edits, +14 words.
C. Leave as is.

### D-02 · The keep-prior-Tax-Pro answer has no effect when scenario_selection items 2 to 6 match first
Anchor: `workflow.schedule_new[1]`; `broadening.scenario_selection` items 2 to 6, 8, 9
Severity: Medium
Class: Human
Issue: Step 2 asks every returning client with an active prior Tax Pro "whether to keep them", and a yes "selects returning_same_tax_pro". Selection is first-match-wins after ready, and items 3 to 6 precede item 8. The yes selects nothing on physical_drop_off (item 2), emerald_advance, tax_notice_service and callback (item 4), tax_extension with an open window (item 5), or any same-day request (item 6). The ladders for those scenarios carry no same-Tax-Pro rung. No rule sends the kept Tax Pro as `taxProPreference` with source `prior_tax_pro`. Item 8 also still says "who asks for the prior Tax Pro".
Fix: Options:
A. (Recommended) Scope the question: in `workflow.schedule_new[1]`, replace "If a returning client's prior Tax Pro is active, ask whether to keep them;" with "On tax_prep with a returning client whose prior Tax Pro is active, ask whether to keep them;". Same-day still wastes one answer. 1 edit, +7 words.
B. Move item 8 above item 6 and scope the question as in A. 2 edits, +10 words.
C. Keep the question for every type and send the kept Tax Pro as `taxProPreference` (source `prior_tax_pro`) in every scenario. 2 edits, +25 words.

### D-03 · Reschedule floor: step 4 raise conflicts with the type floor and the physical_drop_off null
Anchor: `workflow.reschedule_existing[3]`; `scheduler_always` floor items; §2 Complexity Matching > Reschedule
Severity: Medium
Class: Human
Issue: Same conflict as B-04, C-03, E-05. Type is immutable on reschedule, so the bound appointment can be emerald_advance, tax_notice_service, callback, or physical_drop_off, whose floors are 1 or null. Step 4 says "the higher of" baseline and level with no type exception.
Fix: Options:
A. (Recommended) Type floors apply on reschedule. In `workflow.reschedule_existing[3]`, add ", except the type floors in scheduler_always (1 or null)". In the §2 Reschedule prose add "raised to the bound Tax Pro's cert level". 2 edits, +18 words.
B. The reschedule rule wins for emerald_advance, tax_notice_service, and callback; physical_drop_off stays null. 2 edits, +15 words.

### D-04 · After "stay" at the peak trade-off, rung 5 of returning_same_tax_pro is undefined
Anchor: §2 State 3 Tax Pro Trade-off; `broadening.ladders.returning_same_tax_pro.rungs[4]`; `scenario_selection` item 7
Severity: Medium
Class: Human
Issue: D-064 makes "stay" hold "for the rest of the invocation", and item 7 never switches after it. Rung 5 (`any_qualified_tax_pro`) still runs "only after the Tax Pro trade-off returns permission", which is the same question. Reachable: a peak-season no_slots with office_at_capacity triggers the item 7 trade-off, the caller says stay, the ladder reaches rung 5. The spec does not say whether the earlier "stay" counts as the refusal or whether the question is asked again.
Fix: Options:
A. (Recommended) The earlier "stay" answers rung 5. In §2 Tax Pro Trade-off, replace `"Stay" holds for the rest of the invocation.` with `"Stay" holds for the rest of the invocation, including the ladder step that drops the Tax Pro.` In rung 5, add "; exhausted after a stay". 2 edits, +14 words.
B. Ask again at rung 5 and let that answer override the earlier stay. 2 edits, +12 words.

### D-05 · "officeRef on either handoff" no longer covers Part 4's another-Tax-Pro handoff
Anchor: §1.5 `terminal_payload_contract`; §4 `agent_specific_outcomes.routed_to_scheduler`
Severity: Medium
Class: Safe
Issue: D-085 narrowed the second handoff to "to appointment_scheduler for a callback". "Either handoff" now names only the message and callback handoffs. Part 4 `routed_to_scheduler` for another Tax Pro carries "officeRef only when known" (D-040, still binding). Part 1 outranks Part 4 (C-1). D-085 changed only taxProRef.
Fix: In `terminal_payload_contract`, replace `and officeRef on either handoff` with `and officeRef, when known, on any handoff to leave a message or to appointment_scheduler`. 1 edit, +8 words. (Duplicate of B-02, E-08; the orchestrator will use the B-02 wording, which is explicit about routed_to_scheduler.)

### D-06 · phone_callback reason has no capture point when the method is chosen after step 3
Anchor: `scheduler_always` item "On any phone_callback, capture the reason..."; §2 Appointment Type Rules table, callback row; `workflow.schedule_new[2]`; `broadening.ladders.tax_notice.rungs[5]`
Severity: Medium
Class: Human
Issue: D-083 requires the one-phrase reason on any phone_callback and gives no timing. `workflow.schedule_new[2]` captures "method-specific contact detail" before readiness. On the tax_notice ladder, rung 6 (`phone_callback`) is accepted during step 4, after step 3 has passed, and the flow goes straight to the gate. The gate never reads the reason back (D-086), so nothing prompts for it. `appointmentNotes` would go out null on a phone_callback.
Fix: Options:
A. (Recommended) State the timing once. In the `scheduler_always` phone_callback item and the callback table row, replace "On any phone_callback, capture the reason" with "On any phone_callback, including an accepted phone_callback rung, capture the reason before the gate". 2 edits, +10 words.
B. Capture the reason only when the method is chosen at step 2 and skip it on a rung acceptance, with `appointmentNotes` null there. 2 edits, +8 words.

### D-07 · Cross-Office Restriction can no longer fire after D-044 and D-094
Anchor: §3 Office Contact Triage > Routed Office and > Cross-Office Restriction; `office_never` phone item; `office_always[2]`
Severity: Medium
Class: Human
Issue: Named Office resolves a caller-named office through a ZIP and a match. D-044 makes that office "the routed office for the rest of the invocation", and D-094 extends this to office_contact. Cross-Office Restriction allows a phone number "only for the routed office", so any office the caller names becomes the routed office, the rule never triggers, and the `office_never` phone item is unreachable.
Fix: Options:
A. (Recommended) Keep D-044 and delete Cross-Office Restriction and the `office_never` phone item. About -45 words, 2 edits.
B. Restrict D-044's promotion to hours and status, and keep the phone number to the dialed `routedOfficeRef` office. 2 edits, +15 words.

Summary: 7 findings. Critical 0, High 0, Medium 7, Low 0. Safe 1 (D-05), Human 6 (D-01, D-02, D-03, D-04, D-06, D-07).
