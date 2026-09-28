# Round 9 · Lens B findings

Saved by the orchestrator from the reviewer's reply.

### B-01 · office_never still sends every appointment question to the Scheduler (D-097)
Anchor: §3 State 2 office_never[0]; §1.5 global_always informational item; §3 Out of Scope
Severity: Medium
Class: Safe
Issue: Same as E-01, C-03.
Fix: As E-01.

### B-02 · The same_day rung speaks the office_at_capacity line with no condition
Anchor: §2 State 5 broadening.ladders.same_day.rungs[1]; §1.4 Same-Day caller, next-day rung row; §2 State 3 Ladders, Same-Day row
Severity: Medium
Class: Safe
Issue: §1.4 limits "Today's fully booked at that office, I'm afraid." to office_at_capacity; the prose Same-Day row keeps "only if find_available_slots returned office_at_capacity". The round 7 L-392 trim changed the JSON rung to an unconditional "Lead with ...", dropping the trigger.
Fix: Old: "next_day morning or afternoon at the selected or nearby offices. Lead with the global_voice_lexicon.empathy office_at_capacity line." New: "next_day morning or afternoon at the selected or nearby offices. On office_at_capacity, lead with the global_voice_lexicon.empathy office_at_capacity line." (+3 words)

### B-03 · ladder_state reads as wiping identity and carried context on every restart
Anchor: §2 State 5 invalidation.ladder_state; invalidation.partial_acceptance; invalidation.customer_identity; §1.1 customerRef row
Severity: Medium
Class: Safe
Issue: "Apply customer_identity invalidation before any restart." read literally wipes STATE (and, since D-092, the carried values) on every restart, including a D-090 Tax Pro rejection. Contradicts §1.1 "never re-authenticate unless the transaction subject changes".
Fix: Old: "Apply customer_identity invalidation before any restart." New: "On an identity change, apply customer_identity invalidation before any restart." (+4 words)

### B-04 · Part 4 transfer_to_agent entry omits the D-091 multiple_matches transfer
Anchor: §4 State 2 agent_specific_tools.transfer_to_agent; §4 Generic Request; workflow.speak_to_tp_generic[2]
Severity: Low
Class: Safe
Issue: The tool entry lists local triggers as "plus third-party or authentication failure"; D-091 added find_customer multiple_matches.
Fix: Old: "Call per global_always transfer conditions, plus third-party or authentication failure." New: "Call per global_always transfer conditions, plus third-party or authentication failure and find_customer multiple_matches." (+3 words)

### B-05 · Mini-Dialogue 3B offers Digital Drop-Off by text only (D-099, C-9)
Anchor: §2 State 3 Mini-Dialogues > 3B, fourth Agent turn; scheduler_never method-token item; global_voice_lexicon.method_descriptions.digital_drop_off
Severity: Low
Class: Safe
Issue: D-099 requires method_descriptions when offering a method. The DDO description is "I'd text or email you a secure link to send your documents in, no appointment needed." 3B offers text only.
Fix: Old: "There's another way that skips the wait: I can text you a secure link to send your documents in, and you wouldn't need an appointment at all. Want me to do that?" New: "There's another way that skips the wait: I'd text or email you a secure link to send your documents in, no appointment needed. Want me to do that?" (about -5 words; frozen line changed under C-9 to follow D-099)

Other checks: D-084 to D-089, D-093, D-094, D-096, D-098 propagation complete apart from items above.

Summary: 5 findings (0 Critical, 0 High, 3 Medium, 2 Low).
