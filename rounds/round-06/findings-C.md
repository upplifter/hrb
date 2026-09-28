# Round 6 · Lens C findings

Saved by the orchestrator from the reviewer's reply.

### C-01 · no_acceptable_availability carries "agreed constraints", which is not a contract field
Anchor: agent_specific_outcomes.no_acceptable_availability; terminal_payload_contract
Severity: Medium
Class: Human
Options: A. map the agreed constraints to transfer_to_agent knownSoFar; B. state them in interactionSummary; C. add a contract field (C-7).

### C-02 · office_not_found on an officeRef the caller did not give has no handling
Anchor: §3 Office Details Logic > No Match; Part 3 agent_specific_tools.transfer_to_agent; §5.3 get_office_details
Severity: Medium
Class: Human
Issue: office_not_found on routedOfficeRef, a matched nearbyOffices officeRef, or yroOfficeRef has no rule.
Options: A. office lookup failure, transfer as system_failure; B. routedOfficeRef returns handoff_invalid, others system_failure; C. capture a ZIP and run the caller-ZIP rule.

### C-03 · Five names for the ladder's office
Anchor: Ladders table rows; broadening.ladders.*.primary; tax_notice.rungs[3]; same_day.rungs[1]; scenario_selection[7]
Severity: Medium
Class: Safe
Fix applied: "nearest", "primary", "desired", and "preferred" office -> "selected office" (primary clashes with primaryOfficeId; nearest contradicts §1.1 rollover).
