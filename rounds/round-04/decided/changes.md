# Round 4 decided changes (D-038 to D-049)

Format: `ledger ID | anchor | change | net words (approx.)`. Applied by the orchestrator. Lint after the batch: RESULT WARN, no FAIL; round growth +0.99% (limit 1.0%); JSON valid.

L-288 | §1.1 interactionId row; context_envelope.interactionId; closure.re_entry | interactionId is per agent invocation, issued new by Head of Call; re_entry drops "fresh idempotency key namespace" (D-038) | +8
L-289, L-320 | §1.3 Leave-a-Message Ownership fourth bullet; §1.4 agent_unavailable message-available row; closure.line_patterns | Head of Call speaks support hours and the offer on leave_message_offer; flow-internals list cut to one sentence (C-11) (D-039) | -18
L-290 | §2 State 2 Appointment Type Rules > After Part 4 (new bullet); scheduler_always routed_to_scheduler item (new); interruptions.intent_change | After a Part 4 routed_to_scheduler, a callback request books a tax_prep phone_callback appointment, never handed back (D-040) | +40
L-239 | §4 No Matches / Inactive; tax_pro_always unavailable item; tax_pro_options_declined | Declining the Scheduler offer returns tax_pro_options_declined (D-040) | +14
L-244, L-298 | §4 Generic Request; tax_pro_always unavailable item; routed_to_scheduler | Generic path reads priorTaxProStatus only; no prior Tax Pro skips the unavailable line; routed_to_scheduler carries officeRef only when known (D-040) | +15
L-240 | §1.1 operation row; context_envelope.operation | The book/change/cancel answer sets the operation (D-041) | +8
L-292 | §2 State 4 Write Tools > cancel_appointment; interruptions.cancel_said | cancel_said covers only an existing appointment; "cancel this booking" at a gate is a gate no (D-041) | +14
L-291, L-302 | §2 State 4 Post-Commit Requests (new bullet); interruptions.cancel_said | Post-commit cancel or change hands back intent_changed with routingTarget appointment_scheduler and the committed reference (D-041) | +30
L-241 | workflow.reschedule_existing[1]; agent_specific_outcomes.appointment_already_canceled | Canceled appointments never offered on reschedule; canceled-only match returns appointment_already_canceled on either operation (D-041) | +16
L-293, L-294, L-295 | §1.2 No-Match Rule; global_always no-match item; global_outcomes.intent_unclear (deleted); terminal_payload_contract; §3 Unclear intent; office_always disambiguation item; tax_pro_always unclear item | Unclear intent is a no-match ending in clarification_exhausted; intent_unclear deleted (D-042) | -25
L-296 | terminal_payload_contract intent enum; global_outcomes.no_approved_answer | `informational` deleted from the intent enum; no_approved_answer takes the served intent by the contract default (D-042) | -4
L-242, L-315 | §1.4 intro paragraph and validation_failed/system_failure row Path; global_always transfer-results item; global_outcomes.outcome_unknown; §5.1 transfer_to_agent Transfer results | Failed call speaks nothing, returns transfer_unavailable with nextAction transfer; outcome_unknown keeps its name and idempotencyKey; §1.4 intro rewritten to 2 sentences (D-043) | -2
L-316 | §1.4 handoff_invalid row; global_outcomes.handoff_invalid, configuration_missing | Never call transfer_to_agent; "call no tools" in the frozen row per D-043 | +9
L-297 | global_outcomes.customer_abandoned | After a commit, transactionOccurred true with the committed reference (D-043) | +8
L-243 | §3 Routed Office (split from Cross-Office Restriction); office_always named-office item | A ZIP- or name-resolved office becomes the routed office for the invocation (D-044) | +28
L-299 | §3 ZIP Not Found (new bullet); agent_specific_tools.transfer_to_agent; terminal_payload_contract transferReason | office_not_found on a caller ZIP is a no-match; only a tool error is a lookup failure (D-044) | +33
L-304 | §3 Named Office; office_always named-office item | Match against the returned office and its nearbyOffices (D-044) | +10
L-238 | §3 If hours_unavailable; workflow.office_contact_flow[2]; office_contact_triage_complete | hours_unavailable returns office_contact_triage_complete with leave_message_offer (D-045) | +25
L-305 | §3 Office Contact Triage first bullet; workflow.office_contact_flow[1] | office_contact checks seasonalStatus first (D-045) | +12
L-303 | §3 Silence After an Answer (split from Standard Blurb); workflow.office_info_flow[3] | First silence after an answer returns office_info_provided with no reprompt; Standard Blurb trimmed (D-045) | +18
L-300 | §2 State 3 No Answer (new bullet); search_knowledge_base (Scheduler); global_always followUpTopics item; §5.1 KB results | Scheduler says it has no answer and resumes; outside the Scheduler a non-answer returns no_approved_answer; §5.1 KB results reduced to a pointer (D-046) | +20
L-246 | global_always followUpTopics item | requires_tax_pro in office_information hands back to speak_to_tax_pro. Scoped to office_information like D-034's informational item; Part 4 is itself speak_to_tax_pro (D-046) | +12
L-310 | global_always KB item; §2 State 3 Informational Interruptions > Action | tax_prep_and_records limited to what to bring or prepare (D-046) | +12
L-309 | global_always identity item (new, split for length); §2 State 3 Transfer (new bullet) | Identity theft, fraud, and other-department questions transfer as out_of_scope (D-046) | +30
L-317 | §2 State 3 Personal Questions; search_knowledge_base (Scheduler); scheduler_never loan item | On cancel and drop-off paths a personal question hands back to speak_to_tax_pro; scheduler_never now points to search_knowledge_base (D-046) | +25
L-306 | §4 By Name Request > 1 Match | Single match confirmed by consequence; caller correction follows No Matches / Inactive (D-047) | +14
L-312 | §4 Out-of-Scope (Appointments), renamed from (New Appointment); tax_pro_always callback item | Any book, reschedule, or cancel request routes to appointment_scheduler (D-047) | +3
L-307 | §2 State 3 Declined Offices; workflow.schedule_new[1] | Rejected last-served office moves to same_tax_pro_nearby_offices; "(digital_drop_off for DDO)" and "per context_envelope" cut for length (D-048) | +18
L-311 | §2 State 3 Ladders Rescheduling row primary cell; scenario_selection item 3 | Callback and physical_drop_off reschedules use only time and date rungs (D-048) | +16
L-301 | scheduler_always find_offices_near item; agent_specific_tools.find_available_slots | invalid_constraints moved to find_available_slots: re-run readiness once, second transfers as system_failure (D-048) | +12
L-308 | §1.1 knownPreferences; context_envelope.knownPreferences; workflow.schedule_new[2] | preferredTaxPro other than prior or carried follows Tax Pro Requests; step 3 drops "Tax Pro preference" (D-049) | +22
L-313 | §1.1 entryReason | Other Check Refund Status handoffs arrive with operation null and no entryReason (D-049) | +13
L-314 | §2 State 3 Appointment Details (new bullet); objective; agent_specific_tools.get_customer_appointments | Scheduler answers appointment-details questions read-only after authentication, nextAction offer_additional_help; objective trimmed (D-049) | +25

## Brevity trims made to stay within the 1% round budget (Safe, rule 9)

- How to Read, Part 3 and Part 4 bullets shortened.
- §1.1 intro shortened to two sentences; §1.2 lead-in "Enforce these rules..." deleted.
- §2 State 2 and State 3 intro sentences shortened.
- §3 State 1 intro shortened.
- Part 5 intro, §5.1 search_knowledge_base intro, §5.1 transfer_to_agent usage sentence (now points to §1.5 global_always), check_search_readiness, find_available_slots, and get_office_details intros shortened.

## Known gaps left for round 5

- After D-042 deleted `intent_unclear`, no outcome uses nextAction capture_intent. Removing it needs a decision (C-7).
- D-049's appointment-details read path returns nextAction offer_additional_help but no finalOutcome exists for it. Adding one needs a decision (C-7).
