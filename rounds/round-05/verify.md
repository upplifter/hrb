# Round 5 verification (L-326 to L-345)

`python tools/lint.py check` gives RESULT WARN with no FAIL, and the JSON is valid. New warnings fell from 34 to 13 against lint-before, round growth is -0.42%, and the 3 web_deflection warnings existed before this round. The diff does not touch frozen text (§1.4 lines, global_voice_lexicon, dialogue Agent lines). Every deleted rule still lives where its pointer says. The only open reference, "the deterministic flow" in workflow.office_contact_flow[0], is already backlogged as L-354.

L-326 | pass
L-327 | pass
L-328 | pass
L-329 | fix-needed | §2 State 5 interruptions.intent_change; §3 State 2 interruptions.intent_change; §4 State 2 interruptions.intent_change: in all three, replace "a global_always identity question" with "an identity-theft, fraud, or other-department question". The global_always item covers identity theft, fraud, and other-department questions. "Identity question" names only the first, so a fraud question could still hit "never transfer", and in the Scheduler the phrase can be read as an authentication question. The Scheduler item becomes 60 words.
L-330 | pass
L-331 | pass
L-332 | pass
L-333 | pass
L-334 | pass
L-335 | pass
L-336 | pass
L-337 | pass
L-338 | pass
L-339 | pass
L-340 | pass
L-341 | pass
L-342 | pass
L-343 | pass
L-344 | pass
L-345 | pass

Checks behind the passes:

- L-326 is D-048's wording on the anchor D-048 names. The item is 58 words. A "no" to keeping the Tax Pro still falls to "otherwise resolve the office by entryPoint".
- L-327 matches D-043, §1.4 intro, the global_always transfer-results item, and §5.1 Transfer results. It is 60 words. supportHoursSpoken and "else close" are now scoped to agent_unavailable. callContained is false on a failed call because it is not a message action. "Speak nothing" and the outcome_unknown exception still live in global_always.
- L-328: the §1.3 bullet is 35 words and 2 sentences, and it mirrors the JSON. It agrees with §3 If hours_unavailable and workflow.office_contact_flow[2] (D-045).
- L-335: the text offer, its position, and its DDO skip live in the scheduler_always text-offer item. The explicit yes lives in the scheduler_always consent item and agent_specific_tools.book_appointment and reschedule_appointment. The before-and-after readback lives in agent_specific_tools.reschedule_appointment.
- L-336: the §4 Elicit the Reason First prose still carries the long form, which is allowed under C-2 A and consistent.
- L-337: the office_contact scope is gone. The unscoped rule agrees with §1.2 ("Take office hours and phone numbers only from get_office_details and check_office_open_status"), which wins under C-1.
- L-338: the tax_pro_always by-name item still holds the ZIP capture.
- L-339: global_voice_lexicon.questions_per_turn still holds "exactly one primary question per turn, placed at the end".
- L-340: the book_appointment request carries neither field. §5.2 find_available_slots Orthogonal Payload Separation still names both.
- L-342: §2 State 3 Principles and the broadening item keep "Never silently change/substitute a Tax Pro".
- L-343: global_outcomes.intent_changed keeps "Close any committed transaction".
- L-345: scenario_selection item 8 and §4 Generic Request still state how priorTaxProStatus is used.
