# Backlog

Low findings and deferred items. They do not block the exit.

- L-034 | §1.5 terminal_payload_contract and other JSON strings over 60 words | Needs a string-to-array restructure | Human, Low.
- L-035 | §3 Mini-Dialogue 3B; §2 Mini-Dialogue 1B | Frozen Agent turns run three sentences | Human, Low.
- L-167 | §2 State 5 scheduler_always callback item | Part 4 call reason not carried to the Scheduler | Human, Low.
- L-168 | §1.5 context_envelope.customerStatus | No enum | Human, Low.
- L-169 | §5.2 find_customer and other responses | Fields no rule reads | Human, Low.
- L-176 | §1.5 global_outcomes.transfer_unavailable | 70 words, over the 60-word limit | Low; fold into L-034 restructure. Fixed by L-327 (round 5).
- L-197 | §5.2 send_secure_link Outcome Results | No not_confirmed or rejected result | Human, Low.
- L-198 | §5.1 search_knowledge_base attempt | attempt value on clarifier re-query undefined | Human, Low.
- L-223 | §3 If OPEN; By-Appointment-Only | Editorial trim held until L-186 and L-081 are decided | Safe, Low.
- L-237 | §2 State 2 Tax Extension bullet | Heading home ambiguous | Human, Low.
- L-246 | §5.1 search_knowledge_base KB results | requires_tax_pro outside the Scheduler: D-025 vs D-034 | Human, Low. Decided D-046, fixed.
- L-248 | agent_specific_outcomes.customer_declined_options | "requesting a person" ambiguous after D-034 | Human, Low.
- L-251 | §1.5 terminal_payload_contract | 214 words; fold into L-034 restructure | Low.
- L-318 | §2 Mini-Dialogue 1A | No one-line purpose; fix adds words to a frozen line | Human, Low.
- L-319 | §2 Mini-Dialogue 2A, 2B | Latency bridges outside preamble_phrases | Human, Low.
- L-320 | §1.3 Leave-a-Message Ownership | F-10 trim held until L-289 is decided | Safe, Low. Decided D-039, fixed.
- L-321 | Part 5 Conventions | F-02 trim; oscillation guard (edited rounds 1-3) | Human, Low.
- L-346 | §1.5 global_outcomes.configuration_missing | Copies handoff_invalid; oscillation guard (edited rounds 2-4). | Human, Low.
- L-347 | agent_specific_tools.find_available_slots | Restates rules; oscillation guard (edited rounds 2-4). | Human, Low.
- L-348 | scheduler_never loan item | Repeats global_never; oscillation guard. | Human, Low.
- L-349 | scheduler_always DDO item | Descriptive sentence and "execute"; oscillation guard. | Human, Low.
- L-350 | agent_specific_tools.check_search_readiness | Repeats one-question rule; oscillation guard. | Human, Low.
- L-351 | §4 State 2 objective | Partial repeat of Base handback; oscillation guard. | Human, Low.
- L-352 | §3 Unclear intent; office_always disambiguation item | Wordy; oscillation guard (edited rounds 1, 2, 4). | Human, Low.
- L-353 | §4 State 2 tax_pro_always callback item | Prose now names routed_to_scheduler, JSON spells it out; oscillation guard. | Human, Low.
- L-354 | §3 State 2 workflow.office_contact_flow[0] | Describes the Leave a Message flow's internals; oscillation guard. | Human, Low.
- L-355 | agent_specific_outcomes.appointment_already_canceled; Part 5 Conventions summary bullet | canceledSummary means a write result and a retrieved record; oscillation guard. | Human, Low.
- L-356 | Part 5 Conventions first bullet | Dead envelope synonyms; oscillation guard (L-321). | Human, Low.
