# Round 8 · Lens D findings

Saved by the orchestrator from the reviewer's reply.

### D-01 · After Part 4, the keep-prior-Tax-Pro question contradicts D-081
Anchor: §2 State 5 workflow.schedule_new[1]; scheduler_always routed_to_scheduler item; §2 State 2 Appointment Type Rules > After Part 4
Severity: Medium
Class: Human
Issue: Under D-050, after a Part 4 routed_to_scheduler, schedule_new[1] still asks whether to keep an active prior Tax Pro, and a yes selects returning_same_tax_pro. Under D-081, a request for the caller's own Tax Pro after Part 4 gets "this booking is with another Tax Pro". Take the D-061 path, where Part 4 confirmed an active prior Tax Pro and said only a callback can be booked with them. There the Scheduler asks a question it must then refuse on a yes.
Options: A. (Recommended) After Part 4, skip the keep-prior question. Add "except After Part 4" to schedule_new[1] and to the After Part 4 prose. This supersedes the D-050 "still asks" clause. B. Keep the question and let a yes book with the prior Tax Pro. D-081's statement then applies only to the Tax Pro Part 4 named when that Tax Pro is not the prior one. C. Keep the question only when Part 4 named a Tax Pro other than the prior one. Footprint: A ≈ 2 edits, +10 words; B ≈ 3 edits, +20 words; C ≈ 2 edits, +18 words.

### D-02 · efile entry proposes an inactive prior Tax Pro
Anchor: §2 State 5 scheduler_always efile_rejection_retail item; workflow.schedule_new[1]; scenario_selection items 8-9
Severity: Medium
Class: Human
Issue: The efile item says "Propose the prior Tax Pro returned by find_customer where there is one". find_customer returns priorTaxProName even when priorTaxProStatus is inactive. schedule_new[1] and scenario_selection item 8 act on the prior Tax Pro only when active, and item 9 selects returning_tax_pro_unavailable for an inactive one. So the caller can be offered a Tax Pro whom the selected scenario never searches.
Options: A. (Recommended) Change "where there is one" to "when priorTaxProStatus is active". B. Keep the proposal, and on an inactive prior Tax Pro state once that they are unavailable before following workflow.schedule_new. Footprint: A ≈ 1 edit, +3 words; B ≈ 1 edit, +14 words.

### D-03 · A readiness conflict that is neither a past date nor a type-row closed window has no branch
Anchor: §2 State 5 agent_specific_tools.check_search_readiness; §5.2 check_search_readiness Outcome Results (conflict)
Severity: Medium
Class: Human
Issue: After D-078, a conflict speaks the past-date line only for a past date, and a closed window follows the type row. Only tax_extension and emerald_advance have a closed-window row. §5.2 also defines conflict as "Constraints conflict" in general, so an implementer must guess the first-turn handling in two cases: any other conflict, and a closed window on tax_prep, tax_notice_service, or callback. Only the second consecutive conflict is capped.
Options: A. (Recommended) On any other conflict, reprompt once for the conflicting constraint, then the Readiness Cap applies. B. On any other conflict, transfer as system_failure. C. On any other conflict, transfer as validation_failed. Footprint: A ≈ 2 edits (JSON entry and Readiness Cap bullet), +14 words; B ≈ 2 edits, +10 words; C ≈ 2 edits and a global_outcomes.validation_failed wording check, +12 words.

### D-04 · partial_acceptance widens with no scenario or rung for find_available_slots
Anchor: §2 State 5 invalidation.partial_acceptance; invalidation.ladder_state; broadening.scenario_selection; ladders.returning_same_tax_pro, ladders.reschedule
Severity: Medium
Class: Human
Issue: After D-074, rejecting a proposed Tax Pro while keeping the office widens to eligible Tax Pros at that office without the trade-off. find_available_slots requires scenario and rung, and returning_same_tax_pro and reschedule reach "any qualified Tax Pro" only at their last rung, after the trade-off. The spec does not say whether the widening re-selects the scenario, which ladder_state does only on a caller-initiated constraint change, or jumps to the any_qualified_tax_pro rung, skipping the earlier ones.
Options: A. (Recommended) Treat the rejection as a caller-initiated constraint change: apply ladder_state, so returning_same_tax_pro re-selects returning_tax_pro_unavailable at that office, and other scenarios restart at their primary offer. B. Send rung any_qualified_tax_pro in the current scenario and mark earlier rungs skipped. Footprint: A ≈ 1 edit, +12 words; B ≈ 2 edits, +15 words.

### D-05 · book_appointment example books a phone_callback with null appointmentNotes
Anchor: §5.2 book_appointment Request JSON (Existing Customer).appointmentMethod
Severity: Low
Class: Safe
Issue: D-083 requires the one-phrase reason in appointmentNotes on any phone_callback. The existing-customer example is a tax_prep phone_callback with appointmentNotes null, which D-072 fixed as null. Changing the method is the only fix that satisfies both decisions.
Fix: Old: "\"appointmentMethod\": \"phone_callback\"," New: "\"appointmentMethod\": \"in_person\","

Summary: 5 findings (4 Medium, 1 Low).
