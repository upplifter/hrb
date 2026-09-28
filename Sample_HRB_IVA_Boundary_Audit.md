# HRB IVA Agents Specification — Hostile Architecture & Agent-Boundary Audit

**Artifact under review:** `HRB_IVA_Agents_Spec.md` (1,857 lines / 133 KB, H&R Block IVA Agents Specification)
**Review type:** Agent-boundary, ownership and scope-escalation audit (hostile)
**Date:** 2026-09-25
**Output:** Findings only. No specification rewrite is included, per instruction.

---

## 0. How this review was conducted

**Evidence layers treated as separate, not interchangeable:**

| Layer | Contents in this document |
|---|---|
| A. Objectives & scope | Part 2 State 5 `objective`; Part 3 State 2 `objective`; Part 4 State 2 `objective`; Part 1 §1.1/§1.3 envelope and handback ownership |
| B. Global routing/orchestration | Part 1 §1.1 entry context, §1.2 guardrails, §1.3 terminal handbacks, §1.5 `global_outcomes`, `terminal_payload_contract` |
| C. Agent "always/never" | `scheduler_always`/`scheduler_never` (L509–562); `office_always`/`office_never` (L820–836); `tax_pro_always`/`tax_pro_never` (L965–983) |
| D. Workflows | Part 2 State 1–4 + `workflow.schedule_new/reschedule_existing/cancel_existing` + `broadening` (L563–706); Part 3 `workflow` (L837–850); Part 4 `workflow` (L984–1005) |
| E. Tools | Part 2 `agent_specific_tools` (L722–735), Part 3 (L852–857), Part 4 (L1007–1012), Part 5 catalog (L1024–1857) |
| F. Examples | Mini-dialogues 1A/1B, 2A/2B, 3A/3B, 4A/4B (Part 2); 3A–3D (Part 3); 4A–4E (Part 4) |
| G. Outcomes & payloads | `global_outcomes` (L231–247), `agent_specific_outcomes` (L741–748, L862–867, L1017–1020), `terminal_payload_contract` (L248) |
| H. Other agents | Parts 2/3/4 objectives and workflows read against each other |
| I. Deterministic flows | Head of Call (close, additional-help, transfer node, intent routing); Refund Status Flow; FAQ Agent; Leave a Message flow; DDO |

**Review principle applied:** consistency is not evidence of correctness. Where multiple sections, examples, tools and outcomes all authorize the same capability, that propagation is treated as a *risk signal* about the original ownership decision, not as confirmation of it.

**Confidence rules used:** *Certain* = direct textual evidence. *Likely* = follows strongly from cross-section comparison. *Speculative* = an external architectural decision is required. No architectural violation is declared Certain where no authoritative ownership rule exists in the supplied material; those are labelled **Architecture decision required**.

**Line references** are to the reviewed file and are given so each finding can be re-checked without re-reading the whole document.

---

## A. Executive verdict

**The specification is operationally coherent for the happy-path booking flow and architecturally unsafe everywhere an intent crosses an agent seam.** Four agents plus five deterministic flows share 26 capabilities; only three of those capabilities (booking, rescheduling, cancellation) have a single, uncontested owner. The remaining seams are resolved by whichever agent happens to hold a tool, not by an ownership rule.

Five systemic failures generate most of the individual findings:

**S1 — The Appointment Scheduler's objective is narrower than what its workflows, ladders and tools let it do.** The objective commits it to "at most one schedule_new, reschedule_existing or cancel_existing retail appointment transaction" (L508). Its ladders offer it a fulfillment write (`send_secure_link`, L536) that is not an appointment, its tool list lets it answer general knowledge questions (L733) and run a regional virtual search (L644, L1377), and its extension rung offers self-filing and a live-agent transfer for a product nobody owns (L413/L658). The objective was never widened when broadening became the centre of the design.

**S2 — "Callback" is owned by three actors and means three different things.** Part 4 decides and routes it (L913, L973), the Scheduler books it as an appointment type (L317), two different slot tools can find it (`find_available_slots` with `appointmentType: callback` L1348, and `find_available_cdas_slots` L728/L1437 with a different request *and* response contract), and no ladder or scenario exists for it. The single most-routed object in the document has no authoritative definition.

**S3 — There is no intent-ownership layer.** Intent classification, informational answering, office lookup and human-contact handling are each performed by two or three agents. Routing to the FAQ Agent (L885), the Refund Status Flow (L884) and the Office Information Agent is enforced **only inside Part 4**. Nothing prevents the Scheduler or Office Information agent from answering refund, login or hours questions from `search_knowledge_base` instead of routing (L733, L856).

**S4 — Boundary termination is under-specified, in one direction only.** The document is precise about what an agent may do and what it may never *say*, and nearly silent about which tools an agent must stop calling once it has decided to hand back. There is no post-boundary tool prohibition for any agent, and `capture_intent` — an action used as an ownership transfer by Part 3 (L776) — is never defined as a capability owned by anyone.

**S5 — Two universal rules are locally overridden.** The universal zero-web-deflection rule and its prohibited-phrase list (L60, L170–188) are overridden by Part 4's mandated MyBlock app mention (L902, L972) inside the same agent whose `never` list repeats the universal prohibition (L980). The universal silence rule (L72) says a second silence must **not** transfer, while `customer_abandoned` says an unanswered gate "runs the reprompt rule, then transfers" (L246). Both are the signature of a narrow exception written broadly enough to swallow the rule.

### A.1 Findings index

| ID | Finding | Severity | Confidence |
|---|---|---|---|
| F-01 | Scheduler executes `send_secure_link` (DDO): transaction outside objective, no outcome, no idempotency key, impossible `customerRef` for new callers | Critical | Certain |
| F-02 | DDO write executes on rung acceptance without the confirmation-gate contract; channel-rung method change bypasses invalidation | Critical | Certain |
| F-03 | Callback/CDAS ownership split across Part 4, the Scheduler and two competing slot tools with two response contracts | High | Certain |
| F-04 | No callback scenario/ladder: the `new_client` ladder can offer `digital_drop_off` for a phone-only type | High | Certain |
| F-05 | Callback handoff payload exceeds the terminal payload contract; reason, `taxProRef`, `officeRef`, `appointmentType` have no defined slot | High | Certain |
| F-06 | Part 4's mandated MyBlock mention violates universal zero-web-deflection and Part 4's own `never` list | High | Certain |
| F-07 | Human-contact request has two owners with opposite behaviours; Part 3 lacks Part 4's local-desk transfer prohibition | High | Certain |
| F-08 | FAQ Agent routing bypassed: unrestricted `search_knowledge_base` overlaps its exclusive scope | High | Likely |
| F-09 | Hours/directions/phone answering duplicated between KB categories and Office Info tools; competing sources of truth | High | Likely |
| F-10 | Silence rule (terminate) contradicts `customer_abandoned` (transfer): boundary over who ends the call | High | Certain |
| F-11 | No post-boundary tool-prohibition rules anywhere in the document | High | Certain |
| F-12 | No global intent→agent routing table and no named intent-classification owner; `unclear_intent` only defined in Part 3 | High | Likely |
| F-13 | Office Info converts a satisfied information request into `leave_message_offer` | Medium | Certain |
| F-14 | Callback reason captured into `appointmentNotes` vs universal "never capture message content" | Medium | Certain |
| F-15 | Off-season closure owned twice, from two data sources, with different eligibility outcomes | Medium | Certain |
| F-16 | Part 4 performs `find_customer` / third-party authentication — duplicate identity capability | Medium | Certain |
| F-17 | Part 4 outcome `routed_to_message` asserts slot availability the agent cannot determine | Medium | Certain |
| F-18 | Office Info holds `search_knowledge_base` with unrestricted categories, beyond its stated scope | Medium | Certain |
| F-19 | Office Info holds `transfer_to_agent` with undefined trigger conditions, beyond its stated scope | Medium | Likely |
| F-20 | Tax-extension rung offers self-filing and "transfer to a live agent for self-filing support" — orphaned capability | Medium | Certain |
| F-21 | `capture_intent` undefined; overlaps `offer_additional_help` and the Head of Call mandate | Medium | Certain |
| F-22 | No refund-status or office-information boundary for the Scheduler and Office Info agents | Medium | Likely |
| F-23 | Regional virtual appointment contradicts the Scheduler's "every type is booked against a specific office" | Medium | Certain |
| F-24 | `scenario_selection` runs post-readiness, but drop-off/DDO decisions are pre-readiness | Medium | Likely |
| F-25 | Office Info's `by_appointment_only` branch starts a booking conversation the caller did not request | Medium | Certain |
| F-26 | "Primary routed office" / `yroOfficeRef` / `routedOfficeRef` undefined: cross-office phone restriction has no fixed referent | Medium | Certain |
| F-27 | `not_confirmed` triggers an unbounded re-gate loop | Low | Certain |
| F-28 | `efile_rejection_retail` "open directly on booking" conflicts with "never infer the type from the entry point" | Low | Likely |

---

## B. Detailed findings

### F-01 — Scheduler executes a fulfillment transaction that is not an appointment

**Finding ID:** F-01
**Severity:** Critical
**Confidence:** Certain
**Agent:** Appointment Scheduler (Part 2)
**Capability:** Transaction execution — Digital Drop-Off (DDO) secure-link dispatch
**Observed behavior:** The Scheduler performs a committed transaction that is neither a booking, a reschedule nor a cancellation. It captures and confirms an SMS/email destination, then executes `send_secure_link` (L329, L536, L570 step 6). The tool returns `transactionOccurred: true` (L1717). DDO is simultaneously presented as a *broadening rung* in six of the nine ladders (L623, L633, L642, L651, L678, L702), i.e. it is the standard fallback whenever availability fails.
**Stated scope:** "Contain the call and complete at most one schedule_new, reschedule_existing or cancel_existing retail appointment transaction" (L508). DDO is declared "a fulfillment action, not a calendar appointment" (L327).
**Expected boundary:** Fulfillment dispatch is a write transaction and must be owned either by the Scheduler *under an explicitly widened objective and outcome vocabulary*, or by a deterministic DDO flow. Today it is owned by neither.
**Boundary trigger:** The caller accepts the DDO rung, or requests a secure upload link. At that moment the Scheduler stops being a scheduling agent and becomes a fulfillment executor.
**Required next action:** On acceptance of a DDO rung, the Scheduler should execute the deterministic DDO flow (or execute `send_secure_link` under a named, enumerated outcome — see below) and then yield, with no further scheduling activity.
**Evidence supporting the observed behavior:** L329 "Execute the `send_secure_link` tool. Do not use `book_appointment`"; L536; L570 step 6; L732 tool description; L1717 `transactionOccurred: true`; six ladder rungs.
**Evidence creating the conflicting or overlapping ownership:** The objective enumerates exactly three transactions (L508). `terminal_payload_contract` enumerates `operation` as only `schedule_new | reschedule_existing | cancel_existing` (L248), and `agent_specific_outcomes` contains no DDO outcome (L741–748). `closure.line_patterns` defines only committed / canceled / nothing_to_do / no_transaction / handoff_confirmed / handoff_unavailable shapes (L709) — none fits "link sent". `send_secure_link` has **no `idempotencyKey`** (L1699–1709) although every other write requires one (L547). The request requires `customerRef` (L1702), but a net-new caller has none — `find_customer no_match` creates no profile and profile creation is deferred to the `book_appointment` commit (L266, L551) — and DDO never calls `book_appointment`. A new-customer DDO is therefore unexecutable as specified, on the very ladder (`new_client` rung 3, L623) offered to new customers.
**Why an ordinary contradiction review might miss it:** Nothing contradicts textually. DDO is consistently described as a fulfillment action, consistently offered as a rung, and consistently executed with a dedicated tool. The defect is that the objective, the `operation` enum, the outcome set, the closure patterns and the idempotency rules were never extended to cover the transaction the design now performs routinely.
**Customer or operational risk:** (a) A secure-link send is unreconcilable — no idempotency key means a retry can text the caller twice, and `outcome_unknown` reconciliation instructions (L242, L481) do not cover it. (b) A new caller can reach a dead end at the moment of maximum intent. (c) The agent emits a terminal payload whose `operation` and outcome fields cannot represent what it just did, so downstream reporting under-counts a real transaction as `transactionOccurred: false` or fails validation.
**Recommended specification correction:** Either (i) create a named deterministic DDO flow and reduce the Scheduler to `route_intent`/handback on DDO acceptance, or (ii) widen the Scheduler objective to "one retail appointment transaction **or one DDO fulfillment**", add `send_secure_link` to the `operation` enum or add a separate `fulfillmentOperation` field, add a terminal outcome (`ddo_link_sent` / `ddo_link_failed`), add a closure line pattern, add an `idempotencyKey` derived as `interactionId-officeRef-ddo`, and specify how `customerRef` is absent for net-new callers.
**Sections that must also be changed to avoid residual contradictions:** Part 2 State 5 `objective`; `scheduler_always` (L536) and `workflow.schedule_new` step 6 (L570); `agent_specific_tools.send_secure_link` (L732); `broadening.ladders.*` rungs that name `digital_drop_off`; Part 1 `terminal_payload_contract` (`operation`, `nextAction`, outcome field list); Part 1 `global_outcomes`; Part 2 `closure.line_patterns`; Part 2 `agent_specific_outcomes`; Part 5 §5.2 `send_secure_link` request contract.
**Required regression tests:** (1) Net-new caller, tax_prep, no availability, accepts DDO → tool executes with a resolvable customer identity and one idempotency key; repeat of the same acceptance must not dispatch twice. (2) DDO acceptance produces a terminal payload whose `operation`/outcome fields validate and are non-empty. (3) DDO acceptance followed by any availability search in the same invocation must be rejected as a boundary violation.

### F-02 — DDO performs a write on rung acceptance without the confirmation-gate contract

**Finding ID:** F-02
**Severity:** Critical
**Confidence:** Certain
**Agent:** Appointment Scheduler (Part 2)
**Capability:** Confirmation / transaction execution
**Observed behavior:** "The sequence ends as soon as the caller accepts a slot or method at any rung" (L602), and on DDO the agent "Capture[s] and confirm[s] the secure-link destination (SMS or Email)" and executes the tool (L329). The method change is explicitly exempted from state invalidation: "Any scheduling-constraint change, other than a method change made by accepting a channel rung, resets which rungs have been offered…" (L715).
**Stated scope:** "Secure explicit consent before executing any write tool" (L461); "Require an explicit spoken yes immediately before any write" (L511, L569 step 5).
**Expected boundary:** Every write — including a link dispatch — passes through a readback and an explicit yes. Consent to "method X" is not consent to "execute write Y"; the DDO rung is an acceptance of a *channel*, not of a dispatch.
**Boundary trigger:** Caller says "yes, text me the link" at a DDO rung.
**Required next action:** Either treat DDO like a booking (destination readback + explicit yes + `confirmation` object), or specify that a channel-rung acceptance alone is sufficient consent and say so explicitly, with the exact wording the agent must use.
**Evidence supporting the observed behavior:** Pre-commit gate requires "an explicit spoken yes immediately before any write" (L511); the call-specific gate mechanics (three-sentence chunked readback, text-destination beat) are defined only for bookings (L472, L512); `send_secure_link` has no `confirmation` field in its request (L1699–1709) while all three appointment writes require `confirmation.confirmed/confirmedAt/utterance` (L1507, L1600, L1658).
**Evidence creating the conflicting or overlapping ownership:** `invalidation.upstream_change` says any upstream constraint change invalidates `confirmationStatus` (L714), and the type/method invalidation rule purges slots and confirmation state "except when accepting a channel rung" (L341) — so a DDO channel rung inherits a *pre-existing* confirmation state without a fresh gate.
**Why an ordinary contradiction review might miss it:** The document never says DDO skips the gate, and it never says DDO requires the gate. Each section is individually defensible; the gap only appears when the gate's field-level enforcement (the `confirmation` object) is compared with the DDO tool's request shape.
**Customer or operational risk:** A write is dispatched on an inference rather than an explicit yes, in the one flow where the destination is a personal phone number or email. Conversely, if a gate is belatedly added requiring a `confirmation` object, `send_secure_link` will reject every call.
**Recommended specification correction:** State DDO's consent contract explicitly in `scheduler_always` and the State 2 DDO rules: the destination readback, whether a three-sentence gate applies, and how consent is evidenced. Add `confirmation` (or explicitly document its absence) to the `send_secure_link` contract.
**Sections that must also be changed to avoid residual contradictions:** Part 2 State 2 "Digital Drop-Off (DDO) Rules" (L325–330); Part 2 State 4 "The Pre-Commit Gate" (L469–474); `scheduler_always` (L511, L536); `invalidation.upstream_change` (L714); Part 5 §5.2 `send_secure_link`.
**Required regression tests:** (1) Caller accepts DDO rung then interrupts with a correction to the destination → confirmation state purges and destination is re-confirmed before dispatch. (2) No dispatch occurs without the specified consent evidence. (3) A DDO dispatch after a modified destination does not reuse prior confirmation.

### F-03 — Callback / CDAS ownership is split three ways with two competing tools

**Finding ID:** F-03
**Severity:** High
**Confidence:** Certain
**Agent:** Speak to a Tax Pro (Part 4) vs Appointment Scheduler (Part 2)
**Capability:** Callback setup; availability search
**Observed behavior:** Part 4's objective is to assist callers "by routing them to the Appointment Scheduler for a 15-minute CDAS callback appointment" (L964), and it hand-"routes" `appointmentType = callback` (L913, L973, L941, L956). Part 4 states flatly: "The Speak to a Tax Pro agent triages the request but does not book the calendar slot" (L913). The Scheduler, meanwhile, owns `callback` as an appointment type (L317) and owns **both** slot tools: `find_available_slots` (with the note "For CDAS callbacks, send appointmentType = callback; appointmentMethod, taxProRatingFloor, and timeWindow may be null", L1348) and `find_available_cdas_slots` ("Searches Appointment Manager for 15-minute Callback Appointment (CDAS) slots", L728, contract L1437–1478).
**Stated scope:** Scheduler: five types in scope including `callback` (L508). Part 4: route, do not book (L913). Neither statement assigns the *search*.
**Expected boundary:** Exactly one agent owns callback slot search, and exactly one tool is authoritative for it. Part 4 should terminate at a handback; the Scheduler should own search and commit.
**Boundary trigger:** The caller requests a callback; Part 4 has already elicited the reason and named the Tax Pro.
**Required next action:** Part 4 yields with a defined handback; the Scheduler selects exactly one CDAS search path.
**Evidence supporting the observed behavior:** L728 lists `find_available_cdas_slots` inside the Scheduler's `agent_specific_tools`; L1437–1478 gives it a distinct request shape (`officeRef`, `hrbEmployeeId`, `appointmentType`, `date`, `slotCount`) and a distinct response shape (`availableSlots[]` with `startDateTime`, `startDateTimeSpoken`, `callbackWindowSpoken`) versus `find_available_slots` (`slots[]` with `slotRef`, `isCDAS`, `summary`, `moreAvailable`, `suggest`).
**Evidence creating the conflicting or overlapping ownership:** `find_available_cdas_slots` appears **nowhere** in the Scheduler's `workflow`, `broadening.scenario_selection`, `broadening.ladders`, readiness rules, or outcome vocabulary — while `scenario_selection` has no callback entry, so a callback falls through to `new_client` (L615). `check_search_readiness`'s `askFor`/`ready` semantics are written for `find_available_slots` only (L1296–1348). Part 4's objective claims CDAS as its own outcome while Part 4 holds no slot tool at all (L1007–1012). Part 4's `routed_to_message` outcome even asserts "or no callback slots were available" (L1019) — an availability judgement it cannot make.
**Why an ordinary contradiction review might miss it:** Every statement is individually consistent: Part 4 routes, the Scheduler books, and CDAS is a real product. The overlap lives in the unassigned middle — the *search* — and in a tool that is owned by one agent but used by no workflow.
**Customer or operational risk:** Callback availability can be computed two ways with two contracts, producing divergent offers, and `callbackWindowSpoken` (a 2:00–4:00 PM window, L1464) has no equivalent in the other contract — so the same product can be described to the caller in two incompatible ways. If both paths are ever wired, one Tax Pro's calendar can be offered twice.
**Recommended specification correction:** Assign CDAS search to exactly one owner and one tool; delete the redundant path or mark the other as deprecated; add a `callback` scenario to `scenario_selection` and a callback ladder; and specify whether Part 4's handback is a transfer of state or a fresh invocation.
**Sections that must also be changed to avoid residual contradictions:** Part 2 `objective`; `broadening.scenario_selection`; `broadening.ladders`; `agent_specific_tools` (L727–728); `agent_specific_outcomes`; Part 4 objective (L964), `agent_specific_outcomes` (L1017–1020); Part 5 §5.2 (`find_available_slots` note L1348 and `find_available_cdas_slots`).
**Required regression tests:** (1) Callback request routed from Part 4 → exactly one slot search executes, with the documented contract. (2) Callback availability is spoken identically regardless of entry path. (3) A callback slot cannot be offered by two searches in one invocation.

### F-04 — The callback appointment type has no scenario or ladder, and the fallback ladder offers forbidden methods

**Finding ID:** F-04
**Severity:** High
**Confidence:** Certain
**Agent:** Appointment Scheduler (Part 2)
**Capability:** Availability search; slot selection
**Observed behavior:** `scenario_selection` enumerates ten selection rules (L604–615). None matches `appointmentType = callback`; rule 10 sends every unmatched case to `new_client`. The `new_client` ladder's third rung is `digital_drop_off` (L623) and its fourth is `nearby_offices` — at which point the search is over an office, not a Tax Pro calendar. The `callback` type permits **only** `phone_callback` (L317).
**Stated scope:** "Never propose, select or broaden to an office returning acceptsAppointmentType false for that type" (L521) and the type table's "Permitted Methods" is authoritative (L311–318).
**Expected boundary:** A ladder may never propose a method the type does not permit; a callback must broaden within callback-permitted options (other callback windows with the same Tax Pro, adjacent dates, another office's CDAS inventory) or exhaust and hand back.
**Boundary trigger:** Callback request with no matching CDAS slot.
**Required next action:** Either add a `callback` scenario with an explicit ladder, or make `scenario_selection` declare that callback searches do not broaden and terminate in `no_acceptable_availability`.
**Evidence supporting the observed behavior:** `callback` permits only `phone_callback` (L317); `new_client` rungs include `digital_drop_off` (L623); `scheduler_always` requires the type to be sent on every search call (L521) but the ladder determines what the search asks for.
**Evidence creating the conflicting or overlapping ownership:** The tax_notice ladder (L669–679) explicitly lists `phone_callback` as a rung, demonstrating that the design does treat channel substitutions as rungs — but only where the type's permitted-methods set allows them. The design never performs that check for callback, and `emerald_advance` is the one type whose ladder was deliberately restricted to permitted methods (L661–668) yet callback — equally restricted — was not.
**Why an ordinary contradiction review might miss it:** There is no textual contradiction: no rule says "callback has a ladder". The omission is only detectable by testing the type table against the ladder table.
**Customer or operational risk:** A caller routed for a 15-minute callback can be offered an in-person or digital drop-off appointment the business never intended for that intent, or an office-scoped search that silently converts a Tax Pro callback into a walk-in — the exact "silent substitution" the broadening principles forbid (L595).
**Recommended specification correction:** Add `callback` to `scenario_selection` (before the `new_client` catch-all) with a callback ladder restricted to CDAS-permitted rungs, and add a global ladder guard: "no rung may propose a method outside the type's Permitted Methods set."
**Sections that must also be changed to avoid residual contradictions:** Part 2 `broadening.scenario_selection` (L604–615); `broadening.ladders` (add `callback`); `broadening.principles` (add the method-permission guard); Part 2 State 2 appointment-type table (L311–318); Part 5 `find_available_slots` rung enum (L1396).
**Required regression tests:** (1) Callback with zero CDAS results never offers `digital_drop_off`, `virtual`, or `in_person`. (2) Callback broadening never changes `appointmentType`. (3) Type/method permission is enforced at the ladder level for every one of the five types.

### F-05 — The callback handback payload exceeds the terminal payload contract and loses required context

**Finding ID:** F-05
**Severity:** High
**Confidence:** Certain
**Agent:** Speak to a Tax Pro (Part 4) → Appointment Scheduler
**Capability:** Deterministic handoff; context transfer
**Observed behavior:** Part 4 is required to "return route_intent with routingTarget set to appointment_scheduler and appointmentType set to callback" (L973), and the examples show the payload carrying "nextAction = route_intent, routingTarget = appointment_scheduler, and appointmentType = callback" (L941, L956).
**Stated scope:** "On route_intent include routingTarget (refund_status, faq_agent, appointment_scheduler, tax_prep, or named destination). Carry applicable outcome fields: …" (L248). `appointmentType` is not among the carried fields.
**Expected boundary:** A handoff must carry exactly the fields the receiving agent needs and no unspecified fields; where the receiving agent's workflow requires identity, that requirement must be expressible in the contract.
**Boundary trigger:** Part 4 yields after eliciting the reason and resolving the Tax Pro by name (L996–1000).
**Required next action:** The contract must define the callback handoff fields, or the handback must be restructured so the receiving agent re-collects them.
**Evidence supporting the observed behavior:** L973, L941, L956 pass `appointmentType`; L909 requires Part 4 to "Pass the resolved taxProRef or officeRef" for the message path only; L913 defines the callback handoff as a payload with no reason field.
**Evidence creating the conflicting or overlapping ownership:** The Scheduler's callback rule requires capturing "the reason for the call in appointmentNotes" (L527) — but Part 4 already elicited the reason (L881, L966) and has no contractual field in which to pass it. Meanwhile the Scheduler's `schedule_new` step 1 requires authentication and `find_customer` before retrieval (L565), and its skip rule depends on `customerRef` arriving (L514) — which the contract permits only "when identity was resolved" and which Part 4 is never told to pass on the callback path.
**Why an ordinary contradiction review might miss it:** Both halves read correctly in isolation: Part 4 routes a callback; the Scheduler books callbacks and asks for the reason. Only the field-level comparison of the two shows that the reason is collected twice, discarded once, and that the type field travels outside the contract.
**Customer or operational risk:** The caller repeats their reason to the second agent (or the Scheduler proceeds without it and the Tax Pro calls back blind). Under a strict payload validator, the out-of-contract `appointmentType` field is dropped and the Scheduler re-asks the type — defeating the entire purpose of the handoff.
**Recommended specification correction:** Add the callback handoff explicitly to `terminal_payload_contract`: required carried fields (`appointmentType`, `intent`, `sourceUtterance`/reason, resolved `taxProRef`/`officeRef`, `customerRef`/`customerStatus` when authenticated) and a prohibition on re-collecting elicitation already performed. State whether a handback is a fresh invocation (with the Head of Call envelope) or an in-process transfer.
**Sections that must also be changed to avoid residual contradictions:** Part 1 `terminal_payload_contract` (L248); Part 1 `global_outcomes.intent_changed` (L234); Part 4 `tax_pro_always` (L973), `workflow.speak_to_tp_by_name` step 7 (L1000); Part 2 `scheduler_always` (L514, L527) and `workflow.schedule_new` step 1 (L565).
**Required regression tests:** (1) Callback handed back from Part 4 carries the reason and Tax Pro and the Scheduler does not re-elicit either. (2) A handoff payload missing a contract field is rejected, not silently completed. (3) Post-handback authentication is not re-run when `customerRef` and `customerStatus` are present.

### F-06 — Part 4's mandated MyBlock mention overrides the universal zero-web-deflection rule

**Finding ID:** F-06
**Severity:** High
**Confidence:** Certain
**Agent:** Speak to a Tax Pro (Part 4)
**Capability:** Informational/promotional speech (web/app referral)
**Observed behavior:** Part 4 is required to proactively promote an app: "Mention MyBlock ('For your convenience, you can also message your tax pro anytime through the MyBlock app')" (L972), and the examples show it in the standard option statement (L922, L954).
**Stated scope:** Universal: "Never suggest going online. Never speak a URL, website, portal, or app name. Exception: For Digital Drop-Off (DDO), state only that a secure upload link is being sent via text or email." (L60, repeated L158) and `prohibited_phrases` includes "messaging system" (L185). Part 4's own `agent_never`: "Never suggest going online, a portal, online scheduling, or a web link; only the DDO secure-upload-link statement is exempt" (L980).
**Expected boundary:** No agent speaks an app, portal or web destination. Feedback about the messaging channel belongs to a global marketing/handoff owner, not to an agent whose objective is to *avoid* channel proliferation.
**Boundary trigger:** Any Part 4 turn that states the callback/message options (L971).
**Required next action:** Remove the mandate, or elevate it into the universal exception list with an explicit governance statement that it overrides L60/L158/L980 — and then propagate that exception everywhere the universal rule is stated.
**Evidence supporting the observed behavior:** L902 (Business Intent), L922 (dialogue 4A), L954 (dialogue 4E), L972 (`tax_pro_always`), i.e. four independent sections.
**Evidence creating the conflicting or overlapping ownership:** The universal rule is stated twice as absolute (L60, L158) and is re-asserted inside the same agent that mandates the violation (L980). The DDO exception is described as the *only* exception; MyBlock is not DDO. No section anywhere assigns MyBlock messaging an owner: it is a channel that is neither the deterministic Leave a Message flow nor the Scheduler.
**Why an ordinary contradiction review might miss it:** A reviewer comparing "never" lists would see Part 4's `never` list as merely echoing the universal rule and stop; the conflict is between that agent's `always` and `never` lists, both of which are internally worded as absolutes, and neither of which cross-references the other.
**Customer or operational risk:** (a) An unowned support channel is advertised by an agent that cannot service it — the caller is sent to MyBlock for a message whose handling, retries and SLAs belong to a different flow. (b) Inconsistency across agents: a caller asking the same question to the Office Information agent never hears about MyBlock (L834 forbids pointing to apps), which is auditable and confusing. (c) Any compliance review of the zero-web-deflection rule will find the spec self-contradicting.
**Recommended specification correction:** Delete the MyBlock mandate from Part 4 (the DDO statement remains the sole exception), or add a named global exception with its owner, its exact permitted wording, and a rule stating which agents may speak it.
**Sections that must also be changed to avoid residual contradictions:** Part 4 `tax_pro_always` (L972), `never` list (L980), Business Intent "Fulfillment Priority" (L902), dialogues 4A (L922) and 4E (L954); Part 1 §1.2 "Zero Web Deflection" (L60), `global_never` (L158), `global_voice_lexicon.prohibited_phrases` (L170–188); Part 3 `office_never` (L834) if consistency is to be preserved.
**Required regression tests:** (1) No agent turn contains a URL, website name, portal name or app name, and the assertion is run across all four agents' scripted lines. (2) The only permitted exception string is the DDO statement. (3) Part 4's option statement still works with MyBlock removed.

### F-07 — A request for a human is owned twice, with opposite behaviours, and Part 3 lacks the local-desk transfer prohibition

**Finding ID:** F-07
**Severity:** High
**Confidence:** Certain
**Agent:** Office Information Agent (Part 3) vs Speak to a Tax Pro (Part 4) vs universal rule
**Capability:** Live transfer; office contact triage
**Observed behavior:** Universal rule: "Caller-Initiated Barging (explicit central live-agent request, not local office contact) → Call `transfer_to_agent`." (L108) and `global_always` "Call `transfer_to_agent` … immediately when the caller explicitly requests a live agent (barging)" (L151). Part 4 obeys (L887, L946). Part 3, given the same utterance shape, does **not** transfer: "I need to talk to the receptionist at the Oak Ridge office" is handled by `check_office_open_status` and answered with either `capture_intent` (open, L776/L803) or `leave_message_offer` (closed, L777/L796). Part 3's `transfer_to_agent` description limits itself to "unresolved intent or office lookup failure" (L853).
**Stated scope:** Part 3: "office contact triage (reaching staff, leaving messages) without attempting to schedule or modify appointments" (L758). Part 4: "Requests for local office staff belong to the Office Information Agent" (L877).
**Expected boundary:** Exactly one owner decides whether a human-contact request becomes a live transfer, a captured intent, or a message offer — and one vocabulary (see F-26, F-21) defines "local office contact" versus "central live agent". Part 3 is the only agent that faces local-office contact requests and it is the only agent **without** a prohibition on transferring to a local desk.
**Boundary trigger:** "Transfer me to someone at the front desk" / "I need to talk to the receptionist".
**Required next action:** Define, in one authoritative place, whether local-office contact is a transfer, a capture_intent, or a message offer, and give Part 3 the same explicit never-clause Part 4 holds.
**Evidence supporting the observed behavior:** L108 (the carve-out, which is a parenthetical, not a definition), L151, L776–777, L796–804, L849, L853, L887, L977.
**Evidence creating the conflicting or overlapping ownership:** Part 4's `never`: "Never perform live phone transfers to local office desks or individual Tax Professionals" (L977) has **no counterpart** in Part 3's `office_never` (L830–836) — despite Part 3 being the agent that discusses those very desks and holding `transfer_to_agent`. `capture_intent` (L776, L804) is an undefined action that hands the caller back to Head of Call "to ask how the system can help them today" — functionally a soft transfer whose owner is not named.
**Why an ordinary contradiction review might miss it:** There is no textual contradiction; the universal rule's carve-out ("not local office contact") appears to resolve it. But "local office contact" is never defined, and the only agent that must interpret it (Part 3) is given neither the definition nor the matching prohibition. Reviewers comparing the two `never` lists would have to notice an *absence*.
**Customer or operational risk:** A caller asking for the front desk is bounced back into a menu-like loop (`capture_intent`) or offered a message instead of a human — while the same words to Part 4 produce an immediate transfer. Inconsistent handling of "I want a person" is the single most common source of escalations and complaints in IVA deployments.
**Recommended specification correction:** Add one authoritative definition of local-office-contact vs central-live-agent, add Part 3 to the barging rule with its exact permitted actions, and add the local-desk transfer prohibition to `office_never`.
**Sections that must also be changed to avoid residual contradictions:** Part 1 §1.4 barge row (L108), `global_always` (L151); Part 3 State 1 "Office Contact Triage" (L773–778), `office_never` (L830–836), `agent_specific_tools.transfer_to_agent` (L853); Part 4 scope statement (L877) and `tax_pro_never` (L977).
**Required regression tests:** (1) Every human-contact utterance class is handled identically regardless of which agent receives it. (2) Part 3 never executes a live transfer to a local desk. (3) The "front desk" utterance produces a documented, testable outcome.

### F-08 — The FAQ Agent's scope is bypassable from every agent that holds `search_knowledge_base`

**Finding ID:** F-08
**Severity:** High
**Confidence:** Likely
**Agent:** Appointment Scheduler, Office Information, Speak to a Tax Pro (all hold the tool); FAQ Agent (deterministic destination)
**Capability:** Informational answering; intent routing
**Observed behavior:** Part 4 routes to the FAQ Agent for "general tax questions, login difficulty, MyBlock credential issues, password resets, account access, or income tax course information" (L885). The Scheduler, Office Information and Speak to a Tax Pro agents all hold `search_knowledge_base` with the category set "digital_account_support, financial_products, identity_and_fraud, tax_prep_and_records, appointments_and_logistics, contact_directories" (L733, L856, L1011, L1058) — including `digital_account_support` (login/credential issues), `identity_and_fraud`, and `tax_prep_and_records` (general tax questions). No agent-specific rule tells any of the other three to route such questions to `faq_agent`.
**Stated scope:** FAQ Agent owns general tax questions, login difficulty, credential issues, password resets, account access, income tax courses (L885).
**Expected boundary:** A routing destination exists so other agents *stop* answering. If the same questions can be answered in-agent from the same repository, the destination is advisory only.
**Boundary trigger:** "I can't log into MyBlock" or "what's the standard deduction" said to the Scheduler, Office Info, or Part 4 agent.
**Required next action:** Either restrict each agent's `search_knowledge_base.category` to its own scope, or make the FAQ route mandatory for the overlapping categories, or accept consciously that FAQ is not a boundary.
**Evidence supporting the observed behavior:** The four identical tool descriptions and the six-category enum (L733, L856, L1011, L1058). `interruptions.informational_question` in all three agents (L737, L859, L1014) instructs them to call `search_knowledge_base` and answer — never to route.
**Evidence creating the conflicting or overlapping ownership:** `faq_agent` appears as a `routingTarget` only in Part 4 (L885) and in the global enum (L248). The global `intent_changed` outcome (L234) authorizes routing but no agent-specific rule compels it for FAQ material. `KB results: … requires_tax_pro routes to a Tax Pro` (L1075) is the only KB result with a mandated route, and it names no owning agent.
**Why an ordinary contradiction review might miss it:** Knowledge-base access reads as a harmless shared utility, and each agent legitimately needs *some* KB categories (e.g. `appointments_and_logistics`). The escalation is invisible until each agent's permitted categories are compared against the FAQ Agent's exclusive scope — a permission-table comparison, not a sentence-level one.
**Customer or operational risk:** A caller with a password-reset problem is answered by a scheduling agent from an ungoverned category, possibly with content the FAQ flow would have handled with proper verification; conversely the same question is refused elsewhere, creating an inconsistent product. Duplicate answering also splits `questionsAnswered`/`topicsCovered` reporting across intents.
**Recommended specification correction:** Give each agent a per-agent category allow-list (e.g. Scheduler: `appointments_and_logistics`, `contact_directories`; Office Info: `contact_directories`), and add an explicit instruction: questions in FAQ Agent scope route to `faq_agent` rather than being answered. Define who acts on `requires_tax_pro`.
**Sections that must also be changed to avoid residual contradictions:** Part 2 `agent_specific_tools.search_knowledge_base` (L733) and `interruptions` (L737); Part 3 `agent_specific_tools.search_knowledge_base` (L856) and `interruptions` (L859); Part 4 `agent_specific_tools.search_knowledge_base` (L1011), `tax_pro_always` (L974), `agent_specific_outcomes`; Part 1 `terminal_payload_contract` (`routingTarget`, L248); Part 5 §5.1 `search_knowledge_base` category enums (L1058) and KB results note (L1075).
**Required regression tests:** (1) Each overlapping category from each agent either routes or is refused, per the allow-list. (2) `faq_agent` is reachable from all four agents. (3) `requires_tax_pro` has a defined owner and terminal outcome.

### F-09 — Hours, directions and phone numbers have two owners and two sources of truth

**Finding ID:** F-09
**Severity:** High
**Confidence:** Likely
**Agent:** Office Information Agent vs Appointment Scheduler
**Capability:** Office lookup; informational answering
**Observed behavior:** Office Information owns hours/address/directions via `get_office_details` and owns open/closed status via `check_office_open_status` (L855, L775). The Scheduler holds neither tool, but it holds `search_knowledge_base` with `appointments_and_logistics` and `contact_directories` (L733) and an `interruptions.informational_question` rule telling it to answer and resume (L737). Universal rule: "Never invent hours from memory" (L67) — but KB is a second, non-tool source that the universal rule does not govern.
**Stated scope:** Office Information: "Answer questions about physical office locations, operating hours, landmark directions, and local office contact options" (L819). Scheduler: appointment transaction + informational interruptions.
**Expected boundary:** One source of truth for office hours and one owner of office-facts answering; a scheduling agent that needs hours should route or hand back.
**Boundary trigger:** "Are you open right now?" or "What's your phone number?" asked mid-booking.
**Required next action:** Scheduler routes office-facts questions to the Office Information agent, or its KB categories are restricted so that it cannot answer them.
**Evidence supporting the observed behavior:** L733 vs L856; L823 (Office Info synthesizes `todayHoursSpoken`, `addressLine1Spoken`, `addressDirectionsSpoken`); L775 ("Relies strictly on `check_office_open_status` … Never calculate time math manually"); L1058 category enum available to every KB holder.
**Evidence creating the conflicting or overlapping ownership:** `get_office_details` and `check_office_open_status` are assigned **only** to Part 3 (L852–857), yet the universal `route_intent` `routingTarget` enum contains no `office_info`/`office_contact` value (L248) — so from the Scheduler there is no defined route to the owner of office facts, only the KB workaround. Part 3 additionally owns the cross-office phone-number restriction (L778, L833) which no other agent inherits, so the Scheduler speaking a phone number from `contact_directories` would bypass a governance rule that exists.
**Why an ordinary contradiction review might miss it:** Both agents legitimately need office context; the Scheduler speaks `officeName`/`addressLine1Spoken` throughout the booking flow (L515), so its office competence looks intended. The conflict is between *booked* office data and *quizzed* office facts — two different contracts that happen to share vocabulary.
**Customer or operational risk:** Two offices' hours can be quoted from two repositories in one call; a caller gets a phone number from the Scheduler that Part 3's cross-office rule forbids it from giving; and "never invent hours" is unenforceable against a KB answer.
**Recommended specification correction:** Add `office_info`/`office_contact` to `routingTarget`, add a Scheduler interruption rule that routes office-facts questions, and restrict KB categories per agent (overlaps F-08).
**Sections that must also be changed to avoid residual contradictions:** Part 2 `agent_specific_tools.search_knowledge_base` (L733), `interruptions.informational_question` (L737); Part 3 `agent_specific_tools` (L852–857), `office_never` (L833); Part 1 §1.2 "Hours: One Source, Spoken Once" (L65–67), `terminal_payload_contract` (L248).
**Required regression tests:** (1) Office hours are always sourced from `get_office_details`/`check_office_open_status`. (2) No agent other than Office Information speaks `mainPhoneSpoken`. (3) Cross-office phone restriction is enforced wherever a phone number can be spoken.

### F-10 — The silence rule and the abandonment outcome disagree about who terminates the call

**Finding ID:** F-10
**Severity:** High
**Confidence:** Certain
**Agent:** Universal (all agents) vs Head of Call
**Capability:** Call closure; deterministic handoff (termination)
**Observed behavior:** "On the second consecutive silence, do not call `transfer_to_agent`. Instead, yield the floor and return a terminal payload to the Head of Call to terminate the suspected robocall." (L72, restated L150). The outcome table says the opposite: `customer_abandoned` — "Never treat an unanswered gate as abandonment: an unanswered gate runs the reprompt rule, **then transfers**." (L246).
**Stated scope:** Head of Call owns termination; agents never call `transfer_to_agent` on silence (L1081: "Never call this tool for consecutive silence or suspected robocalls").
**Expected boundary:** On the second consecutive silence exactly one action occurs — silent handback for termination — with no tool call.
**Boundary trigger:** Second consecutive silence, including silence at a confirmation gate.
**Required next action:** Align both texts to the no-tool termination path and state explicitly that a silent gate is not a transfer condition.
**Evidence supporting the observed behavior:** L72, L109, L150, L163, L241, L1081.
**Evidence creating the conflicting or overlapping ownership:** L246 in the same outcome table, which describes an unanswered gate as reprompt-then-transfer. `global_always` (L150) and `global_outcomes.customer_abandoned` (L246) are both in the Universal Base JSON and are inherited by every agent, so every agent contains both instructions.
**Why an ordinary contradiction review might miss it:** The two statements live in different registers — one in prose guardrails, one in the outcomes JSON — and both are individually plausible (an unanswered gate *feels* like it should escalate). The conflict only surfaces when the two are placed side by side, which is exactly what an inheritance review would not normally do.
**Customer or operational risk:** A dead-air robocall can be transferred to a live representative and consume a human seat (the single highest-cost error in the flow); conversely a genuine caller on a bad line can be terminated. Either branch is defensible; both cannot be implemented.
**Recommended specification correction:** Rewrite `customer_abandoned` to remove "then transfers", state the gate case explicitly ("an unanswered gate runs the reprompt rule, then the silence rule"), and state that silence never calls `transfer_to_agent`.
**Sections that must also be changed to avoid residual contradictions:** Part 1 §1.2 "Input Exhaustion & Silence" (L69–73), §1.4 "Consecutive Silence" row (L109), `global_always` (L150), `global_never` (L163), `global_outcomes.consecutive_silence` (L241), `global_outcomes.customer_abandoned` (L246), Part 5 §5.1 `transfer_to_agent` (L1081).
**Required regression tests:** (1) Second consecutive silence produces exactly one terminal payload with `nextAction: end_call` and zero tool calls. (2) Silence at a pre-commit gate does not produce a transfer. (3) A dropped-call platform event produces `customer_abandoned`, and the two cases are distinguishable in telemetry.

### F-11 — No agent has a post-boundary tool-prohibition rule

**Finding ID:** F-11
**Severity:** High
**Confidence:** Certain
**Agent:** All four agents (systemic)
**Capability:** Deterministic handoff; boundary enforcement
**Observed behavior:** The document specifies in detail which tools each agent *may* call and which words it may *not* speak. It never states which tools an agent must **stop** calling once a boundary has been reached: after committing, after deciding `intent_changed`, after `transfer_to_agent` returns, after a `no_acceptable_availability` transfer, after handing back `leave_message`/`leave_message_offer`, or after a barging transfer.
**Stated scope:** The boundaries exist (L234–246, L708–711, L738–739, L860, L1015) but are expressed only as return values, never as tool locks.
**Expected boundary:** Every handback must be accompanied by an explicit prohibition set, e.g. "after emitting `intent_changed`, do not call `book_appointment`, `reschedule_appointment`, `cancel_appointment`, `send_secure_link`, `find_available_slots`, or `check_search_readiness`."
**Boundary trigger:** Any handback or commit.
**Required next action:** Add a per-agent post-boundary prohibition list, mirroring the `never` lists.
**Evidence supporting the observed behavior:** No such list exists in `scheduler_never` (L550–562), `office_never` (L830–836), `tax_pro_never` (L976–983), or the universal `global_never` (L156–165).
**Evidence creating the conflicting or overlapping ownership:** The document explicitly contemplates post-boundary tool use for one tool only: `transfer_to_agent` (`lastQuestionSpoken` is populated with the final question, L1079) and it separately forbids *one* thing after *one* boundary — "one invocation commits at most one transaction" (L711). Nothing else is locked. `interruptions.cancel_said` compounds this: after a commit the agent must "close the committed transaction normally and hand back `intent_changed` rather than starting a second transaction here" (L738) — an instruction that relies on the agent's restraint rather than a tool prohibition.
**Why an ordinary contradiction review might miss it:** Omissions are invisible to contradiction search. Everything the document does say is consistent; the defect is what is not said, and it only becomes observable in a stateful implementation where a model, having handed back, still holds a live write tool.
**Customer or operational risk:** A double transaction (booking plus a second write in the same invocation), a DDO link sent after a message handback, or a re-search after the caller already accepted a slot — all of which the "one transaction per invocation" rule forbids conceptually but cannot enforce mechanically.
**Recommended specification correction:** Add a `post_boundary_prohibited_tools` block to each agent's tool section, plus a universal statement: "After emitting a terminal payload, the invocation is closed; no further tool call of any kind is permitted."
**Sections that must also be changed to avoid residual contradictions:** Part 1 `global_never` (L156–165) and `closure`-equivalent statements (L77–85); Part 2 `scheduler_never` (L550–562), `closure` (L707–712), `interruptions` (L736–740); Part 3 `office_never` (L830–836), `interruptions` (L858–860); Part 4 `tax_pro_never` (L976–983), `interruptions` (L1013–1015); Part 5 tool sections (each write tool).
**Required regression tests:** (1) After any terminal payload, no tool call is possible in the same invocation (assert via tool-call counts). (2) A caller who cancels after committing produces no second write. (3) A caller who accepts a slot and then asks for a person produces no post-acceptance search.

### F-12 — Intent classification has no owner and there is no global intent→agent routing table

**Finding ID:** F-12
**Severity:** High
**Confidence:** Likely
**Agent:** Head of Call (entry) + all four agents
**Capability:** Intent classification; deterministic handoff
**Observed behavior:** The Head of Call envelope passes `sourceUtterance` ("Verbatim Intent", L21) and an `operation` (L26) but no intent classification. Each agent independently establishes intent: the Scheduler establishes the appointment type (L303–308), Office Information disambiguates a three-way choice (L760–765), Part 4 elicits the reason and classifies out-of-scope intents (L881–887). The `terminal_payload_contract` nonetheless requires every agent to "Resolve unclear_intent before return" (L248) — an intent value whose only handling workflow exists in Part 3 (L764).
**Stated scope:** No section states who classifies the caller's intent, or which intent maps to which agent.
**Expected boundary:** An explicit classifier (deterministic or agent-owned) produces an intent, and each agent has a defined entry contract stating which intents it accepts and to which agent every other intent is routed.
**Boundary trigger:** A caller whose utterance is ambiguous, or who changes intent before any agent has committed.
**Required next action:** Name the intent owner and publish the routing table; align the `intent` enum with the values agents can actually resolve.
**Evidence supporting the observed behavior:** L21, L26, L248, L752–765, L881–887; there is no routing table anywhere in Parts 1–5.
**Evidence creating the conflicting or overlapping ownership:** All four agents can classify and all four can answer with KB (F-08); `routingTarget` covers only five values (L248) and omits `office_info`/`office_contact` (F-09) and any destination for `unclear_intent`; Part 4's `tax_pro_always` says "If intent is unclear, ask whether the caller wants a callback appointment" (L974) while Part 3's unclear-intent handling offers hours-or-staff — two different unclear-intent resolutions in two agents, in the same conversation.
**Why an ordinary contradiction review might miss it:** Each agent's local disambiguation is well-written and self-consistent; a reviewer reads them as complementary rather than as four competing classifiers. There is no textual contradiction to find, only an absent ownership rule.
**Customer or operational risk:** The same utterance produces different journeys depending on which agent received it; `unclear_intent` can be resolved into an appointment request the caller never made (Part 4, L974); and reporting via the `intent` field becomes unreliable across agents.
**Recommended specification correction:** Publish an intent→agent routing matrix, assign classification to the Head of Call (or to a named classifier), define the acceptance contract for each agent, and reconcile `unclear_intent` into a single owner.
**Sections that must also be changed to avoid residual contradictions:** Part 1 §1.1 (L15–30), §1.5 `terminal_payload_contract` (L248), `global_outcomes.intent_changed` (L234); Part 2 State 2 (L302–308); Part 3 State 1 (L760–765), `office_always` (L822); Part 4 `tax_pro_always` (L974).
**Required regression tests:** (1) Every enumerated intent routes to exactly one agent, deterministically. (2) `unclear_intent` has one resolution path and cannot become an appointment request. (3) The same ambiguous utterance yields the same journey from every entry point.

### F-13 — Office Information turns a satisfied information request into a message offer

**Finding ID:** F-13
**Severity:** Medium
**Confidence:** Certain
**Agent:** Office Information Agent (Part 3)
**Capability:** Informational answering; message capture handoff
**Observed behavior:** On the `office_contact` path with a closed office, the agent states the closure, reads `nextOpenHoursSpoken`, provides `mainPhoneSpoken`, then "stop[s] speaking and return[s] nextAction = leave_message_offer" (L777, L826, L849). The caller's stated need — to reach the office — has been answered with hours and a number.
**Stated scope:** "office_contact_triage_complete: Caller received office contact details for a closed office **or** explicitly requested a message … nextAction leave_message_offer **or** leave_message" (L864).
**Expected boundary:** `leave_message_offer` should be returned only when the caller's need is unsatisfied, or when the caller asks. A satisfied informational answer should close through `offer_additional_help`.
**Boundary trigger:** Closed-office contact inquiry where the agent has already supplied the phone number and hours.
**Required next action:** Return `offer_additional_help` (or `close`) after a satisfied answer; reserve `leave_message_offer` for the unsatisfied case and for explicit requests.
**Evidence supporting the observed behavior:** L777, L797, L826, L849; `office_never` forbids the agent from asking about a message (L835), so the flow pushes the caller into a message path the agent is forbidden even to explain.
**Evidence creating the conflicting or overlapping ownership:** The deterministic Leave a Message flow "owns the offer where still needed, recipient and office resolution, callback-number capture, recording instructions, recording, transcription, Work Center submission, retries, failure handling, additional help, and call closure" (L85) — so an unnecessary `leave_message_offer` transfers a *satisfied* call, plus call closure, to a flow whose stated purpose is message capture. `office_contact_flow` step 0 already separates explicit message requests (L845), meaning the step-4 offer is unconditioned on need.
**Why an ordinary contradiction review might miss it:** The outcome name (`office_contact_triage_complete`) and the flow step read as a coherent pair; the defect is that "triage complete" was defined to include a message offer regardless of whether anything remains to do.
**Customer or operational risk:** Every closed-office call is funneled into a recording flow the caller did not ask for, inflating message volume, misleading Work Center queues, and replacing a clean close with a recording prompt — while the caller already holds the phone number.
**Recommended specification correction:** Split the outcome into `office_contact_details_provided` (satisfied → `offer_additional_help`/`close`) and `office_contact_message_offered` (unsatisfied → `leave_message_offer`), and state the condition explicitly.
**Sections that must also be changed to avoid residual contradictions:** Part 3 State 1 "Office Contact Triage" (L773–778), `office_always` (L826), `workflow.office_contact_flow` step 4 (L849), `agent_specific_outcomes.office_contact_triage_complete` (L864); Part 1 §1.3 `leave_message_offer` semantics (L85), `global_outcomes.transfer_unavailable` (L245).
**Required regression tests:** (1) Closed-office contact query with a delivered phone number returns no message offer. (2) `leave_message_offer` is returned only when the caller asks or the need is unmet. (3) A satisfied office-info call closes through the standard additional-help path.

### F-14 — "Reason for the call" versus "message content": no authoritative distinction

**Finding ID:** F-14
**Severity:** Medium
**Confidence:** Certain
**Agent:** Appointment Scheduler (Part 2) vs the deterministic Leave a Message flow
**Capability:** Message capture (prohibited in-agent); preference gathering
**Observed behavior:** Universal: agents "never capture, solicit, record, transcribe, store, submit, or confirm delivery of a caller's message" (L85) and "Never ask the caller to dictate a message; never capture message content" (L162). Scheduler: "On callback, capture the reason for the call in `appointmentNotes`" (L527), with the example note "Received IRS letter CP2000" (L1499).
**Stated scope:** Message content is exclusively the deterministic flow's; the Scheduler may capture type-specific structured values (notice details, notes).
**Expected boundary:** A rule distinguishing structured scheduling metadata from free-text caller narration, plus rules on retention, consent and 7216 handling for anything captured into `appointmentNotes`.
**Boundary trigger:** The caller describes why they need the callback.
**Required next action:** Define `appointmentNotes` content policy, or route free-text narration to the deterministic flow and store only enumerated reason codes.
**Evidence supporting the observed behavior:** L527, L317 (callback row), L1499; `tax_notice_service` captures structured notice values rather than narration (L522), showing the design does know how to constrain capture.
**Evidence creating the conflicting or overlapping ownership:** The Leave a Message flow owns "recipient and office resolution, callback-number capture, recording instructions, recording, transcription" (L85); the Scheduler performs office resolution, destination capture and narrative capture for callbacks. Without a definition of "message content", the two rules cannot be reconciled: "the reason for the call" *is* content by any ordinary reading, and it is stored in the same enterprise record the Tax Pro will read.
**Why an ordinary contradiction review might miss it:** "Capture the reason" is a scheduling requirement and "never capture message content" is a compliance rule; they live in different parts of the document and in different registers (workflow vs. global never), and each is impeccable where it stands.
**Customer or operational risk:** Caller utterances — which may include notice codes, financial detail or personal circumstances — are stored in a scheduling note field with no stated retention, redaction or 7216 treatment, bypassing the flow that was built (with transcription and Work Center submission controls) precisely for caller narration.
**Recommended specification correction:** Define "message content" explicitly; constrain `appointmentNotes` to enumerated reason codes or a length-capped, redaction-governed field; state that free-text narration of the caller's problem routes to the deterministic flow.
**Sections that must also be changed to avoid residual contradictions:** Part 1 §1.3 "Leave-a-Message Ownership" (L85), `global_never` (L162), `global_always` (L152); Part 2 State 2 callback row (L317), `scheduler_always` (L527); Part 2 `agent_specific_tools.book_appointment` (L729); Part 5 §5.2 `book_appointment` request examples (L1499).
**Required regression tests:** (1) `appointmentNotes` is bounded by the defined content policy. (2) No agent stores free-text caller narration. (3) Message-content capture is only reachable through the deterministic flow, asserted per field.

### F-15 — Off-season closure is owned twice, from two data sources, with different eligibility outcomes

**Finding ID:** F-15
**Severity:** Medium
**Confidence:** Certain
**Agent:** Appointment Scheduler vs Office Information Agent
**Capability:** Office lookup; seasonal handling
**Observed behavior:** Scheduler: on a closed/unavailable office it calls `find_offices_near` with `isYearRoundOffice: true` and proposes the nearest Year-Round Office, using the approved line "Our [officeName] office is closed for the season, so the closest one that's open year-round is [officeName]. Would that work?" (L383, L530, L111). Office Information: on `seasonalStatus: closed_for_season` it "state[s] the closure, offer[s] `yroOfficeAddressSpoken`, and store[s] `yroOfficeRef`" from `get_office_details` (L771, L828).
**Stated scope:** Scheduler owns office eligibility for a type (`acceptsAppointmentType`, L309, L521); Office Information owns office details (L819).
**Expected boundary:** One owner presents the Year-Round Office alternative, and any office proposed into a booking flow must first be validated for eligibility.
**Boundary trigger:** Any `closed_for_season` state reached from either agent.
**Required next action:** Designate one owner for the YRO proposal; make cross-agent office proposals carry eligibility state.
**Evidence supporting the observed behavior:** L383, L530, L111 (Scheduler); L771, L828, L1760 (`yroOfficeRef`, `yroOfficeAddressSpoken` from `get_office_details`).
**Evidence creating the conflicting or overlapping ownership:** The two implementations use different tools and different fields (`find_offices_near.isYearRoundOffice` vs `get_office_details.yroOfficeRef`). `get_office_details` returns no `acceptsAppointmentType` (L1748–1768) while `find_offices_near` does (L1281) — so an Office Information agent can proactively offer, and later hand to the Scheduler, a YRO that does not accept the caller's appointment type (F-25). The Scheduler's approved line additionally asks a consent question ("Would that work?"), i.e. solicits a booking at the moment of a seasonal edge case.
**Why an ordinary contradiction review might miss it:** The two sections address different intents (book vs. ask) so they never appear side by side; both lines are correct in isolation and neither mentions the other's data source.
**Customer or operational risk:** The caller is offered a Year-Round Office that cannot serve their appointment type, producing a second failure after a seasonal closure; and the same seasonal fact is spoken from two repositories with no reconciliation.
**Recommended specification correction:** Make `find_offices_near` the single authority for any office proposed into a booking flow (including from Part 3), add `acceptsAppointmentType` to `get_office_details`, and specify that a YRO proposal from Office Information is informational and does not constitute a booking offer.
**Sections that must also be changed to avoid residual contradictions:** Part 2 State 3 "Off-Season Closure" (L383), `scheduler_always` (L530), Part 1 §1.4 off-season line (L111); Part 3 State 1 "Off-Season Closure" (L771), `office_always` (L828); Part 5 §5.3 `get_office_details` response (L1748–1771).
**Required regression tests:** (1) No office is proposed for booking without an eligibility check. (2) The YRO alternative is spoken identically from both agents. (3) A YRO that does not accept the type is never offered into a booking flow.

### F-16 — Speak to a Tax Pro performs authentication, a capability assigned to the Scheduler

**Finding ID:** F-16
**Severity:** Medium
**Confidence:** Certain
**Agent:** Speak to a Tax Pro (Part 4)
**Capability:** Authentication; customer retrieval
**Observed behavior:** Part 4's `tax_pro_always` requires: "Disclose a prior-year or assigned Tax Pro only after `find_customer` resolves the owner; for third parties require `registeredAni` true and owner authentication, otherwise transfer without retrieval" (L967), and its tool list contains `find_customer`: "Authenticate the owner before disclosing an assigned or prior-year Tax Pro" (L1008).
**Stated scope:** Part 4's objective is to assist callers in reaching a Tax Pro "via asynchronous Work Center messaging or by routing them to the Appointment Scheduler" and to reroute refund/login queries (L964). Authentication is not named in the objective.
**Expected boundary:** Identity resolution/authentication is a shared capability with one owner and one contract; a routing agent should not run an authentication gate of its own without a defined scope (which values, which third-party rules, which failure outcomes).
**Boundary trigger:** Any Part 4 interaction where a prior-year Tax Pro would be disclosed.
**Required next action:** Either assign third-party authentication to a single owner (Scheduler or a shared pre-handoff gate) and have Part 4 consume `customerRef`, or widen Part 4's objective and mirror the Scheduler's full authentication rule set.
**Evidence supporting the observed behavior:** L967, L988, L1008; Part 2 State 1 defines the authentication logic, third-party requirements, and the `single_match` gate (L260–272).
**Evidence creating the conflicting or overlapping ownership:** Part 4 implements only a fragment of the Scheduler's authentication contract: it requires `registeredAni` and third-party authentication but defines no `multiple_matches`, `no_match`, or `authentication_failed` handling, no DOB/SSN capture sequence, no re-authentication-on-subject-change rule, and no outcome for identity failure beyond `transfer_to_agent` (L1010). Two agents can therefore authenticate the same caller with different rigor and different terminal outcomes.
**Why an ordinary contradiction review might miss it:** Part 4's rule reads as a prudent disclosure guard, and it cites the same concepts (`registeredAni`, third-party) as Part 2 — so it looks like reuse of an existing contract rather than a partial reimplementation of one.
**Customer or operational risk:** Inconsistent identity rigor across the portfolio, with the weaker path possibly disclosing a Tax Pro relationship (and, via `search_tax_pro_by_name`, an office link) on a partial authentication; and duplicated `find_customer` calls with divergent results and telemetry.
**Recommended specification correction:** State that authentication is owned by one agent/gate; in Part 4, replace the tool with consumption of `customerRef`/`customerStatus` (per L28) and add the missing failure outcomes if Part 4 is to retain the capability.
**Sections that must also be changed to avoid residual contradictions:** Part 4 `tax_pro_always` (L967), `workflow.speak_to_tp_generic` step 3 (L988), `agent_specific_tools.find_customer` (L1008), `agent_specific_outcomes` (L1017–1020); Part 2 State 1 (L260–272), `scheduler_always` (L513–514); Part 1 §1.1 `customerRef` (L28).
**Required regression tests:** (1) Third-party disclosure is gated by the same contract from every agent. (2) `find_customer` is not called twice for one subject in one journey. (3) Every authentication failure mode has a defined outcome in each agent that can trigger it.

### F-17 — Part 4 asserts an availability judgement it has no tool to make

**Finding ID:** F-17
**Severity:** Medium
**Confidence:** Certain
**Agent:** Speak to a Tax Pro (Part 4)
**Capability:** Availability search (claimed); outcome definition
**Observed behavior:** `routed_to_message`: "Caller opted to leave a message **or no callback slots were available**. `transactionOccurred` false, `callContained` true, `nextAction` leave_message or leave_message_offer" (L1019).
**Stated scope:** Part 4's tool set is `find_customer`, `search_tax_pro_by_name`, `transfer_to_agent`, `search_knowledge_base` (L1007–1012) — no slot-search tool.
**Expected boundary:** An outcome may only encode conditions the agent can observe. "No callback slots available" is owned by whoever searches CDAS.
**Boundary trigger:** The agent reaches closure without routing a callback.
**Required next action:** Remove the availability clause from Part 4's outcome, or give Part 4 the search tool and move the boundary accordingly (see F-03).
**Evidence supporting the observed behavior:** L1019 against L1007–1012; the only path to "no slots" in Part 4's workflows is a caller declining (L990, L999).
**Evidence creating the conflicting or overlapping ownership:** Part 4's own handoff rule says it "does not book the calendar slot" (L913) and it must return `route_intent` on a callback request (L973). If availability is discovered to be empty, that discovery necessarily happens *after* the handoff, in the Scheduler — so the outcome can only describe a different agent's finding.
**Why an ordinary contradiction review might miss it:** The outcome reads like a natural union of two terminal cases; nothing in the sentence is false, it is simply assignable to the wrong owner and would be untestable in Part 4.
**Customer or operational risk:** Reporting attributes availability failures to the triage agent, masking whether the Scheduler's search actually ran; and if implemented literally, it invites a future implementation where Part 4 silently gains a search tool.
**Recommended specification correction:** Split the outcome into "caller opted for a message" and (if needed) "callback unavailable" with the latter owned by the Scheduler; or fully move CDAS search ownership to Part 4 with the corresponding tools and boundaries.
**Sections that must also be changed to avoid residual contradictions:** Part 4 `agent_specific_outcomes.routed_to_message` (L1019), `agent_specific_tools` (L1007–1012), Business Intent "Fulfillment: CDAS Callback Appointment" (L911–913); Part 2 `agent_specific_outcomes` (L741–748).
**Required regression tests:** (1) Part 4 produces no availability claim. (2) Availability outcomes are emitted only by the agent that ran the search. (3) Every terminal outcome is reachable by the agent that declares it.

### F-18 — Office Information holds an unrestricted knowledge base, beyond its stated scope

**Finding ID:** F-18
**Severity:** Medium
**Confidence:** Certain
**Agent:** Office Information Agent (Part 3)
**Capability:** Informational answering
**Observed behavior:** Part 3 holds `search_knowledge_base`: "Answer approved informational questions without invalidating transaction state" (L856), and `interruptions.informational_question` instructs it to answer and resume (L859). The tool's category enum is the full six-value set (L1058), including `tax_prep_and_records`, `financial_products` and `identity_and_fraud`.
**Stated scope:** "Answer questions about physical office locations, operating hours, landmark directions, and local office contact options" (L819).
**Expected boundary:** An office-facts agent answers office facts. Tax-preparation, financial-product and identity/fraud questions belong to the FAQ Agent, a Tax Pro, or the relevant flow.
**Boundary trigger:** "What should I bring to my appointment?" or "is my refund delayed?" asked of the office-facts agent.
**Required next action:** Restrict the category set per agent and add a routing obligation for out-of-scope categories.
**Evidence supporting the observed behavior:** L856, L859, L1058; `office_never` (L830–836) constrains speech but not answering scope.
**Evidence creating the conflicting or overlapping ownership:** The Office Information objective explicitly excludes scheduling only (L819: "You do not schedule appointments"); it does not exclude tax, financial or identity topics, so there is no stated limit for the KB tool to enforce. Meanwhile `financial_products` and `identity_and_fraud` content overlaps the universal financial boundary (L56: "Never give personalized tax advice… Route to a Tax Pro or `search_knowledge_base`") — which routes *to* the KB and therefore *into* this agent's reach.
**Why an ordinary contradiction review might miss it:** Sharing the tool across agents looks like infrastructure reuse, and `office_never`'s speech rules give a false sense that the agent's subject matter is bounded.
**Customer or operational risk:** A caller obtains tax or refund guidance from an agent that has neither the category governance nor the verification controls of the owning flow, producing a compliance exposure and inconsistent answers per entry point.
**Recommended specification correction:** Add a per-agent category allow-list to `agent_specific_tools.search_knowledge_base` for all four agents, and require a routing handback for out-of-scope categories.
**Sections that must also be changed to avoid residual contradictions:** Part 3 `agent_specific_tools.search_knowledge_base` (L856), `interruptions` (L859), objective (L819); Part 1 §1.2 "PII & IRS Sec. 7216" (L56); Part 5 §5.1 `search_knowledge_base` (L1042–1075).
**Required regression tests:** (1) Each agent's KB calls are constrained to its allow-list. (2) Out-of-scope categories route instead of returning an answer. (3) No agent other than the FAQ Agent and Tax Pro path answers tax-advice questions.

### F-19 — Office Information holds live-transfer capability with no stated conditions

**Finding ID:** F-19
**Severity:** Medium
**Confidence:** Likely
**Agent:** Office Information Agent (Part 3)
**Capability:** Live transfer
**Observed behavior:** `transfer_to_agent`: "Use on unresolved intent or office lookup failure. Call this tool immediately when the caller explicitly requests a live agent (barging)." (L853); `office_info_transfer` outcome (L866).
**Stated scope:** "Answer questions about physical office locations, operating hours, landmark directions, and local office contact options … You do not schedule appointments." (L819)
**Expected boundary:** Either the office-facts agent may transfer (in which case the conditions, the handoff summary fields, and the local-desk restriction must be stated), or it must hand back for a transfer decision elsewhere — consistent with its `leave_message_offer` pattern, where it deliberately does *not* perform the downstream action (L835).
**Boundary trigger:** An unresolved disambiguation, a failed office lookup, or any human-contact request.
**Required next action:** State Part 3's transfer conditions, prohibited transfer targets (mirroring L977), and its handoff summary contract.
**Evidence supporting the observed behavior:** L853, L860, L866, L764 ("transfer or route to leave a message").
**Evidence creating the conflicting or overlapping ownership:** The same agent is explicitly instructed not to *offer* a message but to return `leave_message_offer` (L835) — i.e. it hands off one downstream decision to the deterministic flow while performing another (transfer) itself. Part 3 also defines no `knownSoFar` mapping (L734 defines them for the Scheduler) and no `lastQuestionSpoken`/`interactionSummary` obligations, so its transfer payload contract is unstated.
**Why an ordinary contradiction review might miss it:** Both behaviours are defensible individually, and the asymmetry (offer vs. transfer) looks like deliberate design rather than an unexamined inconsistency.
**Customer or operational risk:** Transfers raised by the office-facts agent may arrive without sufficient context (no `knownSoFar` contract), and the local-desk restriction that Part 4 carries is absent here — the one agent most likely to receive a "transfer me to the office" request.
**Recommended specification correction:** Give Part 3 an explicit transfer contract (conditions, prohibitions, summary fields) or downgrade it to a handback-only agent.
**Sections that must also be changed to avoid residual contradictions:** Part 3 `agent_specific_tools.transfer_to_agent` (L853), `office_never` (L830–836), `interruptions.intent_change` (L860), `agent_specific_outcomes.office_info_transfer` (L866); Part 5 §5.1 `transfer_to_agent` (L1077–1124); Part 4 `tax_pro_never` (L977) for symmetry.
**Required regression tests:** (1) Every Part 3 transfer carries the full contract. (2) No Part 3 transfer targets a local office desk. (3) Transfer conditions are enumerated and testable.

### F-20 — The tax-extension rung offers a product and a transfer nobody owns

**Finding ID:** F-20
**Severity:** Medium
**Confidence:** Certain
**Agent:** Appointment Scheduler (Part 2)
**Capability:** Informational answering; live transfer (self-filing support)
**Observed behavior:** The `extension` ladder's final rung: "with consent, offer self-filing for the extension as a choice. If accepted, offer to hand back for a follow-up tax_prep appointment, or **transfer them to a live agent for self-filing support**" (L658, matching L413).
**Stated scope:** The Scheduler completes "at most one … retail appointment transaction" (L508) and, on the extension path, "commit the extension appointment, close it, and hand back intent_changed … so the second booking runs as a fresh invocation" (L323).
**Expected boundary:** Self-filing is not an appointment; if it has an owner, the rung must route to it by name. A ladder rung may not offer a capability the agent's tool set cannot deliver.
**Boundary trigger:** Extension appointment with the filing window closed and the caller declining virtual.
**Required next action:** Name the owner of self-filing support (a named `routingTarget`), or remove the offer; and specify whether the tax_prep handback is a same-agent re-invocation.
**Evidence supporting the observed behavior:** L413, L658; Part 5's rung enum explicitly says "Self-filing is a handback, not a slot-search rung" (L1396), contradicting its placement inside `ladders.extension`.
**Evidence creating the conflicting or overlapping ownership:** The `routingTarget` enum (L248) has no self-filing destination. The extension section (L323) and the ladder rung (L658) describe the same handback twice with different mechanics ("hand back `intent_changed`" vs "offer to hand back … or transfer them to a live agent"). And a handback to `appointment_scheduler` is a handback to the same agent, which the document never defines as a re-entry pattern (unlike `closure.re_entry`, which describes a fresh session without a same-agent precedent).
**Why an ordinary contradiction review might miss it:** The rung is well-worded and customer-friendly ("Never present self-filing as a dead end"); its defect is that it references destinations and products that the system's routing vocabulary does not contain.
**Customer or operational risk:** A caller chooses self-filing and the transfer has no owner or payload contract; a second booking may or may not happen depending on how the platform treats a same-agent `route_intent`, and "one transaction per invocation" is at risk if it does not.
**Recommended specification correction:** Remove the self-filing offer or add `self_filing_support` as a named routing target with an owner; align L413/L658/L323 on one handback mechanism; define same-agent `route_intent` re-entry semantics explicitly.
**Sections that must also be changed to avoid residual contradictions:** Part 2 State 2 "Tax Extension" (L323), `scheduler_always` (L526), `broadening.ladders.extension` (L654–659), Part 2 State 3 extension row (L413); Part 1 `terminal_payload_contract` (L248), `global_outcomes.intent_changed` (L234); Part 5 `find_available_slots` rung note (L1396).
**Required regression tests:** (1) Every ladder rung resolves to an owned capability. (2) Extension→tax_prep handback produces exactly one further transaction. (3) Self-filing is either routed to a named owner or never offered.

### F-21 — `capture_intent` is an undefined action that overlaps the Head of Call's mandate

**Finding ID:** F-21
**Severity:** Medium
**Confidence:** Certain
**Agent:** Head of Call (owner) vs Office Information Agent (user)
**Capability:** Deterministic handoff; intent classification; call closure
**Observed behavior:** Part 3 returns `nextAction = capture_intent` "so the Head of Call flow can ask how the system can help them today" (L776, L804, L848, L865). The terminal contract lists `capture_intent` in the `nextAction` enum (L248) but defines nothing else about it.
**Stated scope:** The Head of Call owns "the close, the additional-help question, the transfer node, the Leave a Message path, the VOC survey, the goodbye and the disconnect" (L708) — intent capture is not in that list, while `offer_additional_help` already covers "ask how the system can help".
**Expected boundary:** One nextAction per behaviour, with a named owner. `capture_intent` should either be defined as a distinct re-entry into intent classification (with its owner and envelope contract) or removed in favour of `offer_additional_help`.
**Boundary trigger:** An open office's unanswered contact call, or an unresolvable office intent.
**Required next action:** Define `capture_intent` end-to-end (owner, envelope, which agent the next intent routes to) or delete it.
**Evidence supporting the observed behavior:** L248 (enum), L776/L804/L848 (usage), L865 (`office_open_unanswered` `callContained: false` with `capture_intent`).
**Evidence creating the conflicting or overlapping ownership:** Two values express the same caller-facing question; the Head of Call mandate names neither explicitly; and after `capture_intent` the caller's new intent must be classified by an owner that F-12 shows does not exist — so the control flow terminates in an unowned classifier.
**Why an ordinary contradiction review might miss it:** `capture_intent` is syntactically legal everywhere it appears; its absence of definition is only visible by reading the nextAction enum against the ownership paragraph, and by asking what happens next.
**Customer or operational risk:** A call can end in a state where the caller has been asked how they can be helped and no owner exists to receive the answer — a silent dead end, or an unintended re-entry with no envelope (`interactionId`, `operation`, `customerRef`) contract.
**Recommended specification correction:** Define `capture_intent` (owner, envelope, routing) or collapse it into `offer_additional_help`; state `callContained` semantics for each.
**Sections that must also be changed to avoid residual contradictions:** Part 1 §1.3 "The Yield, Do Not Solicit Rule" (L79–83), `terminal_payload_contract` (L248), `global_outcomes` (L231–247); Part 3 `office_always` (L825), `workflow.office_contact_flow` (L848), `agent_specific_outcomes` (L865).
**Required regression tests:** (1) Every emitted `nextAction` has a defined owner and continuation. (2) `capture_intent` either routes a classified intent or is not emitted. (3) No call ends immediately after an unanswered question to the caller.

### F-22 — No refund-status or office-information boundary exists for the Scheduler or Office Information agents

**Finding ID:** F-22
**Severity:** Medium
**Confidence:** Likely
**Agent:** Appointment Scheduler; Office Information Agent
**Capability:** Intent routing; informational answering
**Observed behavior:** Refund status is routed only by Part 4: "If the utterance includes 'Where's my money?', refund status checks … transition immediately to the deterministic Refund Status Flow via `intent_changed` with `routingTarget = refund_status`" (L884). Neither Part 2 nor Part 3 contains an equivalent rule. Both hold `search_knowledge_base` with `financial_products` (L733, L856).
**Stated scope:** The Scheduler's financial boundary is phrased as an enumerated `never` list — loan amounts, notice interpretation, fees, penalties, interest (L553) — which does not include refund status or payment tracking.
**Expected boundary:** Refund/payment questions route from any agent, or the refund flow's ownership is only advisory.
**Boundary trigger:** "Where's my refund?" asked mid-booking or during an office-hours conversation.
**Next action required by the boundary:** `intent_changed` with `routingTarget = refund_status`, with the Scheduler-specific rule that an in-flight booking is closed or suspended first.
**Evidence supporting the observed behavior:** L884 (Part 4 only), L733/L856 (KB reach), L553 (enumerated boundary that omits refunds).
**Evidence creating the conflicting or overlapping ownership:** `refund_status` is in the global `routingTarget` enum (L248) but appears in no agent-specific rule except Part 4's. Meanwhile the Refund Status Flow's ownership is asserted only in the document's reading guide (L… reading notes, "Out-of-Scope (Refund Status): … via intent_changed with routingTarget = refund_status") and in L884.
**Why an ordinary contradiction review might miss it:** The boundary is written where the capability was first hit (Part 4's elicitation flow) and never propagated; enumerated `never` lists create the impression that the financial boundary is comprehensive.
**Customer or operational risk:** A refund question reaches either a KB-sourced answer (no verification, no status lookup) or an agent with no route for it, producing a wrong answer at the highest-sensitivity moment in tax services.
**Recommended specification correction:** Add a universal out-of-scope routing rule (refund_status, faq_agent) inherited by every agent, and reword the Scheduler's financial boundary from an enumeration to a principle ("never answer questions about return/refund status, payment tracking, or financial products; route per the universal table").
**Sections that must also be changed to avoid residual contradictions:** Part 2 `scheduler_never` (L553), `interruptions.intent_change` (L739); Part 3 State 1 intent scope (L760–765), `interruptions.intent_change` (L860); Part 4 Business Intent (L884); Part 1 `terminal_payload_contract` (L248), `global_outcomes.intent_changed` (L234).
**Required regression tests:** (1) Refund questions route identically from all four agents. (2) No agent answers refund status from the knowledge base. (3) A refund question during a booking produces a defined suspension/handback, not a state purge.

### F-23 — Regional virtual booking contradicts the Scheduler's own office-anchored objective

**Finding ID:** F-23
**Severity:** Medium
**Confidence:** Certain
**Agent:** Appointment Scheduler (Part 2)
**Capability:** Availability search; office lookup
**Observed behavior:** The objective states: "Every type is booked against a specific office." (L508). Two ladders offer appointments not anchored to the caller's office: `returning_tax_pro_unavailable` rung 5 is "virtual with a qualified regional Tax Pro, searchScope regional" (L644, L411), and the `peak_capacity`/`extension` ladders offer `virtual` as their first rung (L649, L656).
**Stated scope:** L508; the office-eligibility rule requires every proposed office to return `acceptsAppointmentType: true` (L521).
**Expected boundary:** Either the objective acknowledges office-independent virtual booking (with its own eligibility rules), or the regional rung is removed.
**Boundary trigger:** Returning-client relaxation ladder reaching rung 5, or peak-capacity/extension reaching the virtual rung.
**Required next action:** State which office owns a regional virtual appointment (for `officeRef`, post-commit address readback, and terminal payload) or drop the rung.
**Evidence supporting the observed behavior:** L411, L644, L656–658; `find_available_slots` accepts `searchScope: office | nearby | regional (virtual rung only)` (L1396) and requires `officeRef` in the same request (L1373) — so a regional search must still name an office.
**Evidence creating the conflicting or overlapping ownership:** The post-commit readback and terminal outcome are required to speak `addressLine1Spoken` + `addressLine2Spoken` for the office (L515, L571, L580, L731). A regional virtual appointment has no naturally corresponding office address, so the closure contract and the booking contract disagree about what the appointment is attached to. `physical_drop_off` shows the design does differentiate office-attached versus not (L418), but virtual was never given the same treatment.
**Why an ordinary contradiction review might miss it:** The objective sentence and the ladder are in different sections with different framings (commercial promise vs. operational rung), and the rung itself is defensible — virtual appointments genuinely are office-independent.
**Customer or operational risk:** The agent reads back, and the terminal payload reports, the address of an office where the appointment does not take place — a correctness failure in the last thing the caller hears and in the record the Tax Pro downstream receives.
**Recommended specification correction:** Amend the objective to "every type is booked against a specific office, except virtual appointments, which carry a named home office for reporting and readback purposes", and specify the readback content for virtual (method-first phrasing, no physical address, or the owning office explicitly labelled as administrative).
**Sections that must also be changed to avoid residual contradictions:** Part 2 `objective` (L508), `broadening.ladders.returning_tax_pro_unavailable` (L637–645), `peak_capacity` (L647–652), `extension` (L654–659), Part 2 State 3 broadening table (L411), `scheduler_always` (L515), `workflow.*` step 7 (L571, L580), `agent_specific_tools.*` post-commit rules (L729–731); Part 5 `find_available_slots` (`searchScope`, L1396).
**Required regression tests:** (1) Virtual bookings produce a readback with no misleading physical address. (2) `officeRef` sent with `searchScope: regional` is the documented home office. (3) Terminal payloads for virtual appointments are distinguishable from in-person ones.

### F-24 — `scenario_selection` runs post-readiness but two of its inputs are pre-readiness decisions

**Finding ID:** F-24
**Severity:** Medium
**Confidence:** Likely
**Agent:** Appointment Scheduler (Part 2)
**Capability:** Workflow sequencing; availability search
**Observed behavior:** `broadening.scenario_selection` states: "First match wins **after readiness returns ready**" (L605). Rule 2 of that selector is "On `schedule_new`, drop-off request: where the caller has not said in the office or by secure upload link, ask. In the office on `tax_prep`: `physical_drop_off`." (L606). Yet `check_search_readiness` must be called "once constraints are gathered" and "only after authentication" (L387, L726), and readiness for a digital drop-off is explicitly forbidden: "never call on the digital drop-off no-slot path" (L726) and "Skip readiness and availability only on a digital drop-off" (L567).
**Stated scope:** The drop-off/DDO branch determines the method, which is an input to readiness and to the search.
**Expected boundary:** Decisions that determine the method must precede the readiness call; the scenario selector must be reachable before readiness for those branches, or it must be split.
**Boundary trigger:** A caller who requests a drop-off, or who chooses the "secure upload link" option.
**Required next action:** Specify the pre-readiness decision point for drop-off/DDO and state what the readiness request contains in those cases (or that it is skipped).
**Evidence supporting the observed behavior:** L605 (post-ready), L606 (drop-off question), L567/L726 (readiness skipped/excluded for DDO), L329 (DDO skips `book_appointment`), L341 (method change invalidation).
**Evidence creating the conflicting or overlapping ownership:** Because the selector is defined as post-readiness and DDO never reaches readiness, the only documented path that selects the DDO branch is the ladder rung — the "ask about drop-off" rule (L606) cannot execute as written. The two mechanisms (rule 2 and the ladder rung) both choose DDO, from different points in the flow, without a stated precedence.
**Why an ordinary contradiction review might miss it:** Each rule is individually well-formed; the contradiction is a two-step ordering dependency across sections (readiness rules in State 3 vs. the selector in the JSON block) that no single sentence reveals.
**Customer or operational risk:** Implementation-dependent behaviour: some builds ask about drop-off before readiness, others never ask and only reach DDO via a failed search — producing different journeys for the same caller and unpredictable DDO volumes.
**Recommended specification correction:** State the pre-readiness decision point explicitly ("ask the drop-off form before readiness; if DDO is chosen, skip readiness and search"), and give rule 2 precedence over the ladder rung or remove the duplication.
**Sections that must also be changed to avoid residual contradictions:** Part 2 State 3 "Readiness & Availability" (L385–390), `scheduler_always` (L567-equivalent rule), `broadening.scenario_selection` (L604–615), `broadening.ladders.new_client` (L618–626), Part 2 State 2 "Digital Drop-Off (DDO) Rules" (L325–330), `agent_specific_tools.check_search_readiness` (L726).
**Required regression tests:** (1) The drop-off form question occurs before any readiness call. (2) Choosing DDO produces no readiness or availability call. (3) DDO is reachable by exactly one documented mechanism.

### F-25 — Office Information's `by_appointment_only` branch starts a booking flow the caller did not request

**Finding ID:** F-25
**Severity:** Medium
**Confidence:** Certain
**Agent:** Office Information Agent (Part 3)
**Capability:** Deterministic handoff; appointment intent solicitation
**Observed behavior:** "If `seasonalStatus` is `by_appointment_only`, do not quote standard daily hours. State that the office operates by appointment only. **Do not ask if they want to book one.** Stop speaking and return `nextAction = route_intent` with `routingTarget = appointment_scheduler`." (L770, L827; dialogue 3D L806–811).
**Stated scope:** Office Information "does not schedule appointments" and must "hand back `intent_changed` immediately if scheduling is requested" (L831).
**Expected boundary:** A handback into the appointment flow is triggered by the caller's request, not by an office attribute. Route to the scheduler only when the caller asks to book.
**Boundary trigger:** "Can I walk into the Westport office tomorrow morning?" with `by_appointment_only`.
**Required next action:** Return `offer_additional_help` (or `close`) after the informational answer, and route to the scheduler only on an explicit booking request.
**Evidence supporting the observed behavior:** L770, L809, L827; the rule simultaneously forbids the solicitation question and performs the solicitation routing.
**Evidence creating the conflicting or overlapping ownership:** Routing into the Scheduler initiates a booking workflow whose own entry contract (L565) begins with authentication and type selection. The Office Information agent therefore decides that a booking journey should start, on a caller who asked a walk-in question — an ownership decision the Scheduler's objective reserves to the caller ("The appointment method is the caller's choice", L508) and the broadening principles reserve to consent ("Get the caller's consent before every step", L399). The intended-use carve-out is to *avoid* pressure, yet the mechanism applies pressure without a question.
**Why an ordinary contradiction review might miss it:** The rule is written as an anti-pressure safeguard ("do not ask if they want to book one"), so it reads as consistent with a no-solicitation design; the routing that follows it looks like a neutral handback rather than an initiation.
**Customer or operational risk:** A walk-in inquiry converts into an authentication-and-booking journey the caller never asked for; combined with the Scheduler's `entryReason` handling (L531), the caller may be pushed deep into a booking before they can say no.
**Recommended specification correction:** Replace the unconditional `route_intent` with an offer gated on a caller request ("If the caller asks to book, hand back `route_intent`; otherwise offer additional help"), and add the same gate to the `closed_for_season` branch.
**Sections that must also be changed to avoid residual contradictions:** Part 3 State 1 "By-Appointment-Only" (L770), `office_always` (L827), dialogue 3D (L806–811), `office_never` (L831), `agent_specific_outcomes.office_info_provided` (L863); Part 2 `objective` (L508), `broadening.principles` (L399).
**Required regression tests:** (1) No appointment flow starts without a caller booking request. (2) `by_appointment_only` produces an informational answer plus an offer, not a route. (3) An explicit booking request routes to the scheduler with the required payload.

### F-26 — "Primary routed office", `routedOfficeRef`, `officeRef` and `yroOfficeRef` have no fixed referent for the cross-office phone rule

**Finding ID:** F-26
**Severity:** Medium
**Confidence:** Certain
**Agent:** Office Information Agent (Part 3); Appointment Scheduler (Part 2)
**Capability:** Informational answering; office lookup
**Observed behavior:** "Direct phone numbers are restricted to the currently routed office (`officeRef`). If the caller asks to contact a different office, state that you can only provide the direct number for the current office, but can offer the address for the other location." (L778) and "Never provide direct transfer numbers for offices other than the primary routed office" (L833). Meanwhile the agent is instructed to "store `yroOfficeRef` to answer follow-up questions" after a seasonal closure (L828).
**Stated scope:** Conventions define the ref family: "`officeRef`, `primaryOfficeId`, `priorOfficeRef`, `nearOfficeRef`, and `routedOfficeRef` identify offices in their respective roles" (L1030) — roles stated, but not which one is "primary".
**Expected boundary:** The restricted office must be one named ref, and follow-up questions about an office reached via a seasonal detour must have a defined answer.
**Boundary trigger:** "What's the phone number for Westport Center?" after the YRO was stored, or after a rollover.
**Required next action:** Define the single canonical "current/primary routed office" ref and state how `yroOfficeRef` (and `ruleOfficesNear` results) affect it.
**Evidence supporting the observed behavior:** L778, L833, L828, L22 (`dialedOfficeNumber` resolves `routedOfficeRef`), L1261 ("`routedOfficeRef` is populated on rollover, null on central-line searches").
**Evidence creating the conflicting or overlapping ownership:** On a **central-line** call `routedOfficeRef` is **null** (L1261) — so the agent whose rule is stated in terms of `officeRef` and "the currently routed office" may be holding an office the caller selected from `find_offices_near`, which is not "routed" at all. Four office refs with overlapping meanings (`officeRef`, `routedOfficeRef`, `yroOfficeRef`, `nearOfficeRef`) and two different phrases ("currently routed office", "primary routed office") govern one caller-facing restriction.
**Why an ordinary contradiction review might miss it:** The conventions paragraph looks like it resolves the vocabulary, and the restriction reads cleanly — the ambiguity only appears when the blocked case (a central-line caller asking about a *different* office than the one being discussed, or about a stored YRO) is walked through.
**Customer or operational risk:** Either phone numbers are disclosed for offices the business meant to withhold, or a caller who was deliberately shown a YRO address cannot get its number even though it is now the relevant office — inconsistent enforcement of a policy that exists for a reason.
**Recommended specification correction:** Define one canonical field (`currentOfficeRef`) for the restriction, state its value for central-line, rollover, rejection, nearby-office and YRO cases, and state explicitly whether the YRO becomes the restricted office.
**Sections that must also be changed to avoid residual contradictions:** Part 3 State 1 "Cross-Office Restriction" (L778), `office_always` (L822, L828), `office_never` (L833); Part 1 §1.1 `entryPoint` (L23); Part 5 conventions (L1030), `find_offices_near` note (L1261), `get_office_details` response (`yroOfficeRef`, L1759).
**Required regression tests:** (1) The phone-number restriction has one tested referent in rollover, central-line, rejection and YRO states. (2) A stored YRO's phone number is either permitted or refused per an explicit rule. (3) `phrase "primary routed office"` is replaced by a testable field reference.

### F-27 — `not_confirmed` triggers an unbounded re-gate loop

**Finding ID:** F-27
**Severity:** Low
**Confidence:** Certain
**Agent:** Appointment Scheduler (Part 2)
**Capability:** Confirmation; transaction execution
**Observed behavior:** "On `not_confirmed`, re-gate" (L540), with `not_confirmed` defined as "Confirmation evidence missing/incomplete" for `book_appointment` (L1573) and `cancel_appointment` (L1689).
**Stated scope:** No attempt cap is stated for re-gating, unlike input handling (`MAX_INPUT_ATTEMPTS: 2`, L126) and KB attempts (L1075).
**Expected boundary:** A bounded number of re-gate attempts, after which the agent stops and hands back (the caller's "yes" is not being captured correctly — a system fault, not a caller error).
**Boundary trigger:** Repeated `not_confirmed` from a write tool.
**Required next action:** Cap re-gating and define the terminal outcome (`validation_failed`/`system_failure` → transfer) on exhaustion.
**Evidence supporting the observed behavior:** L540; the absence of any counter in `scheduler_always`.
**Evidence creating the conflicting or overlapping ownership:** `global_outcomes.validation_failed` ("A tool rejects an uncorrectable request … `nextAction` transfer", L238) overlaps `not_confirmed` but is assigned to a different cause, leaving no rule for this specific loop.
**Why an ordinary contradiction review might miss it:** "Re-gate" is a single word in a long handling sentence; the missing bound is invisible unless attempt budgets are audited across the document.
**Customer or operational risk:** A caller paying a compliment ("sure, that sounds good") instead of a literal yes can be asked the same question indefinitely — a severe experience failure caused by a confirmation object the agent cannot satisfy.
**Recommended specification correction:** Add "re-gate at most once, then speak the `system_failure` line and transfer", and define how a captured "yes" is validated before re-asking.
**Sections that must also be changed to avoid residual contradictions:** `scheduler_always` (L540); Part 2 State 4 gate (L473); `global_constants` (L125–129); Part 1 `global_outcomes` (L238–239); Part 5 §5.2 outcome tables (L1573, L1689).
**Required regression tests:** (1) Two consecutive `not_confirmed` results terminate in transfer. (2) The re-gate counter is independent of `MAX_INPUT_ATTEMPTS`. (3) A valid "yes" that the tool rejects twice cannot loop a third time.

### F-28 — `efile_rejection_retail` entry conflicts with "never infer the appointment type from the entry point"

**Finding ID:** F-28
**Severity:** Low
**Confidence:** Likely
**Agent:** Appointment Scheduler (Part 2)
**Capability:** Entry-context handling; appointment-type establishment
**Observed behavior:** "When `entryReason` is `efile_rejection_retail`, **open on the booking**, never re-ask the intent, never repeat the rejection announcement, and never quote `sourceUtterance`. Propose the prior Tax Pro returned by `find_customer` where there is one; otherwise apply the Tax Pro trade-off. Everything else follows `schedule_new`." (L531; also L24 "Open directly on booking. Do not ask intent.").
**Stated scope:** "Establish the appointment type before the appointment method and before any office lookup… **Never infer it from the entry point**, the season or the caller's history." (L521, L508).
**Expected boundary:** If the type may be inferred for a system-initiated entry, the rule must say so; if not, the agent must still ask for the type on a rejection-driven entry.
**Boundary trigger:** Invocation with `entryReason: efile_rejection_retail`.
**Required next action:** State the type-handling rule for system-initiated entries explicitly (ask, or infer `tax_prep` with a stated rationale), and place the Tax Pro trade-off at a defined point in the ladder.
**Evidence supporting the observed behavior:** L24, L531, L521, L508.
**Evidence creating the conflicting or overlapping ownership:** The trade-off question is governed by a fixed rule — "Ask 'Do you want to stay with [Name], or would you rather see whoever's free first?' **only at the ladder step that drops the Tax Pro preference**" (L390, L534) — while L531 applies it outside any ladder step, i.e. before availability. Two placements for one question, one of which violates the "only at" constraint.
**Why an ordinary contradiction review might miss it:** The `efile_rejection_retail` rule is an explicit special case, so it reads as intentionally exempt; only the `scheduler_always` prohibition's exact phrasing ("never infer it from the entry point") makes the exemption a violation.
**Customer or operational risk:** Either the type question is asked (contradicting "open on the booking" and re-surfacing the rejection context the design wanted suppressed), or the type is silently inferred and the caller's appointment may be created with the wrong type, notes and eligibility.
**Recommended specification correction:** Add an explicit exception clause: "On `efile_rejection_retail`, `appointmentType` is `tax_prep` by rule" (and state whether the method is asked), and move the Tax Pro trade-off for this entry to the documented ladder placement or declare a named exception.
**Sections that must also be changed to avoid residual contradictions:** Part 1 §1.1 `entryReason` (L24); Part 2 `scheduler_always` (L521, L531, L534); Part 2 State 3 "Tax Pro Trade-off" (L390); `broadening.principles` (L595).
**Required regression tests:** (1) `efile_rejection_retail` produces a deterministic `appointmentType`. (2) The rejection is never re-announced or quoted. (3) The Tax Pro trade-off occurs exactly once, at a documented point, for this entry.

---

## C. Mandatory final outputs

### C.1 Agent Capability Ownership Matrix

Ownership status: **Exclusive** = one owner, no other path in the document. **Shared** = two owners with a stated contract. **Ambiguous** = two or more owners with no stated precedence or state-transfer contract. **Orphaned** = capability asserted with no owner.

| # | Capability | Primary owner (documented) | Additionally performed by | Enabling tools / flows | Ownership status |
|---|---|---|---|---|---|
| 1 | Intent classification | Head of Call (implied by envelope only) | Scheduler (type), Office Info (3-way disambiguation), Part 4 (reason elicitation + out-of-scope) | `sourceUtterance`, `entryReason`, per-agent clarifiers | **Ambiguous — no owner named** (F-12) |
| 2 | Authentication (third-party) | Scheduler (Part 2 State 1) | Speak to a Tax Pro Part 4 | `find_customer` | **Ambiguous** (F-16) |
| 3 | Customer retrieval | Scheduler | Part 4 | `find_customer` | **Shared, contract unstated** (F-16) |
| 4 | Informational answering | FAQ Agent / KB (destination) | All four agents | `search_knowledge_base` | **Ambiguous / bypassed** (F-08, F-18) |
| 5 | Office lookup | Scheduler (`find_offices_near`) | Office Info (`get_office_details` + `includeNearby`) | two tools, two contracts | **Ambiguous** (F-09, F-15, F-26) |
| 6 | Office open/closed + hours | Office Info | Scheduler via KB category | `check_office_open_status`, `get_office_details`, KB | **Ambiguous / competing sources** (F-09) |
| 7 | Availability search (retail) | Scheduler | — | `find_available_slots` | **Exclusive** |
| 8 | Availability search (CDAS) | Scheduler (`find_available_cdas_slots` in tool list) | Scheduler also via `find_available_slots`; Part 4 claims the outcome | two competing tools | **Ambiguous — duplicate tooling** (F-03) |
| 9 | Preference gathering | Scheduler | Office Info, Part 4 | conversational | **Shared, low risk** |
| 10 | Slot selection | Scheduler | — | `find_available_slots` + ladder | **Exclusive** (but no callback ladder, F-04) |
| 11 | Message capture | Deterministic Leave a Message flow | Scheduler (callback reason → `appointmentNotes`); Part 4 promotes MyBlock messaging | `book_appointment` notes field | **Ambiguous — boundary undefined** (F-14, F-06) |
| 12 | Callback setup | Scheduler (books) | Part 4 (decides + routes), Office Info (offers via route_intent) | `book_appointment`, `find_available_slots`/`find_available_cdas_slots` | **Ambiguous** (F-03, F-05, F-25) |
| 13 | Appointment booking | Scheduler | — | `book_appointment` | **Exclusive** |
| 14 | Rescheduling | Scheduler | — | `reschedule_appointment` | **Exclusive** |
| 15 | Cancellation | Scheduler | — | `cancel_appointment` | **Exclusive** |
| 16 | DDO link dispatch | Scheduler | — | `send_secure_link` | **Exclusive but outside the objective** (F-01) |
| 17 | Live transfer decision | Head of Call (transfer node) | All four agents hold `transfer_to_agent`; Office Info replaces it with triage | `transfer_to_agent` | **Ambiguous** (F-07, F-19) |
| 18 | Deterministic handoff (`intent_changed`/`route_intent`) | All agents (as callers) | Head of Call (as node) | `routingTarget` | **Shared; routing table missing** (F-12, F-22) |
| 19 | Confirmation gate | Scheduler | — | `confirmation` object on 3 writes | **Exclusive for appointments; undefined for DDO** (F-02) |
| 20 | Transaction execution | Scheduler | Leave a Message flow (Work Center submit) | 3 write tools + `send_secure_link` | **Shared across two owners, DDO boundary blurred** (F-01) |
| 21 | Confirmation evidence / readback | Scheduler | Office Info (answers), Part 4 (option statement) | spoken | **Shared, low risk** |
| 22 | Call closure | Head of Call | Office Info (`leave_message_offer` ends the IVA segment); Part 3 (`capture_intent`) | terminal payload | **Exclusive owner, but two IVA nextActions pre-empt it** (F-13, F-21) |
| 23 | Silence / robocall termination | Head of Call | — | terminal payload, no tool | **Exclusive — contradicted by `customer_abandoned`** (F-10) |
| 24 | Refund status | Deterministic Refund Status Flow | Only Part 4 routes it; all agents can answer via KB | `routingTarget: refund_status` | **Ambiguous — routing enforced in one agent only** (F-22) |
| 25 | FAQ / login / account access | FAQ Agent | All four agents via KB | `routingTarget: faq_agent` | **Ambiguous — bypassed** (F-08) |
| 26 | Tax Pro lookup & prior-Tax-Pro disclosure | Part 4 (`search_tax_pro_by_name`) | Scheduler (`find_customer` prior Tax Pro) | two tools | **Shared** |
| 27 | Self-filing support | **Nobody** | Scheduler offers it and offers a transfer to it | extension ladder rung | **Orphaned** (F-20) |
| 28 | Seasonal / YRO handling | Scheduler | Office Info | `find_offices_near`, `get_office_details` | **Ambiguous** (F-15) |

**Reading:** of 28 capabilities, 8 are Exclusive, 9 are Shared-with-contract or low-risk, and **11 are Ambiguous or Orphaned**. Every ambiguous row is a place where the boundary is decided by tool availability rather than by an ownership rule.

### C.2 Duplicate or Overlapping Capabilities

| Overlap | Agents/flows | Same transaction? | Precedence stated? | Finding |
|---|---|---|---|---|
| CDAS availability search | `find_available_slots` vs `find_available_cdas_slots` (both Scheduler-owned) | Yes | No | F-03 |
| Callback decision + booking | Part 4 decides/routes; Scheduler books; two ladders → `new_client` fallback | Yes | Partially (Part 4 does not book) | F-03, F-04, F-05 |
| Human-contact handling | Universal barge rule; Part 3 triage; Part 4 transfer | Same caller intent, three treatments | Only for "central" vs "local", and "local" is undefined | F-07 |
| FAQ-scope answering | FAQ Agent vs all four agents' KB access | Yes | No | F-08 |
| Office hours / directions / phone | Office Info tools vs KB `appointments_and_logistics`/`contact_directories` | Yes | No | F-09 |
| Seasonal closure / YRO offer | Scheduler (`find_offices_near.isYearRoundOffice`) vs Office Info (`get_office_details.yroOfficeRef`) | Yes | No | F-15 |
| Identity authentication | Scheduler (full contract) vs Part 4 (partial contract) | Yes | No | F-16 |
| Message capture | Leave a Message flow vs Scheduler `appointmentNotes` | Partially (narration vs notes) | No definition of "message content" | F-14 |
| Transfer summary packaging | All four agents call `transfer_to_agent`; only Scheduler has a `knownSoFar` mapping | Yes | Partially | F-19 |
| Call-closure / end-of-turn behaviour | Head of Call vs Part 3 `capture_intent` / `leave_message_offer` | Yes | No (two nextActions) | F-13, F-21 |
| Tax Pro disclosure | Part 4 `search_tax_pro_by_name` vs Scheduler `find_customer` prior Tax Pro | Related but distinct | No cross-reference | F-16 |
| Informational tax answering | KB (any agent) vs `requires_tax_pro` path | Yes | `requires_tax_pro` has no owner | F-08, F-18 |

### C.3 Missing Stop Conditions

| # | Missing stop condition | Consequence | Finding |
|---|---|---|---|
| 1 | No post-boundary tool prohibition for any agent (no rule states which tools must not be called after commit, handback, transfer, or message handoff) | Double writes, post-handoff searches, DDO after a message handback | F-11 |
| 2 | No terminal state for a completed DDO dispatch (no `operation` value, no outcome, no closure pattern, no idempotency key) | Unreportable and non-reconcilable transaction | F-01 |
| 3 | No stop rule for the Scheduler after it has decided to hand back `intent_changed` (it may still hold every write tool) | Second transaction in one invocation | F-11 |
| 4 | No stop rule after `transfer_to_agent` returns `agent_available` beyond "one short handoff line, only after agent_available" (L709) | Continued tool use while a live agent is being connected | F-11 |
| 5 | No attempt cap on `not_confirmed` re-gating | Unbounded confirmation loop | F-27 |
| 6 | No stop rule for Office Info after answering a closed-office contact question (it proceeds to a message offer) | Satisfied call handed to a recording flow | F-13 |
| 7 | No stop rule for Part 4 after resolving the Tax Pro (it continues to an options statement and a MyBlock promotion) | Extended dialogue where a handoff was available | F-17, F-06 |
| 8 | No stop rule / boundary for the Scheduler on refund-status and FAQ-class questions (only an enumerated financial `never` list) | Wrong-channel answering at high sensitivity | F-22 |
| 9 | No definition of what happens after `capture_intent` | Unowned continuation classifier | F-21 |
| 10 | No stop condition on same-agent `route_intent` (extension → tax_prep) | Undefined re-entry, possible second transaction | F-20 |
| 11 | No explicit stop for ladder progression on a channel rung vs a search rung | Rung sequencing unspecified after a method change | F-02, F-24 |
| 12 | Silence: two mutually exclusive stop behaviours documented (terminate vs transfer) | Robocall may consume a human seat | F-10 |

### C.4 Agents With Potentially Excessive Tool Access

| Agent | Tool | Why it exceeds the stated scope | Finding |
|---|---|---|---|
| Scheduler | `send_secure_link` | Fulfillment write outside "at most one appointment transaction"; no idempotency, no outcome | F-01, F-02 |
| Scheduler | `search_knowledge_base` (all six categories) | Cannot be reconciled with "you do not answer refund/login/FAQ material" — because no such rule exists | F-08, F-18 |
| Scheduler | `find_available_cdas_slots` | Owned but never invoked by any workflow, ladder, scenario or outcome — dead capability that invites parallel implementation | F-03 |
| Scheduler | `transfer_to_agent` | Used for `no_acceptable_availability` (in-scope), but also the implied vehicle for out-of-scope intents the Scheduler has no routing rule for (refund, FAQ, office info) | F-22 |
| Office Information | `search_knowledge_base` (all six categories) | Objective is office facts only; no category restriction | F-18 |
| Office Information | `transfer_to_agent` | Objective is answering questions; no transfer conditions, no summary contract, no local-desk prohibition | F-19, F-07 |
| Office Information | `get_office_details(includeNearby)` | Returns nearby offices and a YRO ref that can influence a booking flow without eligibility data (`acceptsAppointmentType`) | F-15 |
| Speak to a Tax Pro | `find_customer` | Runs authentication without the owning agent's full contract (no `multiple_matches`/`no_match`/re-auth rules) | F-16 |
| Speak to a Tax Pro | `search_knowledge_base` (all six categories) | Objective is routing to a Tax Pro; answering is not in scope and overlaps the FAQ Agent | F-08 |
| All agents | `transfer_to_agent` | Four callers, one transfer node owner, no per-agent trigger enumeration and no post-transfer prohibition | F-07, F-11, F-19 |

### C.5 Examples That Broaden Scope

| Example | Location | Behaviour shown | Why it broadens scope |
|---|---|---|---|
| 3B (Office Contact — closed) | L792–797 | States closure, hours and main line (correct), then returns `leave_message_offer` | Demonstrates the outcome as normative; the message offer is bundled with an answer that needs nothing more (F-13) |
| 3C (Office Contact — open) | L799–804 | "Transfer me to someone at the front desk" → busy-staff statement → `capture_intent` | Demonstrates that a human-contact request is *not* transferred by this agent, contradicting the universal barging rule (F-07) |
| 3D (by-appointment-only) | L806–811 | Walk-in question → closure statement → `route_intent` to the Scheduler | Demonstrates starting a booking journey with no booking request (F-25) |
| 4A / 4E (Part 4 happy path) | L917–925, L949–956 | Promotes the MyBlock app inside the option statement | Demonstrates the app mention as standard practice, normalizing a universal-rule violation (F-06) |
| 4C (by-name + CDAS) | L933–941 | Resolves a named Tax Pro, offers options, then handback `appointmentType = callback` | Demonstrates the out-of-contract handoff field and the reason-loss path (F-05) |
| 4B ("Where's my money?") | L927–931 | "I can help you check on your refund right now." | Demonstrates an agent speaking a capability it does not own and does not invoke (the refund flow does) — a reference case for F-22 |
| 4D (barging) | L943–947 | Immediate `transfer_to_agent` on "give me a real person" | Correct in itself; contrasts with 3C and shows the same utterance class handled two ways (F-07) |
| 3B (Part 2 broadening) | L443–455 | Full rung-by-rung negotiation ending in a Tax Pro trade-off | Demonstrates ladder consent mechanics; useful as the reference for the missing callback ladder (F-04) |
| 1B (third-party auth) | L285–297 | Captures DOB and SSN and confirms the owner's name | Correct; shows the capture contract Part 4 only partially inherits (F-16) |
| 2B (notice capture) | L356–371 | Five-beat capture with grouped readback | Correct reference for structured capture; underscores the absence of an equivalent policy for `appointmentNotes` narration (F-14) |

### C.6 Outcomes That Broaden Scope

| Outcome | Location | Declared terminal result | Why it broadens scope |
|---|---|---|---|
| `routed_to_message` | L1019 | "Caller opted to leave a message **or no callback slots were available**" | Asserts an availability finding Part 4 has no tool to produce (F-17) |
| `office_contact_triage_complete` | L864 | "…or explicitly requested a message … `leave_message_offer` **or** `leave_message`" | Fuses a satisfied information answer with a message offer (F-13) |
| `office_open_unanswered` | L865 | `callContained: false`, `nextAction: capture_intent` | Introduces an undefined continuation action as a terminal result (F-21) |
| `office_info_transfer` | L866 | "Unresolved office intent or lookup failure … `nextAction: transfer`" | Grants a transfer capability with no conditions or summary contract (F-19) |
| `customer_abandoned` | L246 | "an unanswered gate runs the reprompt rule, **then transfers**" | Overrides the universal silence rule and misassigns the termination decision (F-10) |
| `no_acceptable_availability` | L747 | "Call `transfer_to_agent` with `transferReason: no_acceptable_availability` … carry … `exhaustedRungs`" | In-scope and well-formed — but it is the only place the ladder-exhaustion contract is defined; there is no equivalent for DDO or callback (F-01, F-04) |
| `existing_appointment_rescheduled` | L743 | Carries `previousAppointmentRef` "only when a new record was issued" | Well-formed; noted because the payload contract (L248) lists the field unconditionally, so the conditional rule is not enforceable from the contract (F-05 class) |
| `appointment_already_canceled` | L745 | `transactionOccurred: false` with `canceledAppointmentRef` + `canceledSummary` | Requires summary data that only retrieval produces; no rule states which tool supplies it when no write ran (minor, same class as F-01) |
| `routed_to_scheduler` | L1018 | `intent: speak_to_tax_pro`, `routingTarget: appointment_scheduler` | Correct routing values, but carries no `appointmentType`/reason despite the mandated handoff (L973) — contract gap (F-05) |

### C.7 Undefined or Colliding Business Terms

| Term / family | Competing meanings in the document | Risk |
|---|---|---|
| **callback** | appointment type `callback` (L317); method token `phone_callback` (L1030); CDAS = "Callback Appointment" (L1439); `callbackWindowSpoken` (L1464); "phone callback" as a tax_notice rung (L677); `callbackNumber` (L1547); method description "a tax professional would call you at your appointment time" (L219); Part 4's "callback appointment" (L913) | The most-routed object in the spec has no authoritative definition; determines which type/tool/ladder applies (F-03, F-04) |
| **message** | Work Center message (deterministic flow, L85); MyBlock message (L972); "leave a message" intent (L763); `appointmentNotes` "reason for the call" (L527); `leave_message` vs `leave_message_offer` nextActions (L245) | Defines whether capture is allowed and who owns it (F-14, F-06) |
| **transfer / route / hand back** | `transfer_to_agent` (live rep); `route_intent` (deterministic handback); `routingTarget`; `routedOfficeRef`; "routing hints" (`knownPreferences`); `capture_intent`; "hand back"; `returnControlTo` | Four terms for one concept; some are caller-facing and forbidden to speak (L62), others are payload fields (F-12, F-21) |
| **office refs** | `officeRef`, `routedOfficeRef`, `primaryOfficeId`, `priorOfficeRef`, `nearOfficeRef`, `yroOfficeRef`, and the phrases "currently routed office" / "primary routed office" | The cross-office phone restriction has no fixed referent (F-26) |
| **confirmation** | the pre-commit gate/consent; the `confirmation` request object (`confirmed/confirmedAt/utterance`); "Confirmed at capture" readback; "Optional Text Confirmation"; `confirmationNumber`; `confirmationStatus` (state flag); `confirmedSummary` | Six meanings for one word, one of which ("confirmation") is a caller-visible concept the agent must never speak as a number (F-02) |
| **availability** | `check_search_readiness` (readiness), `find_available_slots`, `find_available_cdas_slots`, `moreAvailable`, `isReschedulable`, `takingAppointmentsInd`, "availability" in the broadening ladder | Two contracts, one word (F-03) |
| **complexity / rating** | `clientComplexity`, `priorTaxProCertLevel`, `taxProCertLevel`, `tpRating`, `taxProRatingFloor`, "baseline floor", "inherited baseline", "cert level", `taxProRatingFloor = null` on drop-off | Part 5 partially reconciles them (L1030); "floor" vs "cert level" vs "complexity" remain interchangeable in the ladder text (F-28 class) |
| **drop-off** | `digital_drop_off`, `physical_drop_off`, `isDropOff`, "drop-off request", "secure upload link", "DDO", "self-filing" | Two rungs that share a name but not a method; `isDropOff` is true only for physical (L1030) while both names contain "drop-off" (F-24) |
| **appointment** | a booked calendar slot; `callback` (15-min CDAS); DDO ("a fulfillment action, not a calendar appointment", L327); physical drop-off ("booked as a calendar slot", L313); self-filing (neither) | The document's central noun covers four objects with four lifecycle rules (F-01, F-20) |
| **human** | "live agent", "central customer service" (L887), "local office staff"/"receptionist" (L763), "Tax Pro" (Part 4 objective), "a person" (L106) | Determines whether a request transfers, triages, or is answered (F-07) |
| **nextAction** | `close`, `transfer`, `leave_message`, `leave_message_offer`, `route_intent`, `offer_additional_help`, `capture_intent`, `end_call`, `none` — with `capture_intent` undefined and overlapping `offer_additional_help` | Two values for one Head of Call behaviour; one value with no owner (F-21) |
| **vague destination terms** | "another specialized service" (L606), "named destination" (L248), "self-filing support" (L658) | Routing values that resolve to nothing (F-20) |

### C.8 Architecture Decisions Required

Each item below cannot be resolved from the supplied material; a human owner must decide. Findings are labelled **Architecture decision required** where the specification is internally consistent but the correct owner is not determinable.

| # | Decision required | Options | Affected findings |
|---|---|---|---|
| AD-1 | **Who owns Digital Drop-Off?** A deterministic DDO flow, or the Appointment Scheduler under a widened objective with its own outcome, idempotency and closure contract? | (a) New deterministic flow, Scheduler hands back; (b) Scheduler owns it formally | F-01, F-02, F-24 |
| AD-2 | **Who owns CDAS/callback slot search, and which tool is authoritative?** | (a) `find_available_cdas_slots` only, retire the callback path of `find_available_slots`; (b) `find_available_slots` only, delete `find_available_cdas_slots` | F-03, F-04, F-17 |
| AD-3 | **Is the Speak to a Tax Pro agent a router or a fulfiller?** If a router, it must not authenticate, must not promote a channel, and must hand back with a defined payload. | (a) Pure router; (b) partial fulfiller with a stated search capability | F-03, F-05, F-06, F-16, F-17 |
| AD-4 | **Who classifies intent, and where is the routing table?** | (a) Head of Call classifies deterministically; (b) a named classifier agent; (c) each agent self-classifies with a published acceptance contract | F-12, F-08, F-09, F-22 |
| AD-5 | **Is the FAQ Agent a boundary or a suggestion?** Are KB categories agent-scoped? | (a) Hard route with per-agent category allow-lists; (b) FAQ is best-effort | F-08, F-18 |
| AD-6 | **Who owns office facts (hours, directions, phone) outside the booking flow, and does the Scheduler get a route to them?** | (a) Office Info exclusive, add `office_info` routingTarget; (b) Scheduler may answer from KB with a scoped category | F-09, F-26 |
| AD-7 | **What is the definition of "message content" versus "reason for the call", and what may be stored in `appointmentNotes`?** | (a) Enumerated reason codes only; (b) governed free text with retention/7216 treatment | F-14 |
| AD-8 | **Is a request for local office staff a live transfer, a triage, or a message offer?** | (a) Triage (current Part 3); (b) transfer under the barging rule; (c) message offer only | F-07, F-19, F-26 |
| AD-9 | **Does silence at a gate transfer or terminate?** (The two universal texts disagree; only one can be implemented.) | (a) terminate silently (L72); (b) transfer (L246) | F-10 |
| AD-10 | **Do post-boundary tool prohibitions become part of the specification?** | (a) Per-agent prohibition lists; (b) a universal "no tool calls after terminal payload" rule enforced by the platform | F-11 |
| AD-11 | **Is a regional virtual appointment attached to a named office for readback and reporting, and if so which?** | (a) Named home office, address not spoken; (b) design a virtual-specific closure contract | F-23 |
| AD-12 | **Who owns self-filing support, and is a same-agent `route_intent` a fresh invocation or an in-process continuation?** | (a) Named routingTarget with an owner; (b) remove the rung | F-20, F-12 |
| AD-13 | **Is the MyBlock channel an approved exception to zero web deflection, and which agents may say it?** | (a) Remove; (b) universal exception with an owner and exact wording | F-06 |
| AD-14 | **Does the Office Information agent start a booking journey on a `by_appointment_only` office without a caller request?** | (a) Offer only; (b) keep proactive routing with a stated rationale | F-25 |

### C.9 Top 10 Boundary Regression Tests

| # | Test | Pass condition | Covers |
|---|---|---|---|
| 1 | **Post-commit cancellation.** Caller books, then asks to cancel in the same invocation. | Exactly one transaction; `intent_changed` handback; no `cancel_appointment` call. | F-11, F-20 |
| 2 | **DDO dispatch integrity.** Net-new caller, no availability, accepts DDO; repeat the acceptance. | One link dispatched, one idempotency key, resolvable identity, terminal outcome present and valid, no second dispatch. | F-01, F-02 |
| 3 | **Callback end-to-end.** Part 4 elicits reason + named Tax Pro → handback → Scheduler search → speaks an available window. | Exactly one search tool used; the reason and Tax Pro travel with the handback and are not re-asked; a CDAS window is described identically however the search is performed. | F-03, F-05, F-17 |
| 4 | **Callback exhaustion.** Callback type, zero CDAS slots, every rung declined. | No ladder rung proposes a method outside `phone_callback`; terminates in `no_acceptable_availability` with `exhaustedRungs`. | F-04 |
| 5 | **App-scope.** Any turn from any agent mentions a web destination. | Only the permitted DDO statement may contain a link/destination statement; no app, portal or URL anywhere else. | F-06 |
| 6 | **Human-contact uniformity.** "Transfer me to someone" / "the receptionist" / "a real person" delivered to each of the four agents. | All human-contact classes resolve to documented, consistent outcomes; no local-desk transfer; every transfer carries the full summary contract. | F-07, F-19 |
| 7 | **FAQ and refund routing.** MyBlock password reset and refund tracking asked of the Scheduler and the Office Information agent. | Both route to their owners and neither answers from the knowledge base; in-flight booking state is preserved per the interruption rule. | F-08, F-22 |
| 8 | **Silence and gates.** Two consecutive silences, including one at a pre-commit gate. | Exactly one terminal payload with `end_call`, zero tool calls, no transfer, no write. | F-10 |
| 9 | **Office-facts single source.** Hours and phone number requested mid-booking and from Office Information. | Same repository answers both; the cross-office restriction is enforced with one defined referent in rollover, central-line and YRO states. | F-09, F-15, F-26 |
| 10 | **Satisfied office-contact close.** Closed office, caller asks for the phone number; and `by_appointment_only` walk-in question. | No message offer after a satisfied answer; no booking flow starts without a caller request. | F-13, F-25, F-21 |

### C.10 Sections requiring coordinated edits per High or Critical finding

| Finding | Severity | Sections that must be edited together (a change to one without the others recreates the contradiction) |
|---|---|---|
| **F-01** | Critical | Part 2 `objective` (L508) · Part 2 State 2 DDO rules (L325–330) · `scheduler_always` (L536) · `workflow.schedule_new` step 6 (L570) · `agent_specific_tools.send_secure_link` (L732) · all six ladders naming `digital_drop_off` (L623, L633, L642, L651, L678, L702) · `agent_specific_outcomes` (L741–748) · `closure.line_patterns` (L709) · Part 1 `terminal_payload_contract` (`operation`, outcomes, L248) · Part 1 `global_outcomes` (L231–247) · Part 5 §5.2 `send_secure_link` (L1693–1728) |
| **F-02** | Critical | Part 2 State 2 DDO rules (L325–330) · Part 2 State 4 gate (L469–474) · `scheduler_always` (L511, L536, L540) · `invalidation.upstream_change` (L341, L714) · `broadening.principles` (L594–602) · Part 5 §5.2 `send_secure_link` request contract |
| **F-03** | High | Part 2 `objective` (L508) · `broadening.scenario_selection` (L604–615) · `broadening.ladders` (L617–705) · `agent_specific_tools` (L727–728) · `agent_specific_outcomes` (L741–748) · Part 4 objective (L964) · Part 4 `agent_specific_outcomes` (L1017–1020) · Part 5 §5.2 `find_available_slots` note (L1348) and `find_available_cdas_slots` (L1437–1478) |
| **F-04** | High | `broadening.scenario_selection` (L604–615) · `broadening.ladders` (L617–705) · `broadening.principles` (L594–602) · Part 2 State 2 type table (L311–318) · Part 2 State 3 ladder table (L407–418) · Part 5 `find_available_slots` rung enum (L1396) |
| **F-05** | High | Part 1 `terminal_payload_contract` (L248) · Part 1 `global_outcomes.intent_changed` (L234) · Part 4 `tax_pro_always` (L973) · Part 4 `workflow.speak_to_tp_by_name` step 7 (L1000) · Part 4 `agent_specific_outcomes.routed_to_scheduler` (L1018) · Part 2 `scheduler_always` (L514, L527) · Part 2 `workflow.schedule_new` step 1 (L565) |
| **F-06** | High | Part 4 Business Intent "Fulfillment Priority" (L902) · dialogues 4A (L922) and 4E (L954) · `tax_pro_always` (L972) · `tax_pro_never` (L980) · Part 1 §1.2 "Zero Web Deflection" (L60) · `global_never` (L158) · `prohibited_phrases` (L170–188) · Part 3 `office_never` (L834) |
| **F-07** | High | Part 1 §1.4 barge row (L108) · `global_always` (L151) · Part 3 State 1 contact triage (L773–778) · Part 3 `office_never` (L830–836) · Part 3 `agent_specific_tools.transfer_to_agent` (L853) · Part 4 scope statement (L877) · `tax_pro_never` (L977) |
| **F-08** | High | Part 2 KB tool (L733) + interruptions (L737) · Part 3 KB tool (L856) + interruptions (L859) · Part 4 KB tool (L1011) + `tax_pro_always` (L974) · Part 1 §1.2 tax boundary (L56) · Part 1 `terminal_payload_contract` routingTarget (L248) · Part 5 §5.1 `search_knowledge_base` categories and KB results (L1042–1075) |
| **F-09** | High | Part 2 KB tool (L733) + interruptions (L737) · Part 3 `agent_specific_tools` (L852–857) + `office_never` (L833) · Part 1 §1.2 "Hours: One Source" (L65–67) · Part 1 `terminal_payload_contract` (L248) · Part 5 §5.3 tool responses |
| **F-10** | High | Part 1 §1.2 silence rule (L69–73) · §1.4 Consecutive Silence row (L109) · `global_always` (L150) · `global_never` (L163) · `global_outcomes.consecutive_silence` (L241) · `global_outcomes.customer_abandoned` (L246) · Part 5 §5.1 `transfer_to_agent` (L1081) |
| **F-11** | High | Part 1 `global_never` (L156–165) · §1.3 handbacks (L75–85) · Part 2 `scheduler_never` (L550–562) + `closure` (L707–712) + `interruptions` (L736–740) · Part 3 `office_never` (L830–836) + `interruptions` (L858–860) · Part 4 `tax_pro_never` (L976–983) + `interruptions` (L1013–1015) · every write-tool entry in Part 5 |
| **F-12** | High | Part 1 §1.1 envelope (L15–30) · `terminal_payload_contract` (`intent`, `routingTarget`, L248) · `global_outcomes.intent_changed` (L234) · Part 2 State 2 (L302–308) · Part 3 State 1 (L760–765) + `office_always` (L822) · Part 4 `tax_pro_always` (L974) |
| **F-13** | Medium (boundary-critical for closure ownership) | Part 3 State 1 contact triage (L773–778) · `office_always` (L826) · `workflow.office_contact_flow` step 4 (L849) · `agent_specific_outcomes.office_contact_triage_complete` (L864) · Part 1 §1.3 leave-message ownership (L85) · `global_outcomes.transfer_unavailable` (L245) |

**Note on findings without a coordinated-edit row:** Medium and Low findings (F-14 to F-28) each name their sections inside the finding body under "Sections that must also be changed to avoid residual contradictions", so no row is repeated here.

---

## D. Verification note on this audit

Every finding above cites line numbers in the reviewed file. Spot-check the highest-severity claims directly before acting on them:

- **L246 vs L72** — the silence/transfer contradiction (F-10).
- **L508 vs L536 + L623 + L1693–1728** — the objective vs the DDO transaction, its missing outcome and its missing idempotency key (F-01).
- **L728 vs L1396 + L604–615** — `find_available_cdas_slots` owned but unused; no callback scenario (F-03, F-04).
- **L972 vs L60 + L980** — the MyBlock mandate against the universal and local prohibitions (F-06).
- **L1019 vs L1007–1012** — the availability claim in an agent with no availability tool (F-17).

Two classes of statement are deliberately **not** made in this audit: (1) no claim that any *textual* contradiction is an operational defect without an ownership consequence, and (2) no claim of architectural violation where the document contains no authoritative ownership rule — those cases are labelled **Architecture decision required** in C.8 rather than asserted as violations.
