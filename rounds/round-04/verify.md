# Round 04 verification

Diff checked: `git diff 60b01a1 cb2c45d -- HRB_IVA_Agents_Spec.md`. Lint: `python tools/lint.py check` gives RESULT WARN, with no FAIL, and the JSON is valid. The new WARNs are dup_mirror pairs, which C-2 A allows (L-260 now mirrors §1.2 on purpose), and web_deflection hits on the D-006 Online Message Center lines, which only moved. Frozen text is untouched. In 4D, the Agent line keeps its words and only its label changed.

L-245 | pass
L-247 | pass
L-249 | pass
L-250 | pass
L-252 | pass
L-253 | pass
L-254 | fix-needed | In `§2 State 5 closure.line_patterns`, replace "handoff_unavailable: mention no person; on a failed transfer call, follow global_always; when leaveMessageAvailable is true," with "handoff_unavailable: on a failed transfer call, follow global_always only. On agent_unavailable, mention no person; when leaveMessageAvailable is true,". As written, a failed call (no leaveMessageAvailable) still falls into "otherwise speak supportHoursSpoken", and "mention no person" contradicts the system_failure line that global_always speaks.
L-255 | pass
L-256 | pass
L-257 | pass
L-258 | pass
L-259 | pass
L-260 | pass
L-261 | pass
L-262 | pass
L-263 | pass
L-264 | pass
L-265 | pass
L-266 | fix-needed | In §2 State 3 Search Broadening Ladder > Principles, restore the ranking clause: "Present at most three slots per turn, in the order they're returned. The tool ranks named Tax Pros ahead of CDAS; never filter out CDAS." Deleting it from both prose and JSON removes the only statement of the ranking order, since §5.2 find_available_slots says only "already ranked". The JSON deletion of "never filter CDAS out" is fine, because `scheduler_never` "Never re-order, re-rank, promote, or filter returned slots" covers it.
L-267 | pass
L-268 | pass
L-269 | pass
L-270 | pass
L-271 | pass
L-272 | pass
L-273 | pass
L-274 | fix-needed | In `§2 State 5 scheduler_always` office identity item, replace "Until the post-commit readback," with "Outside the post-commit readback and terminal outcome,". "Until the post-commit readback" also covers terminal outcomes with no commit (e.g., appointment_already_canceled, customer_declined_options), which the next sentence sends to addressLine1Spoken, so there are two readings. The original phase list excluded terminal outcomes.
L-275 | pass
L-276 | pass
L-277 | pass
L-278 | pass
L-279 | pass
L-280 | pass
L-281 | pass
L-282 | pass
L-283 | pass
L-284 | pass
L-285 | pass
L-286 | pass
L-287 | pass

Judgment calls:
- L-266: removing "never filter CDAS out" from the JSON is accepted, because `scheduler_never` bans filtering. The prose ranking sentence was also removed, and that needs a fix (see above).
- L-261: pointing the conflict branch to the past-date line in `global_voice_lexicon.empathy` is accepted. It mirrors the §1.4 "conflict from readiness" row exactly, and that line already asks for the next day, so dropping E-09's "re-ask the date" loses nothing. The question of non-date conflicts stays with L-146 (Human).

## New issues

- None at Medium or higher beyond the three fix-needed items above. L-254 and L-274 would each be Medium (implementer must guess) if left as written.
