# Round 4 findings, lens B (Universal rules vs local overrides)

Saved by the orchestrator from the reviewer's reply (write blocked).

### B-01 · handoff_unavailable line pattern has no failed-call branch
Anchor: §2 State 5 closure.line_patterns (handoff_unavailable); §1.5 global_always transfer-results item; §5.1 transfer_to_agent Transfer results
Severity: Medium
Class: Safe. D-026 and C-1.
Issue: The pattern's else-branch says "otherwise speak supportHoursSpoken exactly as returned and invite a call back", which a failed call falls into; Part 1 says a failed call speaks the system_failure line with no supportHoursSpoken.
Proposed fix: Append "On a failed transfer call, follow global_always." to the handoff_unavailable pattern.

### B-02 · "Tax Pro covers it at the appointment" on paths with no appointment or no Tax Pro
Anchor: §2 State 3 Informational Interruptions > Personal Questions; §2 State 5 agent_specific_tools.search_knowledge_base; scheduler_never loan/fee/notice item; §1.5 global_voice_lexicon.method_descriptions
Severity: Medium
Class: Human
Issue: The Scheduler always says "the Tax Pro covers it at the appointment", including on cancel_existing, digital_drop_off, and physical_drop_off, where the frozen lexicon says there is "no appointment" or "you won't be meeting with a specific tax professional".
Proposed fix: Ask which line or handback applies on cancel_existing, DDO, and physical_drop_off.

### B-03 · State 2 prose hands back any request for the caller's own Tax Pro
Anchor: §2 State 2 Appointment Type Rules > Tax Pro Requests; interruptions.intent_change; broadening.scenario_selection item 8
Severity: Medium
Class: Safe. D-034 and the JSON mirror.
Issue: Same as A-03 and E-01.
Proposed fix: "A request to speak to a specific or own Tax Pro".

### B-04 · Post-commit cancel request hands back intent_changed with no routingTarget
Anchor: §2 State 5 interruptions.cancel_said; §1.5 global_outcomes.intent_changed; terminal_payload_contract routingTarget
Severity: Medium
Class: Human
Issue: Same as D-02.
Proposed fix: Ask which routingTarget and carried reference a post-commit cancel request returns.

### B-05 · "Confirm the Tax Pro" on a single by-name match vs confirmation by consequence
Anchor: §4 By Name Request > 1 Match; §1.2 Confirmation Strategy > Confirmed by consequence
Severity: Medium
Class: Human
Issue: "1 Match: Confirm the Tax Pro" vs Part 1's "never spend a turn asking 'Did I get that right?'" except for unverifiable raw data and a third-party owner's name.
Proposed fix: Ask whether a single match gets a spoken confirm turn; if not, "Treat the match as the confirmed Tax Pro".

### B-06 · Part 4 rule tells the agent to offer "the Appointment Scheduler"
Anchor: §4 No Matches / Inactive; §4 State 2 tax_pro_always unavailable item; §1.2 Zero Web Deflection & Prohibited Speech
Severity: Low
Class: Safe
Issue: "Offer only the Appointment Scheduler" and "offer only to route to the Appointment Scheduler" name internal architecture, which §1.2 bans.
Proposed fix: "offer only to book with another qualified Tax Pro at that location (routed_to_scheduler, appointmentType null)".

### B-07 · Mini-Dialogue 4D speaks the handoff line with no agent_available result, under a System label
Anchor: §4 Mini-Dialogue 4D; §1.4 Approved Recovery Lines intro
Severity: Low
Class: Safe (C-9)
Issue: 4D goes from "Calls `transfer_to_agent`" to the spoken line under "**System (Agent):**", with no result shown.
Proposed fix: "**System:** `transfer_to_agent` returns agent_available." then "**Agent:**" with the unchanged line.

### B-08 · Mini-Dialogue 1A opens a two-question sequence with no one-line purpose
Anchor: §2 Mini-Dialogue 1A; §1.2 Voice Persona & Delivery
Severity: Low
Class: Safe (reviewer); orchestrator: Human (adds caller-heard words to a frozen line)
Issue: Part 1 says "Frame any multi-question sequence with a one-line purpose"; 1A opens with only "May I have your first and last name?"
Proposed fix: Prefix a short purpose clause.

### B-09 · 2A and 2B close with latency bridges outside preamble_phrases
Anchor: §2 Mini-Dialogue 2A, 2B (last Agent turns); §1.5 global_always latency-preamble item
Severity: Low
Class: Human
Issue: "let me find you the right person." and "Let me find someone who can go over it with you." lead into a tool call but are not preamble_phrases entries.
Proposed fix: Ask whether these count as preambles.
