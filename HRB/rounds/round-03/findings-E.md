- anchor: §2 State 5 scheduler_always (digital drop-off item)
  also: §2 State 2 Digital Drop-Off (DDO) Rules > Rescheduling; workflow.reschedule_existing
  severity: Medium
  claim: D-017's rule that a DDO change request is a new schedule_new DDO send reached the prose only, so the runtime JSON would run reschedule_existing and search for an appointment that does not exist.
  evidence: "Handle a requested change as a new schedule_new DDO send in the Scheduler." | "For digital drop-off, execute send_secure_link instead of book_appointment."
  class: safe
  fix: Append "A DDO change request is a new schedule_new DDO send." to the scheduler_always digital drop-off item.

- anchor: §5.2 get_customer_appointments Outcome Results
  also: §2 State 5 agent_specific_outcomes.appointment_already_canceled
  severity: Medium
  claim: Every result row counts only active appointments, so the tool never returns a canceled bound appointment and appointment_already_canceled (D-021) cannot fire.
  evidence: "No active future appointments exist." | "get_customer_appointments returned the bound appointment with status canceled"
  class: human
  decision: canceled-appointment-return-scope

- anchor: §4 State 2 tax_pro_always (callback item)
  also: §4 Intent Scope & Out-of-Scope Rerouting > Out-of-Scope (New Appointment); interruptions.intent_change
  severity: Medium
  claim: The prose (D-018) sends any new tax_prep request to appointment_scheduler and keeps callbacks for a confirmed Tax Pro, but the Part 4 JSON has no such rule, so a "phone appointment" request could be treated as a callback.
  evidence: "If the caller requests a new tax prep appointment in any method" | "If the caller moves to something outside reaching a Tax Pro, hand back intent_changed."
  class: safe
  fix: Append to the tax_pro_always callback item "A new tax_prep request in any method returns intent_changed with routingTarget appointment_scheduler; a callback only reaches a confirmed Tax Pro."

- anchor: §3 State 2 office_always (OPEN item)
  also: §3 Office Contact Triage > If OPEN; workflow.office_contact_flow[1]
  severity: Medium
  claim: The prose bans giving the main line number when the office is open, but the JSON OPEN item omits the ban while the flow fetches mainPhoneSpoken first.
  evidence: "Do not provide the main line number to call directly." | "state that the staff is helping other clients, stop speaking, and return nextAction capture_intent" | "Call get_office_details to retrieve mainPhoneSpoken."
  class: safe
  fix: In the OPEN item, insert "never speak mainPhoneSpoken," after "state that the staff is helping other clients,".

- anchor: §2 State 5 invalidation.upstream_change
  also: §2 State 2 Dynamic State Invalidation: Type & Method Edge Cases
  severity: Medium
  claim: The JSON still omits the prose re-check of method/office eligibility and the floor after a type or method change, and the channel-rung readiness skip (L-098 was reverted, not fixed).
  evidence: "re-derive the floor, and re-run readiness except when accepting a channel rung" | "Purge invalid state, update the constraint, check readiness, and search only on ready."
  class: safe
  fix: Rewrite as "Any upstream constraint change invalidates returnedSlots, selectedSlotRef, and confirmationStatus (not text opt-in); location change also invalidates taxProRef, except on accepting same_tax_pro_nearby_offices. A permitted Tax Pro trade-off invalidates taxProRef and dependent slots. A type or method change re-checks method/office eligibility and the floor. Purge, update the constraint, check readiness except on an accepted channel rung, and search only on ready." (59 words)

- anchor: §1.2 PII & IRS Sec. 7216 Compliance > Tax/Financial Boundary
  also: §1.5 global_always (informational-question item); §1.5 global_always (followUpTopics item)
  severity: Medium
  claim: The prose hands advice, calculation, and notice questions to a Tax Pro, but the JSON hands "general tax questions" to faq_agent and returns no_approved_answer outside the Scheduler (D-025), so the target for a personal tax question is unclear.
  evidence: "Hand loan, fee, and penalty questions to faq_agent, and the rest to a Tax Pro." | "faq_agent for login, password, account, income tax course, loan, fee, penalty, or general tax questions" | "Any other non-answer returns no_approved_answer."
  class: human
  decision: tax-advice-question-target

- anchor: §1.5 global_voice_lexicon.prohibited_phrases
  also: §1.2 Zero Web Deflection & Prohibited Speech (internal-architecture bullet)
  severity: Medium
  claim: The prose allows "transfer" when it refers to a live human agent, but the frozen lexicon bans "transfer you to" in every case, and it lacks the prose ban on "scheduling department".
  evidence: "'transfer' (unless referring to a live human agent)" | "transfer you to"
  class: human
  decision: transfer-word-for-live-agent

- anchor: §2 State 5 agent_specific_tools.check_search_readiness
  also: §1.4 needs_more (askFor) row; §5.2 check_search_readiness Outcome Results
  severity: Medium
  claim: The prose and Part 5 define a needs_more result that asks exactly the askFor item, but the Scheduler JSON handles only ready and out_of_scope.
  evidence: "Ask exactly the one missing item, in plain words, as a single question" | "On out_of_scope, call transfer_to_agent with transferReason out_of_scope."
  class: safe
  fix: Append "On needs_more, ask only the askFor item as one question at the end of the turn." to agent_specific_tools.check_search_readiness.

- anchor: §3 State 2 agent_specific_outcomes.office_open_unanswered
  also: §3 Office Contact Triage > If OPEN; §3 Mini-Dialogue 3C
  severity: Medium
  claim: The prose OPEN rule fires for any office_contact caller, including one who asks for the front desk, but the outcome covers only callers whose open office did not answer, so that case has no outcome.
  evidence: "Caller reached the IVA because the open office did not answer." | "Transfer me to someone at the front desk."
  class: human
  decision: office-open-outcome-scope

- anchor: §1.5 global_always (one-question-per-turn item)
  also: §1.2 Voice Persona & Delivery (multi-question bullet); §2 State 5 scheduler_always multi-value capture item
  severity: Low
  claim: The prose requires a one-line purpose before any multi-question sequence, but no JSON item carries it.
  evidence: "Frame any multi-question sequence with a one-line purpose" | "Ask exactly one primary question per turn and place it at the end."
  class: safe
  fix: Append "Open a multi-question sequence with a one-line purpose." to the global_always one-question-per-turn item.

- anchor: §2 Mini-Dialogue 1B
  also: §2 Mini-Dialogue 2B; §1.5 global_always (latency preamble item)
  severity: Low
  claim: Two frozen Agent turns speak the latency preamble "Let me take a look" when no tool call is in progress, against the preamble rule.
  evidence: "Let me take a look. And his date of birth?" | "Let me take a look, and which tax year is it about?" | "Speak a short latency preamble when a tool call will take noticeable time"
  class: human
  decision: frozen-dialogue-preamble-misuse
