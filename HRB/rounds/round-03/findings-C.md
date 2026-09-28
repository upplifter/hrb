- anchor: §5.2 find_available_slots (rung values Note)
  also: §2 State 5 agent_specific_tools.check_search_readiness; workflow.schedule_new[2]; broadening.ladders.*.rungs (digital_drop_off)
  severity: Medium
  claim: The slot-search rung enum includes digital_drop_off, but DDO has no slots and skips readiness and availability, so an implementer must guess whether a DDO rung calls find_available_slots.
  evidence: "digital_drop_off, next_day. Self-filing is a handback, not a slot-search rung." | "Skip readiness and availability only on a digital drop-off."
  class: human
  decision: ddo-rung-in-slot-search-enum

- anchor: §2 State 5 scheduler_always idempotency item
  also: §2 State 5 scheduler_always not_confirmed item; §5.2 book_appointment, cancel_appointment Outcome Results
  severity: Medium
  claim: The re-gate after not_confirmed reuses the same slot or appointment, so the key formula yields the same idempotencyKey, and the contract does not say whether the retry reuses it or takes a new one (as the DDO re-send does).
  evidence: "Generate idempotencyKey as interactionId-slotRef for booking" | "On not_confirmed, re-gate once; a second not_confirmed transfers as validation_failed."
  class: human
  decision: idempotency-key-on-not-confirmed-regate

- anchor: §1.4 Approved Recovery Lines (multiple_matches row)
  also: §5.4 search_tax_pro_by_name Outcome Results; §4 Tax Pro Lookup & Disambiguation > Multiple Matches
  severity: Medium
  claim: multiple_matches names both a find_customer result that transfers with a recovery line and a search_tax_pro_by_name result that disambiguates, and the unscoped §1.4 row outranks Part 4 under C-1.
  evidence: "I found more than one match, so I don't want to guess. Let me get someone who can help." | "More than one Tax Pro matched. Requires disambiguation."
  class: human
  decision: scope-multiple-matches-row

- anchor: §5.2 get_customer_appointments Outcome Results
  also: §2 State 5 agent_specific_outcomes.appointment_already_canceled; §5.2 get_customer_appointments Note
  severity: Medium
  claim: After D-021 the tool returns status canceled, but several_appointments and none_found count only active appointments, so a caller whose only appointment is canceled may get none_found and never reach appointment_already_canceled.
  evidence: "status is active or canceled." | "No active future appointments exist." | "Two or three active future appointments."
  class: human
  decision: canceled-appointments-in-result-counts

- anchor: §1.5 global_outcomes.handoff_invalid
  also: §1.5 global_outcomes.configuration_missing; §1.5 terminal_payload_contract (transferReason)
  severity: Medium
  claim: Both outcomes return nextAction transfer with no transferReason, and the transferReason enum has no value for an unusable envelope or missing configuration.
  evidence: "The inbound sessionEnvelope is unusable." | "Use the handoff_invalid reference rule. callContained false, nextAction transfer."
  class: human
  decision: transfer-reason-for-handoff-invalid

- anchor: §1.4 Approved Recovery Lines (Unregistered ANI or third-party blocked row)
  also: §1.5 global_outcomes.identity_or_appointment_mismatch; §1.5 terminal_payload_contract (transferReason)
  severity: Medium
  claim: The unregistered-ANI transfer maps to no named transferReason or outcome; identity_unresolved assumes identity was attempted, and automation_blocked lists other cases, so both readings are plausible.
  evidence: "Unregistered ANI or third-party blocked" | "Identity cannot be resolved or the appointment cannot be matched."
  class: human
  decision: transfer-reason-for-unregistered-ani

- anchor: §1.5 global_outcomes.question_answered
  also: §1.5 global_always search_knowledge_base item; §1.5 terminal_payload_contract (intent informational)
  severity: Medium
  claim: After D-012 search_knowledge_base serves only mid-task questions that resume the task, so no path ends in question_answered, and its intent informational conflicts with the served intent.
  evidence: "Caller asked an informational question and received an approved answer." | "answer in one brief turn, then resume with a single targeted question"
  class: human
  decision: question-answered-trigger

- anchor: §5.2 send_secure_link Outcome Results
  also: §2 State 5 scheduler_always not_confirmed item
  severity: Low
  claim: send_secure_link carries confirmation evidence like the other writes but has no not_confirmed or rejected result, so the scheduler's not_confirmed and rejected handling cannot apply to it.
  evidence: "Link could not be sent to the provided destination." | "On not_confirmed, re-gate once; a second not_confirmed transfers as validation_failed."
  class: human
  decision: send-secure-link-rejection-results

- anchor: §5.1 search_knowledge_base (intro)
  also: §1.5 global_always followUpTopics item
  severity: Low
  claim: attempt counts caller rephrasings, but after D-025 the only re-query is the clarifier choice, so the value to send on that call is undefined.
  evidence: "attempt tracks the number of times the caller has rephrased the question"
  class: human
  decision: kb-attempt-meaning
