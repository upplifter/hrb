- anchor: §2 State 5 workflow.schedule_new[1]
  also: §2 State 2 Appointment Type Rules > Capture; §2 State 3 Office Resolution > Rollover; §1.1 appointmentType, taxProRef, officeRef
  severity: Medium
  claim: The Scheduler re-establishes type, re-asks about the prior Tax Pro, and re-resolves the office by entryPoint, ignoring the carried appointmentType, taxProRef, and officeRef that §1.1 says to use without re-asking.
  evidence: "If present, use them without re-asking." | "If a returning client's prior Tax Pro is active, ask whether to keep them" | "otherwise resolve the office by entryPoint per scheduler_always"
  class: human
  decision: carried-context-precedence-in-scheduler

- anchor: §3 Intent Scope & Disambiguation > office_info
  also: §3 Office Contact Triage > If OPEN; §1.2 Hours: One Source, Spoken Once; §1.5 global_always informational item
  severity: Medium
  claim: Part 1 sends every phone-number question to office_information, but Office Information's office_info scope omits phone numbers and its office_contact open branch withholds the number.
  evidence: "Other agents hand these questions back with routingTarget office_information." | "The caller wants operating hours, the physical address, or driving directions." | "Do not provide the main line number to call directly."
  class: human
  decision: office-info-phone-number-answer

- anchor: §3 Office Contact Triage > If OPEN
  also: §3 State 2 agent_specific_outcomes.office_open_unanswered; office_always open item; workflow.office_contact_flow[3]; Mini-Dialogue 3C
  severity: Medium
  claim: The open-office branch returns capture_intent after giving the caller a status answer, while the Part 1 contract limits capture_intent to calls where nothing was served.
  evidence: "capture_intent means Head of Call re-asks the caller's need; use it only when nothing was served" | "return nextAction = capture_intent so the Head of Call flow can ask how"
  class: human
  decision: open-office-next-action

- anchor: §1.5 global_always informational item
  also: §2 State 5 interruptions.informational_question
  severity: Medium
  claim: The Base JSON says an informational question invalidates nothing, while D-022 and the Scheduler void a gate yes given before the interruption.
  evidence: "An informational question is not a constraint change and invalidates nothing." | "A yes given before the interruption is void; re-read the gate and ask again."
  class: safe
  fix: Change "invalidates nothing." to "invalidates nothing except a gate yes already given."

- anchor: §2 Mini-Dialogue 1B
  also: §2 Mini-Dialogue 2B; §1.5 global_always latency-preamble item
  severity: Low
  claim: Two frozen Agent turns speak the latency preamble "Let me take a look" mid-capture with no tool call pending, against the Base rule that ties the preamble to a slow tool call.
  evidence: "Let me take a look. And his date of birth?" | "Let me take a look, and which tax year is it about?" | "when a tool call will take noticeable time"
  class: human
  decision: frozen-dialogue-preamble-edit

- anchor: §4 Mini-Dialogue 4A
  also: §1.3 Leave-a-Message Ownership; §1.5 global_always leave-message item
  severity: Low
  claim: After the caller asks to leave a message, the frozen Agent turn speaks a new sentence, while Part 1 says to finish the current sentence, stop speaking, and return leave_message.
  evidence: "Absolutely, I can help you leave a message for her." | "explicitly requests or accepts leaving a message, stop speaking"
  class: human
  decision: frozen-4a-message-ack
