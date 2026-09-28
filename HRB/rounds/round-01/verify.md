L-001 | pass
L-002 | fix-needed | The merged global_always transfer_to_agent item dropped "immediately" from the deleted agent-block sentence "Call this tool immediately when the caller explicitly requests a live agent (barging)". That drops a timing limit. Restore it, e.g., "On barging, suspend any transaction and call it immediately."
L-003 | pass
L-004 | pass
L-005 | pass
L-006 | pass
L-007 | pass
L-008 | pass
L-009 | pass
L-010 | pass
L-011 | pass
L-012 | pass
L-013 | pass
L-014 | pass
L-015 | pass
L-016 | pass
L-017 | pass
L-018 | pass
L-019 | pass
L-020 | pass
L-021 | pass
L-022 | pass
L-023 | pass
L-024 | pass
L-025 | pass
L-026 | pass
L-027 | pass
L-028 | pass
L-029 | pass
L-030 | pass
L-031 | pass
L-032 | fix-needed | Splitting the scheduler_always tax_notice item left "Treat a missing value as a required field under MAX_INPUT_ATTEMPTS..." as a standalone item without its tax_notice_service trigger, so it reads as a general rule. Restore the scope, e.g., "On tax_notice_service, treat a missing notice value as a required field...".
lint | RESULT WARN (no errors; new warnings are dup_mirror L483/L564, allowed as a mirror under C-2 A, plus length L790 and L253, which were already over the limit before this round and are shorter or backlogged under L-034)
L-002 | pass (after follow-up) | orchestrator re-checked: "call it immediately" restored
L-032 | pass (after follow-up) | orchestrator re-checked: tax_notice_service trigger restored
