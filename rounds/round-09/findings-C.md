# Round 9 · Lens C findings

Saved by the orchestrator from the reviewer's reply. Reviewer checked and found no problems in: the D-085 taxProRef/officeRef clause against Part 4 outcomes; D-093, D-098, D-099, D-091, D-092, D-096, D-089, D-078; key-path and heading pointers; rung tokens vs the `find_available_slots` rung list; idempotency key and confirmation evidence on all four writes.

### C-01 · schedule_new[1] still asks the prior-Tax-Pro question that D-084 forbids after Part 4
Anchor: §2 State 5 `workflow.schedule_new[1]`
Severity: Medium
Class: Safe
Issue: D-084 added "Never ask whether to keep the prior Tax Pro" (§2 State 2 After Part 4, and the `scheduler_always` routed_to_scheduler item). Step 2 of `workflow.schedule_new` still says "If a returning client's prior Tax Pro is active, ask whether to keep them" with no exception. Round 8 left the step unedited under the oscillation guard, but that guard covers the L-417 trim, not a D-084 propagation.
Fix:
- Old: `If a returning client's prior Tax Pro is active, ask whether to keep them; yes selects`
- New: `If a returning client's prior Tax Pro is active, ask whether to keep them (never after a Part 4 routed_to_scheduler); yes selects`
- Net +6 words. Item stays over the 60-word limit (L-417). (Duplicate of B-01.)

### C-02 · Reschedule floor: prose omits the raise to the bound appointment's cert level
Anchor: §2 State 2 Complexity Matching & Tax Pro Rating Floor > Reschedule
Severity: Medium
Class: Safe
Issue: D-095 says the reschedule floor is the inherited baseline "raised to the bound appointment's taxProCertLevel". JSON says so. The prose bullet does not. C-1 makes prose win.
Fix:
- Old: `- **Reschedule:** Use the baseline silently, with no gatekeeper or waterfall.`
- New: `- **Reschedule:** Use the baseline silently, with no gatekeeper or waterfall, raised to the bound appointment's taxProCertLevel.`
- Net +6 words. If C-03 is decided with a scope, add the same scope here. (Duplicate of B-03, E-01.)

### C-03 · D-095 reschedule floor vs the fixed floors of emerald_advance, tax_notice_service, callback, physical_drop_off
Anchor: `workflow.reschedule_existing[3]`; `scheduler_always` floor items; §2 State 2 Appointment Type table
Severity: Medium
Class: Human
Issue: The type rules send exactly 1 (null for physical_drop_off) and skip complexity screening. D-095 sends the higher of the inherited baseline and the bound `taxProCertLevel` on every reschedule_existing, unscoped. For a rescheduled emerald_advance or tax_notice_service appointment the D-095 value can exceed 1. (Same as B-04, E-05.)
Fix: Options:
1. (Recommended) Type floors win; D-095 applies to tax_prep and tax_extension only. Insert `On tax_prep and tax_extension,` before `Send taxProRatingFloor as the higher of` in `workflow.reschedule_existing[3]`, and `On tax_prep and tax_extension:` after the label in the prose Reschedule bullet. +8 words, 2 edits.
2. D-095 wins on every reschedule. Add `except on reschedule_existing` after `send taxProRatingFloor as 1` in the type rules. +6 words, 1 edit.
3. Leave as is.

### C-04 · Part 4 handoff carries taxProRef and officeRef, but no rule says which ref or which office
Anchor: §4 Fulfillment: CDAS Callback Appointment > Handoff; §4 `tax_pro_always` callback item; §4 `agent_specific_outcomes.routed_to_scheduler`; §5 Conventions
Severity: Medium
Class: Human
Issue: For a by-name match, `taxProRef` is `taxPros[].hrbEmployeeId` (Conventions equate them). For a generic request it is `find_customer` `priorTaxProRef`, which Conventions never equate with `taxProRef`. For the office there are four candidates: `routedOfficeRef`, the ZIP-derived office, the matched Tax Pro's `primaryOfficeId`, or `priorOfficeRef`. A wrong office can return no slots for a Tax Pro who works elsewhere. (Same as A-01.)
Fix: Options:
1. (Recommended) Define the sources once in §5 Conventions and point to them from Part 4: `On a Part 4 handoff, taxProRef is hrbEmployeeId (by name) or priorTaxProRef (generic), and officeRef is the Tax Pro's primaryOfficeId (by name) or priorOfficeRef (generic).` +30 words, 1 edit.
2. Define officeRef as `routedOfficeRef`, or the ZIP-resolved office on central_line. About +15 words.
3. Carry only taxProRef on a callback; the Scheduler resolves the office. Changes D-085. About -10 words.

### C-05 · transfer_unavailable: leave_message_offer is not tied to leaveMessageAvailable
Anchor: §1.5 `global_outcomes.transfer_unavailable`; §1.3 Leave-a-Message Ownership (third bullet); `global_always` leave-message item
Severity: Medium
Class: Safe
Issue: The outcome reads "if leaveMessageAvailable is false, speak supportHoursSpoken and invite a call back ... nextAction leave_message if requested or accepted, leave_message_offer if not yet offered, else close". With leaveMessageAvailable false, "not yet offered" is true, so an implementer returns leave_message_offer, and Head of Call offers a message the tool said is unavailable. Agents never offer a message themselves (§1.3), so "not yet offered" always holds and gates nothing.
Fix:
- Old: `nextAction leave_message if requested or accepted, leave_message_offer if not yet offered, else close;`
- New: `nextAction leave_message if requested or accepted, else leave_message_offer if leaveMessageAvailable is true, else close;`
- Net +1 word. Optional mirrors (net 0 to +2 each): §1.3 third bullet and the `global_always` leave-message item, replace `a message may be offered` / `messaging may be offered` with `leaveMessageAvailable is true`.
- Orchestrator note: verify against the deterministic flow spec (Head of Call) that the handoff supports this before applying; it touches what the caller hears, so treat as Human if the flow spec does not settle it.

### C-06 · No rule sends taxProPreference or taxProRef to the search tools, and caller_stated has no producer
Anchor: §5.2 `check_search_readiness` Request `taxProPreference` and `taxProPreference.source`; §5.2 `find_available_slots` Request `taxProRef`; `scheduler_always`
Severity: Medium
Class: Human
Issue: D-079 defines `source` as caller_stated, prior_tax_pro, carried, or existing_appointment. No Scheduler rule says when to send `taxProPreference`, or when to send `taxProRef` to `find_available_slots`. After D-049 the Scheduler captures no Tax Pro preference, so caller_stated is never produced, and no rule selects the other three values.
Fix: Options:
1. (Recommended) Add one `scheduler_always` item: `Send taxProPreference with taxProRef and source on check_search_readiness, and taxProRef on find_available_slots, when a Tax Pro is bound: prior_tax_pro when the caller keeps the prior Tax Pro, carried when the envelope carries taxProRef, existing_appointment on reschedule_existing; otherwise send null.` Delete `caller_stated` from the Part 5 `taxProPreference.source` list (amends D-079). About +39 words.
2. Keep all four values and add the item with a caller_stated case for a caller who accepts the prior Tax Pro by name. About +45 words.
3. Leave as is.

### C-07 · check_search_readiness conflict has three branches, but issue is declared "not a caller-facing enum"
Anchor: §5.2 `check_search_readiness` (`issue` bullet and conflict row); `agent_specific_tools.check_search_readiness`; §2 State 3 Readiness & Availability
Severity: Medium
Class: Human
Issue: After D-078 and D-089 a `conflict` result has three responses: the past-date line, the type row's closed-window handling, and "ask once for another date or time". The only discriminator is `issue`, which Part 5 calls "A backend explanation, not a caller-facing enum". Nothing separates a past date from a closed window from another conflict.
Fix: Options:
1. (Recommended) Replace the `issue` bullet with `issue: On conflict, past_date, window_closed, or other; otherwise a backend explanation, never spoken.` +12 words in Part 5. Adds enum values (C-7).
2. Add `Classify a conflict from issue as a past date, a closed window, or other.` +14 words, no new values.
3. Leave as is.

### C-08 · Transfer paths with no §1.4 line have no defined agent_available line
Anchor: §1.4 intro sentence; `global_always` transfer-results item; §1.5 `global_outcomes.transferred_to_human`, `clarification_exhausted`
Severity: Medium
Class: Human
Issue: The rule is "On agent_available, speak the path's recovery line". §1.4 has no row for transfers with transferReason clarification_exhausted, out_of_scope, and automation_blocked (type or method change on reschedule, not_cancelable, rejected, change_not_allowed, false isCancelable or isReschedulable). The spec does not say whether to speak the generic `agent_available` row, speak nothing, or improvise.
Fix: Options:
1. (Recommended) Default to the agent_available row. §1.4 intro: `speak the path's line only on agent_available` becomes `speak the path's line, or the agent_available row when the path has none, only on agent_available`. `global_always` transfer-results item: `speak the path's recovery line and return` becomes `speak the path's recovery line, or the agent_available line when the path has none, and return`. +10 words each.
2. Speak nothing on those paths. +7 words each.
3. Leave as is.

Summary: 8 findings. Critical 0, High 0, Medium 8, Low 0. Safe 3 (C-01, C-02, C-05). Human 5 (C-03, C-04, C-06, C-07, C-08).
