# Round 8 decided changes (D-084 to D-099)

Format: `ledger ID | anchor | change | net words (approx.)`. Applied by the orchestrator. Lint after the batch: RESULT WARN, no FAIL; round growth +0.92% (limit 1.0%); total growth +3.24%; JSON valid. Only the two pre-existing length warnings remain (L-417).

L-418 | §2 State 2 After Part 4 (new sub-bullet); scheduler_always routed_to_scheduler item | Never ask whether to keep the prior Tax Pro after a Part 4 routed_to_scheduler (D-084) | +12
L-419 | §1.5 terminal_payload_contract | taxProRef only on a message handoff or a callback handoff to appointment_scheduler; officeRef on either (D-085). "For a callback" was scoped to taxProRef so officeRef still reaches the Scheduler on every handoff, as §4 routed_to_scheduler requires. | +6
L-420, L-401 | §1.2 Confirmed at capture; global_always confirm-at-capture item; scheduler_always third-party item | Third-party owner's name added to global_always; phone_callback reason exempt in both; "Confirm the name at capture." deleted from scheduler_always (D-086) | +8
L-421 | global_always empathy item | Free acknowledgment only with a line that promises no person; other lines only on their own path (D-087) | +15
L-422 | scheduler_always efile_rejection_retail item | "where there is one" to "when priorTaxProStatus is active" (D-088) | +1
L-423 | §2 State 3 Readiness (new Other Conflict bullet); agent_specific_tools.check_search_readiness | Any other conflict asks once for another date or time (D-089) | +20
L-424 | invalidation.partial_acceptance | Caller-initiated change under ladder_state; returning_same_tax_pro re-selects returning_tax_pro_unavailable (D-090) | +10
L-398 | §4 Generic Request (new sub-bullet); workflow.speak_to_tp_generic[2] | multiple_matches transfers as identity_unresolved (D-091) | +16
L-399 | §2 State 1 Dynamic State Invalidation: Identity; invalidation.customer_identity | Identity change also clears carried customerRef, appointmentType, taxProRef, officeRef (D-092) | +20
L-404 | scheduler_always new-customer item; §5.2 book_appointment Note | newCustomer.phoneNumber is the callback number; contact.callbackNumber removed (D-093) | -6
L-397 | §3 Office Contact Triage; workflow.office_contact_flow[1] | Resolve a caller-named office per Named Office (D-094) | +18
L-395 | workflow.reschedule_existing[3]; §2 Complexity Matching (new Reschedule bullet) | Inherited baseline taken silently, no gatekeeper or waterfall (D-095) | +18
L-396 | §2 State 3 Ladders, Rescheduling row; ladders.reschedule rungs[2], [3] | No named Tax Pro: rung 3 any qualified Tax Pro, rung 4 skipped (D-096). Condition placed in the Primary cell to avoid a new cell-length warning. | +20
L-400 | global_always informational item; §1.2 Tax/Financial Boundary; §2 Informational Interruptions > Hand back; §3 Out of Scope | Out-of-task logistics questions to faq_agent; Part 3 hands back only questions about an existing appointment (D-097) | +12
L-402 | §1.4 outcome_unknown row; global_voice_lexicon.empathy | Both frozen copies reworded per D-098 | -2
L-403 | scheduler_never method-token item | Per D-099 | +2

Offsetting Safe trims (every trigger kept):
- §1.2 Confirmed at capture: "raw data the system can't verify and won't say again" to "unverifiable raw data never spoken again".
- global_always informational item: "invalidates nothing except" to "voids only".
- §2 Informational Interruptions > Hand back: dropped "goes".
- scheduler_always routed_to_scheduler item: "the caller's own Tax Pro or the Tax Pro named in Part 4" to "the caller's own or the Part 4-named Tax Pro"; "appointment" dropped after phone_callback; "never a handback" to "Never hand back."
- agent_specific_tools.check_search_readiness: "and once enough constraints are captured" to "with enough constraints captured"; "call transfer_to_agent with transferReason out_of_scope" to "transfer as out_of_scope".
