# Round 3 verification (D-026 to D-037)

Lint: `python tools/lint.py check` gives RESULT WARN, with no FAIL. Round growth is +0.97% against a 1.0% limit. Total growth is -1.46%. JSON is valid.
Stale-reference sweep: nothing is left for `office_info_transfer`, `question_answered`, "general tax", "request for a person", "without re-asking", or the year reprompt. The only `capture_intent` return left is `intent_unclear`. `digital_drop_off` remains only in the `broadening.ladders` offers, the method tokens, and `method_descriptions`, which is correct under D-037. "transfer you to" appears only in the new `prohibited_phrases` entry.
Frozen text: changes are limited to the `prohibited_phrases` and `reprompt` entries (D-036 names them), the 4C Agent line (D-033 names it), and the §1.4 Path column of one row. No approved line changed. The 3C edit is a System line (C-9).

L-170 | pass
L-171 | pass
L-174 | fix-needed | `global_outcomes.transfer_unavailable` now says "returned agent_unavailable or failed" but still makes speech depend on leaveMessageAvailable, and a failed call has no leaveMessageAvailable. Limit the leaveMessageAvailable speech rule and the nextAction rule to agent_unavailable. For a failed call, point to global_always (e.g., "transfer_to_agent returned agent_unavailable, or failed (then speak and close per global_always)."). Stay within 60 words, for example by trimming "known context per the global_always leave-message item" to "known context per global_always".
L-194 | pass
L-195 | pass
L-184 | pass
L-178 | pass
L-177 | fix-needed | §2 State 2 Appointment Type Rules > Tax Pro Requests opens with "A request to speak to a Tax Pro". That is any Tax Pro, which is broader than D-034 ("a specific or own Tax Pro") and its mirror `interruptions.intent_change` ("a specific or their own Tax Pro"). Change it to "A request to speak to a specific or own Tax Pro". To stay within 35 words, shorten "hands back intent_changed with routingTarget speak_to_tax_pro" to "returns intent_changed to speak_to_tax_pro", or split the bullet into two sentences.
L-180 | pass
L-193 | pass
L-179 | pass
L-199 | pass
L-204 | pass
L-191 | pass
L-201 | pass
L-203 | pass
L-205 | pass
L-165 | pass
L-186 | pass
L-185 | pass
L-202 | fix-needed | §3 Office Details Logic > By-Appointment-Only: the trim "with no standard hours and no booking question" turned two prohibitions into a phrase the agent could speak ("we have no standard hours"). Restore them as imperatives: "If seasonalStatus is by_appointment_only, state that the office operates by appointment only; never quote standard hours or ask whether to book. Stop speaking and return nextAction = route_intent with routingTarget = appointment_scheduler."
L-206 | pass
L-152 | pass
L-153 | pass
L-200 | pass
L-175 | pass
L-142 | pass
L-154 | pass
L-173 | pass
L-182 | fix-needed | The `global_always` informational item sends personal advice, calculation, and notice questions to speak_to_tax_pro "outside the Scheduler". That scope includes Part 4, so the Speak to a Tax Pro agent would hand back to itself. Change "outside the Scheduler," to "in office_information,". Mirror it in the §1.2 Tax/Financial Boundary sub-bullet, e.g., "...and the rest to speak_to_tax_pro from Part 3; in the Scheduler, see Part 2, Informational Interruptions."
L-196 | pass
L-181 | pass
L-098 | pass
L-151 | pass
L-210 | pass
L-172 | pass
L-190 | pass
L-072 | pass

## Judgment calls

- (a) Supported. D-029 says "any gate", but Q-28 framed the gap as the booking, reschedule, and DDO gates, since the cancellation no already maps to `customer_declined_options`. cancel_existing also has no negotiation for "ask what to change" to re-enter. That leaves one workable fix.
- (b) Supported. A literal "any caller-named Tax Pro hands back" would break `scenario_selection` item 8 (the returning client who asks for the prior Tax Pro), the efile-rejection prior Tax Pro proposal, and the carried-taxProRef callback. Excluding the prior and carried Tax Pro is the only reading consistent with the spec.
- (c) Supported. D-031 sets the OPEN branch's nextAction to leave_message_offer. `office_open_unanswered` is the only outcome for an open office, so its nextAction had to follow. Widening it to "or is busy" covers 3C. The alternative was to extend `office_contact_triage_complete`. Fix still needed, but not blocking: neither the §3 If OPEN bullet nor the office_always OPEN item names finalOutcome `office_open_unanswered`. See New issues.
- (d) Supported. Its only leave_message_offer trigger was the unavailable-Tax-Pro path, which D-033 removed. The transfer-unavailable case returns `transfer_unavailable`, not `routed_to_message`.
- (e) Supported. Without it, the D-031 OPEN branch would return leave_message_offer outside the §1.3 triggers, and §1.3 wins under C-1. Widening the trigger is the only way to comply.
- (f) Supported. "Confirmation state means confirmationStatus, not text opt-in" is still enforced by `invalidation.text_confirmation` (opt-in survives constraint changes). "Purge invalid state" is implied by "invalidates", and the prose Action bullets still say "Purge". No trigger, limit, or exception was lost. D-035's 60-word cap forced the cut (the item is now 59 words).
- (g) Supported. None of these trims dropped a trigger, limit, or exception:
  - scheduler_never loan clause: loan, fee, and penalty routing stays in the `global_always` informational item, which merges into the Scheduler. Only a pointer was dropped.
  - cancel_said: the dropped scheduler_never pointer's rule still stands in scheduler_never. "If the caller wants to cancel" keeps the confirm-intent condition, and the before-commit and after-commit branches are intact.
  - Objective method sentence: `workflow.schedule_new[1]` still covers it ("ask (never infer) the method it permits").
  - tax_pro_never merge: the old "never ask if they want to leave a message when a transfer is unavailable" is a yes/no question, which the merged item bans. The "return leave_message_offer" instruction is kept.

## New issues

- `§3 Office Contact Triage > If hours_unavailable; workflow.office_contact_flow[2]` | Medium | Confirmed (fixer L-152). After giving the address, the path names no finalOutcome or nextAction, so the implementer must guess the terminal payload.
- `§4 Tax Pro Lookup & Disambiguation > No Matches / Inactive; tax_pro_always unavailable item` | Medium | Confirmed (fixer L-175). A caller who declines the only offer (the Scheduler) has no outcome. `tax_pro_options_declined` covers only declining callback and message.
- `§1.1 operation; objective; §2 State 4 Write Tools > cancel_appointment` | Medium | D-027 and D-028 overlap. With a null operation, the Scheduler asks whether to book, change, or cancel. But the Scheduler may cancel only on operation cancel_existing or a mid-booking request, so a caller who answers "cancel" to that question has no permitted path.
- `§5.2 get_customer_appointments Outcome Results; workflow.reschedule_existing[1]` | Medium | Results now include canceled appointments. On reschedule_existing, a canceled-only one_appointment, or a canceled entry among several_appointments, has no rule or outcome. `appointment_already_canceled` covers only cancel_existing.
- `§1.4 validation_failed, system_failure, or a failed transfer call; global_always transfer-results item` | Medium | On a failed transfer call, the caller hears "Let me get you to a person" and the call then closes with nextAction close and no person. The line promises what the path does not deliver (this is a caller-experience change, so Human).
- `§3 Cross-Office Restriction; office_never phone item; office_always CLOSED item` | Medium | "Routed office" is undefined when routedOfficeRef is null. After the L-153 ZIP capture, the CLOSED branch speaks mainPhoneSpoken for an office that is not routedOfficeRef, which office_never forbids.
- `§4 Generic Request; tax_pro_always unavailable item; agent_specific_outcomes.routed_to_scheduler` | Medium | A generic caller with no prior Tax Pro is told "they are unavailable", with no Tax Pro to name. routed_to_scheduler also requires officeRef "at that location", which the generic path never resolves on central_line.
- `§3 If OPEN; office_always OPEN item` | Low | The OPEN branch names no finalOutcome. `office_open_unanswered` is the implied one and should be named.
- `§5.1 search_knowledge_base KB results` | Low | Outside the Scheduler, requires_tax_pro returns no_approved_answer. Under D-034, personal questions outside the Scheduler hand back to speak_to_tax_pro.
- `workflow.schedule_new[1]; §2 State 3 Office Resolution > Rollover; scheduler_always rollover item` | Low | These still ask about the prior Tax Pro and resolve the office by entryPoint, with no pointer to carried-context precedence. The scheduler_always context-envelope item settles it, but the step text reads unconditionally.
- `agent_specific_outcomes.customer_declined_options` | Low | "without ... requesting a person" is ambiguous after D-034, which split person requests into a live-agent barge and a speak_to_tax_pro handback.
- `global_outcomes.validation_failed` | Low | "a result other than rejected" still overlaps change_not_allowed and not_cancelable, which `terminal_payload_contract` maps to automation_blocked.
- `§2 State 3 Informational Interruptions > Personal Questions` | Low | The bullet omits "resume", which its JSON mirror `agent_specific_tools.search_knowledge_base` carries.
- `terminal_payload_contract` | Low | Pre-existing. At 214 words, the string exceeds the 60-word JSON item limit, and this round added to it.
