# Round 5 · Lens B findings

Saved by the orchestrator from the reviewer's reply.

B-01 | Medium | Safe | §1.3 third bullet; global_always leave-message item | leave_message_offer triggers omit D-045's hours_unavailable case | §1.3: "...or the caller's target office is closed, busy, or hours_unavailable."; JSON: "or the target office is closed, busy, or hours_unavailable,"
B-02 | Medium | Safe | interruptions.intent_change (Parts 2, 3, 4); global_always identity item | "never transfer" blocks the D-046 identity/fraud transfer | Scheduler: "Outside scheduling, other than a cancellation, a live-agent request, or a global_always identity question, hand back intent_changed; never transfer or attempt it." Part 3: "Outside office information, other than a live-agent request or a global_always identity question, hand back intent_changed." Part 4: "Outside reaching a Tax Pro, other than a live-agent request or a global_always identity question, hand back intent_changed."
B-03 | Medium | Human | §2 State 2 After Part 4; scheduler_always routed_to_scheduler item | After Part 4 rule collides with a carried callback type | Same as A-01, C-02, E-02, D-05.
B-04 | Medium | Human | terminal_payload_contract taxProRef/officeRef clause; routed_to_scheduler; §1.1 taxProRef | Contract carries the unavailable Tax Pro's taxProRef into the another-Tax-Pro handoff, and committed refs into Scheduler intent_changed handoffs | Decide which handoffs to appointment_scheduler carry taxProRef and officeRef.
B-05 | Medium | Human | §2 State 3 Appointment Details; get_customer_appointments; informational_question | Details answer ends a booking in progress | Same as D-03.
B-06 | Low | Safe | global_outcomes.intent_changed | Defined as "outside scope", but D-041 and D-019 use it inside scope | "Caller moves outside the current agent's scope or, after a commit, asks for another transaction."
B-07 | Low | Safe | office_never[3] | Repeats global_never | Same as F-05.
B-08 | Low | Safe | §5.2 find_customer Note | Narrows priorTaxProStatus purpose; explains why | "Note: priorTaxProStatus is never spoken."
