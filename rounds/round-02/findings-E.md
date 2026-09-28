- anchor: §2 State 1 Authentication Logic (failure bullet)
  also: §2 State 5 scheduler_always (unregistered ANI item); §1.5 global_always (transfer_to_agent item); §1.4 Authentication failed row
  severity: High
  claim: Part 2 prose and JSON speak the recovery line, which promises a person, before calling transfer_to_agent, while the Base JSON requires the call before any promise of a person.
  evidence: "speak the approved recovery line, then call `transfer_to_agent` without retrieval" | "before promising a person, and handle its results exactly as specified under tools"
  class: human
  decision: recovery-line-vs-transfer-order

- anchor: §2 State 5 scheduler_always (tax_notice_service digital drop-off item)
  also: §5.2 send_secure_link Request JSON; §2 State 2 Digital Drop-Off (DDO) Rules
  severity: High
  claim: The Scheduler JSON requires sending all five notice values on a tax_notice DDO fallback, but DDO runs only send_secure_link, whose request has no taxNoticeDetails field.
  evidence: "and still capture and send all five notice values" | "Then execute `send_secure_link`, never `book_appointment`"
  class: human
  decision: tax-notice-ddo-notice-values

- anchor: §5.2 find_offices_near
  also: §1.1 The Head of Call Envelope (routedOfficeRef row); §2 State 5 scheduler_always (find_offices_near result item)
  severity: Medium
  claim: After D-010, Head of Call resolves routedOfficeRef, but find_offices_near still takes dialedOfficeNumber, resolves the DNIS itself, and returns invalid_dnis.
  evidence: "Office that Head of Call resolved from dialedOfficeNumber" | "Rollover DNIS did not map to an active office." | "routedOfficeRef is populated on rollover, null on central-line searches"
  class: human
  decision: find-offices-near-rollover-input

- anchor: §2 State 5 scheduler_always (isCDAS item)
  also: Part 5 Conventions Common to Every Tool (CDAS bullet); §2 State 5 broadening.ladders.callback.primary
  severity: Medium
  claim: After D-003, Part 5 defines every callback appointment as CDAS, but the Scheduler JSON treats a callback slot with a carried Tax Pro as named, so the two require different spoken phrasing.
  evidence: "CDAS names a callback appointment and any slot with no named Tax Pro" | "When isCDAS is true, treat the slot as CDAS." | "with the carried Tax Pro when present"
  class: human
  decision: callback-cdas-phrasing

- anchor: §2 State 5 invalidation.upstream_change
  also: §2 State 2 Dynamic State Invalidation: Type & Method Edge Cases
  severity: Medium
  claim: The prose re-derives the floor on a type or method change and skips readiness when a channel rung is accepted, but the JSON always re-checks readiness and never re-derives the floor.
  evidence: "re-derive the floor, and re-run readiness except when accepting a channel rung" | "check readiness, and search only on ready"
  class: safe
  fix: In invalidation.upstream_change, add that a type or method change re-confirms office eligibility and re-derives the floor, and that accepting a channel rung skips readiness.

- anchor: §2 State 5 scheduler_always (tax_extension item)
  also: §2 State 2 Tax Notice Services Guardrails > Tax Extension
  severity: Medium
  claim: The prose commits the extension and then returns route_intent when the caller also wants tax prep, but the JSON ties route_intent only to the ladder's final rung, which offers self-filing, not tax prep.
  evidence: "commit the extension, then return route_intent to appointment_scheduler" | "its final rung offers follow-up tax_prep; on acceptance return route_intent"
  class: safe
  fix: Replace "its final rung offers follow-up tax_prep; on acceptance return route_intent" with "If the caller also wants tax_prep, commit the extension, then return route_intent", keeping the sourceUtterance clause.

- anchor: §1.5 global_always (search_knowledge_base item)
  also: §5.1 search_knowledge_base (intro; KB results)
  severity: Medium
  claim: The Base JSON ignores followUpTopics on every result, but Part 5 builds the clarification_needed path and the clarifier field from followUpTopics.
  evidence: "silently ignore followUpTopics" | "clarification_needed may populate clarifier from followUpTopics"
  class: human
  decision: kb-clarification-handling

- anchor: §5.1 search_knowledge_base KB results (requires_tax_pro)
  also: §2 State 5 scheduler_never (loan, fee, penalty item)
  severity: Medium
  claim: Part 5 says requires_tax_pro routes to a Tax Pro, but no agent JSON maps that result to a routingTarget, transfer, or outcome, and the Scheduler leaves it to the Tax Pro at the appointment.
  evidence: "requires_tax_pro routes to a Tax Pro" | "or leave it to the Tax Pro at the appointment"
  class: human
  decision: kb-requires-tax-pro-handling

- anchor: §5.2 send_secure_link Outcome Results
  also: §2 State 4 Write Tools & Payload Mechanics > Indeterminate Writes; §2 State 5 scheduler_always (idempotencyKey item)
  severity: Medium
  claim: After D-001, send_secure_link is a keyed write, but Part 5 lists no indeterminate result, so the State 4 outcome_unknown path cannot fire for DDO.
  evidence: "interactionId-ddo-1 for a secure link" | "Never retry. Call `transfer_to_agent` with transferReason outcome_unknown and idempotencyKey" | "Link could not be sent to the provided destination"
  class: human
  decision: ddo-indeterminate-result

- anchor: §4 Mini-Dialogues: Speak to a Tax Pro > 4C
  also: §4 Tax Pro Lookup & Disambiguation > Multiple Matches; §4 State 2 tax_pro_always (multiple matches item)
  severity: Medium
  claim: On two matches the rule asks a location disambiguation question, but 4C offers one match as a yes/no confirmation.
  evidence: "Ask a location/city disambiguation question using primaryOfficeName" | "I found Paul Miller at the Westport office. Is that who you're looking for?"
  class: human
  decision: 4c-multiple-match-turn

- anchor: §2 State 5 workflow.reschedule_existing[2]
  also: §2 State 2 Appointment Type Rules > Immutability
  severity: Medium
  claim: The prose makes only the type immutable on reschedule, while the JSON also bars a method change and gives no handler for a method-change request.
  evidence: "Type cannot be changed on a reschedule." | "never change the appointment type or method through reschedule"
  class: human
  decision: reschedule-method-change

- anchor: §1.5 global_outcomes.configuration_missing
  also: §1.4 handoff_invalid or configuration_missing row
  severity: Medium
  claim: The prose gives configuration_missing no caller-facing line, but the JSON only forbids mentioning configuration, which implies the agent speaks.
  evidence: "Say nothing, ask nothing, hand back immediately. No caller-facing line" | "Do not mention configuration. Use the handoff_invalid reference rule"
  class: safe
  fix: In global_outcomes.configuration_missing, replace "Do not mention configuration." with "Say nothing, ask nothing, and hand back immediately."

- anchor: §5.2 book_appointment (Note; Request JSON (Existing Customer))
  also: §2 State 5 scheduler_always (new-customer contact item)
  severity: Medium
  claim: The JSON and the Part 5 note require contact.callbackNumber only for new customers, but the existing-customer example sends it, so the rule for existing callers is unclear.
  evidence: "include contact.callbackNumber for phone callbacks" | "New-customer contact.callbackNumber is required on phone callbacks" | "Request JSON (Existing Customer)"
  class: human
  decision: callback-number-existing-customer

- anchor: §4 Mini-Dialogues: Speak to a Tax Pro > 4C
  also: §4 Fulfillment Priority step 2; §4 State 2 tax_pro_always (Online Message Center item)
  severity: Low
  claim: The rule speaks the Online Message Center line after the options, but the 4C options turn omits it, unlike 4A and 4E.
  evidence: "After the options, say 'For your convenience" | "I can check Paul's calendar for a callback, or I can help you leave a message"
  class: human
  decision: 4c-message-center-line

- anchor: §1.5 global_never (web deflection item)
  also: §1.2 Zero Web Deflection & Prohibited Speech > Tax Pro messaging
  severity: Low
  claim: The prose limits the Online Message Center exception to Part 4, but the Base JSON grants it to every agent.
  evidence: "In Part 4, name only the" | "for Tax Pro messaging, name only the Online Message Center"
  class: safe
  fix: In global_never, change "for Tax Pro messaging" to "for Tax Pro messaging in the Speak to a Tax Pro agent".
