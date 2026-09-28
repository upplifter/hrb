# Round 4 findings - Lens D (Flow and termination)

Saved by the orchestrator from the reviewer's reply (write blocked).

### D-01 · "Cancel" said mid-booking always runs cancel_existing
Anchor: §2 State 5 interruptions.cancel_said; §2 State 4 The Pre-Commit Gate ("On a no")
Severity: Medium
Class: Human
Issue: `cancel_said` says "If the caller wants to cancel before any commit, abandon the booking and run the cancel_existing workflow in full", so "no, cancel that" at a booking gate matches both this rule and the gate-no branch. A new caller has no customerRef for `get_customer_appointments`; a returning caller gets none_found and a transfer.
Proposed fix: Scope `cancel_said` to cancelling an existing appointment; treat "cancel this booking" as a gate no or customer_declined_options.

### D-02 · cancel_said after commit names no routing target
Anchor: §2 State 5 interruptions.cancel_said; §1.5 global_outcomes.intent_changed
Severity: Medium
Class: Human
Issue: "After a commit, close the committed transaction normally and hand back intent_changed" names no routingTarget and carries no operation cancel_existing, so the next invocation asks book, change, or cancel again.
Proposed fix: Name the routingTarget and the operation or reference the handback carries.

### D-03 · KB non-answer mid-booking terminates the transaction
Anchor: §1.5 global_always (followUpTopics item); §2 State 5 interruptions.informational_question; §5.1 search_knowledge_base KB results
Severity: Medium
Class: Human
Issue: "Any other non-answer returns no_approved_answer" is terminal, so a below-threshold logistics answer mid-negotiation ends the booking, while `informational_question` says "Resume at the first unanswered requirement".
Proposed fix: Decide whether a Scheduler KB non-answer states it has no answer and resumes, or ends with no_approved_answer.

### D-04 · invalid_constraints to readiness loop has no cap
Anchor: §2 State 5 scheduler_always (find_offices_near result item); §5.2 find_available_slots Outcome Results
Severity: Medium
Class: Human
Issue: On `invalid_constraints` the agent re-runs readiness, and ready leads back to `find_available_slots` with no cap or exit. The rule also sits in the `find_offices_near` item, though only `find_available_slots` returns that result.
Proposed fix: Cap the re-run at once, name the exit (e.g., system_failure transfer), and move the rule to the find_available_slots entry.

### D-05 · Re-entry reuses idempotency keys, so a DDO change is deduplicated
Anchor: §2 State 5 scheduler_always idempotency item; closure.re_entry; §2 State 2 DDO Rules > Rescheduling
Severity: High
Class: Human
Issue: `re_entry` demands "a fresh idempotency key namespace", but every key starts with interactionId, which §1.1 defines per session. A DDO change under D-017 reuses "interactionId-ddo-1", so the backend can replay the old send while the agent reports ddo_link_sent.
Proposed fix: State whether interactionId changes per invocation, or add an invocation discriminator to every key format.

### D-06 · A post-commit change request has no path
Anchor: §2 State 4 Write Tools > Post-Commit Readback; §2 State 5 closure.re_entry; scheduler_always mid-gate correction item
Severity: Medium
Class: Human
Issue: A change requested during or after the post-commit readback ("actually, make it Wednesday") matches only the mid-gate correction rule, which would lead to a second write in one invocation, against "One invocation commits at most one transaction".
Proposed fix: Route a post-commit change request as intent_changed to appointment_scheduler (reschedule_existing), or name another exit.

### D-07 · Office info has no stop trigger after the blurb
Anchor: §3 Office Details Logic > Standard Blurb; §3 State 2 workflow.office_info_flow[3]; §1.3 The Yield, Do Not Solicit Rule
Severity: Medium
Class: Human
Issue: "Answer follow-ups ... in the same invocation, then return office_info_provided", but §1.3 bans "Is there anything else?". Caller silence after the blurb runs the No-Input Rule and ends as consecutive_silence instead of office_info_provided.
Proposed fix: Define the trigger that returns office_info_provided (e.g., the first silence after an answer), exempt from the robocall path.

### D-08 · Named-office match skips the office the ZIP resolves to
Anchor: §3 Office Details Logic > Named Office, No Name Match; §3 State 2 office_always named-office item
Severity: Medium
Class: Human
Issue: The agent must "match officeName in nearbyOffices", but the ZIP's own office is the top-level officeRef and officeName, so naming it yields a false no-match and a system_failure transfer.
Proposed fix: Match officeName against the top-level office and nearbyOffices.

### D-09 · office_contact ignores seasonalStatus
Anchor: §3 State 2 workflow.office_contact_flow; §3 Office Contact Triage > If CLOSED
Severity: Medium
Class: Human
Issue: `office_info_flow` checks by_appointment_only and closed_for_season, but `office_contact_flow` does not, so a closed_for_season office takes the CLOSED branch and the caller hears no Year-Round Office.
Proposed fix: Add the seasonalStatus check to office_contact_flow, or state that CLOSED covers seasonal closure.

### D-10 · Single by-name match has no branch for a caller "no"
Anchor: §4 Tax Pro Lookup & Disambiguation > By Name Request > 1 Match; §4 State 2 workflow.speak_to_tp_by_name
Severity: Medium
Class: Human
Issue: "1 Match: Confirm the Tax Pro" can mean asking the caller or confirming internally; if asked, no rule covers a "no", and the workflow has no confirm step.
Proposed fix: State whether the single match is confirmed with the caller, and if so, route a "no" to No Matches / Inactive.

### D-11 · Returning caller who keeps the Tax Pro but rejects the last-served office
Anchor: §2 State 5 workflow.schedule_new[1]; §2 State 3 Office Resolution > Declined Offices; invalidation.rejected_rollover_office
Severity: Medium
Class: Human
Issue: "A yes selects returning_same_tax_pro and proposes their last-served office", and declining every proposed office returns customer_declined_options. A caller who wants the same Tax Pro elsewhere has no path to same_tax_pro_nearby_offices or ZIP capture.
Proposed fix: Name the step after a rejected last-served office.
