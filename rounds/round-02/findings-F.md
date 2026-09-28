- anchor: §2 State 5 scheduler_never (slot-order and silent-relax item)
  also: §2 State 5 workflow.schedule_new[3]; workflow.reschedule_existing[3]
  severity: Low
  claim: The scheduler_never item and both workflow step 4 entries restate broadening.principles on consent per rung and the never-relaxed floor, and step 4 also restates the physical_drop_off null-floor rule.
  evidence: "Never silently relax a Tax Pro, office, date, time-window or method constraint" | "Obtain an explicit yes before each rung." | "with caller consent and never relax the floor or credentialRequired" | "except physical_drop_off where it is null"
  class: safe
  fix: Cut the scheduler_never item to "Never re-order, re-rank, promote, or filter returned slots."; in both step 4 strings delete the consent and never-relax clauses; in reschedule step 4 delete "except physical_drop_off where it is null" (scheduler_always floor item keeps it).

- anchor: §4 Fulfillment: Leave a Message > Handoff
  also: §4 Fulfillment: CDAS Callback Appointment > Handoff; §4 Tax Pro Lookup & Disambiguation > Generic Request
  severity: Low
  claim: The two Handoff bullets and the Generic Request bullet restate §1.3 Leave-a-Message Ownership, and the CDAS bullet opens in third person.
  evidence: "finish the current sentence, stop speaking, and return the terminal payload with nextAction = leave_message" | "The Speak to a Tax Pro agent triages the request but does not book the calendar slot." | "If the caller explicitly requests to leave a message, return control with nextAction = leave_message."
  class: safe
  fix: Leave a Message Handoff becomes "Once the caller opts in, hand back per §1.3 Leave-a-Message Ownership, passing the resolved taxProRef or officeRef."; CDAS Handoff opens "Never book the callback slot." and keeps the route_intent sentence; delete the Generic Request third sentence.

- anchor: §3 State 2 objective
  also: §3 State 2 office_always[0]; §3 State 2 interruptions.intent_change
  severity: Low
  claim: The objective restates office_always and office_never, office_always[0] restates global_never, and intent_change restates the intent_changed outcome for an agent that never commits a transaction.
  evidence: "rely entirely on deterministic API tools for hours and timezones" | "You do not schedule appointments." | "Never speak internal IDs or raw system variables." | "outside office information, close any committed transaction, then hand back intent_changed"
  class: safe
  fix: Cut the objective to its first sentence; delete the second sentence of office_always[0]; cut intent_change to "If the caller moves to something outside office information, hand back intent_changed."

- anchor: §2 State 5 broadening.principles
  also: §1.5 global_never (prohibited-phrases item)
  severity: Low
  claim: principles[0] says the one-relaxation rule twice, principles[4] repeats a global_never ban, principles[7] restates scheduler_never's method_descriptions rule with "must", and global_never names a phrase already on the list it points to.
  evidence: "Never chain two relaxations in one offer." | "Never say 'due to time sensitivities'." | "Digital drop-off and virtual appointments are different and must be described differently." | "Never say 'due to time sensitivities' or any phrase on global_voice_lexicon.prohibited_phrases"
  class: safe
  fix: Delete "Never chain two relaxations in one offer." and "Never say 'due to time sensitivities'." from principles, delete principles[7], and cut the global_never item to "Never say any phrase on global_voice_lexicon.prohibited_phrases."

- anchor: §5.1 search_knowledge_base (intro paragraph)
  severity: Low
  claim: The second intro sentence restates the KB results line below the response.
  evidence: "It returns a customer-safe answer already phrased for speech, a clarification prompt" | "requires_tax_pro routes to a Tax Pro"
  class: safe
  fix: Delete the intro's second sentence.

- anchor: §2 State 5 scheduler_always (post-commit readback item)
  severity: Low
  claim: The item restates global_always's final-turn rule and closure.principle, a Base rule repeated in an agent block (C-3 A).
  evidence: "Speak the post-commit readback as your final spoken turn, finish the sentence, stop speaking" | "End the final turn with the outcome, finish the current sentence, stop speaking" | "Your readback is your last spoken turn."
  class: safe
  fix: Delete the scheduler_always post-commit readback item.

- anchor: §2 State 1 Authentication Logic > State Persistence
  severity: Low
  claim: The bullet restates the §1.1 customerRef rule in different words.
  evidence: "treat the caller as authenticated. Do not re-run `find_customer` unless the transaction subject changes" | "If present, do not re-authenticate unless the transaction subject changes."
  class: safe
  fix: Replace the bullet text with "Apply the customerRef rule (see §1.1, The Head of Call Envelope)."

- anchor: §5.2 reschedule_appointment (Note and Changing Array bullet)
  severity: Low
  claim: The Note and the Changing Array bullet describe the same field in 53 words, including an explanatory clause.
  evidence: "Note: changing may contain date, time, office, and taxPro." | "even though the replacement slot includes the preserved time"
  class: safe
  fix: Delete the Note and make the bullet "**Changing Array:** changing lists which of date, time, office, and taxPro differ from the bound appointment; unchanged lists the rest (e.g., a day-only reschedule sends date only)."

- anchor: §2 State 5 scheduler_always (emerald_advance, tax_notice_service, and callback items)
  severity: Low
  claim: Three type items each restate the same skip-waterfall and floor-1 clause.
  evidence: "skip both the complexity waterfall and the gatekeeper question"
  class: safe
  fix: Put one clause in the emerald_advance item ("On emerald_advance, tax_notice_service, and callback, skip both the complexity waterfall and the gatekeeper question and send taxProRatingFloor as 1") and cut that clause from the tax_notice and callback items, keeping callback's phone_callback and target-tool wording.

- anchor: §5.2 check_search_readiness (Note paragraph)
  also: §5.1 transfer_to_agent (intro paragraph); Part 5 Conventions > Spoken-field governance; §5.2 get_customer_appointments > Cognitive Overload Protection
  severity: Low
  claim: The readiness Note is a 72-word wall that repeats the needs_more row, the transfer_to_agent intro runs 4 sentences, and the other two bullets run 3 sentences.
  evidence: "askFor names the missing request field" | "One more constraint is needed. askFor names it." | "Answers one question: can a live representative take this call right now?" | "Do not read the list aloud. Transfer immediately using"
  class: safe
  fix: Split the readiness Note into bullets (seasonPhase, out_of_scope, callbacks, issue) and drop the askFor clause; merge the transfer_to_agent intro into two sentences keeping lastQuestionSpoken and knownSoFar; cut the other two bullets to two sentences.

- anchor: PART 5 intro paragraph
  severity: Low
  claim: The Part 5 intro spends 42 words to say the tools serve every agent type that exchanges JSON.
  evidence: "This section specifies the deterministic tools available to H&R Block conversational AI agents." | "The contract holds for real-time speech-to-speech (RT S2S) agents"
  class: safe
  fix: Replace with "These deterministic tools serve RT S2S agents, Cascade agents, and any agent that exchanges JSON requests and responses."

- anchor: §2 State 5 agent_specific_tools.search_knowledge_base
  also: §3 State 2 agent_specific_tools.search_knowledge_base; §4 State 2 agent_specific_tools.search_knowledge_base
  severity: Low
  claim: The same string appears in all three agent blocks and restates the global_always search_knowledge_base item (C-3 A).
  evidence: "Answer approved informational questions without invalidating transaction state." | "keep everything in STATE"
  class: safe
  fix: Set each of the three values to "Per global_always."

- anchor: §2 State 5 objective
  severity: Low
  claim: The objective's last sentence restates base_persona's division of reasoning and tool work (C-3 A); the lint flags the string at 68 words.
  evidence: "Ask, confirm, disambiguate and hold state yourself; call tools to resolve identity" | "You do all conversational reasoning; deterministic tools do business logic"
  class: safe
  fix: Delete the objective's last sentence and leave the other sentences untouched (L-091 is open on them).

- anchor: §2 State 5 scheduler_never (date-of-birth readback item)
  severity: Low
  claim: The item restates global_never's DOB and ssnLast4 ban in an agent block (C-3 A).
  evidence: "Exclude date of birth and ssnLast4 from the pre-commit readback and never speak them" | "Never speak or read back date of birth or ssnLast4, in whole or in part."
  class: safe
  fix: Delete the scheduler_never date-of-birth item.

- anchor: §2 State 5 agent_specific_tools.find_available_slots
  severity: Low
  claim: The 74-word entry restates the scheduler_always duration rule and the trigger that scenario_selection item 7 already states.
  evidence: "Speak durationSpoken exactly as returned and apply the CDAS and ladder rules." | "A noResults of office_at_capacity during peak triggers peak_capacity per scenario_selection item 7."
  class: safe
  fix: Change the duration sentence to "Apply the duration, CDAS, and ladder rules." and delete the last sentence.

- anchor: §5.2 find_available_slots > Any-One-Of Matching
  severity: Low
  claim: The 45-word, 3-sentence bullet can say the same in two sentences, and "either" narrows the set to two credentials.
  evidence: "A Tax Pro holding either credential qualifies." | "is never relaxed or substituted by the numeric rating floor to manufacture a match"
  class: safe
  fix: Rewrite as "credentialRequired (e.g., ["EA", "CPA"]) matches a Tax Pro holding any one listed credential. The appointment type sets it; never relax it or substitute the rating floor for it."

- anchor: §4 Intent Scope & Out-of-Scope Rerouting (Refund Status, FAQ Agent, New Appointment bullets)
  also: §4 State 1 Business Intent intro; §4 State 2 objective; §4 agent_specific_tools.search_tax_pro_by_name; §5.4 search_tax_pro_by_name intro
  severity: Low
  claim: The out-of-scope bullets pad the handback with "transition immediately to ... via", and Part 4 and Part 5 rules say "Tax Professional" where the style guide requires "Tax Pro".
  evidence: "transition immediately to the FAQ Agent via intent_changed with routingTarget = faq_agent" | "transition immediately to the deterministic Refund Status Flow via intent_changed" | "Handle caller inquiries requesting to speak directly with a Tax Professional"
  class: safe
  fix: Write each bullet's action as "hand back intent_changed with routingTarget = <target>" and replace "Tax Professional(s)" with "Tax Pro(s)" in rule text.

- anchor: §1.1 The Head of Call Envelope (priorTransaction, entryReason, registeredAni rows)
  severity: Low
  claim: The priorTransaction cell runs 5 sentences, entryReason runs 4 "Do not" sentences, and registeredAni uses "3rd-party" where the spec uses "third-party".
  evidence: "It never authorizes a write. It never replaces retrieval. It is never trusted over the system of record." | "Open directly on booking. Do not ask intent." | "Mandatory for 3rd-party authentication."
  class: safe
  fix: priorTransaction becomes "Previous operation and outcome. Never authorizes a write, replaces retrieval, or outranks the system of record; wipe completely on identity change."; entryReason becomes one "never" sentence; replace "3rd-party" with "third-party".

- anchor: §1.5 base_persona
  severity: Low
  claim: The 76-word persona restates global_always[0] and the turn_length lexicon entry.
  evidence: "You are the sole spoken interface for this real-time speech-to-speech transaction." | "You are the only agent authorized to speak to the caller."
  class: safe
  fix: Replace the first two sentences with "H&R Block real-time speech-to-speech IVA." and cut "Everyday language, contractions, brief turns." to "Everyday language and contractions."

- anchor: §2 State 5 invalidation.rejected_rollover_office
  severity: Low
  claim: The last sentence restates the scheduler_always central-line item.
  evidence: "Capture and validate a five-digit ZIP, then call find_offices_near and return the three nearest eligible offices" | "capture a validated five-digit ZIP and return the three nearest eligible offices for caller selection"
  class: safe
  fix: Replace the last sentence with "Then resolve the office per the scheduler_always central-line item."

- anchor: §1.3 The Audio Seam & Terminal Handbacks (intro sentence)
  severity: Low
  claim: The third-person intro restates the Yield, Do Not Solicit bullets.
  evidence: "The agent completes transactions and answers questions; it does not end calls." | "The Head of Call flow owns the close."
  class: safe
  fix: Delete the intro sentence.

- anchor: §4 State 2 tax_pro_always (by-name and multiple-match items)
  also: §4 State 2 interruptions.intent_change
  severity: Low
  claim: tax_pro_always[3] restates the disambiguation that [2] already requires, and intent_change carries a closing clause for an agent that never commits a transaction.
  evidence: "handle disambiguation if matchedTpCount is greater than 1" | "If multiple matches, disambiguate by location using the primaryOfficeName field." | "outside reaching a Tax Pro, close any committed transaction"
  class: safe
  fix: In [2] write "disambiguate by location using primaryOfficeName if matchedTpCount is greater than 1", delete [3], and cut intent_change to "If the caller moves to something outside reaching a Tax Pro, hand back intent_changed."

- anchor: §1.2 Confirmation Strategy > Exceptions (DOB & SSN)
  severity: Low
  claim: The bullet restates the Zero Readback bullet in the PII section of the same heading.
  evidence: "Never speak a Date of Birth or SSN back to the caller." | "Never speak or read back DOB or SSN in any form."
  class: safe
  fix: Replace the bullet text with "Exempt from every readback (see §1.2, PII & IRS Sec. 7216 Compliance)."

- anchor: §2 State 2 Tax Notice Services Guardrails > Notice Capture Sequence
  severity: Low
  claim: The 40-word, one-sentence bullet restates the §1.2 grouped-capture rule.
  evidence: "acknowledging each briefly, then confirm all five in a single grouped readback before the search" | "ask for them one by one with brief acknowledgments"
  class: safe
  fix: Rewrite as "Capture the five notice values one per turn in fixed order (Letter Date, Respond-By Date, Notice Code, Tax Year, POM Status) as a grouped capture (see §1.2, Confirmation Strategy), before the search."

- anchor: §1.2 Voice Persona & Delivery (jargon bullet)
  also: §1.2 Spoken Office Identity Fallback; §2 State 1 Authentication Logic (Third-Party, single_match, New Customers bullets); §2 State 2 Appointment Type table tax_prep row; §2 State 3 Dynamic State Invalidation: Location & Time > Action
  severity: Low
  claim: These bullets and cells break the 35-word or 2-sentence limit, according to lint-before.
  evidence: "Do not use corporate jargon, IVR-style prompts, or multi-part explanations." | "Reserve the full address for post-commit summaries in the Appointment Scheduler" | "Proceed only on single_match. On failure or unregistered ANI" | "A location change also purges the assigned Tax Pro."
  class: safe
  fix: Split the jargon bullet at "Never say" and the office bullet before "Reserve", and merge sentence pairs in the other bullets and cells so each has at most two; keep "Profile creation is deferred to the book_appointment commit" verbatim (L-094 open).
