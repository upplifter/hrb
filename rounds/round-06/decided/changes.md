# Round 6 decided changes (D-061 to D-072)

Format: `ledger ID | anchor | change | net words (approx.)`. Applied by the orchestrator. Lint after the batch: RESULT WARN, no FAIL; round growth +0.81% (limit 1.0%); JSON valid.

L-369 | §4 Out-of-Scope (Appointments) (new sub-bullet); tax_pro_always callback item and new item after it; routed_to_scheduler; tax_pro_options_declined | Non-callback booking with a confirmed Tax Pro: state once only a callback can be booked, offer callback, message, or another Tax Pro, never intent_changed; routed_to_scheduler no longer limits appointmentType null to an unavailable Tax Pro; tax_pro_options_declined covers declining every offered option (D-061) | +50
L-081, L-370 | §3 By-Appointment-Only; §3 If closed_for_season (now "or by_appointment_only"); office_always by_appointment_only item; workflow.office_contact_flow[1]; office_info_provided; office_contact_triage_complete; Mini-Dialogue 3D System line (C-9) | office_info returns office_info_provided; office_contact skips open status, gives no number, returns office_contact_triage_complete with leave_message_offer (D-062) | +20
L-371 | §2 State 3 Declined Offices (split into sub-bullets); ladders.returning_same_tax_pro rungs 3 and 5; customer_declined_options | customer_declined_options only at office resolution; rejected last-served office exhausts rung 5; declining every rung 3 office moves on (D-063) | +35
L-372 | §2 State 3 Tax Pro Trade-off; scenario_selection item 7 | "Stay" holds for the rest of the invocation (D-064) | -5
L-375 | scheduler_always too_many item; §2 State 3 Appointment Details sub-bullet; §5.2 Automation Flags | Flags apply on reschedule_existing or cancel_existing; details questions ignore them (D-065) | +22
L-376 | §1.3 Leave-a-Message Ownership third bullet; global_always leave-message item | Closed, busy, by_appointment_only, hours_unavailable trigger scoped to office_contact (D-066; by_appointment_only per D-062) | +5
L-377 | §1.3 second bullet; global_always leave-message item (split in two); §2 State 3 Informational Interruptions (new Message Request bullet); scheduler_always (new message item) | Scheduler hands a message request back to speak_to_tax_pro or office_information outside transfer_unavailable (D-067) | +70
L-378 | agent_specific_outcomes.no_acceptable_availability | Agreed constraints go in knownSoFar; carry scenario and exhaustedRungs (D-068) | 0
L-379 | §3 Office Details Logic (new Lookup Failure bullet); Part 3 agent_specific_tools.transfer_to_agent; terminal_payload_contract transferReason system_failure | office_not_found on a non-caller officeRef transfers as system_failure (D-069) | +25
L-084, L-150 | §2 State 1 (new No Match Outside a New Booking bullet); scheduler_always ANI/authentication item; §4 Generic Request; tax_pro_always unavailable item | Scheduler no_match on reschedule, cancel, or details transfers as identity_unresolved; Part 4 first-party no_match offers only the Scheduler (D-070) | +40
L-085, L-135 | §2 State 1 State Persistence; scheduler_always customerRef item; workflow.speak_to_tp_generic[2]; §5.2 find_customer request (customerRef field, approved) and new Carried identity bullet | Carried customerRef skips identity questions; find_customer runs with customerRef alone (D-071) | +45
L-090, L-160, L-163 | global_never message item; §2 State 2 callback row; scheduler_always callback item; §5.2 book_appointment existing-customer example | Callback reason is one short phrase and not message content; example drops phoneNumber and contact and sets appointmentNotes null (D-072) | +10

Offsetting Safe trims (every trigger kept), about -115 words:
- §1.3 second bullet: "finish the current sentence, stop speaking, and return control to Head of Call" became "finish the sentence, stop, and return" (returnControlTo is always head_of_call).
- closure.line_patterns handoff_unavailable: restated global_always and global_outcomes.transfer_unavailable; now points to them (C-3 A).
- scheduler_always gate-correction item: steps restating invalidation.upstream_change replaced by a pointer.
- Scheduler, Part 3, and Part 4 agent_specific_outcomes: dropped "transactionOccurred false" and, in the Scheduler and Part 4, "intent <own intent>", which restate the terminal_payload_contract default. Part 3 keeps intent because it varies by path.
- customer_declined_options: "a second own-Tax-Pro request" became "repeats an own-Tax-Pro request" (grammar; the length WARN is cleared).
- Skipped for the oscillation guard: §5.1 transfer_to_agent Transfer results (edited in rounds 2 to 4).

## Follow-up from verify.md

L-369 (follow-up) | Part 4 objective; §4 Fulfillment Priority step 4; tax_pro_always callback item | Stale "when that one is unavailable" and "decline both" updated; positional pointer made a key path | 0
L-081, L-370 (follow-up) | §3 If closed_for_season or by_appointment_only | Year-Round Office address kept on closed_for_season | +5
L-379 (follow-up) | §3 Lookup Failure | "On either path" | +2
L-084, L-150 (follow-up) | §2 State 1 No Match Outside a New Booking | Heading-path pointer | 0
L-090, L-160, L-163 (follow-up) | §5.2 book_appointment Note | "appointmentNotes is null except on callback." | +6
