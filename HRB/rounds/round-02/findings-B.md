- anchor: §2 State 1 Authentication Logic (failure bullet)
  also: §2 State 5 scheduler_always (unregistered ANI item); §1.5 global_always (transfer_to_agent item); §1.4 Authentication failed, multiple_matches, too_many, no_acceptable_availability rows
  severity: High
  claim: Part 2 speaks the person-promising recovery line before calling transfer_to_agent, while Base JSON requires the call before any promise of a person, and only D-007 settled the order for outcome_unknown.
  evidence: "speak the approved recovery line, then call `transfer_to_agent` without retrieval" | "before promising a person, and handle its results exactly as specified under tools" | "Let me get you to someone who can take another look."
  class: human
  decision: recovery-line-vs-transfer-order

- anchor: §2 State 1 Mini-Dialogue 1A
  also: §1.5 global_always (confirm-at-capture item); §2 State 4 The Pre-Commit Gate
  severity: Medium
  claim: A new customer's dictated name is never read back at capture or at the gate, although the Base rule requires confirming any value a tool cannot check and the agent will not speak later.
  evidence: "cannot be checked against a tool result and will not be spoken later" | "Read back all details (Method, Tax Pro, officeName, Date, Time, Text Destination)." | "And your date of birth?"
  class: human
  decision: new-customer-name-readback

- anchor: §1.4 conflict from readiness
  also: §5.2 check_search_readiness Outcome Results (conflict); §1.5 global_voice_lexicon.empathy
  severity: Medium
  claim: The only approved conflict line assumes a past date, but the Part 5 conflict result also covers conflicting constraints, so the agent has no sanctioned line for a non-date conflict.
  evidence: "That date's already gone by, what's the next day that could work for you?" | "Constraints conflict, or the date has passed. issue explains why."
  class: human
  decision: readiness-conflict-line-scope

- anchor: §5.1 search_knowledge_base (intro; KB results)
  also: §1.5 global_always (search_knowledge_base item)
  severity: Medium
  claim: Base JSON tells the agent to silently ignore followUpTopics, while the Part 5 tool note has the agent prompt the caller with followUpTopics on clarification_needed and send the choice as clarifier.
  evidence: "silently ignore followUpTopics" | "clarification_needed may populate clarifier from followUpTopics" | "from a previous followUpTopics prompt"
  class: human
  decision: kb-clarification-followup-topics

- anchor: §2 State 5 broadening.ladders.extension (rung 2)
  also: §2 State 5 scheduler_always (tax_extension item); §2 State 2 Tax Notice Services Guardrails > Tax Extension
  severity: Medium
  claim: The extension handback sets sourceUtterance to a scripted string, while §1.1 and context_envelope define sourceUtterance as the caller's verbatim words.
  evidence: "Verbatim caller intent that routed them here." | "return route_intent to appointment_scheduler with sourceUtterance set to 'schedule a tax preparation appointment'"
  class: human
  decision: extension-handback-source-utterance

- anchor: §2 State 5 scheduler_always (tool-result item: invalid_location, invalid_dnis)
  also: §1.2 Input Exhaustion & Silence > No-Match Rule; §1.5 global_always (no-match item)
  severity: Medium
  claim: The ZIP reprompt on invalid_location has no attempt cap, so it is unclear whether a tool-rejected ZIP counts toward the §1.2 two-failure transfer limit.
  evidence: "reprompt for a valid ZIP; none_nearby transfers" | "On the second consecutive failure, call `transfer_to_agent`."
  class: human
  decision: invalid-zip-attempt-cap

- anchor: §2 State 5 agent_specific_tools.search_knowledge_base
  also: §3 State 2 agent_specific_tools.search_knowledge_base; §4 State 2 agent_specific_tools.search_knowledge_base
  severity: Low
  claim: All three agent blocks describe the KB tool as answering any approved informational question, broader than the D-012 Base rule limiting it to mid-task questions in two categories.
  evidence: "Answer approved informational questions without invalidating transaction state." | "Use search_knowledge_base only for a mid-task question in appointments_and_logistics or tax_prep_and_records"
  class: safe
  fix: Replace each of the three identical entries with "Call per global_always."
