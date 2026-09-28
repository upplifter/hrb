# Round 7 · Lens F findings

Saved by the orchestrator from the reviewer's reply. 20 findings, all Low, about -158 words. [R6] marks round 6 text. Full current and replacement strings are in the reviewer's reply as passed to the fixer (see changes.md).

| ID | Anchor | Proposal | Words | Triage |
|---|---|---|---|---|
| F-01 | §1.5 context_envelope.taxProRef, officeRef | Point to context_envelope.appointmentType | -14 | Backlog (oscillation guard) |
| F-02 | §4 workflow.speak_to_tp_generic[2] | Point to tax_pro_always third-party rule | -13 | Backlog (oscillation guard) |
| F-03 | §5.1 transfer_to_agent > Transfer results | Point to global_always and global_outcomes.outcome_unknown | -10 | Fix |
| F-04 | [R6] §5.2 Automation Flags; scheduler_always too_many item | Drop "Appointment-details questions ignore both flags" | -11 | Backlog (D-065 text, held) |
| F-05 | [R6] §3 office_always by_appointment_only item | Drop the return sentence | -10 | Backlog (D-062 text, held) |
| F-06 | scheduler_always invalid_location item | Drop none_nearby sentence (in no_acceptable_availability) | -9 | Fix |
| F-07 | scheduler_always rollover item | "Never ask for or speak entryPoint or dialedOfficeNumber." | -9 | Backlog (oscillation guard) |
| F-08 | §4 agent_specific_tools.find_customer | "Read-only; per tax_pro_always." | -8 | Fix |
| F-09 | §3 Office Contact Triage > If CLOSED | Trim | -7 | Backlog with C-04 (oscillation guard) |
| F-10 | §3 Office Contact Triage > If OPEN; office_always OPEN, CLOSED | Drop "stop speaking" | -7 | Backlog with C-04 (oscillation guard) |
| F-11 | [R6] §3 Office Details Logic > By-Appointment-Only | Drop the return sentence | -7 | Backlog (D-062 text, held) |
| F-12 | §4 tax_pro_always options item | Drop stale "declines both" clause (outcome defines it) | -7 | Fix |
| F-13 | §4 tax_pro_always last item | Drop message clause (global_always, C-3 A) | -7 | Fix |
| F-14 | closure.line_patterns | Trim nothing_to_do and no_transaction values | -6 | Backlog (oscillation guard) |
| F-15 | §2 DDO Rules second bullet | Drop "skip the text offer and execute" | -5 | Backlog (oscillation guard) |
| F-16 | broadening.ladders.same_day.rungs[1] | Point to the lexicon office_at_capacity line | -4 | Fix |
| F-17 | scheduler_always gatekeeper and waterfall items | "run", drop filler | -3 | Backlog (oscillation guard) |
| F-18 | §3 Off-Season Closure; office_always closed_for_season item | Drop "proactively", "explicitly" | -2 | Fix |
| F-19 | §5.2 get_customer_appointments Note | Merge fragments, drop "Used to" | -1 | Fix |
| F-20 | Part 5 Conventions rating bullet; §1.1 customerRef row | En dash; "do not" -> "never" | 0 | §1.1 half fixed; Conventions half backlog (guard) |
