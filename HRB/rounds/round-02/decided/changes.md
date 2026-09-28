L-129 | §1.4 intro; §2 State 1 Authentication Logic; scheduler_always unregistered-ANI item; global_always transfer item | transfer_to_agent called first; recovery line only on agent_available (D-014) | +20
L-130 | global_always (new transfer-results item); global_outcomes.transferred_to_human, transfer_unavailable | agent_available returns reason outcome; agent_unavailable returns transfer_unavailable (D-015) | +45
L-131 | global_outcomes.outcome_unknown | callContained follows transfer_unavailable on agent_unavailable (D-015) | +2
L-157 | terminal_payload_contract transferReason; §2 State 2 Immutability; workflow.reschedule_existing[3]; scheduler_always tool-result items; Part 3 agent_specific_tools.transfer_to_agent | Unmapped triggers mapped to automation_blocked, no_acceptable_availability, system_failure (D-015) | +35
L-158 | §5.1 transfer_to_agent Transfer results; global_always transfer-results item | Failed transfer call treated as agent_unavailable, no message (D-015) | +10
L-132 | §2 State 3 Dynamic State Invalidation: Location & Time; invalidation.upstream_change | Accepting same Tax Pro at nearby offices keeps taxProRef (D-016) | +14
L-145 | scheduler_always tool-result item; broadening.principles nearby-office item | none_nearby exhausts nearby-office rung; first lookup still transfers (D-016) | +16
L-147 | broadening.scenario_selection item 7; §2 State 3 Tax Pro Trade-off | Trade-off asked before peak switch from returning_same_tax_pro (D-016) | +28
L-094 | scheduler_never profile item; §2 State 1 New Customers; §5.2 send_secure_link link_sent row | send_secure_link may create the new-customer profile at commit (D-017) | +10
L-133 | §5.2 send_secure_link Request JSON and note; agent_specific_tools.send_secure_link | taxNoticeDetails added to send_secure_link request (D-017) | +14
L-144 | §2 State 2 DDO Rules > Rescheduling | DDO change is a new schedule_new DDO send in Scheduler (D-017) | +1
L-156 | §2 State 2 DDO Rules; §2 State 4 Optional Text Confirmation; scheduler_always text item; workflow.schedule_new[4] | DDO skips text offer; destination readback is the whole gate (D-017) | +30
L-166 | §5.2 send_secure_link Outcome Results | outcome_unknown row added (D-017) | +6
L-095 | §1.1 appointmentType row; §1.5 context_envelope | taxProRef and officeRef added as prior-handoff envelope fields (D-018) | +22
L-159 | §2 State 3 CDAS phrasing; scheduler_always isCDAS item | CDAS phrasing skipped when envelope carries taxProRef (D-018) | +8
L-141 | §4 Out-of-Scope (New Appointment) | Any-method tax_prep goes to Scheduler; callback only for confirmed Tax Pro (D-018) | +9
L-096 | §2 State 2 Tax Extension; scheduler_always tax_extension item | Committed-extension tax_prep returns intent_changed with caller's words (D-019) | -4
L-148 | broadening.ladders.extension rung 2; §2 State 3 Ladders Extension row; customer_declined_options | Self-filing rung asks one either-or with three named exits (D-019) | -15
L-149 | broadening.ladders.extension rung 2; §2 State 2 Tax Extension | sourceUtterance carries the caller's own words (D-019) | 0
L-069 | §1.5 terminal_payload_contract | capture_intent defined as Head of Call re-ask when nothing served (D-020) | +18
L-070 | §1.5 terminal_payload_contract | "Resolve unclear_intent" replaced by reprompt once, then capture_intent (D-020) | +5
L-071 | §3 Intent Scope > unclear_intent; office_always; Part 3 transfer_to_agent; office_info_transfer; tax_pro_always unclear item | Unclear intent after one reprompt returns capture_intent (D-020) | +5
L-073 | scheduler_always not_confirmed item | Re-gate once; second not_confirmed transfers as validation_failed (D-021) | +8
L-092 | agent_specific_outcomes.appointment_already_canceled; §5.2 get_customer_appointments note | status canceled on cancel_existing triggers appointment_already_canceled (D-021) | +12
L-093 | §5.2 reschedule_appointment Outcome Results | not_confirmed and rejected rows added (D-021) | +8
L-076 | interruptions.informational_question; scheduler_always explicit-yes item; §2 State 4 Pre-Commit Gate | Any interruption after the gate yes voids it (D-022) | -10
L-155 | §2 State 4 Pre-Commit Gate (new split bullet); scheduler_always correction item | Text-destination correction updates destination only, re-reads gate (D-022) | +36
L-082 | §1.3 leave_message_offer bullet; global_always message item | leave_message_offer also applies when target office is closed (D-023) | +16
L-083 | §1.3 leave_message_offer bullet | Part 4 may name the message option (D-023) | +11
L-086 | §2 State 1 New Customer DOB Check; §2 Mini-Dialogue 1A | DOB year re-ask bullet and last 1A Agent turn deleted (D-024) | -29
L-087 | §1.2 Data Sanitization | Exception extended to newCustomer payloads of book_appointment, send_secure_link (D-024) | +7
L-088 | §1.5 global_never tax-advice item | Notice interpretation and loan, fee, penalty bans added (D-024) | +8
L-097 | §1.2 Tax/Financial Boundary; scheduler_never loan item; §4 Out-of-Scope (FAQ Agent) | Loan, fee, and penalty questions go to faq_agent (D-025) | +10
L-137 | §5.1 KB results; global_always followUpTopics item; Scheduler agent_specific_tools.search_knowledge_base; §2 State 3 Informational Interruptions | requires_tax_pro handled per agent; other non-answers return no_approved_answer (D-025) | +40
L-138 | global_always KB item; §5.1 KB results | followUpTopics used only on clarification_needed (D-025) | +5
L-139 | global_always informational item; §1.2 Hours; interruptions.informational_question | Every agent hands hours and phone questions to office_information (D-025) | -12
L-143 | global_always informational item; §2 State 3 Hand back | Password and income tax course questions go to faq_agent everywhere (D-025) | +10
L-130 (follow-up) | global_outcomes.transfer_unavailable | Dropped outcome_unknown exception and restated message-action rules; tightened nextAction wording | -26
L-147 (follow-up) | §2 State 3 Tax Pro Trade-off | Split the two ask points into sub-bullets; Peak Capacity trigger now separate | +5
L-159 (follow-up) | scheduler_always isCDAS item | Restored "explicitly ... specific"; shortened CDAS-slot clause to stay within 60 words | -1
L-139 (follow-up) | global_always informational item | Office hours/phone hand-back limited to every agent except office_information | +5
