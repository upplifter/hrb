# H&R Block — Future IVA Experience
## Deterministic Flow Specification (agent-readable Markdown)

**Version:** 1.0 (draft, transcribed from the five Lucid flow diagrams dated Sep 2026)
**Purpose:** A lossless, machine-readable rendering of the visual IVA flow diagrams, so an AI agent or IVR developer can implement the flows deterministically — every prompt, every input, every branch, every retry, every exit.
**Source documents (all five are single-page Lucid flow diagrams, "READY FOR HRB APPROVAL")**

| # | Document | Flow |
|---|----------|------|
| 1 | `HRB Future IVA Experience - Head of Call.pdf` | Head of Call (master router) |
| 2 | `HRB Future IVA Experience - Check Refund Status.pdf` | Check Refund Status (deterministic) |
| 3 | `HRB Future IVA Experience - Request Live Agent.pdf` | Request Live Agent (deterministic) |
| 4 | `HRB Future IVA Experience - Leave a Message.pdf` | Leave a Message (deterministic) |
| 5 | `HRB Future IVA Experience - VOC Survey.pdf` | VOC Survey (deterministic) |

---

## 0. How to read this document

### 0.1 What "deterministic flow" means here
These are **scripted state machines**, not free-form conversational AI. The IVA speaks a fixed prompt, collects one input, evaluates a fixed condition, and moves to a fixed next state. Natural-language utterances are only interpreted at explicitly marked points (`→ NLU`), where the utterance is passed to the NLU Intent Engine.

**An implementing agent must never improvise a prompt, invent a branch, or reorder a node.** Where the source diagram is ambiguous or leaves a decision open, this spec marks it `⚠️ OPEN` rather than guessing — those are listed verbatim in each flow's *Open items* section and must be resolved by H&R Block before build.

### 0.2 Notation

| Token | Meaning |
|---|---|
| `ID` | Stable node identifier. Prefixes: `CE` call entry, `ID` identification, `PA` proactive appointment, `IC` intent capture, `IT` intent treatment, `EH` error handling, `C` check-refund, `LA` live agent, `LM` leave message, `V` VOC survey, `G` global. |
| `SAY` | Verbatim prompt. Never paraphrase. |
| `${var}` | Runtime variable (from API, screen-pop, or prior capture). |
| `[ ]` | Placeholder H&R Block must fill (e.g. HOOPS hours). |
| `DTMF` / `SPEECH` / `EITHER` | Accepted input modality. |
| `(1) (2) (3)` | DTMF keypad selection and/or spoken equivalent. |
| `TRUE / FALSE` | Decision-diamond evaluation. |
| `FM` | Flow Milestone — a named event written to the reporting/analytics layer. |
| `SPF` | Screen Pop Field — data handed to a live agent or the next system. |
| `E` | Diagram connector **E** = the shared Error Handling hub (see §1.4). |
| `G` | Diagram connector **G** = return to Head of Call, Entry Point G (see §1.5). |
| `⚠️ OPEN` | Unresolved in the source diagram. Do not implement until HRB decides. |
| `→ NLU` | Utterance is passed to the NLU Intent Engine for intent classification. |

### 0.3 Universal retry policy (applies to every input in every flow)
1. **First failure** → play the node's `1st Attempt` re-prompt (`HRB_Invalid Input 1` for no-match, `HRB_No Input 1` for silence) and set `FM <Node> No Input/Not Match 1`.
2. **Second failure on the same required input** → set `FM <Node> No Input/Not Match 2`, play `HRB_Invalid Input 2` ("I still didn't get that.") or `HRB_Error Okay` ("I still didn't get that, but that's okay." — used where the flow *continues* without the answer), then hand to connector **E** (Error Handling).
3. **Menu timeouts**: where the diagram says `Timeout/ Invalid (Repeat 1x, No Selection 5 sec)` → 5-second inter-digit timeout, menu replayed once, then treated as no-input.
4. **Escalation rule (Head of Call, confirmed 9.4.26):** the IVR attempts to **identify intent before** initiating live-agent or after-hours handling. Transfer/escalation occurs **after two consecutive failures on the same required input or system interaction**.

### 0.4 HOOPS (Hours of Operation) — always dynamic
Every agent-transfer / office-closed prompt contains bracketed hours that must be rendered from HRB-provided HOOPS at runtime:
`Monday through Friday from [7 AM to 10 PM] and weekends from [7 AM to 8 PM] central.`

### 0.5 Exit taxonomy (every flow ends in exactly one of these)

| Exit | Definition |
|---|---|
| `EXIT-CONTAINED` | Caller answered "No" to *Is there anything else I can help with?* → `FM Call Contained = TRUE` → goodbye → disconnect. |
| `EXIT-NEWINTENT` | Caller answered "Yes / other utterance" → `FM New Intent = TRUE` → **To Head of Call (Entry Point G)**. |
| `EXIT-TRANSFER` | Warm/cold transfer to a live agent, queue, or agentic flow. |
| `EXIT-SELF-SERVICE-INCOMPLETE` | Flow could not complete (API/validation failure) → `FM ... Self-Service Incomplete`. |
| `EXIT-DISCONNECT` | Informed disconnect after an informational prompt. |

### 0.6 Flow map (how the five documents interconnect)

```
                     Incoming Call / DNIS
                             │
                             ▼
        ┌────────────────────────────────────────────┐
        │            HEAD OF CALL  (§1)              │
        │  Call Entry → Caller ID → Proactive Appt   │
        │            → Intent Capture                │
        └───────┬──────────┬──────────┬──────────────┘
                │          │          │
     Intent =   │          │          │  Intent = Request Live Agent
   Get Refund   │          │          ▼                     ▲
     Status     │          │   REQUEST LIVE AGENT (§3) ──────┘ (from ANY flow,
                ▼          │   (or caller says "agent"/press 0)   universal escalation)
   CHECK REFUND STATUS (§2)
                │
                │  Intent = Leave a Message
                ▼
        LEAVE A MESSAGE (§4)  ◄── also entered from "Speak To Tax Pro" flows, and
                                  from DNIS rollover when a field office doesn't answer
                │
                │  Post-call offer from Head of Call wrap-up (and from other flows)
                ▼
           VOC SURVEY (§5)

  Intent treatment also routes to AGENT / CASCADE flows (built elsewhere):
  Appointment Scheduling (S2S) · Speak To Tax Pro (cascade) · Office Information (cascade)
  · Log-in Help (S2S) · Tax Question (S2S) · Income Tax Course Assistance (S2S)
  · FAQ Agent · Orchestration Agent (S2S)
```

**Universal agent escalation (global rule):** a rule must be enabled across the *entire* call flow — if the caller says "agent" (or a recognised synonym) **or presses 0**, honour the first request and transfer into the Request Live Agent flow (§3), from any node in any flow.

---

## 1. Shared components & global rules

### 1.1 Screen Pop Fields (SPF) — the data contract
Fields passed to a live agent when a flow escalates:

| Field | Source | Notes |
|---|---|---|
| `UCID` | Client Profile Search API / identification | Unique customer id. The only input to `Client Interactions` / `Client Transactions`. |
| `Customer Status` | Identification result | `Existing`, `New`, or `Unknown`. |
| `Intent` | NLU Intent Engine | The classified intent name (e.g. `Check Refund Status`, `Request Live Agent`, `Leave a Message`). |
| `Authentication Status` | Verification nodes | `Caller Authenticated = TRUE/FALSE`. |
| `IVR Call Summary` | Generated at transfer time | Generated from **Call Transcript + Flow Milestones + Screen Pop Fields**. |

### 1.2 Flow Milestones — the reporting contract
Named boolean/numeric events emitted as the call progresses. Milestone families used across these flows:

`Survey Accepted` · `Survey Offer No Input/Not Match 1/2` · `Survey Q1 No Input/Not Match 1/2` · `Survey Q2 No Input/Not Match 1/2` · `Live Agent Request MAX Attempts` · `LiveAgentAvailable No Input` · `LiveAgentNotAvailable2 No Input` · `OfficeOpen` · `Agent Transfer` · `New Intent` · `Call Contained` · `IntentNoMatch` · `Client Profile Found` · `Multiple Profiles Matched` · `Caller Name Verified` · `Caller Authenticated` · `Caller Identified` · `Appointment Identified` · `Calling About Appointment` · `Future Appointment Found` · `Multiple Appointments Found` · `Future Appointments >3` · `Appointment Confirmation API Successful` · `Appointment Cancellation API Successful` · `ModifyAppt Max Attempts` · `VMRecipient` · `Callback Number Identified` · `Office identified from DNIS` · `OfficebyZipCode API Successful` · `EDS_Associate API Successful` · `TP Name Search API Successful` · `WC Leave Message API Successful` · `WC Leave Message API MAX Attempts` · `Leave a Message Self-Service Incomplete` · `Federal Tax Return/Refund Status Found` · `GetCustomerByFilingYear Successful` · `WIM$ Self-Service Successful` · `FullSSNCapture No Input/Invalid Input` · `DOBCapture No Input/Invalid Input` · `FilingYearCapture No Input/Invalid Input`

### 1.3 Node types used in the diagrams

| Type | Rendering in this spec | Behaviour |
|---|---|---|
| Prompt (rect) | `SAY` | Speak text, then set the state's input expectation. |
| Decision (diamond) | `Check:` | Evaluate an expression; take the TRUE/FALSE edge. No speech. |
| API call | `API CALL` | Invoke the named endpoint; a paired `Success`/`Failure` decision always follows. |
| Flow Milestone | `FM` | Write the milestone; pass through. |
| Screen Pop Field | `SPF` | Set/emit the field; pass through. |
| Go To | `→` | Jump to another flow/module (may be a real-time S2S handoff to an agentic flow). |
| Disconnect | `DISCONNECT` | End the call after the preceding goodbye. |

### 1.4 Connector E — Error Handling hub (shared)
Reached when a required input fails twice, or an API fails. Standard spelling:

```
E ── Check: During business hours?
      ├─ TRUE  → FM OfficeOpen = TRUE
      │          HRB_AgentTransfer ── "Let's connect you with someone who can help."
      │          FM Agent Transfer = TRUE
      │          SPF to pass: UCID · Customer Status · Intent · IVR Call Summary
      │          ROUTE TO  Skill/Queue Number: [⚠️ OPEN]  Skill/Queue Name: [⚠️ OPEN]  Agent Tier: [⚠️ OPEN]
      └─ FALSE → FM OfficeOpen = FALSE
                 HRB_OfficeClosed ── "To get help from one of our H&R Block Specialists, please call
                 back Monday through Friday from [7 AM to 10 PM] and weekends from [7 AM to 8 PM] central."
                 HRB_Goodbye ── "Thanks for choosing H&R Block. Have a great day." → DISCONNECT
```

**⚠️ OPEN — live-agent routing matrix.** HRB must finalise the destination queue + required agent skills for: (a) Intent is unknown; (b) each intent in the Intent Treatment section; (c) Intent = Check Refund Status + error entering lookup details; (d) Intent = Check Refund Status + API needed; (e) Intent = Check Refund Status + no response. HRB must also define the **error routing path** (appropriate skill/queue/agent tier) when the customer's intent is unknown, and provide **DNIS routing documentation/requirements**.

### 1.5 Connector G — return to Head of Call
`To Head of Call (Entry Point G)` = re-enter the master router at the **Intent Capture** stage (§1.6 / flow §1 `IC`), preserving `UCID`, `Customer Status`, `Authentication Status`.

### 1.6 NLU Intent Engine — the intent set routed by Head of Call
| Utterance group (Intent Training Utterances) | Routed intent | Destination |
|---|---|---|
| "I want to check my refund", "Give me my tax return details", "How much is my refund?", "Find my refund", "Has the IRS sent my refund?", "What's happening with my refund?", "Has my refund been issued yet?", "What's the status on my return?", "Where is my refund?", "Track my refund." | **Get Refund Status** | §2 Check Refund Status (deterministic) |
| "Leave a message.", "I want to leave a voicemail.", "I need to leave a message for [TPName].", "Leave a message for [OfficeLocation].", "Can someone call me back?", "Leave a note.", "Let the office know", "Let my tax professional know." | **Leave a Message** | §4 Leave a Message (deterministic) |
| "I want to speak with an agent.", "Let me speak to a real person.", "I need to talk to someone.", "Transfer me to a representative.", "Connect me with customer" | **Request Live Agent** | §3 Request Live Agent (deterministic) |
| (appointment utterances) | **Cancel / Change / Confirm Appointment** | Appointment Scheduling agentic flow (cascade) — exception: cancel/confirm handled inline per §1.7 |
| (tax-pro utterances) | **Speak To Tax Pro** | Agent (cascade) |
| (office utterances) | **Office Information** | Agent (cascade) |
| (account utterances) | **Log-in Help** | Log-in Help Agent (real-time S2S) |
| (tax-law utterances) | **Tax Question** | Tax Question Agent (real-time S2S) |
| (course utterances) | **Income Tax Course Assistance** | ITC Assistance Agent (real-time S2S) |
| anything unmatched | **Unknown** | connector E → Error Handling |

Reference artifacts named in the diagrams: `HRB_IVA_NLU Intent Model.xlsx`, `HRB_IVA_NLU Intent Reject Codes - ...xlsx`, `HRB - VOC Survey Requirements.docx`, `VOC Questions.xlsx`, `WIM$_Refund Status Logic.xlsx`, `refundStatusWithDialog.docx`, `HRB - D365 Contact Center Workbook.xlsx`, `Client Profile Interactions Workbook.xlsx`.

### 1.7 Proactive Appointment (shared component, lives in Head of Call)
**Requirement CX-31-P:** the system must recognise callers who *have* appointments and proactively offer appointment actions (confirm, reschedule, cancel, get details) rather than requiring the caller to navigate to them.

**Design decision 9.11.26:** proactive handling of **missed / cancelled / no-show** appointments is **deferred to Phase 2** (office-level processes are inconsistent). Intent handling for callers who need a new appointment after missing one is preserved and passed to the Appointment Scheduling agent.

**Client Interactions API** returns **future appointment data only** (source of previous appointments is Client Transactions — ⚠️ see agent comment in source). Input to `Client Profile Search`: **UCID (only)**.
Endpoint: `https://blockapi-qa.hrblock.net/edp/eods/client-search`
Appointment status endpoint: `https://blockapi-qa.hrblock.com/ecp/fsamtpf/api/AppointmentStatus`

### 1.8 PII handling (global)
- **Do not store PII.** Redact/mask full SSN from the transcript. (DEV note on Check Refund Status.)
- Only the **last four** digits of SSN are spoken for disambiguation; full SSN is entered via keypad where required.
- Leave a Message explicitly warns the caller not to speak SSN/DOB.

### 1.9 Agent barge-in
**Requirement CX-17-P:** disable immediate agent-barging (repeated "live agent, live agent"); gate it with a **turn barrier** while still capturing enough intent to route correctly. Classify each fail-out reason (user-intended, company-intended in-scope, company-unintended out-of-scope) and **always offer a path to support after capturing intent**, so misses are measurable. Dev note: **Disable Agent Barge setting for Head of Call.**

---

## 2. Flow 1 — HEAD OF CALL (master router)
**Source:** `HRB Future IVA Experience - Head of Call.pdf` · **Status:** READY FOR HRB APPROVAL / DESIGN IN PROGRESS
**Role:** the only entry point for the standard IVA experience. Performs compliance, caller identification, proactive appointment handling, intent capture, and intent treatment. Also the destination of connector G from every other flow.

### 2.1 At a glance
| Property | Value |
|---|---|
| Entry | Incoming call / DNIS (also reached as **Entry Point G** from all other flows) |
| Structural lanes | CALL ENTRY → CALLER IDENTIFICATION → PROACTIVE APPOINTMENT → INTENT CAPTURE → INTENT TREATMENT → ERROR HANDLING |
| Screen pop set | `Customer Status` · `UCID` · `Caller Authenticated` · `Caller Identified` · `Intent` |
| Universal rule | Any caller saying "agent"/synonym or pressing **0** is transferred to §3 Request Live Agent |
| Exits | `EXIT-NEWINTENT` (G), `EXIT-TRANSFER`, `EXIT-CONTAINED`, `EXIT-DISCONNECT` |

### 2.2 Flow spine
```
CE-01 Greeting → CE-02 Recording notice
   ↓
ID-01 Client Profile Search (ANI) ── Office number? ──TRUE──► ID-02 Ask alternate phone → ID-01
   │ FALSE
   ├─ API Failure ─────────────────────────────────────────────► ID-20 unknown-caller path
   ├─ Found? FALSE ──► ID-10 no profile → ID-11 new/returning → (new) ID-30 unknown caller
   │                                                          └ (returning) ID-12 SSN → ID-13 DOB → ID-20
   └─ Found? TRUE
        ├─ Multiple profiles? FALSE → ID-05 name confirmation → verified → PA-01 / IC-01
        │                            └ not-verified → ID-11
        └─ Multiple profiles? TRUE  → ID-06 disambiguation → ID-07 SSN(4) → ID-08 DOB → PA-01 / IC-01
   ↓
PA-01 Proactive appointment found? ──TRUE──► PA-02 menu (cancel / change / confirm) → PA-xx → G
   │ FALSE / no appointment
   ▼
IC-01 "In a few words, tell me what I can help with today…" → NLU
   ▼
IT-xx Intent treatment (See §1.6) → deterministic flows (§2–§5) or agent flows
   ▼
EH E ─► Agent Transfer | Office Closed → Goodbye → Disconnect
```

### 2.3 Call Entry
| ID | Type | SAY / DO | Input | → Next |
|---|---|---|---|---|
| `CE-01` | Prompt | **HRB_GreetingAnnouncement** — "Thank you for calling H&R Block." | — | `CE-02` |
| `CE-02` | Prompt | **HRB_ComplianceAnnouncement** — "This call may be recorded for quality assurance." | — | `ID-01` |

### 2.4 Caller Identification
**Design decision 9.11.26:** ANI values are checked against known office numbers using the **Office Search by ANI API**. If an office number is detected, the caller is prompted for an **alternate phone number**. If multiple UCIDs are returned, the system first uses the **last four of the SSN** for disambiguation, then **date of birth** if further verification is required. Customers identified through ANI or alternate phone complete a **name confirmation** step. **Unresolved callers are routed to Intent Capture as unknown callers — never transferred directly to an agent.**

| ID | Type | SAY / DO | Input | Valid | → Next |
|---|---|---|---|---|---|
| `ID-01` | API CALL | **Client Profile Search API** — `.../edp/eods/client-search` (input: ANI / phone; also keyed on `UCID` elsewhere) | — | — | `ID-01a` |
| `ID-01a` | Check | **ANI Check: Office Phone Number?** (Office Search by ANI API) | — | — | TRUE → `ID-02` · FALSE → `ID-03` |
| `ID-02` | Prompt | **HRB_AlternatePhone** — "What phone number should I use to look up your account?" | EITHER | `###-###-####` (also `####` forms in source) | valid → `ID-01` (re-lookup) · 1st fail → `HRB_Invalid Input 1` "I didn't get that…" / `HRB_No Input 1` "I didn't hear anything…" · 2nd fail → `FM AlternatePhone No Input/Invalid Input 2` → `E` |
| `ID-03` | Check | **Client Profile Search API Successful?** | — | — | TRUE → `ID-04` · FALSE → `FM Client Profile Search API Successful = FALSE` → `ID-20` |
| `ID-04` | Check | **Profile Match Found? (Client Found?)** | — | — | TRUE → `ID-04a` · FALSE → `FM Client Profile Found = FALSE` → `ID-10` |
| `ID-04a` | Check | **Multiple Profiles Matched?** | — | — | FALSE (1:1 UCID match) → `ID-05` · TRUE → `FM Multiple Profiles Matched = TRUE` → `ID-06` |
| `ID-05` | Prompt | **HRB_NameVerification** — "I found an account for **${firstName}** matching this phone number. Is that you?" | EITHER | `1` Yes / `2` No | Yes → `ID-05a` · No → **HRB_IncorrectName** "Thanks for letting me know." → `FM Caller Name Verified = FALSE` → `ID-11` · 1st fail → `HRB_Invalid Input 1`/`HRB_No Input 1` · 2nd → `FM NameVerification No Input/Invalid Input 2` → `E` |
| `ID-05a` | Milestone set | **HRB_Great** "Great." → `FM Success Client Profile Search API = TRUE` · `FM Caller Name Verified = TRUE` · `FM Caller Authenticated = TRUE` · `FM Caller Identified = TRUE` · `SPF Customer Status = Existing` · `SPF UCID = {value}` | — | — | `PA-01` |
| `ID-06` | Prompt | **HRB_MultipleProfileMatch** — "I found multiple accounts for the phone number you are calling from…" | — | — | `ID-07` |
| `ID-07` | Prompt | **HRB_SSNIdentification** — "To help me find your account, please say or enter the last 4 of your Social Security Number using the keypad." | EITHER | `####` | valid → `ID-07a` · 1st fail → `HRB_Invalid Input 1`/`HRB_No Input 1` · 2nd → `FM SSNIdentification No Input/Invalid Input 2` → `E` |
| `ID-07a` | Check | **Profile matched? (1:1 UCID match)** | — | — | TRUE → `FM Client Profile Found = TRUE`, `FM Multiple Profiles Matched = FALSE` → `ID-05` · FALSE → `ID-08` |
| `ID-08` | Prompt | **HRB_DOBIdentification** — "Next, please say or enter your date of birth. For example, you can say *April first, nineteen eighty five,* or enter 0-4-0-1-1-9-8-5." | EITHER | date | valid → `ID-08a` · 1st fail → `HRB_Invalid Input 1`/`HRB_No Input 1` · 2nd → `FM DOBIdentification No Input/Not Match 2` → `E` |
| `ID-08a` | Check | **Client Profile Found = FALSE** (still unresolved) | — | — | TRUE → `ID-20` |
| `ID-10` | Prompt | **HRB_NoProfileMatch** — "I couldn't find an account linked to the phone number you're calling from. Okay…" | — | — | `ID-11` |
| `ID-11` | Prompt | **HRB_CustomerType** — "If you're new to H&R Block, say *new customer*. If you've worked with us before, say *returning customer*." | EITHER | `1` New Customer / `2` Returning Customer | New → `SPF Customer Status = New`, `SPF UCID = Unknown`, `FM Caller Identified = TRUE` → `IC-01` · Returning → `ID-12` · 1st fail → `HRB_Invalid Input 1`/`HRB_No Input 1` · 2nd → `FM CustomerType No Input/Not Match 2` → `E` |
| `ID-12` | Capture | **HRB_SSNIdentification** — collect **Full SSN** (Speech or keypad; "For example you can say … or enter 0-4-0-1-1-9-8-5") | EITHER | Full SSN | valid → `ID-13` · 1st/2nd fail → `HRB_Invalid Input 1/2`, `HRB_No Input 1/2` → `E` |
| `ID-12a` | API CALL | **Client Profile Search API** (lookup by Full SSN + DOB) · `Success`/`Failure` decision follows | — | — | Success → `ID-13` · Failure → `E` |
| `ID-13` | Capture | **HRB_DOBIdentification** — collect **DOB** | EITHER | date | valid → `ID-14` · 1st/2nd fail → `E` |
| `ID-14` | Output | Verification result inputs: **Full SSN + DOB**. Outputs: `UCID`; name; PII; tax tenure; match score; failure information | — | — | `PA-01` |
| `ID-20` | Prompt | **HRB_IdentificationNoMatch** — "I wasn't able to find an account based on that information, but that's okay…" | — | — | `SPF Customer Status = Unknown`, `SPF UCID = Unknown`, `FM Caller Authenticated = FALSE`, `FM Client Profile Search API Successful = FALSE` → `IC-01` |
| `ID-21` | Prompt | **HRB_Invalid Input 2** — "I still didn't get that, but that's okay." (repeated for each failed verification leg; `FM Identify Appointment No Input/Not Match 2`) | — | — | `SPF Caller Authenticated = FALSE` → `IC-01` |
| `ID-22` | Prompt | **HRB_NoPhoneMatch** | — | — | `E` |

### 2.5 Proactive Appointment
| ID | Type | SAY / DO | Input | Valid | → Next |
|---|---|---|---|---|---|
| `PA-01` | API CALL | **Client Interactions API** — `.../edp/eods/client-interactions` (input: **UCID**; window `FutureAppointmentSearchStartDate = CurrentDate`; if CurrentDate between Jan 1 and Apr 30 → `FutureAppointmentSearchEndDate = Apr 30 (current year)`, else `CurrentDate + 30 days`) | — | — | `PA-01a` |
| `PA-01a` | Check | **Future Appointment Found?** | — | — | TRUE → `FM Future Appointment Found = TRUE` → `PA-02` · FALSE → `FM Future Appointment Found = FALSE` → `IC-01` · API failure → `FM Client Interactions API Successful = FALSE` → `ID-22`/`E` |
| `PA-02` | Check | **Multiple Appointments Found?** | — | — | FALSE → `PA-03` · TRUE → `FM Multiple Appointments Found = TRUE` → `PA-04` |
| `PA-03` | Prompt | **HRB_Proactive Appointment** — "I see you have an upcoming appointment on **(ApptDay),(ApptDate) at (ApptTime)**. Is this what you're calling about today?" | EITHER | `1` Yes / `2` No | Yes → `FM Calling About Appointment = TRUE` → `PA-05` · No → `FM Calling About Appointment = FALSE` → `IC-01` · 1st fail → `HRB_Invalid Input 1`/`HRB_No Input 1` · 2nd → `FM ProactiveAppointmentMenu No Input/Not Match 2` → `E` |
| `PA-04` | Check | **Appointment >3?** (`Future Appointments >3 = FALSE/TRUE`) | — | — | listed menu → `PA-04a` |
| `PA-04a` | Prompt | **HRB_ProactiveMultipleAppointments** — "I found multiple upcoming appointments. Which appointment can I help you with? For **(ApptDay),(ApptDate) at (ApptTime)**, press 1. For …, press 2. For …, press 3." | DTMF | `[1-3]` | valid → `FM Appointment Identified = TRUE` → `PA-05` · 1st fail → `HRB_Invalid Input 1`/`HRB_No Input 1` · 2nd → `FM Multiple Profile Match For Appointment …` → `E` |
| `PA-05` | Check | **Authentication required?** — `Check: Inputs: Full SSN + DOB, Outputs: UCID; name; PII; tax tenure; match score` (`HRB_SSNIdentification` → `HRB_DOBIdentification`) | EITHER | Full SSN, DOB | success → `PA-06` · failure → `E` |
| `PA-06` | Prompt | **HRB_ModifyAppointmentMenu** — "What would you like to do with your appointment? You can say *cancel*, *change*, or *confirm*." | EITHER | `1` Cancel / `2` Change-Reschedule / `3` Confirm | Cancel → `FM Intent = Cancel Appointment`, `SPF Intent = Cancel Appointment` → `PA-10` · Change → `FM Intent = Change Appointment`, `SPF Intent = Change Appointment` → `HRB_AppointmentChange` "Great! I can help you reschedule." → **Go To Appointment Scheduling (Real Time S2S Flow)** · Confirm → `SPF Intent = Confirm Appointment` → `PA-20` · 1st fail → `HRB_Invalid Input 1`/`HRB_No Input 1` · 2nd → `FM ModifyAppointmentMenu No Input/Not Match 2` → `FM ModifyAppt Max Attempts = TRUE` → `E` |
| `PA-10` | Prompt | **HRB_CancelAppointment** — "Just to confirm, you'd like to cancel your upcoming appointment?" | EITHER | `1` Yes / `2` No | Yes → `PA-11` · No → `HRB_NoProblem` "No problem." → `IC-01` · 1st fail → `HRB_Invalid Input 1`/`HRB_No Input 1` · 2nd → `FM Cancel Appointment No Input/Not Match 2` → `E` |
| `PA-11` | API CALL | **Appointment Status API** — `.../ecp/fsamtpf/api/AppointmentStatus` | — | — | Success → `FM Appointment Cancellation API Successful = TRUE` → `PA-12` · Failure → `FM Appointment Cancellation API Successful = FALSE` → `PA-13` |
| `PA-12` | Prompt | **HRB_AppointmentCancelled** — "Okay, I've cancelled that appointment for you." | — | — | `PA-30` (Additional Help) |
| `PA-13` | Prompt | **HRB_AppointmentCancellationError** — "I'm having trouble cancelling your appointment right now." | — | — | `E` |
| `PA-20` | API CALL | **Appointment Status API** (confirm) | — | — | Success → `FM Appointment Confirmation API Successful = TRUE` → `PA-21` · Failure → `FM Appointment Confirmation API Successful = FALSE` → `PA-22` |
| `PA-21` | Prompt | **HRB_AppointmentConfirmed** — "Great! Your appointment has been confirmed. We look forward to seeing you on **[ApptDay], [ApptMonth] [ApptDate] at [ApptTime]**." | — | — | `PA-30` |
| `PA-22` | Prompt | **HRB_AppointmentCancellationError (confirm variant)** — "I'm having trouble confirming your appointment right now." | — | — | `E` |
| `PA-30` | Prompt | **HRB_Additional Help** — "Is there anything else I can help with?" | EITHER | `1` Yes / Other Utterance · `2` No | Yes/Other → `FM New Intent = TRUE` → **To Head of Call (Entry Point G)** `IC-01` · No → `FM New Intent = FALSE`, `FM Call Contained = TRUE` → `EH-01` · `Timeout/Invalid (Repeat 1x, No Selection 5 sec)` |
| `PA-40` | Prompt | **HRB_Okay / HRB_LetsContinue** — "Okay." / "Let's continue." (used to resume after an appointment detour) | — | — | `IC-01` |

**Design note:** automated business processes already auto-confirm appointments and send AM-owned text/email confirmations — the confirm path duplicates that for self-service callers. Cancel and Confirm are shown in Head of Call *for illustration of the end-to-end experience*; in most cases they do **not** transition into the Appointment Scheduling agentic flow unless the caller needs a new/rescheduled appointment.

### 2.6 Intent Capture
| ID | Type | SAY / DO | Input | → Next |
|---|---|---|---|---|
| `IC-01` | Prompt | **HRB_IntentCapture** — "In a few words, tell me what I can help with today…" | SPEECH | `IC-02` |
| `IC-02` | NLU | Pass utterance to the **NLU Intent Engine** (`HRB_IVA_NLU Intent Model.xlsx`). Set `SPF Intent = <classified>` | — | `IC-03` |
| `IC-03` | Prompt | **HRB_GetStarted** "To get started…" / **HRB_LetsContinue** "Let's continue." | — | `IC-04` |
| `IC-04` | Check | **Intent = ?** (decision chain against the intent set in §1.6) | — | see §2.7 |

### 2.7 Intent Treatment
Each treatment node passes `Data To Pass: UCID · Customer Status · Utterance · Authentication Status` unless noted.

| ID | Check | TRUE → | FALSE → |
|---|---|---|---|
| `IT-01` | `Intent = Get Refund Status?` | **Go To Refund Status (Deterministic Flow)** — §3 of this doc | `IT-02` |
| `IT-02` | `Intent = Cancel Appointment?` | `SPF Intent = Cancel Appointment` → Appointment Scheduling flow (cascade) — *or* inline `PA-10` | `IT-03` |
| `IT-03` | `Intent = Change / Reschedule Existing Appointment?` | Appointment Scheduling Agent (Real Time S2S Flow) | `IT-04` |
| `IT-04` | `Intent = Confirm Appointment?` | `SPF Intent = Confirm Appointment` → Appointment Scheduling flow (cascade) — *or* inline `PA-20` | `IT-05` |
| `IT-05` | `Intent = Request Live Agent?` | **Go To Request Live Agent (Deterministic Flow)** — §4 of this doc | `IT-06` |
| `IT-06` | `Intent = Speak To Tax Pro?` | Speak To Tax Pro Agent (Cascade) | `IT-07` |
| `IT-07` | `Intent = Office Information?` | Office Information Agent (Cascade) | `IT-08` |
| `IT-08` | `Intent = Log-in Help?` | Log-in Help Agent (Real Time S2S Flow) | `IT-09` |
| `IT-09` | `Intent = Tax Question?` | Tax Question Agent (Real Time S2S Flow) | `IT-10` |
| `IT-10` | `Intent = Income Tax Course Assistance?` | ITC Assistance Agent (Real Time S2S Flow) | `IT-11` |
| `IT-11` | `Intent = Leave a Message?` | **Go To Leave a Message (Deterministic Flow)** — §5 of this doc | `IT-12` |
| `IT-12` | `Intent = Unknown / IntentNoMatch` | `SPF Intent = Unknown (Blank)`, `FM Caller Authenticated = FALSE`, `SPF UCID = Unknown` → `IT-13` | — |
| `IT-13` | Prompt | **HRB_LetsContinue** — "Let's continue." → `E` (Error Handling) | — |
| `IT-14` | Prompt | **HRB_Invalid Input 2** — "I still didn't get that, but that's okay." → `E` | — |

**DEV NOTE:** if the intent is not contained within the appropriate agentic flow, the call escalates to **Live Agent (HRB Specialist)**. If after hours, the caller is instructed to call back during the hours provided — **Entry Point E**.

### 2.8 Error Handling & exit
`EH-01` **HRB_Goodbye** — "Thanks for choosing H&R Block. Have a great day." → **Disconnect**
Plus connector **E** exactly as specified in §1.4.

### 2.9 Open items in Head of Call (⚠️ verbatim from source)
1. **Action item** — finalise the live-agent routing matrix (destination queue + required agent skills) for: *Intent is unknown*; *each intent in the intent treatment section*; *caller requires assistance changing/rescheduling an appointment*; *confirming an appointment*; *cancelling an appointment*.
2. **Action item** — for each Head-of-Call identity path, confirm whether the caller is **identified only**, or **considered authenticated** for screen-pop purposes: (a) ANI match + caller name confirmation; (b) alternate phone match + caller name confirmation; (c) last four digits of SSN; (d) last four of SSN + date of birth.
3. **Deferred to Phase 2** — proactive handling of missed / cancelled / no-show appointments.
4. Ingrid Marquardsen / Brian Easton comments: reasoning for placing cancel + confirm inside Head of Call (answered by CG: illustration + readability; cancelling to a separate page would not change underlying flow), and whether Client Transactions is needed as the source for previous appointments (answered: Phase 1 defers; Client Interactions returns future appointment data only).
5. Provide **DNIS routing documentation / requirements**; define the **error routing path** when intent is unknown.
6. Michael Vo comment — context routing: does the **CCO Context API** get called as the first step of the flow? (▲ open)
7. Provide designated **approver(s)** for the IVA design; then transition to build phase.

---

## 3. Flow 2 — CHECK REFUND STATUS (deterministic)
**Source:** `HRB Future IVA Experience - Check Refund Status.pdf` · **Status:** READY FOR HRB APPROVAL
**Entry:** From Head of Call, after `Intent = Get Refund Status`. **Entry Point A**.

### 3.1 At a glance
| Property | Value |
|---|---|
| Inputs | **Filing Year**, **Full SSN**, **DOB** |
| Outputs | `Tax Return Required`, `Status Code`, `federalRefundDue`, `disbursementAmount`, dates |
| Screen pop | `Intent = Check Refund Status`; `Filing Year = dynamic` |
| Sub-lanes | Capture Lookup Fields → Return Lookup → Federal Return Status → State Return Status → Call Wrap-Up |
| Exits | `EXIT-NEWINTENT` (VOC Survey / G), `EXIT-TRANSFER`, `EXIT-CONTAINED`, `EXIT-SELF-SERVICE-INCOMPLETE` |

### 3.2 Flow spine
```
[A: Head of Call] → C-01 Filing Year → C-02 Full SSN → C-03 DOB
   → C-04 TaxOps API: GetCustomerByFilingYear
        ├─ API failure ─────────────────────► C-30 HRB_APIFailure → E
        ├─ "More than One Tax Ops data found!" ─► C-30 → E
        ├─ "No status" + before e-file open ─► C-11 IRS-not-accepting-yet → C-40 wrap-up
        ├─ "No status" + after e-file open  ─► C-12 no status found → C-40 wrap-up
        ├─ RC>10Bd / RC<10Bd / DD>5Bd / DD<5Bd ─► C-13..C-16 (mailed/deposited) → C-40
        ├─ Accepted 09-05/06/15/16 ─► C-17..C-20 bank / non-bank / e-file window variants → C-40
        ├─ Accepted 12-00/12-02 ─► C-21 → C-40
        ├─ 12-09 (Emerald Card) ─► C-22 → Emerald Services transfer | C-40
        ├─ 08-xx rejected ─► C-23/C-24/C-25 retail / software / online → transfer or E
        ├─ 01-05 pending ─► C-26 (<48h) or C-27 (transfer)
        ├─ 01-13 ─► C-28 (transfer)
        └─ 13-00/13-02/14-00 ─► C-29 Go To Appointment Scheduling (S2S)
   → C-40 Read out state if available → C-50 wrap-up → VOC Survey (§6) | G | Goodbye
```

### 3.3 States
| ID | Type | SAY / DO | Input | Valid | → Next |
|---|---|---|---|---|---|
| `C-01` | Prompt | **HRB_FilingYearCapture** — "Would you like to check the refund status for the **current** or **prior** tax year?" | EITHER | `1` Current Year / `2` Prior Year | valid → `C-02` · 1st fail → `HRB_Invalid Input 1` "I didn't get that…" / `HRB_No Input 1` "I didn't hear anything…" · 2nd → `FM FilingYearCapture No Input/Invalid Input`, `HRB_Invalid Input 2` "I still didn't get that." → `E` |
| `C-01a` | Logic | Convert `"Current Year"` / `"Prior Year"` → numeric year for the API (**Valid year range = Current Year − 1 tax years**). Screen pop `Filing Year = dynamic` | — | — | `C-02` |
| `C-02` | Prompt | **HRB_FullSSNCapture** — "To look up the status of your refund, please enter your full Social Security Number using the keypad." | EITHER | `###-##-####` or `##-##-####` | valid → `C-03` · 1st fail → `HRB_Invalid Input 1`/`HRB_No Input 1` · 2nd → `FM FullSSNCapture No Input/Invalid Input` → `E` |
| `C-03` | Prompt | **HRB_DOBCapture** — "…please say or enter your date of birth. For example, you can say *April first, nineteen eighty five,* or enter 0-4-0-1-1-9-8-5." | EITHER | date | valid → `C-04` · 1st fail → `HRB_Invalid Input 1`/`HRB_No Input 1` · 2nd → `FM DOBCapture No Input/Invalid Input` → `E` |
| `C-04` | API CALL | **Tax Ops — `refundStatus` / getCustomerByFilingYear / `TaxReturnStatus`** (input: SSN, DOB, Filing Year) | — | — | `C-05` |
| `C-05` | Check | **GetCustomerByFilingYear API Successful?** | — | — | TRUE → `FM Success GetCustomerByFilingYear Successful = TRUE` → `C-06` · FALSE → `FM Success GetCustomerByFilingYear Successful = FALSE` → `C-30` |
| `C-06` | Check | **Federal Tax Return / Refund Status Found?** (Data Returned = ?) | — | — | TRUE → `FM Federal Tax Return/Refund Status Found = TRUE` → `C-07` · FALSE → `FM … = FALSE` → `C-12` |
| `C-07` | Check | `refundStatus == "More than One Tax Ops data found!"` | — | — | TRUE → `FM Status = More than One Tax Ops data found!` → `C-30` |
| `C-08` | Check | `refundStatus == "No status"` **AND** `isBeforeEfileOpenDate == TRUE` | — | — | TRUE → `C-11` (→ "E" loop back to `C-01`) |
| `C-09` | Check | `refundStatus == "No status"` **AND** `isBeforeEfileOpenDate == FALSE` | — | — | TRUE → `FM Status = No Status` → `C-12` |
| `C-10` | Check | **Dispatch on `refundStatus` / `TaxReturnStatus`** (see decision table §3.4) | — | — | → `C-13` … `C-29` |
| `C-11` | Prompt | **HRB_NoStatusBeforeEfile** — "I couldn't find a status based on that information. The IRS will not begin accepting returns until **${irsEfileOpenDate}**. If you recently filed your return, it may take some time for your refund information to become available." | — | — | `FM WIM$ Self-Service Successful = FALSE` → **E** ("E" connector in source which loops back to the filing-year question) → `C-40` |
| `C-12` | Prompt | **HRB_TaxReturnStatusNF** — "I couldn't find a status based on that information." | — | — | `FM WIM$ Self-Service Successful = FALSE` → `C-40` |
| `C-13` | Prompt | **HRB_>10BDays** — "${disbursementAmount} was mailed on ${checkPrintedDate}. **Have you received your refund?** (1) Yes (2) No" | EITHER | `1` / `2` | → `C-40` · `Timeout/Invalid (Repeat 1x, No Selection 5 sec)` |
| `C-14` | Prompt | **HRB_<10BDays** — "${disbursementAmount} was mailed on ${checkPrintedDate}. Let us know if you have not received the funds by **${checkTenPrintedDate}**." | — | — | `C-40` |
| `C-15` | Prompt | **HRB_>5BDays** — "${disbursementAmount} was sent to your bank account on ${depositDate}. **Have you received your refund?** (1) Yes (2) No" | EITHER | `1` / `2` | → `C-40` · `Timeout/Invalid (Repeat 1x, No Selection 5 sec)` |
| `C-16` | Prompt | **HRB_<5BDays** — "${disbursementAmount} was sent to your bank account on ${depositDate}. Let us know if you have not received the funds by **${fiveDaysDepositDate}**." | — | — | `C-40` |
| `C-17` | Prompt | **HRB_AcceptedInsideRange-BankClient** — "The IRS accepted your return on **${returnReceivedIRSACKDate}**. We offer text message alerts for the status of your refund, and you can enroll now using our automated system. Please note that you will be asked to verify your information again. **Would you like me to transfer you there now?** (1) Yes (2) No" | EITHER | `1` / `2` | Yes → **Go To automated enrollment system** (⚠️ OPEN destination) · No → `C-40` · `Timeout/Invalid (Repeat 1x, No Selection 5 sec)` |
| `C-18` | Prompt | **HRB_AcceptedOutsideRange-BankClient** — "The IRS accepted your return on **${irsEfileOpenDate}**. Most refunds are issued by the IRS within 21 days. Visit IRS.gov/refunds or call 800-829-1954 for details. You will be asked to verify information, including your refund amount. Your estimated refund amount is **${federalRefundDue}**." | — | — | `C-40` |
| `C-19` | Prompt | **HRB_Accepted-NotBankClient** — "The IRS accepted your return on **${returnReceivedIRSACKDate}**. Most refunds are issued by the IRS within 21 days. Visit IRS.gov/refunds or call 800-829-1954 for details. You will be asked to verify information, including your refund amount. Your estimated refund amount is **${federalRefundDue}**." | — | — | `C-40` |
| `C-20` | Prompt | **HRB_AcceptedStatus12-NotBankClient** — same verbiage as `C-19` | — | — | `C-40` |
| `C-21` | Prompt | **HRB_Accepted-Bank-IRS DD To EC Client** — "The IRS accepted your return on **${returnReceivedIRSACKDate}**. Most refunds are issued by the IRS within 21 days. Contact the IRS for the most up-to-date information. I see that you elected to have your refund deposited into your **Emerald Card Account**. **Would you like me to transfer you to the Emerald Services line?** (1) Yes (2) No" | EITHER | `1` / `2` | Yes → **Go To Emerald Services** (⚠️ routing destination to define) · No → `C-40` · `Timeout/Invalid (Repeat 1x, No Selection 5 sec)` |
| `C-22` | Prompt | **HRB_RejectedRetail** — "Your return has been rejected by the IRS. You will need to speak with your tax professional. **Would you like to schedule an appointment now?** (1) Yes (2) No" + read the **reject-code verbiage** (table §3.5) | EITHER | `1` / `2` | Yes → **Go To Appointment Scheduling Agent (Real Time S2S Flow)** · No → `C-40` · `Timeout/Invalid (Repeat 1x, No Selection 5 sec)` |
| `C-23` | Prompt | **HRB_Rejected Digital Software** — "I'm unable to provide your refund status at this time." | — | — | → **route to digital-software support transfer** (⚠️ define routing destination) |
| `C-24` | Prompt | **HRB_Rejected Digital Online** | — | — | `FM ZERO_IDM_MATCHES` → **define subflow** (⚠️ OPEN) |
| `C-25` | Prompt | **HRB_Pending<48Hours** — "Your return has been transmitted to the IRS. There's nothing else you need to do. Your return will be processed within 24 to 48 hours of the IRS receiving it." | — | — | `C-40` |
| `C-26` | Flow milestone | `Status = TRANSFER` (TaxReturnStatus `01-05`, more than 2 working days, `ns2_Source = efile_Retail`) | — | — | **E** |
| `C-27` | Flow milestone | `Status = TRANSFER` (TaxReturnStatus `01-13`, `ns2_Source = efile_Retail`) | — | — | **E** |
| `C-28` | Flow milestone | `Status = TRANSFER` (TaxReturnStatus `13-00`/`13-02`/`14-00`) | — | — | **Go To Appointment Scheduling Agent (Real Time S2S Flow)** |
| `C-30` | Prompt | **HRB_APIFailure** — "I seem to be having trouble locating your tax refund status at this time." | — | — | `FM WIM$ Self-Service Successful = FALSE` → **E** |
| `C-31` | Prompt | **HRB_WIM$ SSN Failure** — "Without a valid Social Security Number I'm unable to access your return details." | — | — | **E** |
| `C-32` | Prompt | **HRB_WIM$ DOBFailure** — "Without a valid date of birth, I'm unable to access your return details." | — | — | **E** |
| `C-33` | Prompt | **HRB_WIM$ FilingYearFailure** — "Without a filing year to search for, I'm unable to look up your return details." | — | — | **E** |
| `C-40` | Action | **Read out state if available** — after federal status is delivered, **offer available state status** (only when available; never read automatically to everyone) | EITHER | — | `C-50` |
| `C-50` | Prompt | **HRB_Additional Help** — "Is there anything else I can help with?" | EITHER | `1` Yes / Other Utterance · `2` No | Yes/Other → `FM New Intent = TRUE` → **Go To VOC Survey (Deterministic Flow)** *(source shows VOC Survey as the post-refund routing)* and/or **To Head of Call (Entry Point G)** · No → `FM New Intent = FALSE`, `FM Call Contained = TRUE` → `C-51` · `Timeout/Invalid (Repeat 1x, No Selection 5 sec)` |
| `C-51` | Prompt | **HRB_Goodbye** — "Thanks for choosing H&R Block. Have a great day." | — | — | **DISCONNECT** |

### 3.4 API decision table (all `#`-prefixed checks evaluated in order)

| Priority | Expression | Status label | Node |
|---|---|---|---|
| 1 | `refundStatus == "More than One Tax Ops data found!"` | More than One Tax Ops data found! | `C-30` |
| 2 | `refundStatus == "No status"` AND `isBeforeEfileOpenDate == TRUE` | No Status | `C-11` |
| 3 | `refundStatus == "No status"` AND `isBeforeEfileOpenDate == FALSE` | No Status | `C-12` |
| 4 | `refundStatus == "RT Check Greater than 10 B days"` | RT Check Greater than 10 B days | `C-13` |
| 5 | `refundStatus == "RT Check Less than 10 B days"` | RT Check Less than 10 B days | `C-14` |
| 6 | `refundStatus == "RT DD Greater than 5 B days"` | RT DD Greater than 5 B days | `C-15` |
| 7 | `refundStatus == "RT DD Less than 5 B days"` | RT DD Less than 5 B days | `C-16` |
| 8 | `TaxReturnStatus in ["09-05","09-06","09-15","09-16"]` AND `ns2_Source == "efile_Retail"` AND e-file date between January and October | Accepted (Bank / Refund Transfer Client) | `C-17` |
| 9 | `TaxReturnStatus in ["09-05","09-06","09-15","09-16"]` AND `ns2_Source == "efile_Retail"` AND e-file date **not** between January and October | Accepted (Bank / Refund Transfer Client) | `C-18` |
| 10 | `TaxReturnStatus in ["09-05","09-06","09-15","09-16"]` AND `ns2_Source != "efile_Retail"` | Accepted (source label says *Bank-Refund Transfer Client* — ⚠️ suspected copy/paste label; verify) | `C-19` |
| 11 | `TaxReturnStatus == "12-00"` OR `TaxReturnStatus == "12-02"` | Accepted (Non-Bank Client) | `C-20` |
| 12 | `TaxReturnStatus == "12-09"` | Accepted (Non-Bank Client) → Emerald Card self-service transfer offer | `C-21` |
| 13 | `TaxReturnStatus in ["13-00","13-02","14-00"]` | TRANSFER | `C-28` |
| 14 | `TaxReturnStatus in ["08-00","08-02","08-04","08-06","08-07"]` AND `ns2_Source == "efile_Retail"` | Rejected Retail | `C-22` |
| 15 | `TaxReturnStatus in ["08-00","08-02","08-04","08-06","08-07"]` AND `ns2_Source != "efile_Retail"` AND `digitalOnlineOrSoftware == "SOFTWARE"` | Rejected Digital Software | `C-23` |
| 16 | `TaxReturnStatus in ["08-00","08-02","08-04","08-06","08-07"]` AND `ns2_Source != "efile_Retail"` AND `digitalOnlineOrSoftware == "ONLINE"` | Rejected Digital Online | `C-24` |
| 17 | `TaxReturnStatus == "01-05"` AND `isMoreThan2WorkingDays(taxPrepDate) == false` | Pending Less than 48 hours | `C-25` |
| 18 | `TaxReturnStatus == "01-05"` AND `isMoreThan2WorkingDays(taxPrepDate) == true` AND `ns2_Source == "efile_Retail"` | TRANSFER | `C-26` |
| 19 | `TaxReturnStatus == "01-13"` AND `ns2_Source == "efile_Retail"` | TRANSFER | `C-27` |

**API fields to check (from TaxOps — `WIM$_Refund Status Logic.xlsx`):**
`ReturnReceivedIRSACKCount` · `ReturnReceivedIRSACKDate` · `SSN` · `DOB` · `FilingYear` · `ns2_Source` · `digitalOnlineOrSoftware` · `depositEntity_count` / `DepositEntity_count` · `CheckEntity_count` · `FlipToCheck` · `DisbursementTypeRequested` · `disbursementAmount` · `rejectCode` · `taxPrepDate` · `eFileDate` · `depositDate` · `irsEfileOpenDate` · `returnReceivedIRSACKDate` · `federalRefundDue` · `checkPrintedDate` · `checkTenPrintedDate` · `fiveDaysDepositDate`
Sample payload fields: `<v21:SSN>453301197</v21:SSN>` · `<v21:DOB>1990-10-10</v21:DOB>` · `<v21:FilingYear>2026</v21:FilingYear>` · `<ReturnReceivedIRSACKCount>1</ReturnReceivedIRSACKCount>` · `<ReturnReceivedIRSACKDate>09/02/26 02:31</ReturnReceivedIRSACKDate>`
Endpoints: `WIM$_Refund` → moving to new `TaxReturnStatus` API in ~2 months; `ns2_Source` · `Endpoint = digitalOnlineOrSoftware`

### 3.5 Reject-code → IRS verbiage mapping

| Reject code | Verbiage |
|---|---|
| `IND-031-01` | According to the |
| `IND-181-01` | According to the |
| `R0000-504-01` | According to the |
| `IND-515` | The IRS has already |
| `F1040EZ-510` | The IRS has already |
| `FW2-502` | According to the |
| `F1040EZ-524-01` | According to the |
| `R0000-500-01` | Your return was |
| `IND-507` | The IRS has already |
| `IND-163` | Since you have had |
| `IND-116-01` | Review the date of |
| `F1040-164-01` | Please review your |

> ⚠️ The source table holds only the **opening words** of each verbiage string. Full strings must be supplied from `refundStatusWithDialog.docx` before build.

### 3.6 Design notes / decisions (verbatim intent)
1. **9.18.26 confirmation:** the TaxOps API response supports **Current Year only** (tax year = current/filing year − 1). Phase 2 opportunity: **5-year look-back** if API is available.
2. **9.10.26 decision:** the TaxOps response includes both federal and state data. The IVA must **present federal information first**, then **offer** state status when available — do not read state information to everyone automatically (not every state requires a state return).
3. **DEV:** do **not store PII**; redact/mask full SSN from the transcript.
4. **DEV:** remove the word *"Next"* from the prompt on the **second loop** of the input question.
5. **DEV:** build logic to convert `'Current Year'` / `'Prior Year'` inputs to a numeric year for the API request; valid range = Current Year − 1 tax years.
6. **Open design question (verbatim):** *"Do we need to ask if they are wanting their tax return status or refund status? OR Does it go.. read out return status, federal refund status, then state refund status?"* — ⚠️ unresolved.
7. Action item — HRB to determine **Live Agent Queue/Skill Routing** for tax-return requests, with applicable **DNIS-based routing**.
8. Provide designated approver(s); on sign-off the design transitions to build.
9. Reference: `HRB_IVA_NLU Intent Reject Codes - ...xlsx`; `refundStatusWithDialog.docx`; screen-pop fields to pass on transfer = `UCID`, `Customer Status`, `Intent: Check Refund Status`, `IVR Call Summary`.
10. Observed real call volumes noted in the diagram: `1-800-799-5841 → 970 calls / last 90 days`; `1-855-211-5328 → 9 calls / last 90 days`; source comment: *"so sounds like 1-800-799-5841 should be the main one used for Admin Hold routing."*

---

## 4. Flow 3 — REQUEST LIVE AGENT (deterministic)
**Source:** `HRB Future IVA Experience - Request Live Agent.pdf` · **Status:** READY FOR HRB APPROVAL
**Entry:** From Head of Call; **from ANY flow** when the caller says "agent" (or a recognised synonym) **or presses 0**.

### 4.1 Flow spine
```
[From Head of Call] ──┐
[From ANY flow  ] ────┴─► LA-01 Live Agent Request > 1?
                              ├─ FALSE → FM Live Agent Request MAX Attempts = FALSE → LA-03
                              └─ TRUE  → FM Live Agent Request MAX Attempts = TRUE  → LA-03
   LA-03 "I understand you would like to speak to someone."
   LA-04 During business hours? ── TRUE ──► FM OfficeOpen=TRUE  → LA-10 Agent Transfer → LA-20 wrap-up
                                └─ FALSE ─► FM OfficeOpen=FALSE → LA-11 Office Closed → Goodbye → Disconnect
   LA-05 (soft-refusal branch) "However, I can help with many of the same questions…" → To Head of Call (G)
   LA-30 Additional Help → (1) New Intent (G) | (2) Goodbye → Disconnect
```

### 4.2 States
| ID | Type | SAY / DO | Input | → Next |
|---|---|---|---|---|
| `LA-01` | SPF | `Screen Pop Field Intent = Request Live Agent` (set on entry) | — | `LA-02` |
| `LA-02` | Check | **Live Agent Request > 1?** | — | TRUE → `FM Live Agent Request MAX Attempts = TRUE` → `LA-03` · FALSE → `FM Live Agent Request MAX Attempts = FALSE` → `LA-03` |
| `LA-03` | Prompt | **HRB_LiveAgent Confirmation** — "I understand you would like to speak to someone." | — | `LA-04` |
| `LA-04` | Check | **During business hours?** | — | TRUE → `FM OfficeOpen = TRUE` → `LA-10` · FALSE → `FM OfficeOpen = FALSE` → `LA-11` |
| `LA-05` | Prompt | **HRB_LiveAgentAvailable** — "However, I can help with many of the same questions and tasks, and often faster. Tell me more about what you're trying to do today." | SPEECH | Pass utterance to **NLU Intent Engine** → **To Head of Call (Entry Point G)** |
| `LA-05a` | Error | **HRB_No Response** — "I didn't hear anything…" → `FM LiveAgentAvailable No Input` → 1st attempt → `LA-06` | — | `LA-06` |
| `LA-06` | Check | **Attempts > 1?** | — | TRUE → `LA-07` · FALSE → `LA-05a` loop |
| `LA-07` | Prompt | **HRB_LiveAgentNotAvailable2** — "I can help with many of the same questions and tasks, and often faster. Tell me more about what you're trying to do today." | SPEECH | `LA-07a` |
| `LA-07a` | Error | **HRB_No Response** — "I didn't hear anything…" → `FM LiveAgentNotAvailable2 No Input` → `LA-08` | — | `LA-08` |
| `LA-08` | Check | **Attempts > 1?** | — | TRUE → `LA-09` · FALSE → `LA-07a` loop |
| `LA-09` | SPF | `Screen Pop Field Intent = Request Live Agent` (re-affirm) → `LA-10` | — | `LA-10` |
| `LA-10` | Prompt | **HRB_AgentTransfer** — "Let's connect you with someone who can help." | — | `FM Agent Transfer = TRUE` → `LA-10a` |
| `LA-10a` | Transfer | **SPF to pass:** `UCID` · `Customer Status` · `Intent` · `IVR Call Summary` (generated from Call Transcript / Flow Milestones / Screen Pop Fields) → **ROUTE TO** `Skill/Queue Number` · `Skill/Queue Name` · `Agent Tier` (⚠️ OPEN) → `LA-30` |
| `LA-11` | Prompt | **HRB_OfficeClosed** — "To get help from one of our H&R Block Specialists, please call back Monday through Friday from [7 AM to 10 PM] and weekends from [7 AM to 8 PM] central." | — | `LA-12` |
| `LA-12` | Prompt | **HRB_Goodbye** — "Thanks for choosing H&R Block. Have a great day." | — | **DISCONNECT** |
| `LA-13` | Prompt | **HRB_LiveAgentNotAvailable1** — "However, our office is currently closed." | — | `LA-04` (re-evaluate hours) |
| `LA-14` | Prompt | **HRB_Invalid Input 2** — "I still didn't get that." → `FM IntentNoMatch` → `SPF Intent = Live Agent` → `LA-10` (transfer) | — | `LA-10` |
| `LA-30` | Prompt | **HRB_Additional Help** — "Is there anything else I can help with today?" | EITHER | `1` Yes / Other Utterance → `FM New Intent = TRUE` → **To Head of Call (Entry Point G)** · `2` No / Timeout / Invalid `(Repeat 1x, No Selection 5 sec)` → `FM New Intent = FALSE`, `FM Call Contained = TRUE` → `LA-31` |
| `LA-31` | Prompt | **HRB_Goodbye** — "Thanks for choosing H&R Block. Have a great day." | — | **DISCONNECT** |

### 4.3 Open items (⚠️ verbatim from source)
1. HRB to define the **error routing path** (appropriate skill/queue/agent tier) when the customer's intent is **unknown**.
2. Provide **DNIS routing documentation / requirements**.
3. Define the **error routing path** when the customer's intent is `'Request Live Agent'`.
4. HRB to **provide/confirm HOOPS** to be dynamic.
5. HRB to determine the **Live Agent Queue/Skill Routing** for live-agent requests, with applicable DNIS-based routing.

---

## 5. Flow 4 — LEAVE A MESSAGE (deterministic)
**Source:** `HRB Future IVA Experience - Leave a Message.pdf` · **Status:** READY FOR HRB APPROVAL

### 5.1 At a glance
| Property | Value |
|---|---|
| Entry | **From Head of Call** (Intent = Leave a Message) · **From Speak To Tax Pro Call Flow** · **From Speak To Tax Pro By Name** · **Rollover** (caller dialled a field office that didn't answer) |
| Lanes | Proactive Recipient Identification → Callback Number Capture → Leave Message → Message Storage & Routing → Office Identification → Tax Pro Identification → Error Handling |
| Outputs | `VMRecipient` (`Tax Professional` \| `Office` \| `Field Office`) · `Callback Number` · `Office ID` · `TP Name` · recorded message + transcription |
| Exits | `EXIT-NEWINTENT` (G), `EXIT-TRANSFER`, `EXIT-SELF-SERVICE-INCOMPLETE`, `EXIT-DISCONNECT` |

### 5.2 States
| ID | Type | SAY / DO | Input | Valid | → Next |
|---|---|---|---|---|---|
| `LM-01` | SPF | `Screen Pop Field Intent = Leave a Message` | — | — | `LM-02` |
| `LM-02` | Check | **Tax Pro explicitly requested by name?** | — | — | TRUE → `FM VMRecipient = Tax Professional` → `LM-03` · FALSE → `LM-10` (rollover: office dialed didn't answer → `A`) |
| `LM-03` | Check | **Tax Pro associated with an upcoming appointment?** | — | — | TRUE → `LM-04` · FALSE → `C` (→ office identification path) |
| `LM-04` | Prompt | **HRB_ConfirmCallback** — "If we need to reach out, is **[###-###-####]** the best number to call you back at?" | EITHER | `1` Yes / `2` No | Yes → `FM Callback Number Identified = TRUE` → `LM-06` · No → `HRB_CallbackNumber` "No problem. All right." → `LM-05` · 1st fail → `HRB_Invalid Input 1`/`HRB_No Input 1` · 2nd → `FM ConfirmCallback No Input/Not Match 2` → `E` |
| `LM-05` | Prompt | **HRB_CallbackNumber** — "What phone number would you like us to use instead?" | EITHER | `###-###-####` | valid → `FM Callback Number Identified = TRUE` → `LM-06` · 1st fail → `HRB_Invalid Input 1`/`HRB_No Input 1` · 2nd → `FM CallbackNumber No Input/No Match 2` → `E` |
| `LM-06` | Check | **Existing customer-to-Tax Pro relationship?** | — | — | TRUE → `LM-07` · (No)/FALSE → `FM VMRecipient = Office` → `B` (office identification) |
| `LM-07` | Prompt | **HRB_VMOfficeLocation (TP variant)** — "Would you like to leave a message with **[TP Name]**?" | EITHER | `1` Yes / `2` No | Yes → `FM VMRecipient = Tax Professional`, `Screen Pop Field TP Name: dynamic` → `LM-30` (record) · No → `B` · 1st fail → `HRB_Invalid Input 1`/`HRB_No Input 1` · 2nd → `FM LeaveOfficeMessage No Input/Not Match 2` → `E` |
| `LM-10` | Check | **Office identified from DNIS?** | — | — | TRUE → `Screen Pop Field Office ID: dynamic` → `LM-11` · FALSE → `LM-20` |
| `LM-11` | SPF | `FM VMRecipient = Field Office`, `Office ID: dynamic` → `LM-12` | — | — | `LM-12` |
| `LM-12` | Check | **Office ID identified?** | — | — | TRUE → `FM VMRecipient = Field Office` → `LM-30` · FALSE → `E` |
| `LM-20` | Prompt | **HRB_OfficeZipSearch** — "Tell me a zip code to search, and I'll help you find an office to leave your message for." | EITHER | zip code | valid → `LM-20a` · 1st fail → `HRB_Invalid Input 1`/`HRB_No Response` · 2nd → `FM OfficeZipSearch No Input/Not Match 2` → `LM-21` (`HRB_OfficeZipSearchFailure`) |
| `LM-20a` | API CALL | **OfficebyZipCode** — `Input: Zip code` → `Output: 3 Nearest Office Locations` | — | — | Success → `FM OfficebyZipCode API Successful = TRUE` → `LM-21` · Failure → `FM … = FALSE` → `LM-25` |
| `LM-21` | Prompt | **HRB_OfficeZipConfirmation** — "I heard **#####**. Is that correct?" | EITHER | Yes / No | Yes → `LM-22` · No → `LM-20` · 1st fail → `HRB_Invalid Input 1`/`HRB_No Response` · 2nd → `FM OfficeZipConfirmation No Input/Not Match 2` → `LM-25` |
| `LM-22` | Prompt | **HRB_OfficeLocations** — "I found three H&R Block offices near that zip code. Which office would you like to leave a message for? For the office on **[StreetName] in [City], [State]**, say *first* or press 1. … say *second* or press 2. … say *third* or press 3. If you'd like to search using a different ZIP code, say *new search* or press 4." | EITHER | `1` First / `2` Second / `3` Third / `4` New Search | `1/2/3` → `FM OfficeLocation1` → `Screen Pop Field Office ID: dynamic` → `LM-30` · `4` → `FM NewOfficeSearch = TRUE` → `B` (→ `LM-20`) · 1st fail → `HRB_Invalid Input 1`/`HRB_No Response` · 2nd → `FM OfficeLocation1 No Input/Not Match 2` → `LM-30`/`E` |
| `LM-23` | Prompt | **HRB_Invalid Input 2** — "I still didn't get that." (per input leg) | — | — | `E` |
| `LM-25` | Prompt | **HRB_APIFailure** — "I seem to be having trouble locating an office to route your message to at this time." | — | — | `FM Leave a Message Self-Service Incomplete` → `E` |
| `LM-26` | Prompt | **HRB_OfficeZipSearchFailure** — "Without a valid zip code I am unable to leave a message." | — | — | `FM Leave a Message Self-Service Incomplete` → `E` |
| `LM-27` | Prompt | **HRB_APIFailure (no office)** — "Without an office selected I am unable to leave a message." | — | — | `FM Leave a Message Self-Service Incomplete` → `E` |
| `LM-28` | Prompt | **HRB_TPNameFailure** — "I seem to be having trouble finding a tax professional by that name." | — | — | `FM Leave a Message Self-Service Incomplete` → `E` |
| `LM-30` | Prompt | **HRB_VMStart** — "Your message can be up to **60 seconds**. For security purposes, don't provide social security numbers or dates of birth. Please start your message **after the tone**. When you're finished, you can simply hang up." | SPEECH (record) | — | `LM-31` |
| `LM-31` | Action | **Record message** — play audible tone at start of recording; **recording limit 90 seconds**; **transcribe** the message; **store recording + transcription within Dataverse** | — | — | `LM-32` |
| `LM-32` | API CALL | **Transmit → WC Leave Message API** | — | — | Success → `FM WC Leave Message API Successful = TRUE` → `LM-40` · Failure → `LM-33` |
| `LM-33` | Check | **Attempts > 1?** (`FM WC Leave Message API MAX Attempts = FALSE/TRUE`) | — | — | TRUE → `FM Leave a Message Self-Service Incomplete` → `E` · FALSE → `LM-32` (retry once) |
| `LM-40` | Prompt | **HRB_Additonal Help** — "Is there anything else I can help with today?" | EITHER | `1` Yes / Other Utterance · `2` No | Yes/Other → `FM New Intent = TRUE` → **To Head of Call (Entry Point G)** · No → `FM New Intent = FALSE`, `FM Call Contained = TRUE` → `LM-41` |
| `LM-41` | Prompt | **HRB_Goodbye** — "Thanks for choosing H&R Block. Have a great day." | — | — | **DISCONNECT** |
| `LM-50` | Transfer | `HRB_AgentTransfer` — "Let's connect you with someone who can help." / `HRB_OfficeClosed` — "To get help from one of our H&R Block Specialists, please call back Monday through Friday from [7 AM to 10 PM] and weekends from [7 AM to 8 PM] central." then `FM Agent Transfer = TRUE` → SPF to pass: `UCID · Customer Status · Intent: Leave a Message · TP Name/ID · Office ID · IVR Call Summary` → **ROUTE TO** Skill/Queue (⚠️ OPEN) | — | — | `LA-30` pattern / DISCONNECT |

### 5.3 Tax Pro identification (Input: Tax Pro **Name** → Output: Office ID)
| ID | Type | Action | → Next |
|---|---|---|---|
| `LM-60` | Check | **Known Data Field? [TP Employee ID]** | TRUE → `LM-61` · FALSE → `LM-62` |
| `LM-61` | API CALL | **EDS_Associate** — `Endpoint: https://blockapi.hrblock.com/edp/eods/Associate` (input: HRB Employee ID, from the caller's existing tax-pro relationship) | Success → `FM EDS_Associate API Successful = TRUE`, `Office ID: dynamic` → `LM-30` · Failure → `FM … = FALSE` → `LM-28`/`E` |
| `LM-62` | API CALL | **Office Search by tax-pro name** — `Output: Office ID` | Success → `FM TP Name Search API Successful = TRUE`, `Office ID: dynamic` → `LM-30` · Failure → `LM-28` |

**DEV NOTE:** the TP-Name path is only applicable if the **TP Name was identified and passed from a previous flow and/or utterance**.

### 5.4 Open items (⚠️ verbatim from source)
1. **Rollover use case** — when a caller dials a field office and the call is not answered, the call may roll over to the IVA. In that scenario the system already knows the specific office the caller originally attempted to reach, which can personalise the experience and support routing decisions. **Open question: clarify whether rollover calls enter through the standard IVA Head of Call flow or through a separate entry point, and provide entry path documentation.**
2. **HRB to define the Office Lookup functionality** — verify whether an API can match a requested tax-pro name to the caller's office and determine whether it returns the relevant office assignment. The current `EDS_Associate` API allows lookup **using employee ID only**.
3. **HRB to provide Existing Tax Pro Data** — identify the EDS/API field containing a caller's existing tax-pro relationship; provide the data field as a customer-to-Tax-Pro relationship + Employee ID to run `EDS_Associate` to determine `Office ID`.
4. **Shared action item:** TTEC Dev team and H&R Block to conduct a follow-up session on **Work Center integration** to review current functionality and confirm API requirements.
5. **HRB to determine Live Agent Queue/Skill Routing** for live-agent requests with applicable DNIS-based routing.
6. **HRB to provide/confirm HOOPS** (dynamic).
7. Provide designated approver(s) for the IVA design.

---

## 6. Flow 5 — VOC SURVEY (deterministic)
**Source:** `HRB Future IVA Experience - VOC Survey.pdf` · **Status:** READY FOR HRB APPROVAL
**Entry:** From Head of Call (post-call wrap-up offer).
**References:** `HRB - VOC Survey Requirements.docx` · `VOC Questions.xlsx`

### 6.1 Flow spine
```
[Head of Call] ─► V-01 Survey offer ("2 brief questions")
                    ├─ 1 Yes → FM Survey Accepted = TRUE  → V-10 Q1 → V-20 Q2 → V-30 End → Disconnect
                    └─ 2 No  → FM Survey Accepted = FALSE → HRB_Okay "Okay" → V-30 End
   Error legs at each input: Invalid → HRB_Invalid Input 1 ; No Input → HRB_No Input 1
     1st failure → FM <node> No Input/Not Match 1 → Check Attempts > 1?
     2nd failure → FM <node> No Input/Not Match 2 → HRB_Error Okay "I still didn't get that, but that's okay." → continue
```

### 6.2 States
| ID | Type | SAY / DO | Input | Valid | → Next |
|---|---|---|---|---|---|
| `V-01` | Prompt | **HRB_SurveyOffer** — "To help us improve would you be willing to answer **2 brief questions** about your experience on this call?" | EITHER | `1` Yes / `2` No | Yes → `FM Survey Accepted = TRUE` → `V-10` · No → `FM Survey Accepted = FALSE` → `V-02` |
| `V-02` | Prompt | **HRB_Okay** — "Okay" | — | — | `V-30` |
| `V-03` | Error | **HRB_Invalid Input 1** — "I didn't get that…" → `FM Survey Offer No Input/Not Match 1` | — | — | `V-04` |
| `V-04` | Error | **HRB_No Input 1** — "I didn't hear anything…" → `FM Survey Offer No Input/Not Match 1` | — | — | `V-05` |
| `V-05` | Check | **Attempts > 1?** | — | — | FALSE → `V-01` (replay offer) · TRUE → `FM Survey Offer No Input/Not Match 2` → `V-06` |
| `V-06` | Prompt | **HRB_Error Okay** — "I still didn't get that, but that's okay." | — | — | `V-30` (skip survey, close) |
| `V-10` | Prompt | **HRB_SurveyQ1** — "Press a number between **one and 5** with one meaning *disagree* and 5 meaning *agree*. **1st question**, H&R Block made it easy for me to handle my issue." | EITHER | `1`–`5` | valid → `V-20` · Invalid → `V-11` · No Input → `V-12` |
| `V-11` | Error | **HRB_Invalid Input 1** — "I didn't get that…" → `FM Survey Q1 No Input/Not Match 1` | — | — | `V-13` |
| `V-12` | Error | **HRB_No Input 1** — "I didn't hear anything…" → `FM Survey Q1 No Input/Not Match 1`, `1st Attempt - No Input` | — | — | `V-13` |
| `V-13` | Check | **Attempts > 1?** | — | — | FALSE → `V-10` (replay Q1) · TRUE → `FM Survey Q1 No Input/Not Match 2` → `V-14` |
| `V-14` | Prompt | **HRB_Error Okay** — "I still didn't get that, but that's okay." | — | — | `V-20` (continue to Q2) |
| `V-20` | Prompt | **HRB_SurveyQ2** — "**Second question…** My issue was resolved completely." (same 1–5 scale as Q1) | EITHER | `1`–`5` | valid → `V-30` · Invalid → `V-21` · No Input → `V-22` |
| `V-21` | Error | **HRB_Invalid Input 1** — "I didn't get that…" → `FM Survey Q2 No Input/Not Match 1` | — | — | `V-23` |
| `V-22` | Error | **HRB_No Input 1** — "I didn't hear anything…" → `FM Survey Q2 No Input/Not Match 1` | — | — | `V-23` |
| `V-23` | Check | **Attempts > 1?** | — | — | FALSE → `V-20` (replay Q2) · TRUE → `FM Survey Q2 No Input/Not Match 2` → `V-24` |
| `V-24` | Prompt | **HRB_Error Okay** — "I still didn't get that, but that's okay." | — | — | `V-30` |
| `V-30` | Prompt | **HRB_SurveyEnd** — "We appreciate your feedback. Thanks for choosing H&R Block. Have a great day." | — | — | **DISCONNECT** |

### 6.3 Notes
- Two questions only (Q1 = *"H&R Block made it easy for me to handle my issue"*, Q2 = *"My issue was resolved completely"*), 1–5 disagree→agree scale, DTMF or spoken digit.
- The survey never blocks the call: a failure at any question still advances (HRB_Error Okay) and the survey closes with the standard thank-you.
- ⚠️ OPEN: the diagram's `Timeout/ Invalid` handling for the 1–5 scale is not drawn; §0.3's universal policy applies unless HRB specifies otherwise.

---

## 7. Master open-items register (everything unresolved across the five diagrams)

| # | Flow | Open item | Owner |
|---|---|---|---|
| O1 | All | Finalise the **live-agent routing matrix**: destination queue + required agent skills for (a) intent unknown, (b) each intent in intent treatment, (c) Check Refund Status + error entering lookup details, (d) Check Refund Status + API needed, (e) Check Refund Status + no response | HRB |
| O2 | All | Define the **error routing path** (appropriate skill/queue/agent tier) when the customer's intent is unknown | HRB |
| O3 | All | Provide **DNIS routing documentation / requirements** | HRB |
| O4 | All | Provide/confirm **HOOPS** so hours verbiage is dynamic | HRB |
| O5 | All | Provide the designated **approver(s)** for the IVA design; then transition to build | HRB |
| O6 | Check Refund Status | Read out **tax return status, federal refund status, then state refund status** — or explicitly ask which the caller wants? | HRB design |
| O7 | Check Refund Status | Supply the **full reject-code verbiage strings** (source holds opening words only) | HRB (`refundStatusWithDialog.docx`) |
| O8 | Check Refund Status | Destination of "**transfer to automated enrollment system**" (text-message alerts) and of the **Emerald Services** / **digital-software support** transfers | HRB |
| O9 | Check Refund Status | `HRB_Rejected Digital Online` → `ZERO_IDM_MATCHES` **subflow** is undefined | HRB |
| O10 | Check Refund Status | Verify the **`HRB_Accepted-NotBankClient` status label** ("Bank-Refund Transfer Client") — suspected copy/paste in the source | HRB |
| O11 | Check Refund Status | Phase 2: **5-year look-back** if the API becomes available | HRB |
| O12 | Head of Call | Confirm, per identity path, whether the caller is **identified only** or **authenticated** (ANI+name, alternate phone+name, SSN last-4, SSN last-4+DOB) | HRB |
| O13 | Head of Call | Is the **CCO Context API** called as the first step of the flow, before the caller hears anything? | HRB (Michael Vo) |
| O14 | Head of Call | Phase 2: **proactive missed / cancelled / no-show appointment** handling | HRB |
| O15 | Leave a Message | **Rollover entry path**: standard Head of Call vs. separate entry point (+ documentation) | HRB |
| O16 | Leave a Message | Confirm whether an API can match a **tax-pro name → office**; `EDS_Associate` currently works by **employee ID only** | HRB |
| O17 | Leave a Message | Provide the **existing tax-pro data field** (customer-to-Tax-Pro relationship + Employee ID) | HRB |
| O18 | Leave a Message | TTEC Dev + HRB follow-up session on **Work Center integration** / API requirements | TTEC + HRB |
| O19 | VOC Survey | Confirm timeout/invalid handling for the 1–5 scale | HRB |
| O20 | Request Live Agent | Deferred/inferred edges (`LA-05` soft-refusal branch trigger, `LA-13` re-evaluation) are not explicitly wired in the drawing — confirm | HRB/TTEC |

---

## 8. Appendix — how an agent should consume this spec

1. **Parse each state table row as a node**: `ID` → `type` → `utterance` → `input spec` → `transition map`.
2. **Determinism contract**: a node is only left via an edge listed in its row. Never generate a new utterance, never skip a milestone, never merge two states.
3. **Retry contract**: apply §0.3 mechanically — `1st` re-prompt, `2nd` → error hub `E`. Milestones `…No Input/Not Match 1` and `…2` must both be emitted.
4. **Data contract**: `${variables}` come only from (a) API responses listed in the flow's API section, (b) screen-pop fields, (c) capture nodes. If a variable is missing, take the documented failure node — do not substitute sample values.
5. **Escalation contract**: from **any** node, the global rule (utterance "agent"/synonym or DTMF `0`) jumps to §4 Request Live Agent. Connector `G` jumps to Head of Call Intent Capture.
6. **Reporting contract**: emit every `FM`; pass every `SPF` at transfer. `IVR Call Summary` is generated from Call Transcript + Flow Milestones + Screen Pop Fields.
7. **Do not implement** any node or edge flagged `⚠️ OPEN` — surface it as a blocking question first.

### Per-flow machine-readable summary (node counts)

| Flow | Nodes specified | Deterministic? |
|---|---|---|
| Head of Call | 45+ (CE/ID/PA/IC/IT/EH) | Partly — intent capture delegates to the NLU engine |
| Check Refund Status | 45 | Yes (API-driven) |
| Request Live Agent | 17 | Yes (branch-wise) |
| Leave a Message | 30+ | Yes (API-driven) |
| VOC Survey | 17 | Yes |

---

*Transcribed from the five H&R Block "Future IVA Experience" Lucid flow PDFs. Verbatim prompt strings, API field names, milestone names, and design/dev notes are reproduced as they appear in the source. Items the source leaves undecided are marked `⚠️ OPEN` and listed in §7 rather than inferred.*
