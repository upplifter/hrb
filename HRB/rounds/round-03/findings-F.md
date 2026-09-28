- anchor: §2 State 5 closure.principle
  also: §1.5 global_always (final-turn item); §1.5 global_never (close item)
  severity: Low
  claim: closure.principle restates the Base JSON final-turn and Head-of-Call-owns-the-close rules in about 45 extra words (C-3 A).
  evidence: "the Head of Call flow owns the close, the additional-help question" | "Stop speaking, emit the one terminal payload" | "End the final turn with the outcome, finish the current sentence"
  class: safe
  fix: Cut closure.principle to "Your readback is your last spoken turn; close per global_always and global_never."

- anchor: §3 State 2 workflow.office_info_flow[2], office_contact_flow[3], office_contact_flow[4]
  also: §3 State 2 office_always[3], office_always[5], office_always[6]
  severity: Low
  claim: The workflow steps restate the office_always blurb, OPEN, and CLOSED items in the same JSON block.
  evidence: "If OPEN, explain staff is busy, stop speaking" | "state that the staff is helping other clients, stop speaking" | "If CLOSED, state closure, read upcoming hours"
  class: safe
  fix: Reduce each workflow step to a pointer (e.g., "3. Apply the office_always OPEN item.") and keep the full rule in office_always.

- anchor: §2 State 5 interruptions.cancel_said
  also: §2 State 5 interruptions.intent_change; §1.5 global_outcomes.intent_changed
  severity: Low
  claim: cancel_said carries a rationale clause and a restated one-transaction rule, and intent_change restates the intent_changed outcome's close-first rule.
  evidence: "nothing has been written, so abandon the booking" | "rather than starting a second transaction here" | "do not transfer and do not attempt it yourself"
  class: safe
  fix: Cut the "nothing has been written, so" and "rather than starting a second transaction here" clauses; rewrite intent_change as "If the caller moves outside scheduling, other than a cancellation or a request for a person, never transfer or attempt it; hand back intent_changed."

- anchor: §2 State 5 workflow.schedule_new[0], reschedule_existing[0], cancel_existing[0]
  severity: Low
  claim: Three step-1 strings end with a filler clause that adds no condition or action.
  evidence: "for the caller's own booking, resolve identity normally" | "for the caller's own appointment, resolve identity normally"
  class: safe
  fix: Cut "; for the caller's own booking/appointment, resolve identity normally" from all three steps.

- anchor: §2 State 5 (intro paragraph)
  also: §3 State 2 (intro paragraph); §4 State 2 (intro paragraph); §1.5 (intro paragraph)
  severity: Low
  claim: The same two-sentence merge statement is repeated before all three agent JSON blocks (lint dup_prose).
  evidence: "This JSON block merges with the Universal Base JSON at runtime" | "This JSON block is inherited by all agents"
  class: safe
  fix: Delete the three agent intro paragraphs and change the §1.5 intro's first sentence to "Every agent inherits this JSON block and merges its own agent-specific block with it at runtime."

- anchor: §3 State 2 agent_specific_tools.get_office_details, check_office_open_status
  also: §4 State 2 agent_specific_tools.search_tax_pro_by_name; §3 office_never[1]; §1.5 global_voice_lexicon.spoken_field_governance
  severity: Low
  claim: These tool entries repeat Part 5 tool descriptions and restate the time-math and spoken-field rules that the same block and the Base JSON already carry.
  evidence: "Retrieves comprehensive operating metadata, address" | "Owns all time math" | "Searches Enterprise Data Services for Tax Pros matching spoken names"
  class: safe
  fix: Reduce each entry to "Read-only." and delete "Preserve addressDirectionsSpoken as written." and "Owns all time math."

- anchor: §2 State 5 scheduler_always (returning-client gatekeeper item; waterfall item)
  severity: Low
  claim: The gatekeeper and waterfall items are wordy; the default-floor clause repeats the floors item's "all no answers leave it at 1".
  evidence: "compute the inherited baseline floor as the higher of the two" | "whether anything has significantly changed with their tax situation since last year" | "starting from the default level 1 floor"
  class: safe
  fix: Rewrite as "For a returning client, set the baseline floor to the higher of the find_customer client complexity and prior Tax Pro cert level, then ask once whether anything significantly changed since last year." Cut ", starting from the default level 1 floor".

- anchor: §1.5 global_always (confirm-at-capture item; one-question item)
  also: §1.5 global_never[0]; global_voice_lexicon.questions_per_turn, names, number_formatting
  severity: Low
  claim: Several Base JSON strings restate another Base JSON string (DOB/SSN no-readback, one question per turn, confirmation numbers, third-party naming).
  evidence: "neither ever receives a spoken confirmation turn" | "Exactly one primary question per turn, placed at the end" | "Never speak a confirmation number"
  class: safe
  fix: Cut global_always DOB sentence to "Date of birth and ssnLast4 are exempt."; cut the first sentence of questions_per_turn; cut "Never speak a confirmation number." and "Never assume they share the appointment owner's last name."

- anchor: §2 State 5 scheduler_always (tax_notice capture item; tax_notice method item)
  also: §2 State 5 workflow.schedule_new[2]
  severity: Low
  claim: The capture timing and send-all-five rules are stated twice more in the same block.
  evidence: "with notice values already captured before the office lookup" | "and still capture and send all five notice values" | "immediately after the appointment type is established and before the office lookup"
  class: safe
  fix: Cut "with notice values already captured before the office lookup" from step 3 and ", and still capture and send all five notice values" from the method item.

- anchor: §4 State 2 tax_pro_never[1]
  also: §4 State 2 tax_pro_always (options item)
  severity: Low
  claim: tax_pro_never[1] repeats the options item's rule against yes/no questions and its wait-for-intent rule.
  evidence: "Never ask a direct yes/no question about leaving a message" | "state the options without asking a yes/no question"
  class: safe
  fix: Delete tax_pro_never[1].

- anchor: §3 Office Contact Triage > If OPEN
  also: §3 Office Contact Triage (first bullet); §3 Office Details Logic > By-Appointment-Only
  severity: Low
  claim: If OPEN (48 words) carries a rationale clause, the first bullet is a third-person fragment, and By-Appointment-Only runs 39 words in 4 sentences (lint length).
  evidence: "so the Head of Call flow can ask how the system can help them today" | "Relies strictly on" | "Do not ask if they want to book one"
  class: safe
  fix: If OPEN: say the quoted line, then "Never give the main line number; stop speaking and return nextAction = capture_intent."; first bullet: "Evaluate open status only with `check_office_open_status`; never do time math."; By-Appointment-Only: "state that the office is by appointment only, never quote standard daily hours or offer to book, then stop speaking and return nextAction = route_intent with routingTarget = appointment_scheduler."

- anchor: §1.2 Confirmation Strategy > Confirmed by consequence
  severity: Low
  claim: The bullet ends with an explanation sentence, against editorial rule 5.
  evidence: "The system proves it understood by what it says next"
  class: safe
  fix: Rewrite as "For everything else, never spend a turn asking 'Did I get that right?'"

- anchor: §4 Fulfillment: Leave a Message > Destination Selection
  also: §4 Fulfillment: Leave a Message > Handoff
  severity: Low
  claim: The two bullets both say to pass the known destination on a caller's message choice.
  evidence: "pass the known destination; the deterministic flow resolves" | "hand back per §1.3 Leave-a-Message Ownership, passing"
  class: safe
  fix: Merge into one bullet: "**Handoff:** When the caller opts to leave a message, hand back per §1.3, Leave-a-Message Ownership, passing any known taxProRef or officeRef."

- anchor: §3 State 1 Business Intent & Rules (intro paragraph)
  also: §3 Intent Scope & Disambiguation > Out of Scope
  severity: Low
  claim: The intro restates the Out of Scope bullet, and that bullet uses third person with "route".
  evidence: "without attempting to schedule or modify appointments" | "immediately hands back intent_changed to route"
  class: safe
  fix: Cut "without attempting to schedule or modify appointments" from the intro; rewrite Out of Scope as "On any request to schedule, reschedule, or cancel, hand back intent_changed with routingTarget = appointment_scheduler."

- anchor: §2 State 5 agent_specific_outcomes.no_acceptable_availability
  also: §2 State 5 broadening.principles[2]
  severity: Low
  claim: The outcome restates the never-relax-floor principle.
  evidence: "The mandatory Tax Pro rating floor and credentialRequired were never relaxed" | "Never relax taxProRatingFloor or credentialRequired at any rung"
  class: safe
  fix: Delete the sentence from no_acceptable_availability.

- anchor: §2 State 5 interruptions.informational_question
  also: §2 State 5 scheduler_always (explicit-yes item)
  severity: Low
  claim: The second sentence repeats the explicit-yes item's rule that any interruption voids the yes.
  evidence: "A yes given before the interruption is void" | "any interruption after the yes voids it, so re-read"
  class: safe
  fix: Delete "A yes given before the interruption is void; re-read the gate and ask again."

- anchor: §3 State 2 office_never[4]
  also: §4 State 2 tax_pro_never[0]; §1.5 global_always (leave-message item)
  severity: Low
  claim: Both agent strings restate the global_always leave_message_offer return (lint dup_json).
  evidence: "let the deterministic flow handle the offer" | "When transfer is unavailable and messaging may be offered"
  class: safe
  fix: In both strings replace "Return leave_message_offer and let the deterministic flow handle the offer." with "Return leave_message_offer per global_always."

- anchor: §1.5 base_persona
  severity: Low
  claim: base_persona is 66 words (JSON limit 60); the last sentence is wordy.
  evidence: "You do all conversational reasoning; deterministic tools do business logic"
  class: safe
  fix: Rewrite the last sentence as "You own the conversation; deterministic tools own business logic, JSON in and JSON out."

- anchor: §4 Intent Scope & Out-of-Scope Rerouting > Out-of-Scope (FAQ Agent)
  severity: Low
  claim: The bullet is 38 words (limit 35) and pads each trigger.
  evidence: "MyBlock credential issues, password resets"
  class: safe
  fix: Rewrite as "If the elicited reason is a general tax, login, MyBlock credential, password, account access, income tax course, loan, fee, or penalty question, hand back intent_changed with routingTarget = faq_agent."

- anchor: §5.2 find_available_slots (Note after Request JSON)
  also: §5.2 book_appointment (Note after New Customer request)
  severity: Low
  claim: Both notes are 4-sentence paragraphs listing field-to-value facts, over the 3-sentence paragraph limit.
  evidence: "Self-filing is a handback, not a slot-search rung" | "peaceOfMindStatus is boolean" | "remain backend field names"
  class: safe
  fix: Split each note into one bullet per field, keeping every sentence's wording.

- anchor: §1.5 global_outcomes.handoff_invalid
  also: §2 State 5 scheduler_always (entryPoint item); invalidation.customer_identity; §2 State 1 Dynamic State Invalidation: Identity
  severity: Low
  claim: JSON and rules use sessionEnvelope and "Head of Call envelope" for the input the JSON key names context_envelope.
  evidence: "The inbound sessionEnvelope is unusable" | "arrive on the Head of Call envelope" | "preserve the Head of Call envelope"
  class: safe
  fix: Replace "sessionEnvelope" and "Head of Call envelope" in these strings and bullets with "context_envelope".

- anchor: §2 State 5 scheduler_always (floor item; third-party text item); §1.5 global_never (unified item)
  also: Part 5 Conventions Common to Every Tool (Spoken fields bullet)
  severity: Low
  claim: Hard limits use "must" or "do not" instead of "never", and one string ends with a rationale sentence.
  evidence: "taxProRatingFloor must be null" | "do not read it back" | "The caller must feel they are speaking"
  class: safe
  fix: Use "send taxProRatingFloor as null", "never read it back", "Never reformat, round, recompute, or replace it"; replace the unified sentence with "; speak as one unified representative."

- anchor: How to Read This Document
  severity: Low
  claim: The Part labels name the parts differently from their headings.
  evidence: "Part 1, The Universal Trunk" | "PART 1: Pre-Handoff" | "PART 2: The Appointment Scheduler RT S2S Lifecycle"
  class: safe
  fix: Change each bold Part label to the matching `# PART N` heading title.

- anchor: §4 Tax Pro Lookup & Disambiguation > By Name Request
  severity: Low
  claim: By Name Request is an empty bullet; its four cases sit as siblings instead of nested sub-bullets.
  evidence: "By Name Request"
  class: safe
  fix: Indent Location Context, 1 Match, Multiple Matches, and No Matches / Inactive as sub-bullets of By Name Request.

- anchor: §2 State 2 Tax Notice Services Guardrails > Tax Extension
  severity: Low
  claim: The Tax Extension bullet sits under the Tax Notice Services Guardrails heading, and moving it has more than one plausible home.
  evidence: "Tax Extension:** One invocation"
  class: human
  decision: tax-extension-bullet-home
