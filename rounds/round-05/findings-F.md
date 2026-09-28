# Round 5 · Lens F findings

Saved by the orchestrator from the reviewer's reply. All Low, Safe, net-negative.

F-01 | workflow.schedule_new[4]; reschedule_existing[4] | Text-and-gate steps repeat scheduler_always | schedule_new[4]: "5 Text and gate. On a no, ask once what to change; a change re-enters negotiation, and a second no returns customer_declined_options. On digital drop-off, the destination readback is the whole gate." reschedule_existing[4]: "5 Text and gate. Handle a no per workflow.schedule_new[4]." | -29w
F-02 | global_outcomes.configuration_missing | Copies handoff_invalid | "A required configuration value is absent. Otherwise identical to handoff_invalid." | -18w
F-03 | agent_specific_tools.find_available_slots | 62 words, restates rules | "Read-only. Call only on ready. Send scenario and rung from broadening; suggest is informational only. Never offer a slot with a non-null relaxedConstraint unless the caller consented to that rung. On invalid_constraints, re-run readiness once; a second one transfers as system_failure." | -18w
F-04 | tax_pro_always[0] | Says the same thing twice | "Elicit the reason for the call first." | -17w
F-05 | office_never[3] | Repeats global_never web ban (C-3 A) | Delete. | -17w
F-06 | office_always[4]; office_never[1] | Open-status rule stated twice | Delete office_always[4]; office_never[1]: "Never perform timezone math, calculate hours, or guess whether an office is open; use only check_office_open_status." | -16w
F-07 | scheduler_never[2] | Repeats global_never finance/notice ban | "Beyond global_never, never state or estimate a loan amount, rate, payment, eligibility, or likelihood of approval, interpret a notice code, or quote a discount or interest figure. Handle personal advice, calculation, and notice questions per agent_specific_tools.search_knowledge_base." | -12w
F-08 | workflow.speak_to_tp_by_name[2] | Repeats tax_pro_always | "3. Call search_tax_pro_by_name per tax_pro_always." | -12w
F-09 | scheduler_always DDO item | Descriptive sentence; "execute" | "For digital drop-off, call send_secure_link, never book_appointment. A DDO change request is a new schedule_new DDO send." | -10w
F-10 | global_always[1] | Repeats questions_per_turn | "Ask questions per global_voice_lexicon.questions_per_turn. Open a multi-question sequence with a one-line purpose." | -9w
F-11 | agent_specific_tools.check_search_readiness | Repeats one-question rule | "On needs_more, ask only the askFor item." | -9w
F-12 | Part 4 objective | Partial repeat of Base handback | Delete "Hand back refund and login queries per global_always." | -8w
F-13 | §3 Unclear intent; office_always[1] | Wordy | Prose: "- **Unclear intent:** Reprompt once with a choice between "hours and address" or "speaking to the office staff"; a second unclear answer transfers as clarification_exhausted." JSON first sentence: "Reprompt an unclear intent once with a choice between 'hours and address' or 'speaking to office staff'; if still unclear, transfer as clarification_exhausted." | -8w
F-14 | §5.2 book_appointment Note third bullet | Names fields the request lacks | Delete. | -8w
F-15 | global_outcomes.customer_abandoned | "unanswered gate" twice | "The platform signaled a dropped call. An unanswered gate is not abandonment; it runs the no-input rule, then terminates. Never write on silence. ..." | -7w
F-16 | tax_pro_always[6] | Prose trim not mirrored | "If the caller chooses a callback, return routed_to_scheduler with appointmentType callback and the confirmed taxProRef and officeRef. A callback only reaches ..." | -6w
F-17 | §2 State 3 Tax Pro Trade-off | Repeats a principle | Delete "Never substitute a Tax Pro silently." | -6w
F-18 | workflow.office_contact_flow[0] | Flow internals (C-11) | "0. On an explicit message request, return leave_message without office triage." | -6w
F-19 | interruptions.cancel_said | Repeats intent_changed close rule | "...After a commit, a cancel or change request hands back intent_changed with routingTarget appointment_scheduler and the committed reference." | -5w
F-20 | scheduler_always text-offer item | "self-service" vs first_party | "For a first-party transaction" | 0w
F-21 | §1.3 last bullet | Ambiguous "the deterministic flow" | "- Pass only known context; the Leave a Message flow collects the rest." | 0w
