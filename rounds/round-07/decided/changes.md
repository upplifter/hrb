# Round 7 decided changes (D-073 to D-083)

Format: `ledger ID | anchor | change | net words (approx.)`. Applied by the orchestrator. Lint after the batch: RESULT WARN, no FAIL, no new warning except two expected C-2 mirror copies (D-076); round growth +0.90% (limit 1.0%); JSON valid.

L-393 | §5.2 get_customer_appointments Response JSON and Note | Added date, requestedTime, officeRef, taxProRef per appointment; Note says taxProRef is null with no named Tax Pro (D-073) | +10
L-074, L-075 | invalidation.partial_acceptance; scheduler_always efile_rejection_retail item | Partial rejection widens without asking the trade-off; efile item follows workflow.schedule_new (D-074) | -5
L-080 | §1.4 Off-season row Path cell | Scoped to "(Scheduler)"; frozen line unchanged (D-075) | +1
L-089 | global_voice_lexicon.empathy | Appended five §1.4 lines with path tags (D-076; budget exception approved) | +70
L-140 | §4 Speak to Tax Pro (Generic) | Deleted "or office associate" (D-077) | -2
L-146, L-394 | §1.4 conflict row Path cell; §2 State 3 Readiness (new Readiness Cap bullet); agent_specific_tools.check_search_readiness; scheduler_always (new cap item); emerald_advance type row and scheduler_always emerald item; customer_declined_options | Past-date line only for a past date; closed emerald_advance window states unavailable and returns customer_declined_options; repeat conflict or needs_more is a second no-match (D-078) | +55
L-162 | §5.2 check_search_readiness (new taxProPreference.source bullet) | Enum caller_stated, prior_tax_pro, carried, existing_appointment (D-079) | +12
L-164 | none | D-080: no edit | 0
L-383 | §2 State 2 Tax Pro Requests and After Part 4; scheduler_always routed_to_scheduler item; customer_declined_options | Own or Part 4-named Tax Pro: one statement that this booking is with another Tax Pro, second request customer_declined_options, never hand back (D-081) | +10
L-384 | §2 State 3 Message Request; scheduler_always message item | No recipient defaults to speak_to_tax_pro (D-082) | -2
L-385 | scheduler_always callback item; §2 After Part 4 first sub-bullet; §5.2 book_appointment Note; global_never message item | Reason captured on any phone_callback (D-083) | +8
L-136 | none | Rejected (Q-76 B, "not an issue") | 0

Offsetting Safe trims (every trigger kept):
- agent_specific_tools.check_search_readiness: dropped "as one question at the end of the turn" (restates global_voice_lexicon.questions_per_turn) and "scheduling".
- customer_declined_options: "without accepting a time or asking for a person" to "without a time or a person"; "a non-cancellation gate; or declines the cancellation gate" to "another gate or once at the cancellation gate".
