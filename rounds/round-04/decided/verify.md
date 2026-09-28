# Round 4 decided verification (D-038 to D-049)

`python tools/lint.py check` gives RESULT WARN with no FAIL, and all 33 JSON blocks parse. Round growth is +0.99% against the 1.0% limit, so the fixes below (net about +25 words) need an offsetting Safe trim in the same batch. The new warnings are 8 dup_mirror (prose/JSON mirrors allowed under C-2 A) and 3 web_deflection on the Part 4 "Online Message Center" lines, which §1.2 allows. The stale-wording sweep for `intent_unclear`, "fresh idempotency key namespace", "the deterministic flow provides", "system_failure line", "nextAction close", "Tax Pro preference" (step 3), "New Appointment", `informational` (intent enum) and "lookup failure" finds no leftovers. Frozen text changed in 3 places: the §1.4 message-available row, which D-039 names; the validation_failed/system_failure Path cell, which follows D-043; and the handoff_invalid row (see L-316). `global_voice_lexicon` and all Agent dialogue lines are unchanged, and no mini-dialogue contradicts the new rules.

L-288 | pass
L-289, L-320 | pass
L-290 | pass
L-239 | pass
L-244, L-298 | pass
L-240 | pass
L-292 | pass
L-291, L-302 | pass
L-241 | pass
L-293, L-294, L-295 | pass
L-296 | pass
L-242, L-315 | pass
L-316 | fix-needed | §1.4 row "handoff_invalid or configuration_missing": replace "call no tools, and" with "never call `transfer_to_agent`, and". Only D-043's rule may change this frozen row, and the JSON mirror says "never call transfer_to_agent".
L-297 | pass
L-243 | fix-needed | office_always[2] covers only a name-resolved office, and no JSON item makes a ZIP-resolved office the routed office. Delete "The resolved office becomes the routed office for the rest of the invocation." from office_always[2]. In office_always[1], replace "capture a 5-digit ZIP code before calling get_office_details." with "capture a 5-digit ZIP code before calling get_office_details; an office resolved from the caller's ZIP or name becomes the routed office for the invocation." ([1] becomes about 55 words.)
L-299 | pass
L-304 | pass
L-238 | pass
L-305 | fix-needed | §3 Office Contact Triage, first bullet: as written, the seasonalStatus check runs only when routedOfficeRef is null. Replace the bullet with: "Before `check_office_open_status`, capture a ZIP if routedOfficeRef is null and check seasonalStatus, as on the office_info path. Evaluate open status only with `check_office_open_status`; never calculate time math."
L-303 | fix-needed | Part 1 outranks Part 3 (C-1), so the §1.2 No-Input Rule and global_always[7] override D-045's robocall exemption. §1.2 Input Exhaustion & Silence, No-Input (Silence) Rule: "On the first silence, reprompt once, except after an office_info answer (see Part 3, Office Details Logic). On the second consecutive silence, never call `transfer_to_agent`; return consecutive_silence (suspected robocall)." global_always[7]: "On the first no-input (silence), reprompt once, except per workflow.office_info_flow step 4. On the second consecutive silence, return consecutive_silence."
L-300 | pass
L-246 | pass
L-310 | pass
L-309 | pass
L-317 | fix-needed | The scheduler_never[2] pointer "per search_knowledge_base" leads to an entry that covers only requires_tax_pro, so the JSON loses how to handle a personal question asked without a KB call. In agent_specific_tools.search_knowledge_base (Scheduler), replace "On requires_tax_pro," with "On requires_tax_pro or a personal advice, calculation, or notice question,". In scheduler_never[2], replace "per search_knowledge_base." with "per agent_specific_tools.search_knowledge_base."
L-306 | fix-needed | No JSON mirror. Append to tax_pro_always[2]: "On one match, name the Tax Pro in the next turn; a caller correction is no_match." (The item becomes about 57 words.)
L-312 | pass
L-307 | pass
L-311 | pass
L-301 | pass
L-308 | pass
L-313 | pass
L-314 | pass
Brevity trims | fix-needed | §5.1 transfer_to_agent: "Call it only on the §1.5 global_always transfer conditions" now excludes the agent-specific extras ("plus an office lookup tool error", "plus third-party or authentication failure"). Replace it with "Call it on the §1.5 global_always transfer conditions and the agent's own transfer_to_agent entry, never on consecutive silence (see §1.2, Input Exhaustion & Silence)." The other trims keep every trigger, limit and exception.
New | §3 Office Details Logic > No Name Match; office_always[2] | Medium | A name no-match after one reprompt transfers as system_failure, but D-044 limits lookup failures to tool errors, and the system_failure outcome means "a tool failed". Choosing between system_failure and clarification_exhausted is Human.
New | global_always followUpTopics item (Part 4 search_knowledge_base) | Medium | In Part 4, requires_tax_pro falls to "any other non-answer returns no_approved_answer", which ends a caller who wants a Tax Pro. D-046 says requires_tax_pro outside the Scheduler hands back to speak_to_tax_pro, and Part 4 is itself that agent. Picking the reading is Human.
New | §2 State 3 Informational Interruptions > Appointment Details; agent_specific_tools.get_customer_appointments | Medium | The read path returns nextAction offer_additional_help with no finalOutcome, so the terminal contract cannot validate. This is already listed in changes.md known gaps and needs a decision (C-7).
New | terminal_payload_contract nextAction capture_intent | Low | No outcome uses capture_intent now that intent_unclear is deleted. This is already listed in known gaps and needs a decision (C-7).
