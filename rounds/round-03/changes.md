L-183 | §4 State 1 intro; §4 State 2 objective | Work Center messaging replaced by leave_message handback; refunds point to global_always | +7
L-187 | §1.5 global_always informational item | "Invalidates nothing" now excepts a gate yes already given | +6
L-188 | §2 Mini-Dialogue 1B, 2B | Replaced preamble with no pending tool call by "Got it" acknowledgment | -6
L-189 | §4 Mini-Dialogue 4A | Deleted Agent turn spoken after the caller's message request | -11
L-207 | §2 State 5 scheduler_always digital drop-off item | Added DDO change request as a new schedule_new DDO send | +10
L-208 | §4 State 2 tax_pro_always callback item | Added new tax_prep goes to appointment_scheduler; callback only for confirmed Tax Pro | +20
L-209 | §3 State 2 office_always OPEN item | Added never speak mainPhoneSpoken | +3
L-211 | §2 State 5 agent_specific_tools.check_search_readiness | Added needs_more asks only the askFor item | +16
L-212 | §1.5 global_always one-question item | Added one-line purpose before a multi-question sequence | +10
L-213 | §2 State 5 closure.principle | Cut to readback-last plus pointer to global_always and global_never | -45
L-214 | §3 State 2 workflow.office_info_flow[2], office_contact_flow[3],[4] | Steps now point to office_always blurb, OPEN, CLOSED items | -16
L-215 | §2 State 5 interruptions.cancel_said, intent_change | Cut rationale clauses and restated close-first rule | -24
L-216 | §2 State 5 workflow.schedule_new[0], reschedule_existing[0], cancel_existing[0] | Cut "resolve identity normally" filler clause | -24
L-217 | §1.5 intro; §2 State 5, §3 State 2, §4 State 2 intros | Merge statement kept once in §1.5; three agent intros deleted | -59
L-218 | §3 agent_specific_tools.get_office_details, check_office_open_status; §4 search_tax_pro_by_name | Entries cut to "Read-only." | -48
L-219 | §2 State 5 scheduler_always gatekeeper and waterfall items | Gatekeeper item tightened; cut default-floor clause | -18
L-220 | §1.5 global_always confirm-at-capture item | DOB/ssnLast4 sentence cut to "are exempt"; frozen lexicon parts skipped | -10
L-221 | §2 State 5 workflow.schedule_new[2]; scheduler_always tax_notice method item | Cut restated notice capture timing and send-all-five clauses | -18
L-222 | §4 State 2 tax_pro_never[1] | Deleted; options item already covers it | -20
L-229 | §3 office_never[4]; §4 tax_pro_never[0] | Leave-message-offer clause now points per global_always | -12
L-224 | §1.2 Confirmation Strategy > Confirmed by consequence | Cut explanation sentence; "never spend a turn" | -10
L-225 | §4 Fulfillment: Leave a Message | Merged Destination Selection into Handoff with §1.3 pointer | -23
L-226 | §3 State 1 intro; §3 Out of Scope | Cut restated scope clause; Out of Scope imperative with routingTarget | -9
L-227 | §2 State 5 agent_specific_outcomes.no_acceptable_availability | Deleted restated never-relax-floor sentence | -11
L-228 | §2 State 5 interruptions.informational_question | Deleted restated void-yes sentence | -15
L-230 | §1.5 base_persona | Last sentence shortened; string now 60 words | -6
L-231 | §4 Out-of-Scope (FAQ Agent) | Triggers compressed to one noun list | -4
L-232 | §5.2 find_available_slots Note; book_appointment Note | Split each note into one bullet per field | 0
L-233 | §1.5 handoff_invalid; scheduler_always entryPoint item; invalidation.customer_identity; §2 State 1 Identity | sessionEnvelope and Head of Call envelope renamed context_envelope | -9
L-234 | §2 scheduler_always floor, third-party text items; global_never unified item; Part 5 Conventions | must/do not to never or send; cut rationale sentence | -7
L-235 | How to Read This Document | Part labels match PART headings; Part 2 body trimmed to fit | +3
L-236 | §4 By Name Request | Four cases nested as sub-bullets | 0
L-222 (follow-up) | §4 State 2 tax_pro_never[1] | Restored yes/no-message ban; dropped repeated options-and-wait sentence | +10
