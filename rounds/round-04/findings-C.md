# Round 4 · Lens C findings (Contracts and vocabulary)

Saved by the orchestrator from the reviewer's reply (write blocked).

### C-01 · intent_unclear and the No-Match Rule both claim an unresolved intent answer
Anchor: §1.5 terminal_payload_contract ("Reprompt an unclear intent once, then return intent_unclear"); §1.2 Input Exhaustion & Silence > No-Match Rule; §1.1 operation; §3 Intent Scope & Disambiguation > unclear_intent
Severity: Medium
Class: Human (picks between two plausible readings; changes the outcome and whether the caller reaches a person)
Issue: The contract says "Reprompt an unclear intent once, then return intent_unclear" (capture_intent, no transfer), while §1.2 says "On the second consecutive failure, call `transfer_to_agent`" (clarification_exhausted). Nothing separates an unclear intent from a no-match, e.g., the Scheduler's null-operation book/change/cancel question or the §3 "hours and address" or "speaking to the office staff" reprompt.
Proposed fix: Define which unresolved answers are an unclear intent (intent_unclear) and which are a no-match (clarification_exhausted), and state whether the Scheduler's operation question counts as intent.

### C-02 · intent_unclear has no intent value where the agent serves two intents
Anchor: §1.5 global_outcomes.intent_unclear; terminal_payload_contract ("intent is the intent the agent is serving"); §3 State 2 office_always disambiguation item
Severity: Medium
Class: Human (the fix picks an enum value or adds one)
Issue: intent_unclear states no intent, so "intent is the intent the agent is serving" applies. In Part 3 the outcome fires because the agent could not tell office_info from office_contact, so no served intent exists.
Proposed fix: Name the intent value intent_unclear carries in Part 3 (and in the Scheduler before an operation is set).

### C-03 · intent_unclear returns capture_intent after the caller was served
Anchor: §1.5 global_outcomes.intent_unclear; terminal_payload_contract ("capture_intent ... use it only when nothing was served"); §3 Office Details Logic > Standard Blurb; workflow.office_info_flow[3]
Severity: Medium
Class: Human (changes which nextAction Head of Call receives)
Issue: intent_unclear always sets "nextAction capture_intent", but the contract allows capture_intent "only when nothing was served". Part 3 answers follow-ups "in the same invocation", so an unclear follow-up after the blurb triggers a nextAction the contract forbids.
Proposed fix: Say whether intent_unclear after a served answer returns offer_additional_help or the served outcome (e.g., office_info_provided) instead.

### C-04 · "unclear_intent" label is a second term for intent_unclear
Anchor: §3 State 1 Intent Scope & Disambiguation > unclear_intent
Severity: Low
Class: Safe. Rename the token-styled label to plain "**Unclear intent:**".
Issue: The bullet label "unclear_intent" is formatted like an intent enum value that does not exist; the same bullet returns "intent_unclear".
Proposed fix: Replace the label "unclear_intent**:**" with "**Unclear intent:**".

### C-05 · Part 4 "return" lists mix nextAction values with a finalOutcome
Anchor: §4 Fulfillment Priority step 4; §4 State 2 workflow.speak_to_tp_generic[4]; workflow.speak_to_tp_by_name[5]
Severity: Low
Class: Safe. Name the three finalOutcomes, whose nextActions are set in agent_specific_outcomes.
Issue: Step 4 says "return `leave_message`; ... return `route_intent` ...; ... return `tax_pro_options_declined`". The first two are nextAction values and the third is a finalOutcome.
Proposed fix: Return routed_to_message, routed_to_scheduler, or tax_pro_options_declined.

### C-06 · intent value `informational` is left with no agent that serves it
Anchor: §1.5 terminal_payload_contract intent enum; global_outcomes.no_approved_answer
Severity: Medium
Class: Human (removes or redefines an enum value and changes an outcome's intent)
Issue: With question_answered deleted, `informational` appears only in no_approved_answer. search_knowledge_base runs "only for a mid-task question", so each no_approved_answer interrupts another served intent, against "intent is the intent the agent is serving".
Proposed fix: Drop "intent informational" from no_approved_answer and delete `informational` from the intent enum.

### C-07 · "Fresh idempotency key namespace" cannot be built from the fixed key formats
Anchor: §2 State 5 closure.re_entry; scheduler_always idempotencyKey item; §5.2 send_secure_link Request JSON
Severity: High
Class: Human (sets the idempotency contract for writes)
Issue: re_entry requires "generate a fresh idempotency key namespace", but every format is fixed from interactionId and refs (e.g., "interactionId-ddo-1"). If interactionId holds for the call, a DDO change request under D-017 rebuilds "interactionId-ddo-1" and the backend deduplicates the send to the new destination.
Proposed fix: State whether interactionId changes per invocation, or add an invocation component to every key format.

### C-08 · customer_abandoned fixes transactionOccurred false after a commit
Anchor: §1.5 global_outcomes.customer_abandoned
Severity: Medium
Class: Human (changes a mandatory outcome value and the fields carried)
Issue: customer_abandoned sets "transactionOccurred false". A dropped call during the post-commit readback follows a committed write, so the payload reports no transaction and carries no committed ref.
Proposed fix: Set transactionOccurred true and carry the committed ref when a write committed before the drop.

### C-09 · Generic Part 4 path checks fields find_customer does not return
Anchor: §4 Tax Pro Lookup & Disambiguation > Generic Request; tax_pro_always unavailable item; workflow.speak_to_tp_generic[3]; Part 5 Conventions (priorTaxProStatus)
Severity: Medium
Class: Human (picks between two plausible readings of "active")
Issue: The generic path acts "If active" and tax_pro_always says "Check both activeStatus and takingAppointmentsInd", but find_customer returns only priorTaxProStatus, which "describes a customer relationship, not the Tax Pro's activeStatus". Those fields come only from search_tax_pro_by_name, which the generic workflow never calls.
Proposed fix: State whether the generic path reads priorTaxProStatus or calls search_tax_pro_by_name.

### C-10 · office_not_found on a dictated ZIP maps to system_failure, not a no-match
Anchor: §3 State 2 agent_specific_tools.transfer_to_agent ("office lookup failure"); §5.3 get_office_details Outcome Results office_not_found; terminal_payload_contract transferReason system_failure
Severity: Medium
Class: Human (changes whether the caller is reprompted and which transferReason applies)
Issue: "Office lookup failure" is undefined. office_not_found fires when "the requested officeRef or postalCode did not match", so a mistyped ZIP in Part 3 transfers at once as system_failure, while the Scheduler reprompts the same input under MAX_INPUT_ATTEMPTS.
Proposed fix: Define office lookup failure, and state whether office_not_found on a caller-given ZIP is a no-match or a system_failure.
