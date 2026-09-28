- anchor: Part 2 State 5 invalidation.ladder_state
  also: Part 2 State 3 Dynamic State Invalidation: Location & Time; Part 2 State 5 broadening.principles
  severity: High
  claim: Only a channel-rung method change is exempt from the ladder reset, so consenting to a time, date, office, or Tax Pro rung resets the ladder and restarts at the primary offer, making every ladder cyclic.
  evidence: "other than a method change made by accepting a channel rung, resets which rungs have been offered" | "Re-run readiness, re-select the scenario under broadening.scenario_selection, and restart at its primary offer."
  class: human
  decision: rung-acceptance-vs-ladder-reset

- anchor: Part 2 State 5 broadening.scenario_selection
  also: Part 2 State 2 Appointment Type table; Part 2 State 5 workflow.reschedule_existing step 3
  severity: High
  claim: Item 7 switches any earlier scenario to peak_capacity, whose virtual and DDO rungs break emerald_advance's in-person-only method and reschedule's fixed method.
  evidence: "except item 7 is evaluated on no_slots and supersedes an earlier selection." | "| emerald_advance | In-person ONLY |" | "never change the appointment method through reschedule"
  class: human
  decision: peak-capacity-scope-by-type

- anchor: Part 2 State 5 broadening.scenario_selection
  also: Part 2 State 2 Appointment Type table (callback); Part 2 State 3 Ladders
  severity: High
  claim: No scenario selects for the callback type, so it falls to new_client (or a returning ladder), whose Digital Drop-Off and nearby-office rungs offer methods callback does not permit.
  evidence: "| callback | phone_callback |" | "10 Otherwise: new_client." | "3. Digital Drop-Off.<br>4. Nearby offices."
  class: human
  decision: callback-ladder

- anchor: §1.5 global_outcomes.outcome_unknown
  also: Part 2 State 4 Write Tools & Payload Mechanics; §1.5 global_always (transfer_to_agent); §1.4 outcome_unknown
  severity: High
  claim: State 4 hands back immediately on outcome_unknown, but the recovery line promises a person, which requires calling transfer_to_agent first, and an agent_unavailable result has no outcome that keeps idempotencyKey.
  evidence: "Never retry. Hand back terminal payload immediately with idempotencyKey." | "Call transfer_to_agent only for system-initiated escalations" | "before promising a person" | "idempotencyKey on outcome_unknown only"
  class: human
  decision: outcome-unknown-transfer-path

- anchor: Part 2 State 5 workflow.schedule_new step 6
  also: Part 2 State 2 Digital Drop-Off (DDO) Rules; Part 2 State 5 scheduler_always (explicit yes); Part 5 send_secure_link
  severity: High
  claim: The spec never settles whether send_secure_link needs the pre-commit readback and explicit yes that gate every write, or only destination confirmation at capture.
  evidence: "Require an explicit spoken yes immediately before any write." | "Capture and confirm the secure-link destination (SMS or Email)." | "call send_secure_link once with the confirmed destination and close."
  class: human
  decision: ddo-consent-gate

- anchor: Part 2 State 5 interruptions.informational_question
  also: Part 2 State 5 scheduler_always (explicit yes); Part 2 State 4 The Pre-Commit Gate
  severity: Medium
  claim: A yes given before a knowledge-base turn survives the interruption, which conflicts with requiring the explicit yes immediately before the write.
  evidence: "A confirmation captured before the interruption stands only if no detail has changed" | "Require an explicit spoken yes immediately before any write."
  class: human
  decision: consent-survives-interruption

- anchor: Part 2 State 5 broadening.scenario_selection
  also: Part 2 State 5 workflow.schedule_new steps 2-3; Part 2 State 5 agent_specific_tools.check_search_readiness
  severity: Medium
  claim: Scenario selection runs only after ready, but the drop-off question, the DDO choice, and the returning-Tax-Pro choice are made before readiness, and DDO never reaches readiness.
  evidence: "First match wins after readiness returns ready" | "where the caller has not said in the office or by secure upload link, ask." | "Skip readiness and availability only on a digital drop-off." | "where a yes selects returning_same_tax_pro"
  class: human
  decision: scenario-selection-timing

- anchor: Part 2 State 5 broadening.scenario_selection
  also: Part 5 check_search_readiness Outcome Results; Part 2 State 5 scheduler_always (tool result handling)
  severity: Medium
  claim: Readiness returns out_of_scope for open claim and Tax Pro Review, but item 1's handback is evaluated only after ready and no rule handles out_of_scope.
  evidence: "out_of_scope covers Tax Pro Review and open claim cases, named in issue." | "1 Open claim, Tax Pro Review or another specialized service: never schedule or broaden" | "First match wins after readiness returns ready"
  class: human
  decision: readiness-out-of-scope-handler

- anchor: Part 2 State 5 agent_specific_outcomes.no_acceptable_availability
  also: Part 2 State 5 agent_specific_outcomes.customer_declined_options
  severity: Medium
  claim: A caller who declines every rung matches both a contained close and a transfer, so the terminal outcome after ladder exhaustion is undefined.
  evidence: "Caller ends without accepting a time or requesting a person, or declines the cancellation gate." | "Every applicable rung of the active scenario ladder under broadening has been offered or declined"
  class: human
  decision: ladder-exhaustion-outcome

- anchor: Part 2 State 5 scheduler_always (tool result handling)
  also: Part 5 book_appointment Outcome Results; Part 5 cancel_appointment Outcome Results
  severity: Medium
  claim: Re-gating on not_confirmed has no attempt cap and no terminal outcome, so a repeated not_confirmed loops without end.
  evidence: "On not_confirmed, re-gate;" | "Confirmation evidence missing/incomplete."
  class: human
  decision: not-confirmed-regate-cap

- anchor: Part 2 State 5 scheduler_always (mid-gate correction)
  also: Part 2 State 4 The Pre-Commit Gate; Part 2 State 5 invalidation.upstream_change
  severity: Medium
  claim: A mid-gate correction calls find_available_slots directly, skipping the readiness check that invalidation and the search rule require after any constraint change.
  evidence: "update the constraint in your state, recall find_available_slots, and force a fresh readback" | "Purge invalid state, update the constraint, check readiness, and search only on ready." | "Call `find_available_slots` only on ready."
  class: safe
  fix: In the State 4 bullet and its scheduler_always copy, replace "recall find_available_slots" with "re-run readiness, search only on ready".

- anchor: Part 2 State 5 invalidation.partial_acceptance
  also: Part 2 State 3 Readiness & Availability > Tax Pro Trade-off; Part 2 State 5 broadening.ladders.returning_same_tax_pro
  severity: Medium
  claim: Rejecting a proposed Tax Pro triggers the trade-off at once, while the ladders allow the trade-off only at the rung that drops the Tax Pro preference.
  evidence: "If the caller rejects a proposed Tax Pro but keeps the office, ask the Tax Pro trade-off first" | "only at the ladder step that drops the Tax Pro preference"
  class: human
  decision: trade-off-timing

- anchor: §1.5 global_always (tool calls after handback)
  also: Part 2 State 5 closure.re_entry; Part 2 State 5 interruptions.intent_change; Part 3 State 2 interruptions.intent_change; Part 4 State 2 interruptions.intent_change
  severity: Medium
  claim: Only consecutive silence forbids tool calls; no rule says which tools stay callable after the agent commits, decides intent_changed, or gets a transfer_to_agent result.
  evidence: "Call no tools, say nothing, and hand back immediately." | "One invocation commits at most one transaction." | "Close any committed transaction, then hand back intent_changed."
  class: human
  decision: post-handback-tool-lock

- anchor: Part 5 send_secure_link Outcome Results
  also: Part 2 State 5 workflow.schedule_new step 6
  severity: Medium
  claim: The DDO path ends with "close" and never handles delivery_failed, so the retry, re-capture, or transfer step after a failed link is undefined.
  evidence: "Link could not be sent to the provided destination." | "call send_secure_link once with the confirmed destination and close."
  class: human
  decision: ddo-delivery-failed-path

- anchor: Part 3 State 1 Intent Scope & Disambiguation > unclear_intent
  also: §1.2 Input Exhaustion & Silence > No-Match Rule; §1.5 terminal_payload_contract
  severity: Medium
  claim: After one failed reprompt, unclear_intent may either transfer or go to a message, with no rule for choosing, while the No-Match Rule says to transfer.
  evidence: "If unresolved after one reprompt, transfer or route to leave a message." | "On the second consecutive failure, call `transfer_to_agent`." | "Resolve unclear_intent before return."
  class: human
  decision: office-unclear-intent-exit
