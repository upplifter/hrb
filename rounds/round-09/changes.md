# Round 9 changes

Reviewers returned findings in replies (the harness blocked their writes); the orchestrator saved them. Per the user's instruction ("lean towards educated guesses, flag really uncertain ones"), Human items were settled by the orchestrator as provisional decisions D-100 to D-113 instead of stopping for questions. Reasons live here, not in the spec.

## Safe
- L-425 §2 Complexity Matching > Reschedule: add the raise to the bound appointment's taxProCertLevel (D-095 propagation).
- L-427 workflow.schedule_new[1]: "(never after a Part 4 routed_to_scheduler)" (D-084 propagation).
- L-428 terminal_payload_contract: officeRef when known on the message and callback handoffs and on routed_to_scheduler for another Tax Pro (D-040 with D-085).
- L-429 §3 office_never[0]: "questions about an existing one" (D-097).
- L-430 faq_agent list in §4 Intent Scope and §2 hand-back bullet: "out-of-task appointment-logistics" (D-097).
- L-439 §2 State 3: new bullet "Rejected Tax Pro, office kept" mirrors partial_acceptance (D-074, D-090; C-1 prose parity).
- L-447 five trims: persona_translation, Part 5 Callbacks bullet, none_nearby row, Scheduler transfer_to_agent pointer, "Principles" bold.
- L-448 trims to fit the round budget: configuration_missing points to handoff_invalid (backlog L-346); find_available_slots drops the duplicated ranking/duration sentence (backlog L-347).

## Decided by orchestrator guess (provisional)
- D-100 (L-426) reschedule floor: type floors stay for emerald_advance, tax_notice_service, callback, physical_drop_off; JSON step 4 and prose bullet.
- D-101 (L-431) callback handoff officeRef source, prose and JSON.
- D-102 (L-432) partial_acceptance on callback hands back to speak_to_tax_pro.
- D-103 (L-433) mid-task defined in the global_always KB item.
- D-104 (L-434) keep-prior question scoped to tax_prep in schedule_new[1].
- D-105 (L-435) contract: after a commit every outcome carries transactionOccurred true; transfer_unavailable defers to the contract.
- D-106 (L-436) prose Tax Pro Trade-off and rung 5: stay answers rung 5.
- D-107 (L-437) phone_callback reason captured before the gate, including on an accepted rung (JSON and callback table row).
- D-108 (L-440) empathy: "one of the first three lines" (no frozen text touched).
- D-109 (L-441) restored "to speak to" in Tax Pro Requests and interruptions.intent_change.
- D-110 (L-442) transfer_unavailable: leave_message_offer only if leaveMessageAvailable is true.
- D-111 (L-443) new scheduler_always item mapping taxProPreference source values; D-079 values unchanged.
- D-112 (L-444) no change.
- D-113 (L-445) paths with no §1.4 row speak the agent_available line (§1.4 intro and global_always).

## Not changed
- L-438 Cross-Office Restriction (Q-96). An edit was tried and reverted: it would remove a phone-number restriction that rounds 1 and 3 kept.
- L-446, L-449, L-450 to backlog.

## Size
17,641 words (lint), 140,825 bytes. Round growth +0.95% (limit 1.0%). Total growth +4.22% (limit 5%). Lint: RESULT WARN, no FAIL.

## Answers applied
- L-438 (Q-96, option A, D-114). Deleted §3 Office Contact Triage > Cross-Office Restriction and `office_never` "Never provide a phone number for any office other than the routed office." The office_info phone-number item (mainPhoneSpoken for the routed office) stays.
- Blank guesses (D-100 to D-113) kept as decided.
