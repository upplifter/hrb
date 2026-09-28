# Round 9 · Lens D findings

Saved by the orchestrator from the reviewer's reply.

### D-01 · schedule_new[1] still asks the keep-prior question after Part 4
Anchor: §2 State 5 workflow.schedule_new[1]; scheduler_always routed_to_scheduler item; §2 State 2 After Part 4
Severity: Medium
Class: Safe
Issue: D-084 says never ask whether to keep the prior Tax Pro after a Part 4 routed_to_scheduler. schedule_new[1], the step that asks the question, has no exception. Same as E-03, C-04, but rated Medium here.
Fix: Old: "If a returning client's prior Tax Pro is active, ask whether to keep them;" New: "If a returning client's prior Tax Pro is active, ask whether to keep them, except per the scheduler_always routed_to_scheduler item;" (+7 words; item already over 60, L-417).

### D-02 · The gatekeeper item still applies to reschedule_existing
Anchor: §2 State 5 scheduler_always gatekeeper item; workflow.reschedule_existing[3]
Severity: Medium
Class: Safe
Issue: D-095: on a reschedule, take the baseline silently, no gatekeeper or waterfall. The scheduler_always gatekeeper item still asks the question for every returning client.
Fix: Old: "For a returning client, set the inherited baseline floor to the higher of the find_customer client complexity and prior Tax Pro cert level, then ask exactly one gatekeeper question: whether anything significantly changed since last year." New: "For a returning client, set the inherited baseline floor to the higher of the find_customer client complexity and prior Tax Pro cert level, then, except on reschedule_existing, ask exactly one gatekeeper question: whether anything significantly changed since last year." (+3 words)

### D-03 · The reschedule floor overrides the floor of 1 for emerald_advance, tax_notice_service, and callback
Anchor: workflow.reschedule_existing[3]; scheduler_always floor-1 item; §2 State 2 Appointment Type table; §2 Complexity Matching > Reschedule; §5.2 check_search_readiness > Callbacks
Severity: Medium
Class: Human
Issue: Same conflict as C-02. Pre-D-095 the computed floor was 1 for these types; now step 4 sends the inherited baseline.
Fix: A. (Recommended) Type floor stands on reschedule: "the higher of the inherited baseline floor (1 on emerald_advance, tax_notice_service, and callback), taken silently"; prose "Use the baseline silently (1 on types that skip screening)". B. Inherited baseline on every reschedule; scope the floor-1 rules to schedule_new.
Footprint: A 2 edits, +13 words. B 5 edits, +15 words, changes which Tax Pros qualify.

### D-04 · A change of transaction subject may not clear the carried values
Anchor: §2 State 1 Dynamic State Invalidation: Identity (Trigger); invalidation.customer_identity; scheduler_always carried-customerRef item
Severity: Medium
Class: Human
Issue: D-092 attached clearing of carried customerRef, appointmentType, taxProRef, officeRef to the identity-change trigger (name, DOB, SSN4). With a carried customerRef, identity questions are skipped, so a switch to a spouse is a first capture, not a change. Unclear whether a subject switch fires the invalidation.
Fix: A. (Recommended) Add the subject to the trigger: prose "or the transaction subject"; JSON "A change to any one, or to transactionSubject, wipes STATE.* completely". B. On a subject change, clear only priorTransaction and the four carried values.
Footprint: A 2 edits, +8 words. B 2 edits, +30 words.

### D-05 · After a partial rejection, the next constraint change re-selects returning_same_tax_pro
Anchor: invalidation.partial_acceptance; invalidation.ladder_state; broadening.scenario_selection[0] items 8-9
Severity: Medium
Class: Human
Issue: Under D-090, rejecting the prior Tax Pro re-selects returning_tax_pro_unavailable, but the item 8 "keep" record is unchanged. A later caller-initiated change re-runs scenario_selection and offers the rejected Tax Pro again.
Fix: A. (Recommended) Append "and records the prior Tax Pro as not kept." B. Rejection holds only "until the next caller-initiated change".
Footprint: A 1 edit, +8 words. B 1 edit, +6 words.

### D-06 · The rejected Tax Pro can return in the widened search, and the agent may not filter
Anchor: invalidation.partial_acceptance; scheduler_never slot-order item; §5.2 find_available_slots Request JSON
Severity: Medium
Class: Human
Issue: find_available_slots has no field to exclude a Tax Pro; scheduler_never forbids filtering slots. The widened search can return the rejected Tax Pro's other times and the agent must offer them.
Fix: A. (Recommended) scheduler_never adds "except slots with a Tax Pro rejected per invalidation.partial_acceptance"; partial_acceptance appends "Never offer that Tax Pro again." B. New request field excludeTaxProRefs (C-7).
Footprint: A 2 edits, +18 words. B 2 edits, +10 words plus a new field.

### D-07 · office_never still sends every appointment question to appointment_scheduler
Anchor: §3 State 2 office_never appointments item
Severity: Medium
Class: Safe
Issue: Same as E-01, C-03.
Fix: As E-01.

Summary: 7 findings (0 Critical, 0 High, 7 Medium, 0 Low).
