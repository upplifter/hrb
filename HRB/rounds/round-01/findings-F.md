- anchor: §State 5 workflow.schedule_new
  also: §State 5 workflow.reschedule_existing; §State 5 workflow.cancel_existing
  severity: Low
  claim: The office-identity rule in scheduler_always[5] is restated in about 20 workflow clauses, and cancel_existing steps 6-7 restate it plus the no-closing-language rule from global_never and closure.principle.
  evidence: "use addressLine1Spoken plus addressLine2Spoken only when present and non-empty in the post-commit readback" | "6 Post-commit output. Do not use officeName in any post-commit readback or terminal outcome"
  class: safe
  fix: Delete every "officeName only" and spoken-address clause from the workflow steps, except reschedule_existing step 3's disambiguation condition. Cut each Close step to "Close. Follow closure" and keep previousSummary/canceledSummary. Delete cancel_existing steps 6-7.

- anchor: §State 5 agent_specific_tools.book_appointment
  also: agent_specific_tools.get_customer_appointments; agent_specific_tools.find_offices_near; agent_specific_tools.find_available_slots; agent_specific_tools.reschedule_appointment; agent_specific_tools.cancel_appointment
  severity: Low
  claim: Six tool entries restate the scheduler_always[5] rule on officeName versus spoken-address fields, each in different wording.
  evidence: "After success, confirmedSummary must use addressLine1Spoken plus addressLine2Spoken only when present and non-empty." | "Preserve the spoken address fields for post-commit output only."
  class: safe
  fix: Delete the officeName and spoken-address sentences and the "using officeName" phrases from these six entries, since scheduler_always[5] governs.

- anchor: §State 5 workflow.schedule_new[0]
  also: workflow.reschedule_existing[0]; workflow.cancel_existing[0]; scheduler_always[3]
  severity: Low
  claim: Each workflow step 1 restates the third-party authentication rule from scheduler_always[3] in 55-82 words.
  evidence: "Before any customer or appointment retrieval, determine whether the caller is acting for themselves or for another person." | "If ANI is unregistered or authentication fails, retrieve nothing, neither confirm nor deny that an appointment exists, and transfer."
  class: safe
  fix: Cut each step 1 to "1 Authentication before retrieval. Apply the authentication rule in scheduler_always; for the caller's own transaction, resolve identity normally."

- anchor: §Part 3 State 1 Office Contact Triage > If OPEN
  also: §Part 3 Office Contact Triage > If CLOSED; §Part 4 workflow.leave_message[1]; §5.1 transfer_to_agent; §5.2 get_customer_appointments; §5.2 find_offices_near; §5.3 check_office_open_status
  severity: Low
  claim: Eight clauses explain why instead of stating what happens, which editorial rule 5 bans.
  evidence: "The call reached the IVA because the local staff is busy." | "so the calling agent can confirm or offer a location before searching for times" | "Owns all time-math to ensure the agent never computes timezones."
  class: safe
  fix: Delete these reason clauses: "The call reached the IVA because...", "so the Head of Call flow can ask...", "so the caller knows when to try again", "so the deterministic flow can record the message", "so the caller does not start over", both "so the calling agent can..." clauses, and "to ensure the agent never computes timezones".

- anchor: §State 5 agent_specific_tools.transfer_to_agent
  also: §State 5 interruptions.intent_change; §Part 3 State 2 agent_specific_tools.transfer_to_agent; §Part 3 State 2 interruptions.intent_change; §Part 4 State 2 agent_specific_tools.transfer_to_agent; §Part 4 State 2 interruptions.intent_change
  severity: Low
  claim: Two barging sentences appear word for word in all three agent blocks, and constitution C-3 A moves such rules to the Base JSON.
  evidence: "Call this tool immediately when the caller explicitly requests a live agent (barging)." | "A direct request for a live agent is a barging event: suspend any transaction, call transfer_to_agent"
  class: safe
  fix: Add one global_always item that merges both sentences, and delete the six agent-block copies.

- anchor: §Part 3 State 2 interruptions.informational_question
  also: §Part 4 State 2 interruptions.informational_question; §State 5 interruptions.informational_question
  severity: Low
  claim: A 45-word informational_question rule is identical in all three agent blocks, and the Scheduler copy only adds gate-resume and confirmation-survival clauses.
  evidence: "An informational question is not a constraint change and invalidates nothing." | "then resume with a single targeted question."
  class: safe
  fix: Under C-3 A, move the shared text to one global_always item, delete the Office and Tax Pro keys, and cut the Scheduler value to its resume-point and confirmation-survival clauses.

- anchor: §State 5 workflow.schedule_new[1]
  also: scheduler_always[10]; scheduler_always[16]
  severity: Low
  claim: The 152-word step 2 restates the type-first, rollover, central-line, and acceptsAppointmentType rules from scheduler_always[10] and [16], and exceeds the 60-word item limit.
  evidence: "Establish the appointment type first and never infer it, then ask the method the type permits" | "Never offer an office returning acceptsAppointmentType false."
  class: safe
  fix: Cut step 2 to the method question with appointmentMethod token, the returning-client same-Tax-Pro question, "resolve the office per scheduler_always", "Apply the digital drop-off rules", and "Never infer the method".

- anchor: §State 5 workflow.schedule_new[5]
  also: workflow.reschedule_existing[5]; workflow.cancel_existing[3]; scheduler_always[38]; agent_specific_tools.reschedule_appointment; scheduler_never[5]
  severity: Low
  claim: The no-retry and no-cancel-and-recreate rules in scheduler_never[5] are restated in three workflow steps, scheduler_always[38], and the reschedule_appointment tool entry.
  evidence: "Never retry an indeterminate outcome." | "Never retry a write after a timeout or indeterminate outcome"
  class: safe
  fix: Delete "Never retry an indeterminate outcome" and "Never cancel and recreate" from the workflow steps and the tool entry, and cut scheduler_always[38]'s second sentence to "A human reconciles an indeterminate write, even after re-entry."

- anchor: §State 5 scheduler_always[17]
  also: invalidation.rejected_rollover_office; workflow.schedule_new[1]
  severity: Low
  claim: The rejected-rollover purge and ZIP rule appears three times in the Scheduler JSON in near-identical wording.
  evidence: "If the caller rejects a rollover office, treat it as a location change" | "A rejected rollover office is a location change."
  class: safe
  fix: Delete scheduler_always[17], and replace the rejection sentence in workflow.schedule_new[1] with "If rejected, apply invalidation.rejected_rollover_office."

- anchor: §Part 4 State 2 tax_pro_never[2]
  also: tax_pro_never[3]; §State 5 agent_specific_tools.transfer_to_agent
  severity: Low
  claim: Three agent-block rules repeat Base JSON rules (global_never[0], global_never[1], terminal_payload_contract), and C-3 A deletes such repeats.
  evidence: "Never speak or read back date of birth or ssnLast4, in whole or in part (global_never)." | "Never include dateOfBirth or ssnLast4 in the transfer summary."
  class: safe
  fix: Delete tax_pro_never[2], tax_pro_never[3], and the DOB/ssnLast4 sentence in the Scheduler transfer_to_agent entry.

- anchor: §State 5 workflow.schedule_new[4]
  also: workflow.reschedule_existing[4]; invalidation.text_confirmation; scheduler_always[9]
  severity: Low
  claim: The third-party text-destination rule in scheduler_always[9] is restated in two workflow steps and in invalidation.text_confirmation.
  evidence: "For a third-party booking, use the appointment owner's mobile number." | "For third-party booking or reschedule, the destination must be the appointment owner's mobile number."
  class: safe
  fix: Delete the third-party mobile-number sentence from both workflow step 5 entries and from invalidation.text_confirmation.

- anchor: How to Read This Document > Part 4
  also: How to Read This Document > Part 1; How to Read This Document > Part 2
  severity: Low
  claim: The Part 4 bullet restates the §1.3 Leave-a-Message rule, and the Part 1, 2, and 4 bullets exceed the 35-word or 2-sentence limit.
  evidence: "the agent returns control to the deterministic Leave a Message flow rather than capturing the message" | "Every state follows the same pattern: Business Intent & Rules first, then Mini-Dialogues."
  class: safe
  fix: Delete the Part 4 leave-a-message sentence, and cut the Part 1 and Part 2 bullets to at most 35 words and 2 sentences each.

- anchor: §State 5 objective
  also: scheduler_always[1]; scheduler_always[10]
  severity: Low
  claim: The 92-word objective restates the type-first rule from scheduler_always[10] and the gate rule from scheduler_always[1].
  evidence: "Establish the type before the appointment method and before any office lookup, and never infer it." | "Enforce the confirmation gate before every write."
  class: safe
  fix: Delete both sentences from objective.

- anchor: §State 5 scheduler_always[7]
  also: scheduler_always[6]; scheduler_always[11]; scheduler_always[12]; scheduler_always[13]
  severity: Low
  claim: The type exceptions in [6] and [7] repeat [11] and [13], [12] repeats the grouped-readback rule in [0], and [7] runs 108 words with redundant ordering words.
  evidence: "Administer the four-question complexity waterfall top down in decreasing order of complexity whenever it is triggered" | "skip both the complexity waterfall and the gatekeeper question" | "confirm the set once in a grouped readback"
  class: safe
  fix: Drop the emerald/tax_notice exceptions from [6] and [7], drop the readback clause from [12], cut "in decreasing order of complexity", and move the small_business_ind sentence into its own item.

- anchor: §5.1 Shared Tools > transfer_to_agent
  also: §1.2 Input Exhaustion & Silence > No-Input (Silence) Rule
  severity: Low
  claim: The tool description restates the §1.2 silence rule in prose and uses an all-caps "AND".
  evidence: "Never call this tool for consecutive silence or suspected robocalls." | "Silence must be handed back to the Head of Call for termination."
  class: safe
  fix: Replace both sentences with "Never call it on consecutive silence (see §1.2, Input Exhaustion & Silence)." and lowercase "AND".

- anchor: §5.1 Shared Tools > search_knowledge_base
  also: §5.1 search_knowledge_base > KB results
  severity: Low
  claim: The intro paragraph runs 5 sentences and restates the 0.85 confidence rule found in the KB results line.
  evidence: "Only provide the answer if confidence is 0.85 or higher." | "answer_found requires confidence at least 0.85"
  class: safe
  fix: Delete the confidence sentence, and merge the attempt and clarifier sentences into one so the paragraph has at most 3 sentences.

- anchor: §1.1 The Head of Call Envelope (Entry Context)
  also: none
  severity: Low
  claim: Table cells open with category labels that add no condition, number, or action.
  evidence: "Session Tracking. Unique identifier for the current session." | "Routing Telemetry. Ignore meetingMethod."
  class: safe
  fix: Delete the leading labels "Session Tracking.", "Time Awareness.", "Verbatim Intent.", "Routing Logic.", "System-Initiated Entry.", "Cross-Invocation Context.", "Strict Guardrails:", and "Routing Telemetry.".

- anchor: §1.2 Zero Web Deflection & Prohibited Speech
  also: §1.2 Hours: One Source, Spoken Once; §1.2 Input Exhaustion & Silence > No-Input (Silence) Rule; §1.2 Input Exhaustion & Silence > Abandonment; §1.2 Confirmation Strategy > Confirmed at capture
  severity: Low
  claim: Five §1.2 bullets exceed 2 sentences or 35 words and carry filler ("simply", "Do not confuse...").
  evidence: "When transitioning intents, simply offer the help directly" | "Do not confuse Support Hours with Retail Office Hours." | "An unanswered gate is not abandonment, it runs the No-Input Rule, then terminates."
  class: safe
  fix: Split the architecture bullet into a prohibited-words bullet and a unified-assistant bullet, delete "simply" and the "Do not confuse" sentence, and join sentences in the other bullets so each is at most 2 sentences with every trigger kept.

- anchor: §State 2 Tax Notice Services Guardrails
  also: §State 2 Complexity Matching & Tax Pro Rating Floor > Returning Client; Complexity Matching > Guardrails; §State 2 Dynamic State Invalidation > Action
  severity: Low
  claim: Several State 2 bullets exceed 2 sentences, the Tax Notice bullet label repeats its heading, and the Tax Extension bullet sits under the Tax Notice heading.
  evidence: "One invocation is still one transaction." | "The numeric rating (1-5) is an internal mandatory filter. Never speak it. Never relax it."
  class: safe
  fix: Merge sentences so each bullet is at most 2 sentences (e.g., "Guardrails: Never speak or relax the numeric rating (1-5); it is an internal mandatory filter."), and drop the redundant "Tax Notice Services:" label.

- anchor: §State 3 Readiness & Availability > Duration Logic
  also: §State 3 Readiness & Availability > CDAS; §State 3 Search Broadening Ladder > Principles; §State 4 Write Tools & Payload Mechanics
  severity: Low
  claim: Duration Logic, CDAS (53 words, 4 sentences), the slot-presentation principle, and the write-tool bullets exceed 2 sentences.
  evidence: "Speak durationSpoken exactly as returned. If uniformDuration is true, speak it once for the entire offer." | "The tool ranks named Tax Pros ahead of CDAS. Never filter out CDAS."
  class: safe
  fix: Split CDAS into a treat-as-CDAS bullet and a spoken-phrase bullet, and join sentences in the other bullets so each is at most 2 sentences.

- anchor: §Part 4 State 1 Intent Scope & Out-of-Scope Rerouting > Elicit the Reason First
  also: §Part 4 Fulfillment Priority; §State 5 scheduler_always[23]; scheduler_always[24]; invalidation.customer_identity; §State 4 Optional Text Confirmation > Third-Party; §5.1 search_knowledge_base > Category Enums
  severity: Low
  claim: Rules use third-person or "you must" phrasing instead of the imperative that loop/style.md requires.
  evidence: "The agent must never accept a generic" | "When a slot is treated as CDAS, you must speak 'with one of our tax professionals'"
  class: safe
  fix: Rewrite to the imperative (e.g., "Never accept a generic request at face value. Ask what it is regarding."; "you must speak" to "speak"; "you must ask exactly" to "ask exactly").

- anchor: §Part 5 Conventions Common to Every Tool
  also: none
  severity: Low
  claim: A 114-word, 2-sentence paragraph writes several field-alias mappings as one wall of prose.
  evidence: "context_envelope, Head of Call envelope, inbound JSON payload, and sessionEnvelope name the same input."
  class: safe
  fix: Split the paragraph into one bullet per alias group (envelope names, method fields and tokens, Tax Pro and office refs, appointment refs and summaries, rating scale, status fields), with no word change.

- anchor: §1.3 The Audio Seam & Terminal Handbacks > Leave-a-Message Ownership
  also: none
  severity: Low
  claim: A 104-word, 5-sentence paragraph exceeds the 3-sentence paragraph limit.
  evidence: "Agents never capture, solicit, record, transcribe, store, submit, or confirm delivery of a caller's message."
  class: safe
  fix: Split it into bullets of at most 2 sentences under the bold label (prohibition, leave_message trigger, leave_message_offer trigger, flow ownership and passed context), with no word change.

- anchor: §1.5 global_always[6]
  also: §State 5 scheduler_always[3]; scheduler_always[9]; scheduler_always[12]; scheduler_always[16]
  severity: Low
  claim: These JSON array items run 66-86 words each, above the 60-word item limit.
  evidence: "On the first no-match for a required field, reprompt once, shorter and rephrased, before counting a failure." | "Before any customer or appointment retrieval, determine whether the caller is acting for themselves or for another person."
  class: safe
  fix: Split each item into two array items at a sentence boundary (e.g., global_always[6] into no-match and no-input items), with no word change.

- anchor: §1.5 terminal_payload_contract
  also: §State 5 closure.line_patterns; closure.continuation_context; §1.5 global_outcomes.transfer_unavailable; agent_specific_tools.find_available_slots
  severity: Low
  claim: These JSON string values run 84-117 words, and trimming them below 60 would need a string-to-array or new-key restructure.
  evidence: "Return exactly one terminal payload with interactionId, operation, registeredAni, finalOutcome" | "committed (booking/reschedule): state the outcome and the essential appointment details."
  class: human
  decision: json-string-over-60-restructure
