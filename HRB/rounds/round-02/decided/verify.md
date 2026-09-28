L-129 | pass
L-130 | fix-needed | global_outcomes.transfer_unavailable grew to 96 words (lint NEW length) with "except on outcome_unknown", which global_always transfer-results item and outcome_unknown already state; delete the clause there
L-131 | pass
L-157 | pass
L-158 | pass
L-132 | pass
L-145 | pass
L-147 | fix-needed | §2 State 3 Tax Pro Trade-off bullet grew from 38 to about 45 words (limit 35); move the Peak Capacity trigger into its own bullet or sub-bullet
L-094 | pass
L-133 | pass
L-144 | pass
L-156 | pass
L-166 | pass
L-095 | pass
L-159 | fix-needed | scheduler_always isCDAS item dropped the qualifier "explicitly" ("explicitly requested that specific Tax Pro by name" became "requested that Tax Pro by name"); restore it to match §2 State 3 CDAS phrasing
L-141 | pass
L-096 | pass
L-148 | pass
L-149 | pass
L-069 | pass
L-070 | pass
L-071 | pass
L-073 | pass
L-092 | pass
L-093 | pass
L-076 | pass
L-155 | pass
L-082 | pass
L-083 | pass
L-086 | pass
L-087 | pass
L-088 | pass
L-097 | pass
L-137 | pass
L-138 | pass
L-139 | fix-needed | global_always informational item now tells every agent, including Office Information, to hand hours and phone questions to office_information; §1.2 Hours says "Other agents". Qualify the JSON to match
L-143 | pass

Open point 1 | new issue, not a fix defect | D-015 narrows transferred_to_human to caller_requested, so out_of_scope and automation_blocked have no agent_available outcome. global_outcomes.validation_failed ("A tool rejects...") also overlaps rejected mapped to automation_blocked. Adding or widening an outcome is Human (C-7). Suggest High.
Open point 2 | new issue, not a fix defect | Part 3 office_info_transfer and global system_failure both fit an office lookup failure on agent_available. Merging or removing an outcome is Human. Suggest Medium.
Open point 3 | new issue, not a fix defect | D-024 names only the §2 bullet and the 1A turn. The global_voice_lexicon.reprompt line is frozen (C-8) and still fits the global_always "re-ask only the missing or invalid part" year re-ask at capture. Removing it needs a decision that names it. Suggest Low.
Open point 4 | not a defect, apart from the L-139 qualifier | Splitting the global_always KB item is a style split that keeps every trigger. Deleting the hours hand-back from interruptions.informational_question is a C-3 dedupe, because global_always now carries it per D-025.
New issue | Parts 3-4 unclear intent now returns capture_intent with no finalOutcome, since office_info_transfer lost "Unresolved office intent" and Part 4 names none. Adding an outcome is Human. Suggest Medium.
New issue | A failed transfer call (L-158) returns no supportHoursSpoken, but the "agent_unavailable, no message" row needs it. Suggest Medium, Human.
New issue | §4 No Matches / Inactive and tax_pro_always still return leave_message_offer with no transfer tried and no closed office, outside the D-023 §1.3 triggers. Suggest Medium, Human.

Lint RESULT: WARN (no FAIL; NEW warnings: dup_mirror 4, length 3 incl. global_outcomes.transfer_unavailable 99w, web_deflection 3)
