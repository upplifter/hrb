- anchor: §2 State 5 workflow.schedule_new[1]
  also: §1.1 The Head of Call Envelope (appointmentType, taxProRef, officeRef); §2 State 5 scheduler_always rollover item
  severity: Medium
  claim: On a callback or routed_to_scheduler handoff that carries taxProRef and officeRef, step 2 still asks whether to keep the prior Tax Pro and resolves the office by entryPoint, so a rollover could propose routedOfficeRef over the carried officeRef.
  evidence: "If a returning client's prior Tax Pro is active, ask whether to keep them" | "otherwise resolve the office by entryPoint per scheduler_always" | "If present, use them without re-asking."
  class: human
  decision: carried-office-vs-entrypoint-precedence

- anchor: §2 State 5 agent_specific_outcomes.customer_declined_options
  also: §2 State 4 The Pre-Commit Gate; §2 State 2 Digital Drop-Off (DDO) Rules
  severity: Medium
  claim: A plain "no" at the booking, reschedule, or DDO gate has no branch; only the cancellation gate's "no" maps to an outcome, so the implementer must guess whether to re-negotiate or close.
  evidence: "declines both extension exits, or declines the cancellation gate" | "Require an explicit spoken "Yes""
  class: human
  decision: non-cancel-gate-decline-exit

- anchor: §4 Fulfillment Priority step 3
  also: §4 State 2 tax_pro_always options item; tax_pro_always unclear-intent item
  severity: Medium
  claim: After the callback-or-message options, a caller who declines both has no exit; the only fallback is capture_intent for an unclear intent, which a clear decline is not.
  evidence: "3. Wait for the caller's intent." | "If intent is unclear, reprompt once, then return capture_intent"
  class: human
  decision: tax-pro-options-declined-exit

- anchor: §2 State 3 Office Resolution > Off-Season Closure
  also: §2 State 5 scheduler_always off-season item; scheduler_always central-line item; §1.4 Off-season office closure row
  severity: Medium
  claim: The Year-Round Office proposal asks "Would that work?" and the central-line step offers three offices, but neither states what happens when the caller declines every proposed office.
  evidence: "to propose the nearest Year-Round Office" | "Would that work?" | "return the three nearest eligible offices for caller selection"
  class: human
  decision: declined-office-proposal-exit

- anchor: §3 State 2 workflow.office_info_flow[3]
  also: §3 State 2 office_always closed_for_season item; §3 Dynamic State Invalidation: Location Change
  severity: Medium
  claim: The office_info flow returns the terminal payload right after the blurb, yet other rules expect later turns for follow-up questions and mid-call office changes, so the stop condition is unclear.
  evidence: "4. Yield the floor and return the terminal payload." | "store yroOfficeRef to answer follow-up questions" | "The caller asks about a different office or ZIP mid-call"
  class: human
  decision: office-info-follow-up-turns

- anchor: §2 State 5 broadening.scenario_selection item 7
  also: §2 State 3 Readiness & Availability > Tax Pro Trade-off
  severity: Medium
  claim: After the caller answers "stay", every later no_slots with office_at_capacity re-triggers item 7, so the peak trade-off question has no rule stopping it from being asked again at each rung.
  evidence: "item 7 is evaluated on no_slots and supersedes an earlier selection" | "on 'stay', keep the returning_same_tax_pro ladder"
  class: human
  decision: peak-trade-off-ask-once

- anchor: §2 State 5 scheduler_always explicit-yes item
  also: §1.5 global_always no-match item; §1.2 Input Exhaustion & Silence
  severity: Medium
  claim: An ambiguous or conditional gate answer is not consent, but no rule says whether it counts as a no-match toward the two-attempt transfer, so the gate can re-ask without a cap.
  evidence: "Ambiguous, partial, conditional, inferred, or silent agreement is not consent" | "On the first no-match for a required field, reprompt once"
  class: human
  decision: ambiguous-gate-answer-cap

- anchor: §2 State 5 scheduler_always tool-result item (slot_taken)
  also: §1.4 slot_taken row; §2 State 5 invalidation.ladder_state
  severity: Medium
  claim: slot_taken re-searches with no stated rung (same rung or primary offer) and no cap, so repeated slot_taken results can loop without a stop condition.
  evidence: "On slot_taken, speak the approved line and re-search"
  class: human
  decision: slot-taken-research-scope

- anchor: §5.2 get_customer_appointments Outcome Results none_found
  also: §2 State 5 agent_specific_outcomes.appointment_already_canceled; closure.continuation_context
  severity: Medium
  claim: When the only matching appointment is canceled, none_found (no active appointments, which transfers) and a canceled status (which returns appointment_already_canceled) both fit, so the cancel branch is undetermined.
  evidence: "No active future appointments exist." | "returned the bound appointment with status canceled; no write ran"
  class: human
  decision: canceled-appointment-result-branch

- anchor: §3 Office Details Logic > Named Office
  also: §3 State 2 office_always named-office item; agent_specific_outcomes.office_info_transfer
  severity: Medium
  claim: If no officeName in nearbyOffices matches the caller-named office, the flow has no branch; it is unclear whether this is an office lookup failure that transfers or a reprompt.
  evidence: "match officeName in nearbyOffices" | "Office lookup failure."
  class: human
  decision: named-office-no-match-branch
