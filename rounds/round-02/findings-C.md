- anchor: §1.5 global_outcomes.transferred_to_human
  also: §1.5 global_outcomes.identity_or_appointment_mismatch, validation_failed, system_failure, clarification_exhausted, transfer_unavailable; §2 State 5 agent_specific_outcomes.no_acceptable_availability; §3 State 2 agent_specific_outcomes.office_info_transfer
  severity: High
  claim: After a reason-specific transfer, agent_available fits both transferred_to_human and the reason outcome, and agent_unavailable fits transfer_unavailable while the reason outcome fixes nextAction transfer and callContained false.
  evidence: "transfer_to_agent returned agent_available." | "transferReason identity_unresolved. callContained false, nextAction transfer." | "transfer_to_agent returned agent_unavailable."
  class: human
  decision: transfer-outcome-precedence

- anchor: §1.5 global_outcomes.outcome_unknown
  also: §1.5 terminal_payload_contract (callContained)
  severity: High
  claim: On agent_unavailable with a message action, outcome_unknown fixes callContained false, while the contract (D-005) sets callContained true on every message handback.
  evidence: "true when no live human is needed, including message handbacks" | "on agent_unavailable, speak and set nextAction per transfer_unavailable" | "transactionOccurred null, callContained false."
  class: human
  decision: outcome-unknown-callcontained-on-message

- anchor: §1.5 terminal_payload_contract transferReason
  also: §2 State 5 scheduler_always tool-result item; §2 State 5 workflow.reschedule_existing[2]; §3 State 2 agent_specific_outcomes.office_info_transfer; §1.5 global_outcomes.handoff_invalid, configuration_missing
  severity: Medium
  claim: Several transfer triggers map to no transferReason value, and not_cancelable fits both validation_failed and automation_blocked.
  evidence: "none_nearby transfers" | "On a type change request, preserve the appointment and call transfer_to_agent." | "on rejected, change_not_allowed, or not_cancelable, transfer without retry" | "Unresolved office intent or lookup failure."
  class: human
  decision: transfer-reason-mapping

- anchor: §5.1 transfer_to_agent Transfer results
  severity: Medium
  claim: A transfer_to_agent failure is signalled only through issue, with no result value and no handler, so the agent cannot tell a failed transfer from agent_available or agent_unavailable.
  evidence: "issue identifies any tool failure." | "Transfer results: agent_available uses waitTimeSpoken; agent_unavailable uses supportHoursSpoken and leaveMessageAvailable."
  class: human
  decision: transfer-tool-failure-result

- anchor: §5.1 search_knowledge_base KB results
  also: §1.5 global_outcomes.no_approved_answer
  severity: Medium
  claim: The KB result set names no result below the 0.85 threshold, requires_tax_pro names no routingTarget or outcome, and no result maps to no_approved_answer.
  evidence: "answer_found requires confidence at least 0.85" | "requires_tax_pro routes to a Tax Pro." | "could not be answered compliantly"
  class: human
  decision: kb-result-mapping

- anchor: §5.2 find_offices_near
  also: §1.5 context_envelope.routedOfficeRef; §2 State 5 scheduler_always entryPoint item
  severity: Medium
  claim: After D-010, Head of Call resolves the dialed number, yet find_offices_near still takes dialedOfficeNumber, returns routedOfficeRef and invalid_dnis, and context_envelope has no dialedOfficeNumber key.
  evidence: "Office resolved by Head of Call from dialedOfficeNumber; null on central_line." | "routedOfficeRef is populated on rollover, null on central-line searches." | "Rollover DNIS did not map to an active office."
  class: human
  decision: dnis-resolution-owner

- anchor: Part 5 Conventions Common to Every Tool (CDAS)
  also: §2 State 5 scheduler_always CDAS item; broadening.ladders.callback.primary
  severity: Medium
  claim: The D-003 CDAS definition names every callback appointment, but its test (isCDAS or null taxProName) leaves a callback slot with the carried Tax Pro undecided for CDAS phrasing.
  evidence: "CDAS names a callback appointment and any slot with no named Tax Pro" | "Callback slots at the selected office, with the carried Tax Pro when present." | "When isCDAS is true, treat the slot as CDAS."
  class: human
  decision: cdas-callback-named-tax-pro

- anchor: §5.2 book_appointment Request JSON (Existing Customer) phoneNumber, contact.callbackNumber
  also: §2 State 5 scheduler_always new-customer contact item; §5.2 book_appointment Note
  severity: Medium
  claim: The rules require contact.callbackNumber only for new customers, the new-customer example omits it, the existing-customer example carries it, and top-level phoneNumber is never defined.
  evidence: "include contact.callbackNumber for phone callbacks" | "New-customer contact.callbackNumber is required on phone callbacks." | `"phoneNumber": "+18005550199",`
  class: human
  decision: book-contact-phone-fields

- anchor: §2 State 5 closure.line_patterns
  also: §2 State 5 agent_specific_outcomes.ddo_link_sent
  severity: Medium
  claim: The line-pattern keys form a second outcome vocabulary with no mapping to finalOutcome values; nothing_to_do matches no outcome and ddo_link_sent matches no pattern.
  evidence: "committed (booking/reschedule): state the outcome and the essential appointment details." | "nothing_to_do: state the true current position" | "Definite secure-link send."
  class: human
  decision: closure-pattern-outcome-map

- anchor: §5.2 check_search_readiness Request JSON taxProPreference.source
  also: §5.2 check_search_readiness Response JSON resolvedConstraints.taxProSource
  severity: Medium
  claim: taxProPreference.source and taxProSource have no defined values, while the sibling requestedTimeSource has an enum, so a prior Tax Pro from find_customer has no source token.
  evidence: `"taxProSource": "caller_stated",` | "Set requestedTimeSource to caller_stated for new requests"
  class: human
  decision: tax-pro-source-enum

- anchor: §5.2 book_appointment Request JSON (Existing Customer) appointmentNotes
  also: §2 State 5 scheduler_always callback item
  severity: Medium
  claim: appointmentNotes is defined only for the callback type, but the example sends it on a tax_prep booking with notice content that belongs in taxNoticeDetails.
  evidence: "On callback, capture the reason for the call in appointmentNotes" | `"appointmentNotes": "Received IRS letter CP2000",`
  class: human
  decision: appointment-notes-scope

- anchor: §1.5 global_outcomes.transferred_to_human
  severity: Low
  claim: "IVR call summary" is a second term for the contract field interactionSummary.
  evidence: "Carry IVR call summary, transferReason, and appointmentRef where applicable."
  class: safe
  fix: Replace "IVR call summary" with "interactionSummary".

- anchor: §5.2 get_customer_appointments Response JSON note
  severity: Low
  claim: The note after the response names no field, so "Internal only" cannot be tied to taxProCertLevel.
  evidence: "Note: Internal only. Used to hold reschedule substitutes to the same level or better."
  class: safe
  fix: Change "Note: Internal only." to "Note: taxProCertLevel is internal only."

- anchor: §1.5 context_envelope.customerStatus
  also: §1.1 customerStatus; §5.2 find_customer Response JSON
  severity: Low
  claim: customerStatus has no defined values; "verified" appears only in examples.
  evidence: "Status of the authenticated identity." | `"customerStatus": "verified",`
  class: human
  decision: customer-status-enum

- anchor: §5.2 find_customer Response JSON customer.hasUpcomingAppointment
  also: §5.2 find_available_slots matchesPreferredTaxPro, matchesPriorTaxPro; §5.3 check_office_open_status currentLocalTimeSpoken; §5.4 search_tax_pro_by_name tpRating
  severity: Low
  claim: These response fields are defined but no agent rule reads them.
  evidence: `"hasUpcomingAppointment": false,` | `"matchesPreferredTaxPro": true,` | `"currentLocalTimeSpoken": "7:44 PM Central",` | `"tpRating": 4`
  class: human
  decision: unused-response-fields
