# Round 5 decided changes (D-050 to D-060)

Format: `ledger ID | anchor | change | net words (approx.)`. Applied by the orchestrator. Lint after the batch: RESULT WARN, no FAIL; round growth +0.99% (limit 1.0%); JSON valid.

L-357, L-358, L-360 | §1.1 operation row; context_envelope.operation; §2 State 2 After Part 4; scheduler_always routed_to_scheduler item | Rule scoped to priorTransaction.finalOutcome routed_to_scheduler with no carried appointmentType; that handoff means schedule_new; the keep-prior-Tax-Pro question stays (D-050, option B) | +25
L-359 | §2 State 2 After Part 4 (sub-bullet); scheduler_always routed_to_scheduler item | Own Tax Pro request after Part 4: say once they aren't available, continue; a second request returns customer_declined_options (D-051) | +30
L-361 | §1.1 appointmentType/taxProRef/officeRef row; context_envelope.appointmentType, taxProRef, officeRef | Carried values are copied by Head of Call from a prior handoff (D-052) | +6
L-362 | §3 If closed_for_season (new bullet); workflow.office_contact_flow[1]; office_contact_triage_complete | closed_for_season on office_contact: skip open status, no phone number, return office_contact_triage_complete with leave_message_offer (D-053) | +45
L-324, L-363, L-364 | §1.1 operation row; context_envelope.operation; §2 State 3 Appointment Details; agent_specific_tools.get_customer_appointments; agent_specific_outcomes.appointment_details_provided (new, approved); §3 Out of Scope; office_never scheduling item; §4 Out-of-Scope (Appointments); tax_pro_always callback item | Details question needs no operation; mid-booking resume, else appointment_details_provided; none_found, several, canceled, too_many handled; Parts 3 and 4 hand appointment questions to the Scheduler (D-054) | +95
L-325, L-365 | terminal_payload_contract nextAction enum and capture_intent definition; §3 Unclear intent; office_always disambiguation item | capture_intent deleted; unresolved Part 3 intent carries intent office_info (D-055) | -12
L-322 | §3 No Match (merged No Name Match and ZIP Not Found); office_always named-office item | Name no-match transfers as clarification_exhausted (D-056) | -10
L-366 | §2 State 2 DDO Rules > Changes (was Rescheduling); scheduler_always DDO item | Post-send change hands back with no reference; null-operation DDO change sets schedule_new with digital_drop_off (D-058) | +30
L-367 | §2 State 4 Operation Switch (new bullet); interruptions.cancel_said; workflow.cancel_existing[2] | Pre-commit switch among book, change, cancel runs the new workflow, keeping authentication (D-059) | +35
L-368 | §2 State 2 tax_extension row; customer_declined_options | Closed-window tax_prep decline returns customer_declined_options; outcome rewritten shorter (D-060) | -2
L-323 | none | D-057 keeps no_approved_answer in Part 4 | 0

Offsetting Safe trims (brevity, every trigger kept): scheduler_always office-identity item and transactionSubject item; closure.continuation_context; tax_pro objective (dropped the restated global_always pointer); durationSpoken item; confirmation-object item; §2 After Part 4 lead-in; interruptions.cancel_said. About -85 words.
