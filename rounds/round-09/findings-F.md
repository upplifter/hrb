# Round 9 · Lens F findings

Saved by the orchestrator from the reviewer's reply.

### F-01 · Write-tool entries repeat the explicit-yes rule
Anchor: §2 State 5 agent_specific_tools.book_appointment, .reschedule_appointment, .cancel_appointment, .send_secure_link
Severity: Low
Class: Safe
Issue: scheduler_always already says "Require an explicit spoken yes immediately before any write, including send_secure_link." All four write-tool entries repeat "and an explicit yes". Net -16 words.
Fix: Delete " and an explicit yes" / ", and an explicit yes" from the four entries.

### F-02 · get_customer_appointments results repeat "active or canceled" and the too_many transfer
Anchor: §5.2 get_customer_appointments > Outcome Results; Note after Response JSON
Severity: Low
Class: Safe
Issue: Every row says "active or canceled"; too_many repeats the Cognitive Overload transfer stated above. Net -11 words.
Fix: Drop "active or canceled" from the four rows and the transfer sentence from too_many; Note: "status is active or canceled; " becomes "status is active or canceled, and every result counts both; ".

### F-03 · §2 State 1 restates the third-party name readback that D-086 put in §1.2
Anchor: §2 State 1 Authentication Logic > Third-Party
Severity: Low
Class: Safe
Issue: D-086 made §1.2 Confirmed at capture the home. Net -6 words.
Fix: Delete " Confirm the owner's name at capture."

### F-04 · After Part 4 still points to the callback row for the reason capture
Anchor: §2 State 2 Appointment Type Rules > After Part 4 (first sub-bullet)
Severity: Low
Class: Human (oscillation guard)
Fix: Delete ", with the reason as on callback" (-6 words).

### F-05 · §4 Generic Request bullet is over 35 words
Anchor: §4 Tax Pro Lookup & Disambiguation > Generic Request
Severity: Low
Class: Human (oscillation guard)
Fix: "state the prior Tax Pro's options" becomes "state the options" (-3 words).

### F-06 · By-name workflow step uses the vague "if needed"
Anchor: §4 State 2 workflow.speak_to_tp_by_name[3]
Severity: Low
Class: Safe
Fix: "4. Disambiguate by location if needed." becomes "4. Disambiguate multiple matches by location."

### F-07 · Returning Client bullet is over 35 words
Anchor: §2 State 2 Complexity Matching & Tax Pro Rating Floor > Returning Client
Severity: Low
Class: Safe
Fix: Split the outcome branch into a sub-bullet: "If No, use baseline; if Yes, or currentDateTime's year minus lastFiledYear exceeds 2, run the waterfall."

### F-08 · Three terms for the out-of-task logistics category after D-097
Anchor: §1.2 Tax/Financial Boundary sub-bullet; §2 State 3 Informational Interruptions > Hand back; global_always informational item
Severity: Low
Class: Human (oscillation guard on §1.2)
Fix: Use "out-of-task appointments_and_logistics questions" in both prose places.

### F-09 · office_never still sends every appointment question to appointment_scheduler
Anchor: §3 State 2 office_never[0]
Severity: Medium
Class: Safe
Issue: Same as E-01.

Summary: 9 findings (0 Critical, 0 High, 1 Medium, 8 Low).
