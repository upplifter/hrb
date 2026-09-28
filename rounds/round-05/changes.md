# Round 5 changes (Safe fixes)

Format: `ledger ID | anchor | change | net words (approx.)`. Lint after the batch: RESULT WARN, no FAIL; round growth -0.42%; JSON valid.

Triage note: L-326 and L-327 sit on anchors edited in 3 earlier rounds. The guard was not applied because each completes a round 4 decision (D-048, D-043) on an anchor that decision names; they are decided propagation, not new rewording. Pure editorial items on guarded anchors went to the backlog (L-346 to L-356).

L-326 | workflow.schedule_new[1] | "rejecting it" became "rejecting that office" (D-048) | +1
L-327 | global_outcomes.transfer_unavailable | nextAction clause and supportHoursSpoken scoped to agent_unavailable; failed call takes nextAction transfer (D-043); now within 60 words, closing L-176 | -3
L-328 | §1.3 third bullet; global_always leave-message item | Target office "closed, busy, or hours_unavailable" (D-045) | +1
L-329 | interruptions.intent_change in Parts 2, 3, and 4 | Exception for a global_always identity question (D-046); Parts 3 and 4 also name the live-agent request | +8
L-330 | global_outcomes.intent_changed | Adds "or, after a commit, asks for another transaction" (D-041, D-019) | +8
L-331 | §3 Routed Office | "On either path" | +3
L-332 | workflow.speak_to_tp_by_name[4] | Options only for an active Tax Pro taking appointments; otherwise the unavailable item | +15
L-333 | §1.3 last bullet | Names the Leave a Message flow | -3
L-334 | office_never web item | Deleted (C-3 A) | -17
L-335 | workflow.schedule_new[4], reschedule_existing[4] | Text-offer and explicit-yes repeats cut | -29
L-336 | tax_pro_always[0] | Second sentence cut | -17
L-337 | office_always office_contact status item; office_never timezone item | Merged into office_never | -16
L-338 | workflow.speak_to_tp_by_name[2] | Points to tax_pro_always | -12
L-339 | global_always questions item | Points to global_voice_lexicon.questions_per_turn | -5
L-340 | §5.2 book_appointment Note | Backend-field bullet deleted | -8
L-341 | global_outcomes.customer_abandoned | Trigger trimmed | -7
L-342 | §2 State 3 Tax Pro Trade-off | "Never substitute a Tax Pro silently." cut (Principles covers it) | -6
L-343 | interruptions.cancel_said | "closes the committed transaction and" cut (intent_changed covers it) | -5
L-344 | scheduler_always text-offer item | "self-service" became "first-party" | 0
L-345 | §5.2 find_customer Note | "Note: priorTaxProStatus is never spoken." | -6
