# Ledger

Status values: open, fixed, asked, decided, deferred, rejected, backlog, reverted.

| ID | Lens | Anchor | Sev | Class | Status | Round | Summary |
|---|---|---|---|---|---|---|---|
| L-001 | E,S | §1.5 global_outcomes.customer_abandoned | High | Safe | fixed | 1 | JSON says an unanswered gate transfers; §1.2 Abandonment says it terminates (F-10). |
| L-002 | E,F | §1.5 global_always (transfer_to_agent item); agent_specific_tools.transfer_to_agent and interruptions.intent_change in Parts 2-4 | High | Safe | fixed | 1 | Base JSON limits transfer_to_agent to system-initiated escalations while §1.4 calls it on barging; barging sentences repeat in all three agent blocks (C-3 A). |
| L-003 | E | §1.5 global_outcomes.transfer_unavailable | Medium | Safe | fixed | 1 | JSON says state only the unavailable outcome; §1.4 no-message line and closure.line_patterns speak support hours and invite a call back. |
| L-004 | E,B | §2 State 5 workflow.schedule_new[1]; scheduler_always rollover item; §2 State 3 Office Resolution > Rollover | Medium | Safe | fixed | 1 | Rollover office is proposed even in the returning same-Tax-Pro scenario, against the §1.1 entryPoint exception. |
| L-005 | E | §2 State 5 workflow.reschedule_existing[2] | Medium | Safe | fixed | 1 | JSON omits the State 2 rule that type is immutable on reschedule and a type change transfers. |
| L-006 | D | §2 State 4 The Pre-Commit Gate (correction bullet); scheduler_always mid-gate correction item | Medium | Safe | fixed | 1 | Mid-gate correction re-searches without readiness, against "find_available_slots only on ready". |
| L-007 | C | §2 State 3 Readiness & Availability > CDAS; scheduler_always CDAS item | Medium | Safe | fixed | 1 | CDAS exception calls physical drop-off an appointment type; it is the method token physical_drop_off. |
| L-008 | C | §2 State 5 broadening.ladders.tax_notice.rungs[3] | Medium | Safe | fixed | 1 | Fourth tax_notice rung lacks the any_qualified_tax_pro rung token. |
| L-009 | A,B | §3 State 2 agent_specific_tools.transfer_to_agent; §4 State 2 agent_specific_tools.transfer_to_agent | Low | Safe | fixed | 1 | Local trigger lists read as exhaustive; Tax Pro entry names an indeterminate write it cannot make. |
| L-010 | B | §4 State 2 tax_pro_never (tax advice item) | Low | Safe | fixed | 1 | Narrower duplicate of the global_never tax-advice rule (C-3 A). |
| L-011 | F | §2 State 5 workflow.* (office identity clauses); cancel_existing[5],[6] | Low | Safe | fixed | 1 | Office-identity rule restated in about 20 workflow clauses; cancel steps 6-7 restate global rules. |
| L-012 | F | §2 State 5 agent_specific_tools (six scheduling tools) | Low | Safe | fixed | 1 | Six tool entries restate the officeName vs spoken-address rule. |
| L-013 | F | §2 State 5 workflow.*[0] | Low | Safe | fixed | 1 | Each workflow step 1 restates the scheduler_always authentication rule. |
| L-014 | F | §3 Office Contact Triage; §4 workflow.leave_message[1]; Part 5 tool intros | Low | Safe | fixed | 1 | Reason clauses ("so the...", "because...") explain why, against editorial rule 5. |
| L-015 | F | §2 State 5 workflow.schedule_new[1] | Low | Safe | fixed | 1 | 152-word step restates type-first, rollover, central-line, and eligibility rules. |
| L-016 | F | §2 State 5 workflow write steps; scheduler_always idempotency item; agent_specific_tools.reschedule_appointment | Low | Safe | fixed | 1 | No-retry and no-cancel-and-recreate rules restated five times. |
| L-017 | F | §2 State 5 scheduler_always rejected-rollover item; invalidation.rejected_rollover_office | Low | Safe | fixed | 1 | Rejected-rollover purge rule appears three times. |
| L-018 | F | §4 State 2 tax_pro_never[2],[3]; §2 State 5 agent_specific_tools.transfer_to_agent | Low | Safe | fixed | 1 | Agent-block rules repeat Base JSON rules (C-3 A). |
| L-019 | F | §2 State 5 workflow step 5 (x2); invalidation.text_confirmation | Low | Safe | fixed | 1 | Third-party text-destination rule restated three times. |
| L-020 | F | How to Read This Document | Low | Safe | fixed | 1 | Part 4 bullet restates §1.3; Part 1, 2, 4 bullets over length. |
| L-021 | F | §2 State 5 objective | Low | Safe | fixed | 1 | Objective restates type-first and gate rules. |
| L-022 | F | §2 State 5 scheduler_always complexity and tax_notice items | Low | Safe | fixed | 1 | Type exceptions and grouped-readback clause repeated; waterfall item 108 words. |
| L-023 | F | §5.1 transfer_to_agent | Low | Safe | fixed | 1 | Tool intro restates the §1.2 silence rule; all-caps "AND". |
| L-024 | F | §5.1 search_knowledge_base | Low | Safe | fixed | 1 | Intro paragraph runs 5 sentences and repeats the 0.85 rule. |
| L-025 | F | §1.1 The Head of Call Envelope | Low | Safe | fixed | 1 | Table cells open with empty category labels. |
| L-026 | F | §1.2 (five bullets) | Low | Safe | fixed | 1 | Bullets over 2 sentences or 35 words; filler words. |
| L-027 | F | §2 State 2 bullets | Low | Safe | fixed | 1 | Bullets over 2 sentences; redundant label. |
| L-028 | F | §2 State 3 Readiness & Availability; Principles; §2 State 4 Write Tools | Low | Safe | fixed | 1 | Bullets over 2 sentences. |
| L-029 | F | §4 Elicit the Reason First; scheduler_always CDAS and trade-off items; other "must" phrasing | Low | Safe | fixed | 1 | Third-person or "you must" phrasing instead of the imperative. |
| L-030 | F | Part 5 Conventions Common to Every Tool | Low | Safe | fixed | 1 | 114-word alias paragraph is a wall of text. |
| L-031 | F | §1.3 Leave-a-Message Ownership | Low | Safe | fixed | 1 | 104-word, 5-sentence paragraph. |
| L-032 | F | §1.5 global_always[6]; scheduler_always items over 60 words | Low | Safe | fixed | 1 | JSON array items over 60 words. |
| L-033 | F | §2-4 interruptions.informational_question | Low | Safe | fixed | 1 | Shared informational_question rule could move to Base JSON; waits on Q-11. |
| L-034 | F | §1.5 terminal_payload_contract; closure strings; transfer_unavailable | Low | Human | backlog | 1 | JSON strings over 60 words need a string-to-array restructure. |
| L-035 | B | §3 Mini-Dialogue 3B; §2 Mini-Dialogue 1B | Low | Human | backlog | 1 | Frozen Agent turns run three sentences. |
| L-036 | A,S,C | §2 State 5 objective; agent_specific_outcomes; §5.2 send_secure_link | Critical | Human | fixed | 1 | DDO write sits outside the objective, has no outcome, no idempotency key, and no new-customer path (F-01). |
| L-037 | D,S | §2 State 2 DDO Rules; scheduler_always explicit-yes item | High | Human | fixed | 1 | Unclear whether send_secure_link needs the pre-commit readback and explicit yes (F-02). |
| L-038 | D,C | §5.2 send_secure_link Outcome Results; workflow.schedule_new[5] | Medium | Human | fixed | 1 | delivery_failed has no handling. |
| L-039 | A,C,S | §2 State 5 agent_specific_tools.find_available_cdas_slots; §5.2 check_search_readiness note | High | Human | fixed | 1 | Two tools own callback slot search; no workflow step calls find_available_cdas_slots (F-03). |
| L-040 | D,S | §2 State 5 broadening.scenario_selection | High | Human | fixed | 1 | No callback scenario; callback falls to new_client with DDO and nearby-office rungs (F-04). |
| L-041 | E | §5.2 check_search_readiness note | Medium | Human | fixed | 1 | Callback may send a null method and floor, against phone_callback and the mandatory floor. |
| L-042 | C | §2 State 3 Readiness & Availability > CDAS | Medium | Human | fixed | 1 | "CDAS" names both the callback type and any unnamed-Tax-Pro slot. |
| L-043 | A,S | §4 State 2 tax_pro_always callback item; §1.5 terminal_payload_contract | High | Human | fixed | 1 | Callback handoff carries appointmentType and Tax Pro context the contract and envelope do not define (F-05). |
| L-044 | A,S,E | §4 State 2 agent_specific_outcomes.routed_to_message | Medium | Human | fixed | 1 | Outcome fires on "no callback slots" though the agent cannot search slots (F-17). |
| L-045 | A | §4 Tax Pro Lookup & Disambiguation > No Matches / Inactive | Medium | Human | fixed | 1 | Route to the Scheduler for another Tax Pro has no type or outcome. |
| L-046 | C | §1.5 terminal_payload_contract | High | Human | fixed | 1 | Outcomes carry fields (appointmentType, appointmentRef, transferReason, supportHoursSpoken, sourceUtterance) the contract never lists. |
| L-047 | C | §1.5 global_outcomes | Medium | Human | fixed | 1 | Several outcomes omit mandatory transactionOccurred, callContained, or intent values. |
| L-048 | C | §1.5 global_outcomes.transfer_unavailable; Part 3-4 outcomes | Medium | Human | fixed | 1 | callContained is undefined and takes opposite values for the same handback. |
| L-049 | C | §5.1 transfer_to_agent transferReason; §1.5 global_outcomes.system_failure | Medium | Human | fixed | 1 | transferReason has no enum; "transfer default" is undefined. |
| L-050 | S,B | §4 State 2 tax_pro_always MyBlock item; §4 Fulfillment Priority; 4A, 4E | High | Human | fixed | 1 | Part 4 must speak an app name that §1.2 forbids (F-06). |
| L-051 | D | §1.5 global_outcomes.outcome_unknown; §2 State 4 Indeterminate Writes | High | Human | fixed | 1 | outcome_unknown hands back at once, but the approved line promises a person, which requires transfer_to_agent first. |
| L-052 | D | §2 State 5 invalidation.ladder_state | High | Human | fixed | 1 | Accepting a time, date, office, or Tax Pro rung resets the ladder, making ladders cyclic. |
| L-053 | D | §2 State 5 agent_specific_outcomes.no_acceptable_availability; customer_declined_options | Medium | Human | fixed | 1 | Declining every rung matches both a contained close and a transfer. |
| L-054 | D | §2 State 5 broadening.scenario_selection item 7 | High | Human | fixed | 1 | peak_capacity override offers virtual and DDO to emerald_advance and reschedule. |
| L-055 | C | §1.5 context_envelope.entryPoint; Parts 3-4 routedOfficeRef uses | High | Human | fixed | 1 | Office Information and Tax Pro agents need routedOfficeRef, but only the Scheduler's find_offices_near resolves it. |
| L-056 | A | §3 State 2 workflow.office_info_flow; §5.3 get_office_details | Medium | Human | fixed | 1 | A caller-named office cannot be resolved; get_office_details takes only officeRef or postalCode. |
| L-057 | A,C | §1.5 terminal_payload_contract routingTarget | Medium | Human | fixed | 1 | routingTarget lists tax_prep and "named destination" and lacks the Office Information and Tax Pro agents. |
| L-058 | A,D,C | §2 State 5 broadening.scenario_selection item 1; §5.2 check_search_readiness out_of_scope | Medium | Human | fixed | 1 | Specialized services hand back with no routingTarget, and readiness out_of_scope has no handler. |
| L-059 | A,S | §2 State 5 broadening.ladders.extension | Medium | Human | fixed | 1 | Self-filing support transfer has no owner, and the tax_prep follow-up uses intent_changed inside Scheduler scope (F-20). |
| L-060 | C | §1.5 global_outcomes.appointment_requested | Medium | Human | fixed | 1 | No rule emits appointment_requested; it overlaps intent_changed. |
| L-061 | A,S,E | §4 Out-of-Scope (FAQ Agent); interruptions.informational_question x3 | Medium | Human | fixed | 1 | FAQ-scope questions are both answered in-agent via search_knowledge_base and routed to faq_agent (F-08). |
| L-062 | A,S | §1.2 Hours: One Source, Spoken Once | Medium | Human | fixed | 1 | The hours source is unnamed; the Scheduler may answer office hours from the KB (F-09). |
| L-063 | S | §3 State 2 agent_specific_tools.search_knowledge_base | Medium | Human | fixed | 1 | Office Information may query every KB category (F-18). |
| L-064 | S | §2 and §3 interruptions.intent_change | Medium | Human | fixed | 1 | Only Part 4 routes refund status to refund_status (F-22). |
| L-065 | A | §1.4 Caller-Initiated Barging; agent transfer_to_agent entries | Medium | Human | fixed | 1 | Live-agent requests are handled in-agent while the Request Live Agent flow may claim them. |
| L-066 | E | §1.4 Caller-Initiated Barging row | Medium | Human | fixed | 1 | Frozen barging row has the agent state hours and offer a message on agent_unavailable; the adjacent row gives both to the flow. |
| L-067 | S | §3 State 2 office_never; §1.4 Barging row | Medium | Human | fixed | 1 | Part 3 lacks Part 4's no-live-transfer-to-local-desk rule; "local office contact" is undefined (F-07). |
| L-068 | S | §3 State 2 agent_specific_tools.transfer_to_agent | Medium | Human | fixed | 1 | Part 3 transfer entry has no knownSoFar mapping (F-19). |
| L-069 | S | §1.5 terminal_payload_contract nextAction capture_intent | Medium | Human | decided | 1 | capture_intent is never defined and overlaps the additional-help question (F-21). |
| L-070 | S | §1.5 terminal_payload_contract "Resolve unclear_intent" | Medium | Human | decided | 1 | unclear_intent has no owner or enum value; Parts 3-4 resolve it differently (F-12). |
| L-071 | D,B,E | §3 Intent Scope > unclear_intent; §3 transfer_to_agent | Medium | Human | decided | 1 | Unresolved intent may transfer or go to a message, with no rule to choose. |
| L-072 | D,S | §2 State 5 broadening.scenario_selection (timing) | Medium | Human | fixed | 1 | Selection runs after ready, but drop-off, DDO, and same-Tax-Pro choices come earlier (F-24). |
| L-073 | D,S | §2 State 5 scheduler_always tool-result item (not_confirmed) | Medium | Human | decided | 1 | Re-gate on not_confirmed has no cap or exit (F-27). |
| L-074 | D,E | §2 State 5 invalidation.partial_acceptance; §2 State 3 Tax Pro Trade-off | Medium | Human | decided | 1 | Trade-off asked outside the rung that drops the Tax Pro. |
| L-075 | S | §2 State 5 scheduler_always efile_rejection_retail item | Medium | Human | decided | 1 | efile entry does not say whether to ask the type; trade-off outside a ladder step (F-28). |
| L-076 | D | §2 State 5 interruptions.informational_question | Medium | Human | decided | 1 | A pre-interruption yes survives, against "explicit yes immediately before any write". |
| L-077 | D,S | §1.5 global_never (post-handback tool calls) | Medium | Human | backlog | 1 | No rule says which tools stay callable after a commit or handback decision (F-11). |
| L-078 | E,S | §3 Cross-Office Restriction; office_never direct-number item | Medium | Human | fixed | 1 | Direct-number scope names two referents (F-26). |
| L-079 | S | §3 office_always closed_for_season; §2 State 3 Off-Season Closure | Medium | Human | backlog | 1 | Two agents propose a Year-Round Office from two tools (F-15). |
| L-080 | B | §3 Office Details Logic > Off-Season Closure; §1.4 Off-season row | Medium | Human | decided | 1 | Office Information speaks the YRO address; the frozen line names officeName and asks a booking question. |
| L-081 | A,S | §3 Office Details Logic > By-Appointment-Only | Medium | Human | fixed | 1 | Routes to the Scheduler without a booking request and has no route_intent outcome (F-25). |
| L-082 | S,B | §3 Office Contact Triage > If CLOSED; leave_message_offer triggers | Medium | Human | decided | 1 | leave_message_offer is returned where no transfer was tried (F-13). |
| L-083 | B | §4 Fulfillment Priority step 1; 4A | Medium | Human | decided | 1 | Part 4 speaks the message offer that §1.3 gives to the flow. |
| L-084 | A,S | §4 State 2 tax_pro_always; agent_specific_tools.find_customer | Medium | Human | fixed | 1 | Part 4 authenticates without the Scheduler's capture and result handling (F-16). |
| L-085 | B | §4 State 2 workflow.speak_to_tp_generic[2] | Medium | Human | fixed | 1 | Part 4 re-runs find_customer despite an envelope customerRef. |
| L-086 | B | §2 State 1 New Customer DOB Check | Medium | Human | decided | 1 | DOB year repair turn vs "DOB never receives a confirmation turn". |
| L-087 | E,B | §1.2 Data Sanitization; §5.2 book_appointment newCustomer | Medium | Human | decided | 1 | PII exception names only find_customer; book_appointment also carries DOB and ssnLast4. |
| L-088 | E | §1.5 global_never tax-advice item | Medium | Human | decided | 1 | Base JSON omits the §1.2 bans on notices, loan terms, fees, and penalties. |
| L-089 | E | §1.5 global_voice_lexicon vs §1.4 | Medium | Human | decided | 1 | Several §1.4 approved lines have no JSON copy under C-2 mirror. |
| L-090 | S | §2 State 5 scheduler_always callback item | Medium | Human | fixed | 1 | appointmentNotes capture vs "never capture message content" (F-14). |
| L-091 | S | §2 State 5 objective; returning_tax_pro_unavailable regional rung | Medium | Human | backlog | 1 | Regional virtual rung has no office anchor (F-23). |
| L-092 | C | §2 State 5 agent_specific_outcomes.appointment_already_canceled | Medium | Human | decided | 1 | No tool result can trigger appointment_already_canceled. |
| L-093 | C | §5.2 reschedule_appointment Outcome Results | Medium | Human | decided | 1 | No not_confirmed or rejected result, though the Scheduler handles both. |
| L-094 | verify | §2 State 5 scheduler_never (new-customer profile item); §5.2 send_secure_link newCustomer | High | Human | decided | 1 | After D-001, send_secure_link accepts newCustomer, but scheduler_never says only book_appointment may create a new-customer profile. |
| L-095 | verify | §1.1 The Head of Call Envelope; §1.5 context_envelope; broadening.ladders.callback | High | Human | decided | 1 | After D-004, route_intent carries taxProRef and officeRef, but the envelope has no field to receive them. |
| L-096 | verify | §2 State 5 broadening.ladders.extension (tax_prep follow-up) | Medium | Human | decided | 1 | After D-011, the post-extension route_intent to appointment_scheduler names no finalOutcome. |
| L-097 | verify | §2 State 5 scheduler_never (loan, fee, penalty item); §1.2 Tax/Financial Boundary | Medium | Human | decided | 1 | After D-012, financial-product questions still go to search_knowledge_base, which now serves only two categories; no handback target. |
| L-098 | E | §2 State 5 invalidation.upstream_change | Medium | Human | fixed | 2 | JSON omits the prose floor re-derivation on a type or method change and the channel-rung readiness skip. |
| L-099 | E | §1.5 global_outcomes.configuration_missing | Medium | Safe | fixed | 2 | JSON implies a caller-facing line; §1.4 gives configuration_missing none. |
| L-100 | E | §1.5 global_never (web deflection item) | Low | Safe | fixed | 2 | Online Message Center exception granted to every agent; §1.2 limits it to Part 4. |
| L-101 | C | §1.5 global_outcomes.transferred_to_human | Low | Safe | fixed | 2 | "IVR call summary" is a second term for interactionSummary. |
| L-102 | C | §5.2 get_customer_appointments Response JSON note | Low | Safe | fixed | 2 | "Internal only" note names no field. |
| L-103 | B,F | Parts 2-4 agent_specific_tools.search_knowledge_base | Low | Safe | fixed | 2 | Three identical entries restate global_always and read broader than D-012. |
| L-104 | E | §4 Mini-Dialogue 4C | Low | Safe | fixed | 2 | 4C options turn omits the Online Message Center line the rule requires (C-9). |
| L-105 | F | §2 State 5 scheduler_never slot-order item; workflow.schedule_new[3], reschedule_existing[3] | Low | Safe | fixed | 2 | Restate broadening.principles consent and floor rules. |
| L-106 | F | §4 Fulfillment Handoff bullets; Generic Request | Low | Safe | fixed | 2 | Restate §1.3; third-person opener. |
| L-107 | F | §3 State 2 objective; office_always[0]; interruptions.intent_change | Low | Safe | fixed | 2 | Restate office_always, global_never, and intent_changed. |
| L-108 | F | §2 State 5 broadening.principles; global_never prohibited-phrases item | Low | Safe | fixed | 2 | Repeated relaxation, prohibited-phrase, and method-description rules. |
| L-109 | F | §5.1 search_knowledge_base intro | Low | Safe | fixed | 2 | Intro restates the KB results line. |
| L-110 | F | §2 State 5 scheduler_always post-commit readback item | Low | Safe | fixed | 2 | Restates global_always final-turn rule (C-3 A). |
| L-111 | F | §2 State 1 Authentication Logic > State Persistence | Low | Safe | fixed | 2 | Restates §1.1 customerRef rule. |
| L-112 | F | §5.2 reschedule_appointment Note and Changing Array | Low | Safe | fixed | 2 | Two descriptions of one field. |
| L-113 | F | §2 State 5 scheduler_always emerald_advance, tax_notice_service, callback items | Low | Safe | fixed | 2 | Skip-waterfall and floor-1 clause stated three times. |
| L-114 | F | §5.2 check_search_readiness Note; §5.1 transfer_to_agent intro; Part 5 Conventions; §5.2 get_customer_appointments | Low | Safe | fixed | 2 | Wall of text and over-length bullets. |
| L-115 | F | PART 5 intro | Low | Safe | fixed | 2 | 42-word intro. |
| L-116 | F | §2 State 5 objective (last sentence) | Low | Safe | fixed | 2 | Restates base_persona. |
| L-117 | F | §2 State 5 scheduler_never DOB item | Low | Safe | fixed | 2 | Restates global_never DOB ban (C-3 A). |
| L-118 | F | §2 State 5 agent_specific_tools.find_available_slots | Low | Safe | fixed | 2 | Restates duration rule and scenario_selection item 7. |
| L-119 | F | §5.2 find_available_slots > Any-One-Of Matching | Low | Safe | fixed | 2 | Three sentences; "either" narrows the set. |
| L-120 | F | §4 Intent Scope out-of-scope bullets; "Tax Professional" in rules | Low | Safe | fixed | 2 | Padded handback phrasing; term drift. |
| L-121 | F | §1.1 Envelope priorTransaction, entryReason, registeredAni | Low | Safe | fixed | 2 | Over-length cells; "3rd-party". |
| L-122 | F | §1.5 base_persona | Low | Safe | fixed | 2 | Restates global_always[0] and turn_length. |
| L-123 | F | §2 State 5 invalidation.rejected_rollover_office | Low | Safe | fixed | 2 | Restates central-line item. |
| L-124 | F | §1.3 The Audio Seam & Terminal Handbacks intro | Low | Safe | fixed | 2 | Restates Yield bullets. |
| L-125 | F | §4 State 2 tax_pro_always[2],[3]; interruptions.intent_change | Low | Safe | fixed | 2 | Duplicate disambiguation item; needless close clause. |
| L-126 | F | §1.2 Confirmation Strategy > Exceptions (DOB & SSN) | Low | Safe | fixed | 2 | Restates Zero Readback bullet. |
| L-127 | F | §2 State 2 Tax Notice Services Guardrails > Notice Capture Sequence | Low | Safe | fixed | 2 | Restates §1.2 grouped capture. |
| L-128 | F | §1.2 Voice Persona jargon bullet; Spoken Office Identity Fallback; §2 State 1 bullets; §2 State 2 tax_prep row | Low | Safe | fixed | 2 | Over-length bullets and cells. |
| L-129 | B,E | §2 State 1 Authentication Logic (failure bullet); scheduler_always unregistered ANI item; §1.4 recovery rows | High | Human | decided | 2 | Recovery line promising a person is spoken before transfer_to_agent, against global_always. |
| L-130 | C,D | §1.5 global_outcomes transfer-reason outcomes vs transferred_to_human, transfer_unavailable | High | Human | decided | 2 | One transfer matches two finalOutcomes; reason outcomes have no agent_unavailable path. |
| L-131 | C | §1.5 global_outcomes.outcome_unknown | High | Human | decided | 2 | callContained false on a message handback, against the D-005 definition. |
| L-132 | D | §2 State 3 Dynamic State Invalidation: Location & Time; invalidation.upstream_change | High | Human | decided | 2 | Location change purges the Tax Pro, but the same_tax_pro_nearby_offices rung must keep it. |
| L-133 | E | §2 State 5 scheduler_always tax_notice DDO item; §5.2 send_secure_link | High | Human | decided | 2 | Five notice values must be sent on DDO, but send_secure_link has no field for them. |
| L-134 | A,C,E | §5.2 find_offices_near; §1.1 routedOfficeRef | Medium | Human | backlog | 2 | After D-010, find_offices_near still resolves DNIS and returns invalid_dnis. |
| L-135 | A | §1.1 customerRef, customerStatus; §2 State 1 State Persistence | Medium | Human | fixed | 2 | Unclear whether Head of Call authentication skips find_customer. |
| L-136 | A | §2 State 5 objective; §1.1 operation | Medium | Human | rejected | 2 | Confirm Appointment routes to the Scheduler, which has no confirm operation. |
| L-137 | A,C,E | §5.1 search_knowledge_base KB results; global_outcomes.no_approved_answer | Medium | Human | decided | 2 | requires_tax_pro and below-threshold results have no handler or outcome. |
| L-138 | B,E | §1.5 global_always KB item; §5.1 search_knowledge_base | Medium | Human | decided | 2 | Base ignores followUpTopics; Part 5 builds clarification from them. |
| L-139 | A | §1.2 Hours: One Source; Part 4 tools | Medium | Human | decided | 2 | Tax Pro agent has no owner for hours and phone questions after D-012. |
| L-140 | A | §4 Speak to Tax Pro (Generic); §3 office_contact | Medium | Human | decided | 2 | "Office associate" requests have two owners. |
| L-141 | A | §4 Out-of-Scope (New Appointment); Fulfillment Priority step 4 | Medium | Human | decided | 2 | Phone tax_prep request fits both new appointment and callback route. |
| L-142 | A,D | §4 Tax Pro Lookup > Generic Request; workflow.speak_to_tp_generic | Medium | Human | fixed | 2 | No path when the caller has no or an inactive prior Tax Pro. |
| L-143 | A | §4 Out-of-Scope (FAQ Agent); global_always informational item | Medium | Human | decided | 2 | Income tax course and password questions have no target outside Part 4. |
| L-144 | A | §2 State 2 DDO Rules > Rescheduling | Medium | Human | decided | 2 | DDO change "in a separate invocation" has no owner or operation. |
| L-145 | D | §2 State 5 scheduler_always none_nearby; broadening.principles | Medium | Human | decided | 2 | none_nearby on a nearby-office rung transfers instead of exhausting the rung. |
| L-146 | B,D | §1.4 conflict from readiness; §5.2 check_search_readiness conflict | Medium | Human | decided | 2 | Conflict line covers only a past date; closed filing windows have no signal. |
| L-147 | D | §2 State 5 scenario_selection item 7; peak_capacity.primary | Medium | Human | decided | 2 | Peak switch from returning_same_tax_pro drops the kept Tax Pro without consent. |
| L-148 | D,E | §2 State 5 broadening.ladders.extension; scheduler_always tax_extension item; §2 State 2 Tax Extension | Medium | Human | decided | 2 | Self-filing rung exits undefined; JSON and prose tie route_intent to different paths. |
| L-149 | B | §2 State 5 broadening.ladders.extension rung 2 | Medium | Human | decided | 2 | sourceUtterance set to a scripted string, not the caller's words. |
| L-150 | D | §2 State 1 New Customers; workflow.reschedule_existing[0], cancel_existing[0] | Medium | Human | fixed | 2 | no_match on reschedule or cancel has no step. |
| L-151 | D,E | §2 State 5 workflow.reschedule_existing[2]; §2 State 2 Immutability | Medium | Human | fixed | 2 | Method change on reschedule is barred in JSON but has no handler; prose bars only type. |
| L-152 | D | §3 State 2 workflow.office_contact_flow[2]; §5.3 check_office_open_status | Medium | Human | fixed | 2 | hours_unavailable has no branch. |
| L-153 | D | §3 State 2 workflow.office_contact_flow[1] | Medium | Human | fixed | 2 | Null routedOfficeRef on office_contact has no resolution step. |
| L-154 | D,E | §4 Tax Pro Lookup > Multiple Matches; 4C | Medium | Human | fixed | 2 | Disambiguation has no exit; 4C shows a yes/no confirm instead. |
| L-155 | D | §2 State 4 Pre-Commit Gate correction bullet; invalidation.text_confirmation | Medium | Human | decided | 2 | Text-destination correction re-runs readiness and search. |
| L-156 | D | §2 State 5 workflow.schedule_new[4]; §2 State 4 Optional Text Confirmation | Medium | Human | decided | 2 | Text offer and full readback run on DDO, whose gate differs. |
| L-157 | C | §1.5 terminal_payload_contract transferReason | Medium | Human | decided | 2 | Several transfer triggers map to no transferReason; not_cancelable fits two. |
| L-158 | C | §5.1 transfer_to_agent Transfer results | Medium | Human | decided | 2 | Tool failure has no result value or handler. |
| L-159 | C,E | Part 5 Conventions (CDAS); scheduler_always isCDAS item; ladders.callback | Medium | Human | decided | 2 | Callback slot with a carried Tax Pro is both CDAS and named. |
| L-160 | C,E | §5.2 book_appointment phoneNumber, contact.callbackNumber | Medium | Human | fixed | 2 | callbackNumber rule for existing customers unclear; phoneNumber undefined. |
| L-161 | C | §2 State 5 closure.line_patterns | Medium | Human | backlog | 2 | Line-pattern keys do not map to finalOutcome values. |
| L-162 | C | §5.2 check_search_readiness taxProPreference.source | Medium | Human | decided | 2 | Tax Pro source has no enum. |
| L-163 | C | §5.2 book_appointment appointmentNotes | Medium | Human | fixed | 2 | Example sends appointmentNotes on tax_prep with notice content. |
| L-164 | B | §2 State 1 Mini-Dialogue 1A; global_always confirm-at-capture item | Medium | Human | decided | 2 | New customer's name is never read back. |
| L-165 | B | §2 State 5 scheduler_always invalid_location item | Medium | Human | fixed | 2 | ZIP reprompt has no attempt cap. |
| L-166 | E | §5.2 send_secure_link Outcome Results | Medium | Human | decided | 2 | No indeterminate result, so outcome_unknown cannot fire for DDO. |
| L-167 | A | §2 State 5 scheduler_always callback item; §4 tax_pro_always[0] | Low | Human | backlog | 2 | Call reason elicited in Part 4 is not carried to the Scheduler. |
| L-168 | C | §1.5 context_envelope.customerStatus | Low | Human | backlog | 2 | customerStatus has no enum. |
| L-169 | C | §5.2 find_customer hasUpcomingAppointment and other response fields | Low | Human | backlog | 2 | Response fields no rule reads. |
| L-170 | V | §1.5 global_outcomes.transferred_to_human, validation_failed; global_always transfer-results item | High | Human | fixed | 2 | After D-015, out_of_scope and automation_blocked transfers have no agent_available outcome; validation_failed overlaps rejected mapped to automation_blocked. |
| L-171 | V | §3 agent_specific_outcomes.office_info_transfer; §1.5 global_outcomes.system_failure | Medium | Human | fixed | 2 | office_info_transfer and system_failure both fit an office lookup failure on agent_available. |
| L-172 | V | §1.5 global_voice_lexicon.reprompt (year line) | Low | Human | fixed | 2 | Frozen "what year was that?" reprompt may be orphaned after D-024 deleted the DOB year re-ask. |
| L-173 | V | §3 and §4 unclear-intent handling; §3 office_info_transfer | Medium | Human | fixed | 2 | Parts 3-4 return capture_intent for an unclear intent with no finalOutcome after office_info_transfer lost "Unresolved office intent". |
| L-174 | V | §1.5 global_always transfer-results item; §1.4 agent_unavailable no-message row | Medium | Human | fixed | 2 | A failed transfer call (D-015) returns no supportHoursSpoken, which the no-message row needs. |
| L-175 | V | §4 No Matches / Inactive; tax_pro_always inactive item; §1.3 | Medium | Human | fixed | 2 | Part 4 still returns leave_message_offer with no transfer tried and no closed office, outside the D-023 §1.3 triggers. |
| L-176 | V | §1.5 global_outcomes.transfer_unavailable | Low | Safe | fixed | 2 | String is 70 words (limit 60); the carried-context list has no other home. |
| L-177 | A | §2 State 5 workflow.schedule_new[2]; §5.2 check_search_readiness taxProPreference | Medium | Human | fixed | 3 | Scheduler captures a named Tax Pro but has no search_tax_pro_by_name to resolve it to a ref. |
| L-178 | A | §1.1 operation; §1.5 context_envelope.operation | Medium | Human | fixed | 3 | Handoffs to appointment_scheduler carry no operation; no owner sets it when null. |
| L-179 | A | §2 State 5 objective; closure.continuation_context | Medium | Human | fixed | 3 | Head of Call cancels inline and the Scheduler owns cancel_existing; which cancellations reach the Scheduler is unstated. |
| L-180 | A | §2 State 2 Appointment Type Rules (callback row); ladders.callback | Medium | Human | fixed | 3 | A direct "have a Tax Pro call me" request fits both phone tax_prep and callback in the Scheduler. |
| L-181 | A | §2 State 5 interruptions.intent_change | Medium | Human | fixed | 3 | "A request for a person" fits both barging transfer and a speak_to_tax_pro handback. |
| L-182 | A,E | §1.2 Tax/Financial Boundary; global_always informational item | Medium | Human | fixed | 3 | Personal tax, calculation, and notice questions go "to a Tax Pro" in prose and to faq_agent or no_approved_answer in JSON. |
| L-183 | A | §4 State 2 objective; §4 State 1 intro | Low | Safe | fixed | 3 | Part 4 objective owns Work Center messaging and "specialized agents", against §1.3 and global_always. |
| L-184 | B,D | §2 State 5 workflow.schedule_new[1]; §1.1 appointmentType, taxProRef, officeRef | Medium | Human | fixed | 3 | Scheduler re-asks type and prior Tax Pro and re-resolves office by entryPoint despite carried context. |
| L-185 | B | §3 Intent Scope > office_info; §3 If OPEN | Medium | Human | fixed | 3 | Phone-number questions go to office_information, whose scope omits phone numbers and whose OPEN branch withholds them. |
| L-186 | B,E | §3 Office Contact Triage > If OPEN; office_open_unanswered | Medium | Human | fixed | 3 | OPEN branch returns capture_intent after serving a status answer; office_open_unanswered excludes callers who asked for the front desk. |
| L-187 | B | §1.5 global_always informational item | Medium | Safe | fixed | 3 | "Invalidates nothing" contradicts D-022 voiding a gate yes on any interruption. |
| L-188 | B,E | §2 Mini-Dialogue 1B, 2B | Low | Safe | fixed | 3 | Agent turns speak the latency preamble with no tool call pending (C-9). |
| L-189 | B | §4 Mini-Dialogue 4A | Low | Safe | fixed | 3 | Agent speaks a new sentence after a message request instead of stopping (C-9). |
| L-190 | C | §5.2 find_available_slots rung Note | Medium | Human | fixed | 3 | digital_drop_off is a slot-search rung though DDO skips readiness and availability. |
| L-191 | C | §2 State 5 scheduler_always idempotency item | Medium | Human | fixed | 3 | Re-gate after not_confirmed: reuse or regenerate idempotencyKey is unstated. |
| L-192 | C | §1.4 multiple_matches row; §5.4 search_tax_pro_by_name | Medium | Human | fixed | 3 | Unscoped multiple_matches recovery line transfers, while Part 4 disambiguates the same result name. |
| L-193 | C,D,E | §5.2 get_customer_appointments Outcome Results; appointment_already_canceled | Medium | Human | fixed | 3 | Result rows count only active appointments, so a canceled-only caller gets none_found and D-021 cannot fire. |
| L-194 | C | §1.5 global_outcomes.handoff_invalid, configuration_missing | Medium | Human | fixed | 3 | Both transfer with no transferReason, and the enum has no value for them. |
| L-195 | C | §1.4 Unregistered ANI row; terminal_payload_contract transferReason | Medium | Human | fixed | 3 | Unregistered-ANI transfer maps to no transferReason or outcome. |
| L-196 | C | §1.5 global_outcomes.question_answered | Medium | Human | fixed | 3 | After D-012 no path ends in question_answered; its intent informational conflicts with the served intent. |
| L-197 | C | §5.2 send_secure_link Outcome Results | Low | Human | backlog | 3 | No not_confirmed or rejected result for send_secure_link. |
| L-198 | C | §5.1 search_knowledge_base attempt | Low | Human | backlog | 3 | attempt value on the clarifier re-query is undefined. |
| L-199 | D | §2 State 5 customer_declined_options; §2 State 4 Pre-Commit Gate | Medium | Human | fixed | 3 | A "no" at the booking, reschedule, or DDO gate has no branch. |
| L-200 | D | §4 Fulfillment Priority step 3; tax_pro_always options item | Medium | Human | fixed | 3 | Caller who declines both callback and message has no exit. |
| L-201 | D | §2 State 3 Off-Season Closure; scheduler_always central-line item | Medium | Human | fixed | 3 | Caller who declines every proposed office has no exit. |
| L-202 | D | §3 State 2 workflow.office_info_flow[3] | Medium | Human | fixed | 3 | Flow returns after the blurb, yet other rules expect follow-up turns and mid-call office changes. |
| L-203 | D | §2 State 5 scenario_selection item 7; §2 State 3 Tax Pro Trade-off | Medium | Human | fixed | 3 | After "stay", item 7 can re-ask the peak trade-off at every no_slots. |
| L-204 | D | §2 State 5 scheduler_always explicit-yes item | Medium | Human | fixed | 3 | Ambiguous gate answers have no cap and no link to the no-match count. |
| L-205 | D | §2 State 5 scheduler_always tool-result item (slot_taken) | Medium | Human | fixed | 3 | slot_taken re-search has no rung scope and no cap. |
| L-206 | D | §3 Office Details Logic > Named Office | Medium | Human | fixed | 3 | No branch when no nearbyOffices officeName matches the caller-named office. |
| L-207 | E | §2 State 5 scheduler_always digital drop-off item | Medium | Safe | fixed | 3 | D-017 DDO change-request rule reached the prose only. |
| L-208 | E | §4 State 2 tax_pro_always callback item | Medium | Safe | fixed | 3 | D-018 new-tax_prep-goes-to-Scheduler rule is missing from Part 4 JSON. |
| L-209 | E | §3 State 2 office_always OPEN item | Medium | Safe | fixed | 3 | JSON omits the prose ban on giving the main line number when open. |
| L-210 | E | §1.5 global_voice_lexicon.prohibited_phrases; §1.2 Zero Web Deflection | Medium | Human | fixed | 3 | Frozen lexicon bans "transfer you to" in all cases and lacks "scheduling department"; prose allows "transfer" for a live agent. |
| L-211 | E | §2 State 5 agent_specific_tools.check_search_readiness | Medium | Safe | fixed | 3 | Scheduler JSON has no needs_more handling. |
| L-212 | E | §1.5 global_always one-question item | Low | Safe | fixed | 3 | JSON lacks the prose one-line-purpose rule for multi-question sequences. |
| L-213 | F | §2 State 5 closure.principle | Low | Safe | fixed | 3 | Restates Base final-turn and close rules. |
| L-214 | F | §3 State 2 workflow.office_info_flow[2], office_contact_flow[3],[4] | Low | Safe | fixed | 3 | Workflow steps restate office_always items. |
| L-215 | F | §2 State 5 interruptions.cancel_said, intent_change | Low | Safe | fixed | 3 | Rationale clauses and restated rules. |
| L-216 | F | §2 State 5 workflow.*[0] | Low | Safe | fixed | 3 | Filler clause "resolve identity normally" in three step-1 strings. |
| L-217 | F | §2, §3, §4 State 2 intro paragraphs; §1.5 intro | Low | Safe | fixed | 3 | Merge statement repeated before each agent JSON block. |
| L-218 | F | §3 agent_specific_tools.get_office_details, check_office_open_status; §4 search_tax_pro_by_name | Low | Safe | fixed | 3 | Tool entries repeat Part 5 descriptions and block rules. |
| L-219 | F | §2 State 5 scheduler_always gatekeeper and waterfall items | Low | Safe | fixed | 3 | Wordy; default-floor clause repeats the floors item. |
| L-220 | F | §1.5 global_always confirm-at-capture, one-question items; global_voice_lexicon | Low | Safe | fixed | 3 | Base JSON strings restate other Base JSON strings. |
| L-221 | F | §2 State 5 scheduler_always tax_notice items; workflow.schedule_new[2] | Low | Safe | fixed | 3 | Notice capture timing and send-all-five restated. |
| L-222 | F | §4 State 2 tax_pro_never[1] | Low | Safe | fixed | 3 | Repeats the tax_pro_always options item. |
| L-223 | F | §3 Office Contact Triage > If OPEN; By-Appointment-Only | Low | Safe | backlog | 3 | Wordy and over length; held while L-186 and L-081 are open on the same anchors. |
| L-224 | F | §1.2 Confirmation Strategy > Confirmed by consequence | Low | Safe | fixed | 3 | Ends with an explanation sentence. |
| L-225 | F | §4 Fulfillment: Leave a Message > Destination Selection, Handoff | Low | Safe | fixed | 3 | Two bullets say the same handoff. |
| L-226 | F | §3 State 1 intro; §3 Out of Scope | Low | Safe | fixed | 3 | Intro restates Out of Scope; third person. |
| L-227 | F | §2 State 5 agent_specific_outcomes.no_acceptable_availability | Low | Safe | fixed | 3 | Restates the never-relax-floor principle. |
| L-228 | F | §2 State 5 interruptions.informational_question | Low | Safe | fixed | 3 | Repeats the explicit-yes item's void rule. |
| L-229 | F | §3 office_never[4]; §4 tax_pro_never[0] | Low | Safe | fixed | 3 | Restate the global_always leave_message_offer return. |
| L-230 | F | §1.5 base_persona | Low | Safe | fixed | 3 | 66 words, over the 60-word limit. |
| L-231 | F | §4 Out-of-Scope (FAQ Agent) | Low | Safe | fixed | 3 | 38 words, over the 35-word limit. |
| L-232 | F | §5.2 find_available_slots Note; book_appointment Note | Low | Safe | fixed | 3 | Four-sentence paragraphs. |
| L-233 | F | §1.5 handoff_invalid; scheduler_always entryPoint item; invalidation.customer_identity; §2 State 1 Identity | Low | Safe | fixed | 3 | sessionEnvelope and "Head of Call envelope" name context_envelope. |
| L-234 | F | §2 scheduler_always floor, third-party text items; global_never unified item; Part 5 Conventions | Low | Safe | fixed | 3 | "must"/"do not" for hard limits; rationale sentence. |
| L-235 | F | How to Read This Document | Low | Safe | fixed | 3 | Part labels differ from headings. |
| L-236 | F | §4 By Name Request | Low | Safe | fixed | 3 | Empty parent bullet; cases not nested. |
| L-237 | F | §2 State 2 Tax Notice Services Guardrails > Tax Extension | Low | Human | backlog | 3 | Tax Extension bullet sits under the Tax Notice heading. |
| L-238 | V | §3 Office Contact Triage > If hours_unavailable; workflow.office_contact_flow[2] | Medium | Human | decided | 3 | After giving the address on hours_unavailable, no finalOutcome or nextAction is named. |
| L-239 | V | §4 No Matches / Inactive; tax_pro_always unavailable item | Medium | Human | decided | 3 | Caller who declines the Scheduler offer on the unavailable-Tax-Pro path has no outcome. |
| L-240 | V | §1.1 operation; §2 State 5 objective; §2 State 4 Write Tools > cancel_appointment | Medium | Human | decided | 3 | Null operation asks book/change/cancel (D-027), but cancel is allowed only on cancel_existing or mid-booking (D-028). |
| L-241 | V | §5.2 get_customer_appointments Outcome Results; workflow.reschedule_existing[1] | Medium | Human | decided | 3 | On reschedule_existing, a canceled appointment in the results has no rule or outcome. |
| L-242 | V | §1.4 system_failure row; global_always transfer-results item | Medium | Human | decided | 3 | Failed transfer call speaks "Let me get you to a person", then closes with no person. |
| L-243 | V | §3 Cross-Office Restriction; office_never phone item; office_always CLOSED item | Medium | Human | decided | 3 | "Routed office" undefined with null routedOfficeRef; CLOSED branch after ZIP capture speaks a number office_never forbids. |
| L-244 | V | §4 Generic Request; tax_pro_always unavailable item; routed_to_scheduler | Medium | Human | decided | 3 | Generic caller with no prior Tax Pro hears "they are unavailable"; routed_to_scheduler needs an officeRef the path never resolves. |
| L-245 | V | §3 If OPEN; office_always OPEN item | Low | Safe | fixed | 3 | OPEN branch does not name office_open_unanswered as its outcome (D-031). |
| L-246 | V | §5.1 search_knowledge_base KB results | Low | Human | decided | 3 | requires_tax_pro outside the Scheduler returns no_approved_answer (D-025) vs speak_to_tax_pro handback (D-034). |
| L-247 | V | workflow.schedule_new[1]; §2 State 3 Office Resolution > Rollover; scheduler_always rollover item | Low | Safe | fixed | 3 | Steps read unconditionally; add pointer to carried-context precedence (D-027). |
| L-248 | V | agent_specific_outcomes.customer_declined_options | Low | Human | backlog | 3 | "requesting a person" ambiguous after D-034 split live-agent and Tax Pro requests. |
| L-249 | V | global_outcomes.validation_failed | Low | Safe | fixed | 3 | "a result other than rejected" overlaps change_not_allowed and not_cancelable, mapped to automation_blocked (D-015). |
| L-250 | V | §2 State 3 Informational Interruptions > Personal Questions | Low | Safe | fixed | 3 | Bullet omits "resume", which its JSON mirror carries. |
| L-251 | V | §1.5 terminal_payload_contract | Low | Human | backlog | 3 | 214 words, over the 60-word JSON item limit; fold into L-034. |
| L-252 | A,B,E | §2 State 2 Appointment Type Rules > Tax Pro Requests; interruptions.intent_change | Medium | Safe | fixed | 4 | Prose "A request for a specific or own Tax Pro" drops "to speak to" (D-034, JSON mirror), which would hand back returning_same_tax_pro bookings. |
| L-253 | E | §2 State 5 workflow.cancel_existing[1]; appointment_already_canceled | Medium | Safe | fixed | 4 | cancel_existing never checks status canceled before the gate (D-021, D-028). |
| L-254 | B | §2 State 5 closure.line_patterns.handoff_unavailable | Medium | Safe | fixed | 4 | Else-branch speaks supportHoursSpoken on a failed transfer call, against global_always (D-026). |
| L-255 | A | §4 State 2 objective | Low | Safe | fixed | 4 | Objective omits routed_to_scheduler for another Tax Pro and tax_pro_options_declined. |
| L-256 | C | §3 State 1 Intent Scope & Disambiguation > unclear_intent | Low | Safe | fixed | 4 | Label "unclear_intent" styled as an enum; the outcome is intent_unclear. |
| L-257 | C | §4 Fulfillment Priority step 4; workflow.speak_to_tp_generic[4], speak_to_tp_by_name[5] | Low | Safe | fixed | 4 | Return lists mix nextAction values with a finalOutcome. |
| L-258 | E | §2 State 5 agent_specific_outcomes.no_acceptable_availability | Low | Safe | fixed | 4 | Definition omits first-lookup none_nearby (D-015, D-016). |
| L-259 | E | §5.2 get_customer_appointments Outcome Results (too_many) | Low | Safe | fixed | 4 | too_many row not updated for D-028 active-or-canceled count. |
| L-260 | E | §1.5 global_never web-deflection item | Low | Safe | fixed | 4 | JSON narrower than §1.2: omits website and app-name ban. |
| L-261 | E | §2 State 5 agent_specific_tools.check_search_readiness | Low | Safe | fixed | 4 | No conflict branch mirroring the §1.4 conflict-from-readiness row. |
| L-262 | E | §1.5 context_envelope.appointmentType, taxProRef, officeRef | Low | Safe | fixed | 4 | Envelope strings omit D-027 precedence over entryPoint and routedOfficeRef. |
| L-263 | B | §4 No Matches / Inactive; tax_pro_always unavailable item | Low | Safe | fixed | 4 | Rule says to offer "the Appointment Scheduler", internal architecture §1.2 bans. |
| L-264 | B | §4 Mini-Dialogue 4D | Low | Safe | fixed | 4 | Handoff line spoken with no agent_available result, under a "System (Agent)" label (C-9). |
| L-265 | F | §2 State 5 agent_specific_tools (find_customer, find_offices_near, find_available_slots, book_appointment); workflow.schedule_new[1],[3], reschedule_existing[3] | Low | Safe | fixed | 4 | F-01: Pointer-only "Apply/Follow the ... rules" sentences (-65w). |
| L-266 | F | §2 State 5 broadening.principles[6]; §2 State 3 Search Broadening Ladder > Principles | Low | Safe | fixed | 4 | F-03: Slot-order/CDAS rule restated; tool-ranking sentence (-29w). |
| L-267 | F | §2 State 5 workflow.cancel_existing[1] | Low | Safe | fixed | 4 | F-04: Retrieval step duplicates reschedule_existing[1] (-27w). |
| L-268 | F | §4 State 2 workflow.leave_message[0],[1] | Low | Safe | fixed | 4 | F-05: Context-pass split across two steps (-20w). |
| L-269 | F | §2 State 5 scheduler_always tax_notice_service capture item | Low | Safe | fixed | 4 | F-06: Five notice values listed twice (-20w). |
| L-270 | F | §2 State 5 scheduler_always three-sentence readback item; §2 State 4 Chunked Readback | Low | Safe | fixed | 4 | F-07: Sentence positions spelled out (-20w). |
| L-271 | F | §2 State 5 workflow.schedule_new[5] | Low | Safe | fixed | 4 | F-08: Booking step restates payload rules (-19w). |
| L-272 | F | §1.5 global_always no-input item | Low | Safe | fixed | 4 | F-09: Restates consecutive_silence outcome (-15w). |
| L-273 | F | §4 Mini-Dialogue 4A last System turn | Low | Safe | fixed | 4 | F-11: System line explains flow internals (-14w). |
| L-274 | F | §2 State 5 scheduler_always office identity item | Low | Safe | fixed | 4 | F-12: Lists every pre-commit phase (-13w). |
| L-275 | F | §2 State 5 scheduler_always reschedule changing item | Low | Safe | fixed | 4 | F-13: Repeats "if ... differs" four times (-13w). |
| L-276 | F | §5.2 find_customer intro; Note | Low | Safe | fixed | 4 | F-14: Read-only and status enum stated twice (-13w). |
| L-277 | F | §2 State 5 closure.continuation_context | Low | Safe | fixed | 4 | F-15: Restates priorTransaction rules (-12w). |
| L-278 | F | §5.3 check_office_open_status intro | Low | Safe | fixed | 4 | F-16: Lists tool inputs (-12w). |
| L-279 | F | §1.5 global_never message item | Low | Safe | fixed | 4 | F-17: Ownership explanation sentence (-11w). |
| L-280 | F | §1.5 Universal Base JSON Prompt intro | Low | Safe | fixed | 4 | F-18: Lists the block's contents (-11w). |
| L-281 | F | §2 State 2 DDO Rules > Rescheduling; Complexity Matching > Guardrails | Low | Safe | fixed | 4 | F-19: Duplicate DDO clause and rationale clause (-11w). |
| L-282 | F | §2 State 5 scheduler_never profile item | Low | Safe | fixed | 4 | F-20: Lists pre-commit phases (-10w). |
| L-283 | F | §5.2 book_appointment intro | Low | Safe | fixed | 4 | F-21: "point of no return" softener (-10w). |
| L-284 | F | §2 State 3 Search Broadening Ladder intro | Low | Safe | fixed | 4 | F-22: Restates one-constraint principle (-9w). |
| L-285 | F | §2 State 5 workflow.reschedule_existing[2] | Low | Safe | fixed | 4 | F-23: Type/method bar stated twice (-9w). |
| L-286 | F | §2 State 5 scheduler_always isCDAS item | Low | Safe | fixed | 4 | F-24: Two conditionals for one definition (-8w). |
| L-287 | F | §2 State 5 closure.re_entry | Low | Safe | fixed | 4 | F-25: Restates the one-transaction limit (-7w). |
| L-288 | C,D | §2 State 5 closure.re_entry; scheduler_always idempotency item; §5.2 send_secure_link | High | Human | decided | 4 | Fresh key namespace on re-entry cannot be built; a DDO change reuses interactionId-ddo-1 and is deduplicated. |
| L-289 | A | §1.3 Leave-a-Message Ownership; §1.4 agent_unavailable message-available row; closure.line_patterns.handoff_unavailable | High | Human | decided | 4 | Spec gives the message offer and support hours to the Leave a Message flow, which has neither; Head of Call has no leave_message_offer node. |
| L-290 | A | §4 No Matches / Inactive; §2 State 2 Tax Pro Requests; interruptions.intent_change | High | Human | decided | 4 | A callback request with no reachable Tax Pro bounces between Part 4 and the Scheduler with no bound. |
| L-291 | B,D | §2 State 5 interruptions.cancel_said; global_outcomes.intent_changed | Medium | Human | decided | 4 | Post-commit cancel request hands back intent_changed with no routingTarget or operation. |
| L-292 | D,E | §2 State 5 interruptions.cancel_said; §2 State 4 Write Tools > cancel_appointment | Medium | Human | decided | 4 | Cancel scope: "mid-booking" vs "before any commit"; gate "no, cancel that" matches cancel_said and gate-no. |
| L-293 | C | §1.5 terminal_payload_contract; §1.2 No-Match Rule; §3 unclear_intent | Medium | Human | decided | 4 | intent_unclear and the No-Match Rule both claim an unresolved intent answer. |
| L-294 | C | §1.5 global_outcomes.intent_unclear | Medium | Human | decided | 4 | No intent value when Part 3 cannot tell office_info from office_contact. |
| L-295 | C | §1.5 global_outcomes.intent_unclear; terminal_payload_contract capture_intent | Medium | Human | decided | 4 | intent_unclear returns capture_intent after the caller was served. |
| L-296 | C | §1.5 terminal_payload_contract intent enum; global_outcomes.no_approved_answer | Medium | Human | decided | 4 | intent informational has no serving agent after question_answered was deleted. |
| L-297 | C | §1.5 global_outcomes.customer_abandoned | Medium | Human | decided | 4 | transactionOccurred false and no committed ref after a drop during post-commit readback. |
| L-298 | C | §4 Generic Request; workflow.speak_to_tp_generic[3]; Part 5 Conventions priorTaxProStatus | Medium | Human | decided | 4 | Generic path checks activeStatus and takingAppointmentsInd, which find_customer does not return. |
| L-299 | C | §3 agent_specific_tools.transfer_to_agent; §5.3 get_office_details office_not_found | Medium | Human | decided | 4 | office_not_found on a caller-given ZIP transfers as system_failure; Scheduler reprompts the same input. |
| L-300 | D | §1.5 global_always followUpTopics item; interruptions.informational_question | Medium | Human | decided | 4 | KB non-answer mid-booking returns terminal no_approved_answer instead of resuming. |
| L-301 | D | §2 State 5 scheduler_always find_offices_near item (invalid_constraints) | Medium | Human | decided | 4 | invalid_constraints to readiness loop has no cap; rule sits in the wrong tool item. |
| L-302 | D | §2 State 4 Post-Commit Readback; closure.re_entry | Medium | Human | decided | 4 | A post-commit change request has no path. |
| L-303 | D | §3 Standard Blurb; workflow.office_info_flow[3]; §1.3 Yield rule | Medium | Human | decided | 4 | Office info has no stop trigger after follow-ups; silence ends as consecutive_silence. |
| L-304 | D | §3 Named Office; office_always named-office item | Medium | Human | decided | 4 | Named-office match ignores the top-level office the ZIP resolves to. |
| L-305 | D | §3 workflow.office_contact_flow; If CLOSED | Medium | Human | decided | 4 | office_contact ignores seasonalStatus; closed_for_season caller hears no Year-Round Office. |
| L-306 | B,D | §4 By Name Request > 1 Match; workflow.speak_to_tp_by_name; §1.2 Confirmed by consequence | Medium | Human | decided | 4 | Single match "Confirm the Tax Pro": spoken confirm or internal; no branch for a caller no. |
| L-307 | D | §2 State 5 workflow.schedule_new[1]; Declined Offices | Medium | Human | decided | 4 | Returning caller who keeps the Tax Pro but rejects the last-served office has no path to nearby offices. |
| L-308 | A | §1.1 knownPreferences; workflow.schedule_new[2] | Medium | Human | decided | 4 | Scheduler captures a Tax Pro preference it cannot resolve after D-027. |
| L-309 | A | §1.5 global_always informational item; §5.1 Category Enums | Medium | Human | decided | 4 | Identity/fraud and other-department contact questions have no owner. |
| L-310 | A | §1.5 global_always KB item and informational item | Medium | Human | decided | 4 | tax_prep_and_records questions have two owners (KB in-agent vs faq_agent). |
| L-311 | A | §2 State 5 scenario_selection items 2-4; ladders.reschedule | Medium | Human | decided | 4 | Callback and physical drop-off reschedules use a ladder with Tax Pro and nearby-office rungs. |
| L-312 | A | §4 Out-of-Scope (New Appointment); interruptions.intent_change | Medium | Human | decided | 4 | Part 4 names no routingTarget for reschedule, cancel, or non-tax_prep booking requests. |
| L-313 | A | §1.1 entryReason; context_envelope.entryReason | Medium | Human | decided | 4 | Refund-status C-28 TRANSFER handoff to the Scheduler has no entryReason. |
| L-314 | A | §2 State 5 objective; global_always informational item | Medium | Human | decided | 4 | Appointment-details questions ("when is my appointment?") have no owner. |
| L-315 | E | §1.5 global_always transfer-results item; global_outcomes.outcome_unknown | Medium | Human | decided | 4 | Failed transfer call on outcome_unknown loses the outcome name and idempotencyKey. |
| L-316 | E | §1.4 handoff_invalid or configuration_missing row; global_outcomes.handoff_invalid, configuration_missing | Medium | Human | decided | 4 | Unclear whether these call transfer_to_agent or hand back without a call. |
| L-317 | B | §2 State 3 Personal Questions; search_knowledge_base; scheduler_never | Medium | Human | decided | 4 | "Tax Pro covers it at the appointment" said on cancel, DDO, and physical drop-off paths. |
| L-318 | B | §2 Mini-Dialogue 1A | Low | Human | backlog | 4 | First turn lacks a one-line purpose; fix adds caller-heard words to a frozen line. |
| L-319 | B | §2 Mini-Dialogue 2A, 2B last Agent turns | Low | Human | backlog | 4 | Latency bridges outside preamble_phrases (frozen). |
| L-320 | F | §1.3 Leave-a-Message Ownership fourth bullet | Low | Safe | decided | 4 | F-10: flow-internals list; held for L-289 ownership question. |
| L-321 | F | Part 5 Conventions (Request, Response, Read result first) | Low | Human | backlog | 4 | F-02: trim -39w; anchor edited in rounds 1-3, oscillation guard. |
| L-322 | V | §3 Office Details Logic > No Name Match; office_always[2] | Medium | Human | fixed | 4 | Name no-match transfers as system_failure, but D-044 limits lookup failures to tool errors. |
| L-323 | V | §1.5 global_always followUpTopics item (Part 4) | Medium | Human | decided | 4 | In Part 4, requires_tax_pro returns no_approved_answer and ends a caller who wants a Tax Pro. |
| L-324 | V | §2 State 3 Appointment Details; agent_specific_tools.get_customer_appointments | Medium | Human | fixed | 4 | Appointment-details read path has no finalOutcome; the terminal contract cannot validate. |
| L-325 | V | §1.5 terminal_payload_contract nextAction capture_intent | Low | Human | fixed | 4 | No outcome uses capture_intent after intent_unclear was deleted (D-042). |
| L-326 | D,E | §2 State 5 workflow.schedule_new[1] | Medium | Safe | fixed | 5 | "rejecting it" could mean the Tax Pro; now "rejecting that office" (D-048 wording; guard not applied: the decision names this anchor). |
| L-327 | C,E | §1.5 global_outcomes.transfer_unavailable | Medium | Safe | fixed | 5 | Failed call still read as nextAction close with supportHoursSpoken; scoped per D-043 (guard not applied: D-043 names this outcome). Closes L-176. |
| L-328 | B | §1.3 Leave-a-Message Ownership third bullet; global_always leave-message item | Medium | Safe | fixed | 5 | leave_message_offer triggers omitted D-045's hours_unavailable case. |
| L-329 | B | interruptions.intent_change (Parts 2, 3, 4) | Medium | Safe | fixed | 5 | "never transfer" and bare handbacks blocked the D-046 identity/fraud transfer. |
| L-330 | B | §1.5 global_outcomes.intent_changed | Low | Safe | fixed | 5 | Defined as outside scope only; D-041 and D-019 use it after a commit inside scope. |
| L-331 | A | §3 Office Contact Triage > Routed Office | Low | Safe | fixed | 5 | Routed Office bullet read as office_contact only; now "On either path". |
| L-332 | E | §4 State 2 workflow.speak_to_tp_by_name[4] | Low | Safe | fixed | 5 | By-name step stated options with no active-status branch. |
| L-333 | E,F | §1.3 Leave-a-Message Ownership last bullet | Low | Safe | fixed | 5 | "the deterministic flow" ambiguous after D-039; names the Leave a Message flow. |
| L-334 | B,F | §3 State 2 office_never web item | Low | Safe | fixed | 5 | Repeated global_never web ban (C-3 A); deleted. |
| L-335 | F | workflow.schedule_new[4]; workflow.reschedule_existing[4] | Low | Safe | fixed | 5 | Text-and-gate steps repeated scheduler_always. |
| L-336 | F | §4 State 2 tax_pro_always[0] | Low | Safe | fixed | 5 | Elicit rule stated twice. |
| L-337 | F | §3 State 2 office_always office_contact status item; office_never timezone item | Low | Safe | fixed | 5 | Open-status rule stated twice; merged into office_never. |
| L-338 | F | §4 State 2 workflow.speak_to_tp_by_name[2] | Low | Safe | fixed | 5 | Repeated tax_pro_always by-name item. |
| L-339 | F | §1.5 global_always questions item | Low | Safe | fixed | 5 | Repeated global_voice_lexicon.questions_per_turn; now points to it. |
| L-340 | F | §5.2 book_appointment Note | Low | Safe | fixed | 5 | Named fields the request does not carry; deleted. |
| L-341 | F | §1.5 global_outcomes.customer_abandoned | Low | Safe | fixed | 5 | Trigger wordy; "unanswered gate" twice. |
| L-342 | F | §2 State 3 Tax Pro Trade-off | Low | Safe | fixed | 5 | Repeated a broadening principle. |
| L-343 | F | §2 State 5 interruptions.cancel_said | Low | Safe | fixed | 5 | Repeated intent_changed close rule. |
| L-344 | F | scheduler_always text-offer item | Low | Safe | fixed | 5 | "self-service" named first_party with a second term. |
| L-345 | B | §5.2 find_customer Note | Low | Safe | fixed | 5 | Note narrowed priorTaxProStatus and explained why. |
| L-346 | F | §1.5 global_outcomes.configuration_missing | Low | Human | backlog | 5 | Copies handoff_invalid; oscillation guard (edited rounds 2-4). |
| L-347 | F | agent_specific_tools.find_available_slots | Low | Human | backlog | 5 | Restates rules; oscillation guard (edited rounds 2-4). |
| L-348 | F | scheduler_never loan item | Low | Human | backlog | 5 | Repeats global_never; oscillation guard. |
| L-349 | F | scheduler_always DDO item | Low | Human | backlog | 5 | Descriptive sentence and "execute"; oscillation guard. |
| L-350 | F | agent_specific_tools.check_search_readiness | Low | Human | backlog | 5 | Repeats one-question rule; oscillation guard. |
| L-351 | F | §4 State 2 objective | Low | Human | backlog | 5 | Partial repeat of Base handback; oscillation guard. |
| L-352 | F | §3 Unclear intent; office_always disambiguation item | Low | Human | backlog | 5 | Wordy; oscillation guard (edited rounds 1, 2, 4). |
| L-353 | F | §4 State 2 tax_pro_always callback item | Low | Human | backlog | 5 | Prose now names routed_to_scheduler, JSON spells it out; oscillation guard. |
| L-354 | E,F | §3 State 2 workflow.office_contact_flow[0] | Low | Human | backlog | 5 | Describes the Leave a Message flow's internals; oscillation guard. |
| L-355 | C | agent_specific_outcomes.appointment_already_canceled; Part 5 Conventions summary bullet | Low | Human | backlog | 5 | canceledSummary means a write result and a retrieved record; oscillation guard. |
| L-356 | C | Part 5 Conventions first bullet | Low | Human | backlog | 5 | Dead envelope synonyms; oscillation guard (L-321). |
| L-357 | A,B,C,D,E | §2 State 2 After Part 4; scheduler_always routed_to_scheduler item | Medium | Human | fixed | 5 | Unscoped rule can book Part 4's own callback handoff as tax_prep; priorTransaction vs priorTransaction.finalOutcome. |
| L-358 | A,D,E | §1.1 operation; routed_to_scheduler | Medium | Human | fixed | 5 | Another-Tax-Pro handoff sets no operation, so the Scheduler re-asks book, change, or cancel. |
| L-359 | A,D | §2 State 2 Tax Pro Requests; interruptions.intent_change | Medium | Human | fixed | 5 | Own or named Tax Pro request after routed_to_scheduler loops back to Part 4. |
| L-360 | A | workflow.schedule_new[1]; scenario_selection item 8 | Medium | Human | fixed | 5 | Scheduler may re-offer the prior Tax Pro Part 4 found unavailable. |
| L-361 | B,C | terminal_payload_contract taxProRef/officeRef clause and appointmentType; §1.1 carried values | Medium | Human | fixed | 5 | Handback fields are re-read as carried values (unavailable Tax Pro's ref; committed type). |
| L-362 | A,C,D | §3 Office Contact Triage; workflow.office_contact_flow | Medium | Human | fixed | 5 | office_contact at a closed_for_season office has no end state. |
| L-363 | B,D | §2 State 3 Appointment Details; get_customer_appointments | Medium | Human | fixed | 5 | Details answer ends a booking in progress; no handling for none_found, several, too_many, canceled. |
| L-364 | A | §3 Out of Scope; §4 Out-of-Scope (Appointments) | Medium | Human | fixed | 5 | Parts 3 and 4 have no route for appointment-details questions. |
| L-365 | C | terminal_payload_contract intent; §3 Unclear intent | Medium | Human | fixed | 5 | Part 3 clarification_exhausted on intent has no valid intent value. |
| L-366 | C,D,E | §2 State 2 DDO Rules > Rescheduling; Post-Commit Requests | Medium | Human | fixed | 5 | DDO change: same-invocation send vs handback; no key; next invocation's "change" hits none_found. |
| L-367 | D | interruptions.cancel_said; workflow.cancel_existing[2] | Medium | Human | fixed | 5 | No pre-commit switch between operations except to cancel. |
| L-368 | D | tax_extension row; scheduler_always tax_extension item | Medium | Human | fixed | 5 | Declining the closed-window tax_prep pivot has no exit. |
| L-369 | A | §4 tax_pro_always callback item; §2 State 2 Tax Pro Requests; scenario_selection items 8-10 | Medium | Human | fixed | 6 | Booking with a named non-prior Tax Pro loops between agents or silently drops the Tax Pro. |
| L-370 | D | §3 Office Contact Triage; workflow.office_contact_flow[1]; office_always by_appointment_only item | Medium | Human | fixed | 6 | office_contact at a by_appointment_only office falls into the booking handoff (joins L-081). |
| L-371 | D | §2 State 3 Declined Offices; workflow.schedule_new[1]; ladders.returning_same_tax_pro rung 5 | Medium | Human | fixed | 6 | Rung 5 returns to the rejected last-served office; declining every rung 3 office ends vs continues. |
| L-372 | D | §2 State 3 Tax Pro Trade-off; scenario_selection item 7 | Medium | Human | fixed | 6 | After "stay" lapses on a constraint change, item 7 has no rule. |
| L-373 | E | scheduler_always carried-context item | Medium | Safe | fixed | 6 | Carried officeRef skipped the keep-prior-Tax-Pro question D-050 keeps. |
| L-374 | E | scheduler_always authentication-failure item; workflow.reschedule_existing[1] | Medium | Safe | fixed | 6 | JSON lacked first-party multiple_matches and none_found transfers. |
| L-375 | E | scheduler_always too_many/flags item; §2 State 3 Appointment Details; §5.2 Automation Flags | Medium | Human | fixed | 6 | Automation flags are unscoped across operations and details questions. |
| L-376 | B | §1.3 Leave-a-Message Ownership third bullet; global_always leave-message item | Medium | Human | fixed | 6 | Closed-office leave_message_offer trigger binds every agent (oscillation guard: Human). |
| L-377 | B | §1.3 Leave-a-Message Ownership second bullet; Scheduler outcomes | Medium | Human | fixed | 6 | Scheduler has no outcome for a caller's message request. |
| L-378 | C | agent_specific_outcomes.no_acceptable_availability | Medium | Human | fixed | 6 | "Agreed constraints" is not a contract field. |
| L-379 | C | §3 Office Details Logic > No Match; §5.3 get_office_details | Medium | Human | fixed | 6 | office_not_found on a non-caller officeRef has no rule. |
| L-380 | C | Ladders table; broadening.ladders primaries; scenario_selection item 7 | Medium | Safe | fixed | 6 | Five names for the ladder's office unified as "selected office". |
| L-381 | F | scheduler_never retry item; durationSpoken item; §1.2 Grouped capture; §2 Central Line; Returning, Same Tax Pro cell; global_always preamble and DOB items; scheduler_always third-party, textConfirmation, book_appointment, type items; office_info_flow[1] | Low | Safe | fixed | 6 | 12 editorial trims (F-01 to F-12), about -62 words. |
| L-382 | V | customer_declined_options; Part 3 transfer_to_agent and office_always; §5.2 get_customer_appointments one_appointment | Low | Safe | fixed | 6 | Round 5 decided follow-up propagation of D-051, D-056, D-054. |
| L-383 | V | §2 State 2 After Part 4; scheduler_always routed_to_scheduler item; §2 Tax Pro Requests | Medium | Human | decided | 6 | After D-061, a caller routed from Part 4 for another Tax Pro who re-asks for the named Tax Pro loops back to Part 4; "they aren't available" can be false. |
| L-384 | V | §2 State 3 Message Request; scheduler_always message item | Medium | Human | decided | 6 | A message request naming no recipient has no rule in the Scheduler (D-067 covers Tax Pro or office staff only). |
| L-385 | V | scheduler_always routed_to_scheduler item; §5.2 book_appointment Note | Medium | Human | decided | 6 | Unclear whether a Part 4 callback request booked as tax_prep phone_callback carries the one-phrase appointmentNotes reason. |
| L-386 | E | §4 State 2 interruptions.intent_change | Medium | Safe | fixed | 7 | Handler lacked D-061's other-booking exception. |
| L-387 | C | §4 State 2 tax_pro_always by-name item; unavailable item | Medium | Safe | fixed | 7 | no_match named three things; first-party by-name no_match had to speak and skip the unavailable line. |
| L-388 | C | §1.5 global_outcomes.validation_failed | Medium | Safe | fixed | 7 | Definition covered second invalid_constraints and delivery_failed, which D-048 and D-001 send to system_failure. |
| L-389 | E | scheduler_always carried-context item | Low | Safe | fixed | 7 | JSON required customerStatus with customerRef; D-071 keys on customerRef alone. |
| L-390 | E | §2 State 1 Authentication Logic > No Match Outside a New Booking | Low | Safe | fixed | 7 | Bare pointer did not name D-070's Authentication failed line. |
| L-391 | C | §1.5 global_never message item | Low | Safe | fixed | 7 | "Work Center message" -> "caller's message". |
| L-392 | F | §5.1 Transfer results; scheduler_always invalid_location item; §4 find_customer entry; tax_pro_always options and last items; same_day rungs[1]; §3 Off-Season Closure; office_always closed_for_season item; §5.2 get_customer_appointments Note; §1.1 customerRef | Low | Safe | fixed | 7 | 9 editorial trims (F-03, F-06, F-08, F-12, F-13, F-16, F-18, F-19, F-20). |
| L-393 | D | workflow.reschedule_existing[3], [4]; changing-array item; §5.2 get_customer_appointments Response | High | Human | decided | 7 | Reschedule has no officeRef, taxProRef, date, or time for the bound appointment. |
| L-394 | D | agent_specific_tools.check_search_readiness; §1.4 conflict row; §1.2 Input Exhaustion | Medium | Human | decided | 7 | Repeated readiness needs_more or conflict has no cap (asked with L-146). |
| L-395 | D | workflow.reschedule_existing[3]; gatekeeper, waterfall, floor items | Medium | Human | decided | 7 | Unclear whether reschedule re-runs complexity screening. |
| L-396 | D | §2 State 3 Ladders, Rescheduling row; ladders.reschedule rungs[2], [3] | Medium | Human | decided | 7 | Reschedule ladder when the bound appointment names no Tax Pro. |
| L-397 | D | §3 Office Contact Triage; office_contact_flow[1]; Named Office | Medium | Human | decided | 7 | office_contact has no step to resolve a caller-named office. |
| L-398 | D | §4 transfer_to_agent; speak_to_tp_generic[3]; §4 Generic Request | Medium | Human | decided | 7 | Part 4 has no branch for find_customer multiple_matches. |
| L-399 | D | invalidation.customer_identity; §2 State 1 Dynamic State Invalidation; §1.1 carried values | Medium | Human | decided | 7 | Subject change keeps carried Tax Pro, office, and type. |
| L-400 | A | global_always search_knowledge_base item; §3 Out of Scope; §4 Out-of-Scope; §2 Informational Interruptions; §1.1 operation | Medium | Human | decided | 7 | Logistics questions outside a task have two owners in Parts 3-4 and none in the Scheduler. |
| L-401 | B | §1.2 Confirmed at capture; global_always confirm-at-capture item; §4 third-party item | Medium | Human | decided | 7 | Base JSON drops the third-party owner's name readback; Part 4 never confirms it. |
| L-402 | B | §1.4 outcome_unknown row; global_voice_lexicon.empathy | Medium | Human | decided | 7 | Frozen outcome_unknown line speaks of a time and double-booking on cancel and secure-link writes. |
| L-403 | B | scheduler_never method-token item; Pre-Commit Gate; 4A, 4B; meetingMethodSpoken | Medium | Human | decided | 7 | "method_descriptions only" conflicts with readbacks and frozen dialogues. |
| L-404 | C,E | scheduler_always new-customer contact item; §5.2 book_appointment Note | Medium | Human | decided | 7 | contact.callbackNumber required but in no request schema; overlaps newCustomer.phoneNumber. |
| L-405 | A | §3 and §4 interruptions.intent_change | Low | Human | backlog | 7 | No routingTarget named for Tax Pro requests in Part 3 or office-staff requests in Part 4 (oscillation guard). |
| L-406 | B,E | §1.3 Leave-a-Message Ownership third bullet; global_always leave-message item | Low | Human | backlog | 7 | Trigger list omits closed_for_season (oscillation guard). |
| L-407 | B | §4 Mini-Dialogues 4A, 4E | Low | Human | backlog | 7 | Prior Tax Pro disclosed with no find_customer System turn (oscillation guard). |
| L-408 | C,F | §3 Office Contact Triage > If CLOSED, If OPEN; office_always OPEN, CLOSED items | Low | Human | backlog | 7 | CLOSED names no finalOutcome; "stop speaking" repeats (oscillation guard; also L-223). |
| L-409 | C | scheduler_always textConfirmation item | Low | Human | backlog | 7 | channel email defined but never captured. |
| L-410 | F | context_envelope; speak_to_tp_generic[2]; rollover item; closure.line_patterns; DDO Rules; gatekeeper and waterfall items; Part 5 Conventions | Low | Human | backlog | 7 | F-01, F-02, F-07, F-14, F-15, F-17, F-20 (Conventions half); oscillation guard. |
| L-411 | F | §5.2 Automation Flags; office_always by_appointment_only item; §3 By-Appointment-Only | Low | Safe | backlog | 7 | F-04, F-05, F-11 trim round 6 decision text; held. |
| L-412 | C,D,E,F | §5.2 book_appointment Request JSON (Existing Customer).appointmentMethod | Medium | Safe | fixed | 8 | Example sent a phone_callback with null appointmentNotes after D-083; method set to in_person. |
| L-413 | B,E,F | §2 State 2 Appointment Type Rules table, callback row | Low | Safe | fixed | 8 | Prose limited the reason capture to the callback type (D-083 propagation). |
| L-414 | C | agent_specific_tools.check_search_readiness | Low | Safe | fixed | 8 | "the appointment-type item" pointed to the wrong item; now names emerald_advance or tax_extension. |
| L-415 | C | §5.2 check_search_readiness Request taxProPreference.source; Response taxProSource | Low | Safe | fixed | 8 | Reschedule example labeled the bound Tax Pro caller_stated (D-079 propagation). |
| L-416 | A,B | §2 State 2 Tax Pro Requests | Medium | Safe | fixed | 8 | "except After Part 4" switched off the whole rule; narrowed to what After Part 4 lists (D-081 scope). |
| L-417 | F | workflow.schedule_new[1] | Low | Human | backlog | 8 | 62 words, over the JSON item limit; oscillation guard. |
| L-418 | A,B,D | workflow.schedule_new[1]; §2 State 2 After Part 4; scheduler_always routed_to_scheduler item | Medium | Human | decided | 8 | After Part 4 the keep-prior-Tax-Pro question (D-050) conflicts with D-081. |
| L-419 | B | terminal_payload_contract taxProRef clause; §4 routed_to_scheduler | Medium | Human | decided | 8 | Part 1 carries taxProRef on Part 4's another-Tax-Pro handoff. |
| L-420 | B | §1.2 Confirmed at capture; global_always confirm-at-capture item; scheduler_always phone_callback item | Medium | Human | decided | 8 | Unclear whether the phone_callback reason is read back at capture. |
| L-421 | B,C | global_always empathy item; global_voice_lexicon.empathy | Medium | Human | decided | 8 | Free acknowledgment may use path-bound lines that promise a person. |
| L-422 | D | scheduler_always efile_rejection_retail item | Medium | Human | decided | 8 | efile entry proposes an inactive prior Tax Pro. |
| L-423 | D,F | agent_specific_tools.check_search_readiness; §2 State 3 Readiness Cap; §5.2 conflict | Medium | Human | decided | 8 | A conflict that is neither a past date nor a closed type window has no first response. |
| L-424 | D | invalidation.partial_acceptance; ladder_state; scenario_selection | Medium | Human | decided | 8 | Widening after D-074 names no scenario or rung. |
| L-425 | B,C,E,F | §2 Complexity Matching > Reschedule | Medium | Safe | fixed | 9 | Prose omitted the D-095 raise to the bound taxProCertLevel. |
| L-426 | B,C,D,E | workflow.reschedule_existing[3]; §2 Reschedule; scheduler_always type floors | Medium | Human | decided | 9 | D-095 floor collides with the fixed floors of emerald_advance, tax_notice_service, callback, physical_drop_off. |
| L-427 | B,C | workflow.schedule_new[1] | Medium | Safe | fixed | 9 | Keep-prior-Tax-Pro question had no D-084 exception. |
| L-428 | B,D,E | §1.5 terminal_payload_contract officeRef clause | Medium | Safe | fixed | 9 | "either handoff" left officeRef off routed_to_scheduler for another Tax Pro. |
| L-429 | E,F | §3 office_never[0] | Medium | Safe | fixed | 9 | Barred every appointment question after D-097. |
| L-430 | E,F | §4 Out-of-Scope (FAQ Agent); §2 Informational Interruptions | Low | Safe | fixed | 9 | faq_agent list missed out-of-task appointment-logistics; three spellings. |
| L-431 | A,C | §4 CDAS Callback Handoff; tax_pro_always callback item | Medium | Human | decided | 9 | Source of taxProRef and officeRef on a callback handoff undefined. |
| L-432 | A | invalidation.partial_acceptance on callback | Medium | Human | decided | 9 | Rejecting the carried Tax Pro on a callback restarts a ladder with no Tax Pro. |
| L-433 | A | global_always search_knowledge_base item | Medium | Human | decided | 9 | "mid-task" undefined; logistics owned by KB and faq_agent. |
| L-434 | D | workflow.schedule_new[1]; scenario_selection items 2-8 | Medium | Human | decided | 9 | Keep-prior answer discarded when items 2-6 match first. |
| L-435 | D | terminal_payload_contract; transfer_unavailable | Medium | Human | decided | 9 | Post-commit transfer exits report transactionOccurred false. |
| L-436 | D | Tax Pro Trade-off; returning_same_tax_pro rung 5 | Medium | Human | decided | 9 | Rung 5 question after a peak "stay" undefined. |
| L-437 | D | scheduler_always phone_callback item | Medium | Human | decided | 9 | Reason capture timing on an accepted phone_callback rung. |
| L-438 | D | §3 Cross-Office Restriction; office_never phone item | Medium | Human | asked | 9 | Rule cannot fire after D-044 and D-094; unchanged pending answer (Q-96). |
| L-439 | E | §2 State 3 Tax Pro Trade-off (prose) | Medium | Safe | fixed | 9 | Prose lacked the D-074 and D-090 rejected-Tax-Pro rule. |
| L-440 | E,F | global_always empathy item | Medium | Human | decided | 9 | "Promises no person" admits path-bound lines. |
| L-441 | E | §2 Tax Pro Requests; interruptions.intent_change | Medium | Human | decided | 9 | "to speak to" lost; a keep-prior answer reads as a Tax Pro request. |
| L-442 | C | global_outcomes.transfer_unavailable | Medium | Human | decided | 9 | leave_message_offer not tied to leaveMessageAvailable. |
| L-443 | C | §5.2 taxProPreference; scheduler_always | Medium | Human | decided | 9 | No rule sends taxProPreference or taxProRef to the search tools. |
| L-444 | C | §5.2 check_search_readiness issue | Medium | Human | decided | 9 | Conflict branches lack a discriminator; no change. |
| L-445 | C | §1.4 intro; global_always transfer results | Medium | Human | decided | 9 | Transfer paths with no row have no agent_available line. |
| L-446 | F | §2 write-tool entries | Low | Human | backlog | 9 | Repeated explicit-yes; consent echo kept. |
| L-447 | F | §1.5 persona_translation; §5.2 Callbacks, none_nearby; §2 State 5 transfer_to_agent; §2 Principles | Low | Safe | fixed | 9 | Five editorial trims (F-06, F-07, F-09, F-11, F-12). |
| L-448 | F | §1.5 global_outcomes.configuration_missing; agent_specific_tools.find_available_slots | Low | Safe | fixed | 9 | Trims of backlog L-346 and L-347 to fit the round budget. |
