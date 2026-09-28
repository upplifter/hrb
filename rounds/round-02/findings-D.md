- anchor: §2 State 3 Dynamic State Invalidation: Location & Time
  also: §2 State 5 invalidation.upstream_change; broadening.ladders.returning_same_tax_pro.rungs[2]; broadening.ladders.reschedule.rungs[2]
  severity: High
  claim: Every location change purges the Tax Pro, but the same_tax_pro_nearby_offices rung changes the office and must keep the Tax Pro, and after D-008 nothing says whether accepting a rung triggers this invalidation.
  evidence: "A location change also purges the assigned Tax Pro. Re-run readiness and search." | "location change also invalidates taxProRef" | "same_tax_pro_nearby_offices"
  class: human
  decision: rung-acceptance-invalidation-scope

- anchor: §1.5 global_outcomes (identity_or_appointment_mismatch, validation_failed, system_failure, clarification_exhausted)
  also: §2 State 5 agent_specific_outcomes.no_acceptable_availability; §3 State 2 agent_specific_outcomes.office_info_transfer; §1.5 global_outcomes.transferred_to_human, transfer_unavailable
  severity: Medium
  claim: Each transfer-reason outcome hard-codes nextAction transfer with no agent_unavailable path, and each overlaps transferred_to_human or transfer_unavailable, so the finalOutcome for one transfer is ambiguous; only outcome_unknown (D-007) resolves this.
  evidence: "A tool failed or the availability check failed. transferReason system_failure" | "transfer_to_agent returned agent_available. Carry IVR call summary" | "Call transfer_to_agent with transferReason no_acceptable_availability"
  class: human
  decision: transfer-outcome-selection-on-unavailable

- anchor: §2 State 5 scheduler_always tool-result item (find_offices_near none_nearby)
  also: §2 State 5 broadening.principles nearby-office item; broadening.ladders.returning_tax_pro_unavailable.rungs[3]
  severity: Medium
  claim: A none_nearby result on a nearby-office rung transfers the caller at once, which skips the ladder's later rungs (e.g., the regional virtual rung) instead of counting the rung as exhausted.
  evidence: "none_nearby transfers." | "Nearby-office rungs search up to three nearby offices, nearest first"
  class: human
  decision: none-nearby-on-broadening-rung

- anchor: §1.4 conflict from readiness
  also: §5.2 check_search_readiness Outcome Results; §2 State 5 scheduler_always tax_extension and emerald_advance items
  severity: Medium
  claim: The only readiness conflict handler covers a past date, yet conflict also covers other constraint conflicts, and no rule says which readiness result signals a closed extension or Emerald Advance window.
  evidence: "That date's already gone by, what's the next day that could work for you?" | "Constraints conflict, or the date has passed. issue explains why." | "let check_search_readiness decide whether the filing window is open"
  class: human
  decision: readiness-conflict-handling

- anchor: §2 State 5 broadening.scenario_selection item 7
  also: §2 State 5 broadening.ladders.peak_capacity.primary; broadening.principles consent item
  severity: Medium
  claim: The peak_capacity switch from returning_same_tax_pro offers any Tax Pro at the three nearest offices, dropping the kept Tax Pro and office without the trade-off or consent.
  evidence: "switch to peak_capacity, re-run readiness, and restart at its primary offer" | "offer slots from the three nearest offices with the requested window" | "Never silently substitute a Tax Pro, office, date, time window or method."
  class: human
  decision: peak-switch-tax-pro-consent

- anchor: §2 State 5 broadening.ladders.extension.rungs[1]
  also: §2 State 5 scheduler_always tax_extension item; §2 State 3 Ladders > Extension row
  severity: Medium
  claim: After self-filing is accepted, no trigger picks the tax_prep handback over the support transfer, "close the extension transaction" refers to a transaction never committed on this path, and a caller who wants neither has no exit.
  evidence: "If accepted, offer to hand back for a follow-up tax_prep appointment, or call transfer_to_agent" | "close the extension transaction and return route_intent to appointment_scheduler" | "its final rung offers follow-up tax_prep"
  class: human
  decision: self-filing-rung-exits

- anchor: §2 State 1 Authentication Logic > New Customers
  also: §2 State 5 workflow.reschedule_existing[0]; workflow.cancel_existing[0]
  severity: Medium
  claim: A first-party no_match is a new-customer path on booking, but no rule says what happens on no_match during reschedule_existing or cancel_existing, and "Proceed only on single_match" reads both ways.
  evidence: "A no_match creates no profile. Profile creation is deferred" | "Proceed only on single_match. On failure or unregistered ANI"
  class: human
  decision: no-match-on-reschedule-cancel

- anchor: §4 Tax Pro Lookup & Disambiguation > Generic Request
  also: §4 State 2 workflow.speak_to_tp_generic
  severity: Medium
  claim: The generic path branches only on an active prior Tax Pro, with no step when the caller has no prior Tax Pro or it is inactive.
  evidence: "If active, state the options for reaching them."
  class: human
  decision: generic-request-no-active-tax-pro

- anchor: §2 State 5 workflow.reschedule_existing[2]
  also: §2 State 2 Appointment Type Rules > Immutability; §2 State 2 Dynamic State Invalidation: Type & Method Edge Cases
  severity: Medium
  claim: Reschedule forbids a method change but handles only a type change request, while the Type & Method invalidation treats a method change as processable, so a mid-reschedule method request has no defined step.
  evidence: "never change the appointment type or method through reschedule" | "On a type change request, preserve the appointment and call transfer_to_agent."
  class: human
  decision: reschedule-method-change-handling

- anchor: §3 State 2 workflow.office_contact_flow[2]
  also: §5.3 check_office_open_status Outcome Results; §3 State 2 agent_specific_tools.transfer_to_agent
  severity: Medium
  claim: The office_contact flow branches only on OPEN or CLOSED, and nothing says whether hours_unavailable counts as an "office lookup failure" that transfers.
  evidence: "Schedule data missing for the requested location." | "plus unresolved intent or office lookup failure"
  class: human
  decision: hours-unavailable-handling

- anchor: §3 State 2 workflow.office_contact_flow[1]
  also: §3 State 2 office_always disambiguation item
  severity: Medium
  claim: With a clear office_contact intent and a null routedOfficeRef, the flow calls get_office_details with no office resolution step, since the ZIP capture applies only during disambiguation.
  evidence: "1. Call get_office_details to retrieve mainPhoneSpoken." | "If routedOfficeRef is missing during disambiguation, capture a 5-digit ZIP code"
  class: human
  decision: office-contact-office-resolution

- anchor: §4 Tax Pro Lookup & Disambiguation > Multiple Matches
  also: §4 State 2 tax_pro_always multiple-matches item; workflow.speak_to_tp_by_name[3]
  severity: Medium
  claim: Location disambiguation of multiple Tax Pro matches has no stop condition or exit when the caller cannot pick one.
  evidence: "Ask a location/city disambiguation question using primaryOfficeName"
  class: human
  decision: tax-pro-disambiguation-exit

- anchor: §2 State 4 The Pre-Commit Gate (correction bullet)
  also: §2 State 5 scheduler_always mid-gate correction item; invalidation.text_confirmation
  severity: Medium
  claim: Every mid-gate correction re-runs readiness and search, including a text-destination correction that invalidation.text_confirmation treats as separate from scheduling constraints, so it is unclear whether the selected slot survives.
  evidence: "update the constraint in your state, re-run readiness, search only on ready, and force a fresh readback" | "Text opt-in and destination survive scheduling-constraint changes"
  class: human
  decision: mid-gate-correction-scope

- anchor: §2 State 5 workflow.schedule_new[4]
  also: §2 State 4 Optional Text Confirmation; §2 State 2 Digital Drop-Off (DDO) Rules
  severity: Medium
  claim: Step 5 offers a text confirmation and a complete readback on every schedule_new, including DDO, whose gate is the destination readback and whose write takes no textConfirmation.
  evidence: "5 Text and gate. Offer optional text immediately before the complete readback." | "Offer on schedule_new and reschedule_existing immediately before the gate." | "Skip readiness and availability only on a digital drop-off."
  class: human
  decision: ddo-gate-sequence
