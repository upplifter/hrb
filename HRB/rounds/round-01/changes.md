L-001 | §1.5 global_outcomes.customer_abandoned | Unanswered gate now runs the no-input rule, then terminates | 0
L-002 | §1.5 global_always (transfer_to_agent item); Parts 2-4 agent_specific_tools.transfer_to_agent, interruptions.intent_change | Barging added to global transfer item; six agent-block barging sentences deleted | -89
L-003 | §1.5 global_outcomes.transfer_unavailable | No-message case speaks supportHoursSpoken and invites call back | +6
L-004 | §2 State 5 workflow.schedule_new[1]; scheduler_always rollover item; §2 State 3 Office Resolution > Rollover | Same-Tax-Pro exception added; step 2 says "otherwise branch on entryPoint" | +14
L-005 | §2 State 5 workflow.reschedule_existing[2] | Type immutable on reschedule; type change preserves appointment and transfers | +13
L-006 | §2 State 4 The Pre-Commit Gate; scheduler_always mid-gate correction item | Correction re-runs readiness and searches only on ready | +8
L-007 | §2 State 3 Readiness & Availability > CDAS; scheduler_always CDAS item | Drop-off exception keyed to appointmentMethod physical_drop_off | -2
L-008 | §2 State 5 broadening.ladders.tax_notice.rungs[3] | Rung uses any_qualified_tax_pro token and trade-off permission wording | +2
L-009 | §3 State 2 and §4 State 2 agent_specific_tools.transfer_to_agent | Point to global_always conditions; dropped Tax Pro indeterminate-write trigger | +4
L-010 | §4 State 2 tax_pro_never | Deleted tax-advice item duplicating global_never | -12
L-011 | §2 State 5 workflow.schedule_new, reschedule_existing, cancel_existing | Office-identity clauses cut; Close steps point to closure; cancel steps 6-7 deleted | -200
L-012 | §2 State 5 agent_specific_tools (six scheduling tools) | Deleted officeName and spoken-address sentences from six tool entries | -101
L-013 | §2 State 5 workflow.*[0] | Each step 1 now authenticates per scheduler_always | -148
L-014 | §3 Office Contact Triage If OPEN/If CLOSED; §4 workflow.leave_message[1]; §5 tool intros | Deleted reason clauses; kept capture_intent Head of Call clause | -69
L-015 | §2 State 5 workflow.schedule_new[1] | Step 2 cut under 60 words, keeps L-004 exception, points to scheduler_always | -79
L-016 | §2 State 5 workflow write steps; scheduler_always idempotency item; agent_specific_tools.reschedule_appointment | Removed restated no-retry and no-cancel-recreate rules | -26
L-017 | §2 State 5 scheduler_always rejected-rollover item; rollover item | Deleted duplicate item; rollover item points to invalidation.rejected_rollover_office | -30
L-018 | §4 State 2 tax_pro_never; §2 State 5 agent_specific_tools.transfer_to_agent | Deleted DOB, online, and transfer-summary PII repeats of Base JSON | -44
L-019 | §2 State 5 workflow step 5 (x2); invalidation.text_confirmation | Deleted third-party mobile-number restatements | -34
L-020 | How to Read This Document | Part 1, 2 bullets trimmed; Part 4 message sentence deleted | -36
L-021 | §2 State 5 objective | Deleted type-first and confirmation-gate restatements | -23
L-022 | §2 State 5 scheduler_always returning-client, waterfall, tax_notice items | Dropped repeated exceptions and readback clause; waterfall split into three items | -22
L-023 | §5.1 transfer_to_agent | Silence rule replaced with §1.2 pointer; lowercased "and" | -10
L-024 | §5.1 search_knowledge_base | Deleted 0.85 sentence; merged attempt and clarifier sentences | -9
L-025 | §1.1 The Head of Call Envelope | Deleted empty category labels from table cells | -16
L-026 | §1.2 Zero Web Deflection; Hours; No-Input; Abandonment; Confirmation Strategy | Architecture bullet split; filler cut; bullets at most 2 sentences | -28
L-027 | §2 State 2 Tax Notice Guardrails; Complexity Matching; Dynamic State Invalidation > Action | Bullets merged to at most 2 sentences; redundant label dropped | -21
L-028 | §2 State 3 Readiness & Availability; Principles; §2 State 4 Write Tools | CDAS split in two; other bullets joined to at most 2 sentences | -1
L-029 | §4 Elicit the Reason First; Fulfillment Priority; scheduler_always; scheduler_never; invalidation.customer_identity; §2 State 4 Third-Party; §5.1 Category Enums | "must" and third-person phrasing rewritten to imperative | -18
L-030 | Part 5 Conventions Common to Every Tool | Alias paragraph split into eight bullets, no word change | 0
L-031 | §1.3 Leave-a-Message Ownership | Paragraph split into five bullets under the label, no word change | 0
L-032 | §1.5 global_always no-match item; scheduler_always auth, returning-client, text, tax_notice, entryPoint items | Over-60-word items split at sentence boundaries, no word change | 0
L-002 (follow-up) | §1.5 global_always (transfer_to_agent item) | Restored "immediately" timing limit on barging call | +3
L-032 (follow-up) | Part 2 scheduler_always (tax_notice missing-value item) | Restored tax_notice_service trigger on missing notice value rule | +3
