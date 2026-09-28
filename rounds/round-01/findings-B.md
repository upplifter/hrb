- anchor: Part 4 State 2 tax_pro_always (Mention MyBlock)
  also: Part 4 State 1 Fulfillment Priority step 2 | Part 4 Mini-Dialogues 4A, 4E | §1.2 Zero Web Deflection & Prohibited Speech | §1.5 global_never
  severity: High
  claim: Part 4 requires the agent to speak an app name, which the Part 1 zero-web-deflection rule forbids with DDO as its only exception, and the added sentence pushes the 4A/4E option turn to four sentences, over the §1.2 turn limit.
  evidence: "Never speak a URL, website, portal, or app name." | "you can also message your tax pro anytime through the MyBlock app"
  class: human
  decision: myblock-mention-vs-zero-web-deflection

- anchor: Part 2 State 3 Office Resolution > Rollover
  also: Part 2 State 5 scheduler_always (entryPoint and dialedOfficeNumber item) | Part 2 State 5 workflow.schedule_new step 2 | §1.1 entryPoint
  severity: Medium
  claim: The Scheduler's rollover rules always propose the dialed office, which drops the §1.1 exception that the prior office wins in the returning-client same-Tax-Pro scenario.
  evidence: "Wins over prior office, except in the returning-client same-Tax-Pro scenario." | "Resolve office from dialedOfficeNumber. Propose it directly. No ZIP prompt."
  class: safe
  fix: Add the §1.1 exception ("except in returning_same_tax_pro, propose the prior office") to the State 3 Rollover bullet, the scheduler_always rollover item, and schedule_new step 2.

- anchor: Part 4 State 2 workflow.speak_to_tp_generic step 3
  also: Part 4 State 2 tax_pro_always (Disclose a prior-year item) | Part 4 State 2 agent_specific_tools.find_customer | §1.1 customerRef
  severity: Medium
  claim: Part 4 requires find_customer before disclosing a Tax Pro with no exception for an envelope customerRef, which contradicts the §1.1 rule against re-authenticating an identity that is already resolved.
  evidence: "If present, do not re-authenticate unless the transaction subject changes." | "3. Resolve the owner through find_customer; on a third-party request require registeredAni true"
  class: human
  decision: part4-honor-envelope-customerRef

- anchor: Part 2 State 1 Authentication Logic > New Customer DOB Check
  also: Part 2 Mini-Dialogues 1A | §1.2 Confirmation Strategy > Exceptions (DOB & SSN) | §1.5 global_always (Confirm at capture item)
  severity: Medium
  claim: The Scheduler adds a dedicated DOB repair turn after no_match, and Part 1 says DOB never receives a spoken confirmation turn, so it is unclear whether the year re-ask is allowed.
  evidence: "If no_match, re-ask the 4-digit year alone as a repair before the confirmation gate." | "neither ever receives a spoken confirmation turn"
  class: human
  decision: dob-year-repair-vs-no-dob-confirmation

- anchor: Part 2 State 5 scheduler_always (For book_appointment, send customerRef item)
  also: Part 5 §5.2 book_appointment Request JSON (New Customer) | §1.2 PII & IRS Sec. 7216 Compliance > Data Sanitization
  severity: Medium
  claim: Part 1 excepts only find_customer payloads from DOB and SSN redaction, but the Scheduler's newCustomer object sends dateOfBirth and ssnLast4 to book_appointment with no matching exception.
  evidence: "Exception: find_customer request payloads require these fields for authentication." | "For new clients, omit customerRef and send the newCustomer object."
  class: human
  decision: dob-ssn-exception-scope-book-appointment

- anchor: Part 4 State 1 Fulfillment Priority step 1
  also: Part 4 State 2 tax_pro_always (Once a Tax Pro is confirmed item) | Part 4 State 2 tax_pro_never (when a transfer is unavailable item) | Part 4 Mini-Dialogues 4A | §1.3 Leave-a-Message Ownership
  severity: Medium
  claim: Part 4 has the agent speak the message offer itself and, in 4A, add a turn after the caller accepts, while §1.3 gives the offer to the deterministic flow and says to stop speaking on acceptance.
  evidence: "The deterministic Leave a Message flow owns the offer where still needed" | "I can check their calendar for a callback, or I can help you leave a message." | "Absolutely, I can help you leave a message for her."
  class: human
  decision: part4-message-offer-owner

- anchor: Part 3 State 1 Intent Scope & Disambiguation > unclear_intent
  also: §1.2 Input Exhaustion & Silence > No-Match Rule | §1.3 Leave-a-Message Ownership
  severity: Medium
  claim: Part 3 lets unresolved intent after one reprompt go to leave a message, but Part 1 sends a second failure to transfer_to_agent and returns leave_message only when the caller asks for or accepts it.
  evidence: "If unresolved after one reprompt, transfer or route to leave a message." | "On the second consecutive failure, call `transfer_to_agent`."
  class: human
  decision: part3-unclear-intent-exhaustion-path

- anchor: Part 3 State 1 Office Details Logic > Off-Season Closure
  also: §1.4 Off-season office closure row | §1.5 global_voice_lexicon.empathy (off-season line) | Part 3 State 2 office_always (closed_for_season item)
  severity: Medium
  claim: Part 3 speaks the Year-Round Office address, while the §1.4 line that must be spoken as written names the office by officeName and asks a booking question, so Office Information cannot follow both.
  evidence: "offer the address of the nearest Year-Round Office (yroOfficeAddressSpoken)" | "the closest one that's open year-round is [officeName]. Would that work?"
  class: human
  decision: off-season-line-scope-office-info

- anchor: Part 3 State 1 Office Contact Triage > If CLOSED
  also: Part 3 State 2 office_always (CLOSED item) | Part 4 State 1 Tax Pro Lookup > No Matches / Inactive | Part 4 State 2 agent_specific_outcomes.routed_to_message | §1.3 Leave-a-Message Ownership
  severity: Medium
  claim: Part 1 defines leave_message_offer for an unavailable transfer, but Parts 3 and 4 return it for a closed office, an inactive Tax Pro, and no callback slots, where no transfer was tried.
  evidence: "When a transfer is unavailable and a message may be offered, return nextAction = leave_message_offer." | "provide the main line number, then stop speaking and return nextAction = leave_message_offer"
  class: human
  decision: leave-message-offer-triggers

- anchor: Part 3 State 2 agent_specific_tools.transfer_to_agent
  also: Part 4 State 2 agent_specific_tools.transfer_to_agent | §1.5 global_always (no-match item) | Part 2 State 5 agent_specific_tools.transfer_to_agent
  severity: Medium
  claim: The Part 3 and Part 4 transfer_to_agent notes list their own triggers and leave out the Part 1 no-match exhaustion trigger, while the Scheduler's note points to the shared conditions.
  evidence: "Use on unresolved intent or office lookup failure." | "Use on third-party or authentication failure, or an indeterminate write." | "Call on the transfer conditions defined above."
  class: safe
  fix: Start both notes with "Call on the global_always transfer conditions and" before the existing local triggers, per constitution C-4.

- anchor: Part 4 State 2 tax_pro_never (tax advice item)
  also: §1.5 global_never (tax advice item) | §1.2 PII & IRS Sec. 7216 Compliance > Tax/Financial Boundary
  severity: Low
  claim: The Part 4 copy of the tax-advice ban adds "formal" and so reads narrower than the global rule it repeats.
  evidence: "Never offer or provide tax advice, refund calculations, or formal tax interpretations." | "Never give personalized tax advice, tax calculations, or interpretations of tax law."
  class: safe
  fix: Delete the Part 4 tax_pro_never item, since global_never already covers it (constitution C-3 A).

- anchor: Part 3 Mini-Dialogues 3B
  also: Part 2 Mini-Dialogues 1B | §1.2 Voice Persona & Delivery
  severity: Low
  claim: Non-readback Agent turns in 3B and 1B run three sentences, and §1.2 caps routine turns at under three.
  evidence: "brief turns (under three spoken sentences" | "Sure, I can look at that. I'll just need a few of his details first."
  class: human
  decision: dialogue-turn-length-trim
