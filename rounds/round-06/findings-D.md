# Round 6 · Lens D findings

Saved by the orchestrator from the reviewer's reply.

### D-01 · office_contact at a by_appointment_only office falls into the booking handoff
Anchor: §3 Office Contact Triage (first bullet); workflow.office_contact_flow[1]; office_always by_appointment_only item
Severity: Medium
Class: Human
Issue: office_contact_flow[1] applies office_info_flow step 2, whose by_appointment_only rule returns route_intent to appointment_scheduler, so a caller wanting the receptionist or a message is handed to booking. The prose branches only on closed_for_season. Related to L-081 (office_info path only); D-045 created this call site.
Options: (a) state appointment-only and continue to check_office_open_status; (b) return office_contact_triage_complete with leave_message_offer, like D-053; (c) keep route_intent for both paths and settle its outcome under L-081.

### D-02 · The "any qualified Tax Pro" rung returns to the office the caller rejected
Anchor: §2 State 3 Declined Offices; workflow.schedule_new[1]; broadening.ladders.returning_same_tax_pro.rungs[4]
Severity: Medium
Class: Human
Issue: After a rejected last-served office (D-048), rung 5 "any_qualified_tax_pro at that office" offers the rejected office. Also, declining every rung 3 nearby office hits Declined Offices (customer_declined_options) while the ladder says move to rung 4.
Options: (a) after a rejected last-served office mark rung 5 exhausted, and declining every rung 3 office moves to rung 4; (b) rung 5 runs at the rung 3 office or the entryPoint office; (c) declining every rung 3 office returns customer_declined_options.

### D-03 · Peak trade-off "once per invocation" leaves no rule after "stay" lapses
Anchor: §2 State 3 Tax Pro Trade-off; broadening.scenario_selection item 7
Severity: Medium
Class: Human
Issue: After "stay" and a caller-initiated constraint change, item 7 fires again but the question cannot be re-asked; the agent must switch silently or keep the ladder without a rule.
Options: (a) "stay" holds for the invocation; (b) a constraint change allows one more trade-off question; (c) after the question is used, item 7 keeps returning_same_tax_pro.

No other Medium-or-higher lens D issues found.
