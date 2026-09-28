L-036 | §2 State 5 objective; scheduler_always idempotency item; agent_specific_outcomes.ddo_link_sent; agent_specific_tools.send_secure_link; §5.2 send_secure_link | D-001: DDO in objective; key, confirmation, newCustomer, ddo_link_sent added | +61
L-037 | §2 State 2 DDO Rules; scheduler_always explicit-yes item; agent_specific_tools.send_secure_link; workflow.schedule_new[5] | D-001: destination readback and explicit yes gate send_secure_link | +2
L-038 | §2 State 2 DDO Rules; agent_specific_tools.send_secure_link | D-001: delivery_failed re-captures and re-gates once, then transfers system_failure | +37
L-039 | §2 State 5 agent_specific_tools.find_available_cdas_slots; §5.2 find_available_cdas_slots | D-002: find_available_cdas_slots deleted from Scheduler tools and Part 5 | -102
L-040 | §2 State 3 Ladders table; broadening.scenario_selection[4]; broadening.ladders.callback | D-002: callback scenario added, rungs time_window and date_window only | +38
L-041 | §5.2 check_search_readiness note; §2 State 2 type table callback row; scheduler_always callback item | D-002: callbacks send phone_callback and floor 1, skip waterfall | +26
L-042 | Part 5 Conventions Common to Every Tool; §2 State 3 Readiness & Availability > CDAS | D-003: CDAS defined once in Part 5; §2 bullet points there | +8
L-043 | §1.1 appointmentType row; §1.5 context_envelope.appointmentType; terminal_payload_contract; §4 CDAS Callback Handoff; tax_pro_always callback item; 4C, 4E System | D-004: callback handoff carries appointmentType, taxProRef, officeRef; envelope gains appointmentType | +52
L-044 | §4 State 2 agent_specific_outcomes.routed_to_message | D-004: deleted "or no callback slots were available" | -5
L-045 | §4 No Matches / Inactive; tax_pro_always inactive item; agent_specific_outcomes.routed_to_scheduler | D-004: inactive-Tax-Pro route uses routed_to_scheduler, appointmentType null | +29
L-046 | §1.5 terminal_payload_contract | D-005: contract lists appointmentType, appointmentRef, transferReason, supportHoursSpoken, sourceUtterance, entryPoint | +6
L-047 | §1.5 terminal_payload_contract; global_outcomes.intent_changed, customer_abandoned | D-005: default transactionOccurred and intent; missing mandatory values filled | +28
L-048 | §1.5 terminal_payload_contract; global_outcomes.transfer_unavailable, consecutive_silence; §3 office_open_unanswered | D-005: callContained defined; message handbacks, silence, capture_intent set true | +15
L-049 | §1.5 terminal_payload_contract; global_outcomes.system_failure; §5.1 transfer_to_agent | D-005: transferReason enum added; system_failure names its reason; §5.1 points there | +39
L-050 | §1.2 Zero Web Deflection; global_never; §4 Fulfillment Priority; tax_pro_always; workflows; 4A, 4E | D-006: MyBlock app renamed Online Message Center exception; 4A, 4E cut to three sentences | +54
L-051 | §1.5 global_outcomes.outcome_unknown; §2 State 4 Indeterminate Writes | D-007: outcome_unknown calls transfer_to_agent, speaks matching line, returns idempotencyKey | +37
L-052 | §2 State 5 invalidation.ladder_state | D-008: accepting a rung never resets; only caller-initiated changes reset | -1
L-053 | §2 State 5 agent_specific_outcomes.customer_declined_options, no_acceptable_availability | D-008: exhaustion returns no_acceptable_availability; early stop is customer_declined_options | 0
L-054 | §2 State 5 broadening.scenario_selection[7]; agent_specific_tools.find_available_slots | D-009: peak_capacity override limited to four schedule_new scenarios | +15
L-055 | §1.1 entryPoint, routedOfficeRef row; §1.5 context_envelope.routedOfficeRef; §2 State 3 Rollover; scheduler_always rollover item | D-010: Head of Call passes routedOfficeRef; Scheduler proposes it directly | +14
L-056 | §3 Office Details Logic > Named Office; office_always | D-010: named office resolved via ZIP and nearbyOffices officeName match | +50
L-057 | §1.5 terminal_payload_contract routingTarget | D-011: routingTarget adds office_information, speak_to_tax_pro; drops tax_prep, named destination | -1
L-058 | §2 State 5 scenario_selection[1]; agent_specific_tools.check_search_readiness; §5.2 check_search_readiness note | D-011: specialized services and readiness out_of_scope transfer with out_of_scope | +22
L-059 | §2 State 2 Tax Extension; §2 State 3 Ladders Extension row; scheduler_always tax_extension item; ladders.extension | D-011: tax_prep follow-up returns route_intent; self-filing transfers as out_of_scope | +3
L-060 | §1.5 global_outcomes.appointment_requested | D-011: appointment_requested deleted | -14
L-061 | §1.5 global_always informational routing item; §2 State 3 Informational Interruptions | D-012: all agents hand back refund_status and faq_agent questions | +59
L-062 | §1.2 Hours: One Source, Spoken Once; §2 interruptions.informational_question | D-012: hours and phones only from Part 3 tools; Scheduler hands back | +37
L-063 | §2 agent_specific_tools.search_knowledge_base; §5.1 search_knowledge_base Category Enums | D-012: agents send only appointments_and_logistics or tax_prep_and_records | -8
L-064 | §1.5 global_always informational routing item | D-012: refund_status routing now in Base JSON for all agents (see L-061) | 0
L-065 | §1.5 global_always transfer_to_agent item | D-013: agents keep transfer_to_agent for barging; no further edit needed | 0
L-066 | §1.4 Caller-Initiated Barging row | D-013: frozen row now uses the matching agent_unavailable row as written | -8
L-067 | §1.5 global_never; §4 tax_pro_never | D-013: no-live-transfer-to-local-desk rule moved to global_never | +8
L-068 | §2 State 5 agent_specific_tools.transfer_to_agent | D-013: knownSoFar mapping deleted; lives only in §5.1 transfer_to_agent | -12
L-033 | §1.5 global_always KB item; §2-4 interruptions.informational_question | C-3 A, D-012: shared rule moved to Base; Scheduler keeps its extra | -62
L-047 (follow-up) | §1.5 terminal_payload_contract | D-005: default intent is now the intent the agent is serving | +2
L-056 (follow-up) | §3 Office Details Logic > Named Office; office_always named-office item | D-010: ZIP match scoped to a named office other than routedOfficeRef | +12
