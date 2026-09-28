# Round 7 · Lens B findings

Saved by the orchestrator from the reviewer's reply.

### B-01 · Base JSON drops the Part 1 rule to confirm the third-party owner's name at capture
Anchor: §1.2 Confirmation Strategy > Confirmed at capture; §1.5 global_always confirm-at-capture item; §4 State 2 tax_pro_always third-party item
Severity: Medium
Class: Human (third-party authentication; Part 4 callers would hear a new readback)
Issue: §1.2 reads back raw data "plus the third-party owner's name". The Base JSON mirror confirms only values "that cannot be checked against a tool result and will not be spoken later", which excludes the owner's name. Only `scheduler_always` restores it ("Confirm the name at capture"); Part 4's `tax_pro_always` third-party item does not.
Proposed fix:
- A. (Recommended, +1 word) global_always confirm-at-capture item adds ", and a third-party owner's name"; delete "Confirm the name at capture." from scheduler_always (C-3 A).
- B. (+6 words) Add "Confirm the owner's name at capture." to the Part 4 third-party item only.
- C. (-6 words) Scope §1.2 "plus the third-party owner's name" to the Scheduler.

### B-02 · The frozen outcome_unknown line does not fit cancellations or secure-link sends
Anchor: §1.4 outcome_unknown row; global_voice_lexicon.empathy (outcome_unknown line); §2 State 4 Write Tools > Indeterminate Writes; global_outcomes.outcome_unknown
Severity: Medium
Class: Human (frozen text C-8; caller-facing)
Issue: The only outcome_unknown line says "confirming that time ... so nothing gets double-booked." `cancel_appointment` and `send_secure_link` also return outcome_unknown, so the caller hears about a time and double-booking while canceling or getting a link.
Proposed fix:
- A. (Recommended, ~0 words, 2 frozen strings) Reword to "I'm sorry, I'm having a little trouble confirming that on my end. Let me get someone to finish this for you so nothing gets done twice."
- B. (+15 words, no frozen edit) On a cancel or secure-link outcome_unknown, speak the system_failure line; keep the current line for book and reschedule.
- C. No change.

### B-03 · The "method_descriptions only" rule conflicts with gate readbacks, meetingMethodSpoken, and frozen dialogues
Anchor: §2 State 5 scheduler_never method-token item; §2 State 4 The Pre-Commit Gate; Mini-Dialogues 4A and 4B; Part 5 Conventions (meetingMethodSpoken)
Severity: Medium
Class: Human (caller-facing; 4A/4B Agent lines frozen)
Issue: scheduler_never says "Describe methods only with global_voice_lexicon.method_descriptions", whose entries are full sentences ("You'd come into the office."). The gate reads back the method, the frozen readbacks say "an in-person appointment", and Part 5 supplies meetingMethodSpoken ("in the office").
Proposed fix:
- A. (Recommended, ~0 words) Replace with "When offering or explaining a method, use global_voice_lexicon.method_descriptions."
- B. Keep "only", add "In a readback, use meetingMethodSpoken where returned", and edit 4A/4B under a decision.
- C. No change.

### B-04 · The Part 1 office_contact leave_message_offer trigger list omits closed_for_season
Anchor: §1.3 Leave-a-Message Ownership third bullet; §1.5 global_always leave-message item
Severity: Low
Class: Safe on the merits; oscillation guard likely
Issue: Part 1 lists "closed, busy, by_appointment_only, or hours_unavailable"; D-053 and `office_contact_triage_complete` list closed_for_season separately.
Proposed fix: Add "closed_for_season," after "closed," in both anchors.

### B-05 · Mini-Dialogues 4A and 4E disclose the prior Tax Pro with no find_customer result
Anchor: §4 Mini-Dialogues 4A and 4E; tax_pro_always disclosure item
Severity: Low
Class: Safe (C-9)
Issue: The Agent names the prior Tax Pro with no System turn showing `find_customer` resolved the owner.
Proposed fix: Insert "**System:** `find_customer` returns single_match with priorTaxProStatus active." before that Agent turn in 4A and 4E.

No other new Medium-or-higher lens B issues; L-074, L-075, L-080, L-146, and L-164 cover the rest.
