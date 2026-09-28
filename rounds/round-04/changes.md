L-252 | §2 State 2 Appointment Type Rules > Tax Pro Requests | "A request for" became "A request to speak to" (D-034, JSON mirror); "other than the prior or carried one" became "who is neither prior nor carried" and "hands back" became "returns" to stay at 35 words | +0
L-253 | §2 State 5 workflow.cancel_existing[1] | Added: bound appointment with status canceled returns appointment_already_canceled (D-021, D-028); merged with L-267 | +9
L-254 | §2 State 5 closure.line_patterns (handoff_unavailable) | Added "on a failed transfer call, follow global_always" ahead of the leaveMessageAvailable branches (D-026) | +7
L-255 | §4 State 2 objective | Added the Scheduler route for another Tax Pro when that one is unavailable; cut "15-minute CDAS" | +7
L-256 | §3 State 1 Intent Scope & Disambiguation | Label "unclear_intent" became "**Unclear intent:**" | +1
L-257 | §4 Fulfillment Priority step 4; §4 State 2 workflow.speak_to_tp_generic[4], speak_to_tp_by_name[5] | Return lists now name finalOutcomes routed_to_message, routed_to_scheduler, tax_pro_options_declined | -5
L-258 | §2 State 5 agent_specific_outcomes.no_acceptable_availability | Added none_nearby at the first office lookup (D-015, D-016) | +9
L-259 | §5.2 get_customer_appointments Outcome Results (too_many) | Now "More than three future appointments, active or canceled" (D-028) | +4
L-260 | §1.5 global_never web-deflection item | Ban now matches §1.2: going online, URL, website, portal, or app name; exceptions kept | +1
L-261 | §2 State 5 agent_specific_tools.check_search_readiness | Added conflict branch: speak the past-date line in global_voice_lexicon.empathy (mirrors §1.4 conflict row) | +10
L-262 | §1.5 context_envelope.appointmentType, taxProRef, officeRef; §2 State 5 scheduler_always context-envelope item | Envelope strings gain "outranks entryPoint and routedOfficeRef" (D-027); scheduler_always duplicate cut to "also outranks the prior Tax Pro question" | +5
L-247 | workflow.schedule_new[1]; §2 State 3 Office Resolution > Rollover; scheduler_always rollover item | Carried-context precedence pointers added: "Carried context outranks this step per context_envelope"; rollover exceptions add "officeRef is carried" (prose points to §1.1) (under L-262) | +24
L-263 | §4 Tax Pro Lookup & Disambiguation > No Matches / Inactive; §4 State 2 tax_pro_always unavailable item | "the Appointment Scheduler" / "route to the Appointment Scheduler" became "to book with" | -5
L-264 | §4 Mini-Dialogue 4D | First line relabeled System and shows agent_available result; spoken line relabeled Agent, words unchanged | -1
L-265 | §2 State 5 agent_specific_tools.find_customer, find_offices_near, find_available_slots, book_appointment; workflow.schedule_new[1],[3], reschedule_existing[3] | Deleted pointer-only "Apply/Follow the ... rules" sentences; also cut "per scheduler_always" in schedule_new[1] to keep it under 60 words after L-247 | -70
L-266 | §2 State 5 broadening.principles[6]; §2 State 3 Search Broadening Ladder > Principles | Deleted tool-ranking sentence; JSON drops "never filter CDAS out" (scheduler_never covers filtering), prose keeps "Never filter out CDAS" | -24
L-267 | §2 State 5 workflow.cancel_existing[1] | Retrieval step now points to workflow.reschedule_existing[1], keeping the target-reference and never-guess clauses | -22
L-268 | §4 State 2 workflow.leave_message[0],[1] | Two steps merged into one: return nextAction leave_message with any known taxProRef and officeRef | -20
L-269 | §2 State 5 scheduler_always tax_notice_service capture item | Five values named once, as the taxNoticeDetails keys in capture order | -18
L-270 | §2 State 5 scheduler_always three-sentence readback item; §2 State 4 Chunked Readback | Sentence positions cut to "appointment details, text destination, then the gate question" | -26
L-271 | §2 State 5 workflow.schedule_new[5] | Cut restated payload rules (appointmentType, type-specific capture, customer data, textConfirmation) | -19
L-272 | §1.5 global_always no-input item | Second silence now returns consecutive_silence instead of restating it | -15
L-273 | §4 Mini-Dialogue 4A last System turn | Deleted parenthetical on flow internals | -14
L-274 | §2 State 5 scheduler_always office identity item | Pre-commit phase list became "Until the post-commit readback"; cut "for spoken office identity" | -14
L-275 | §2 State 5 scheduler_always reschedule changing item | Four "if ... differs" clauses became one field list | -12
L-276 | §5.2 find_customer intro; Note | Intro now "Read-only." once; Note drops the active/inactive enum (in Part 5 Conventions) | -13
L-277 | §2 State 5 closure.continuation_context | Cut "It is context only" and the identity-change discard (context_envelope.priorTransaction, invalidation.customer_identity) | -12
L-278 | §5.3 check_office_open_status intro | Cut the list of tool inputs | -14
L-279 | §1.5 global_never message item | Cut ownership sentence | -11
L-280 | §1.5 Universal Base JSON Prompt intro | Cut sentence listing the block's contents | -11
L-281 | §2 State 2 DDO Rules > Rescheduling; Complexity Matching > Guardrails | Cut duplicate "DDO has no calendar slot", "in the Scheduler", and the "internal mandatory filter" clause | -14
L-282 | §2 State 5 scheduler_never profile item | Phase list became "Only book_appointment or send_secure_link may create a new-customer profile, at commit" | -13
L-283 | §5.2 book_appointment intro | Cut "point of no return" sentence | -10
L-284 | §2 State 3 Search Broadening Ladder intro | One-constraint restatement became "Each scenario has a fixed broadening order" | -9
L-285 | §2 State 5 workflow.reschedule_existing[2] | Cut first of two type/method bar statements | -9
L-286 | §2 State 5 scheduler_always isCDAS item | Two conditionals merged into one CDAS definition | -7
L-287 | §2 State 5 closure.re_entry | Cut one-transaction restatement (objective holds it) | -7
L-245 | §3 Office Contact Triage > If OPEN; §3 State 2 office_always OPEN item | Now return office_open_unanswered with nextAction leave_message_offer (D-031) | +3
L-249 | §1.5 global_outcomes.validation_failed | Excludes change_not_allowed and not_cancelable as well as rejected (D-015) | +3
L-250 | §2 State 3 Informational Interruptions > Personal Questions | Added "and resume" to match agent_specific_tools.search_knowledge_base | +2
L-254 (follow-up) | closure.line_patterns.handoff_unavailable | Failed-call clause now precedes and excludes the agent_unavailable branches | +3
L-266 (follow-up) | §2 State 3 Search Broadening Ladder > Principles | Restored "The tool ranks named Tax Pros ahead of CDAS" in prose | +8
L-274 (follow-up) | scheduler_always office identity item | "Until the post-commit readback" became "Outside the post-commit readback and terminal outcome" | +3
