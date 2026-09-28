# Round 04 · Lens F (Editorial) findings

Saved by the orchestrator from the reviewer's reply (write blocked). 25 findings, all Low and Safe, total -431 words. None touches frozen text. F-02 and F-10 were held at triage (L-321, L-320).

### F-01 · Pointer-only "Apply/Follow the ... rules" sentences in Scheduler JSON
Anchor: §2 State 5 agent_specific_tools.find_customer, .find_offices_near, .find_available_slots, .book_appointment; workflow.schedule_new[1], schedule_new[3], reschedule_existing[3]
Proposed fix: delete "Apply the authentication, no-match, and no-full-SSN rules above." (find_customer); "Follow the rollover, central-line, ZIP, rejection, and seasonal-broadening rules." (find_offices_near); "The tool owns ranking and duration and applies the rating floor. Apply the duration, CDAS, and ladder rules." (find_available_slots); "Follow the existing-customer, new-customer, third-party, text-confirmation, and no-full-SSN rules." (book_appointment); "Apply the digital drop-off rules." (schedule_new[1]); "Apply the Tax Pro trade-off and CDAS rules." (schedule_new[3], reschedule_existing[3]). -65w.

### F-02 · Part 5 Conventions: wordy Request, Response, Read-result bullets (held, L-321)
Proposed fix: "**Request:** Carries only what the tool needs, in enterprise-service field names and shapes." / "**Response:** Carries customer-safe values, never raw system records." / "**Read result first:** Every other response field depends on result. Inapplicable fields are omitted, never empty." -39w.

### F-03 · Slot-order and CDAS-filter rule restated in broadening principles
Anchor: §2 State 5 broadening.principles[6]; §2 State 3 Search Broadening Ladder > Principles (last bullet)
Proposed fix: JSON "Present at most MAX_SLOTS_PER_OFFER slots per turn. When the caller rejects named options and asks for more, request the next set." Prose "Present at most three slots per turn, in the order returned. Never filter out CDAS." -29w.

### F-04 · cancel_existing retrieval step duplicates reschedule_existing
Anchor: §2 State 5 workflow.cancel_existing[1]
Proposed fix: "2 Retrieval and binding. Follow reschedule_existing[1], even when the handoff carries a target reference, and never guess." -27w.

### F-05 · Part 4 leave_message workflow split across two steps
Anchor: §4 State 2 workflow.leave_message[0], [1]
Proposed fix: one item, "1. Stop speaking and return nextAction leave_message with any known taxProRef and officeRef." -20w.

### F-06 · tax_notice capture item lists the five values twice
Anchor: §2 State 5 scheduler_always tax_notice_service capture item
Proposed fix: "On tax_notice_service, right after the type and before the office lookup, capture the five notice values in this order and send them in taxNoticeDetails: letterDate, respondByDate, noticeCode, taxYear, and peaceOfMindStatus." -20w.

### F-07 · Chunked readback spells out sentence positions
Anchor: §2 State 5 scheduler_always three-sentence readback item; §2 State 4 The Pre-Commit Gate > Chunked Readback
Proposed fix: JSON "Split a new-booking pre-commit readback into exactly three sentences: the appointment details, the text-destination beat, then the gate question." Prose "**Chunked Readback:** Split a new-booking readback into exactly three sentences: the appointment details, the text-destination beat, then the gate question." -20w.

### F-08 · schedule_new Booking step restates payload rules
Anchor: §2 State 5 workflow.schedule_new[5]
Proposed fix: "6 Booking. Call book_appointment once per confirmed slot with an immutable idempotency key, or send_secure_link for digital drop-off, per agent_specific_tools." -19w.

### F-09 · Silence item restates the consecutive_silence outcome
Anchor: §1.5 global_always no-input item
Proposed fix: "On the first no-input (silence), reprompt once. On the second consecutive silence, return consecutive_silence." -15w.

### F-10 · §1.3 lists the Leave a Message flow's internals (held, L-320)
Proposed fix: "- The deterministic Leave a Message flow owns the rest of the message path, including the offer where still needed." -14w.

### F-11 · Mini-Dialogue 4A System line explains the flow
Anchor: §4 Mini-Dialogues > 4A (last System turn)
Proposed fix: "- **System:** Agent stops speaking and returns terminal payload with nextAction = leave_message, passing taxProRef and officeRef." -14w.

### F-12 · Office-identity item lists every pre-commit phase
Anchor: §2 State 5 scheduler_always office identity item
Proposed fix: "Before commit, including retrieval and every pre-commit readback, identify an office by officeName only; if it is null, empty, or duplicates the spoken address, use addressLine1Spoken. In the post-commit readback and terminal outcome, speak addressLine1Spoken, then addressLine2Spoken only when present and non-empty." -13w.

### F-13 · Changing-array item spells out each comparison
Anchor: §2 State 5 scheduler_always reschedule_appointment changing item
Proposed fix: "For reschedule_appointment, list in changing each of 'date', 'time', 'office' (officeRef), and 'taxPro' (taxProRef) that differs between the new slot and the bound appointment." -13w.

### F-14 · find_customer read-only and status enum stated twice in §5.2
Anchor: §5.2 find_customer (intro; Note)
Proposed fix: Intro "Resolves the subject of the transaction to a single customer profile. Read-only." Note "Note: priorTaxProStatus selects between the returning-client scenarios and is never spoken." -13w.

### F-15 · continuation_context restates the envelope's priorTransaction rules
Anchor: §2 State 5 closure.continuation_context
Proposed fix: delete "It is context only." and "Discard it on a change of customer identity." -12w.

### F-16 · check_office_open_status intro lists tool inputs
Anchor: §5.3 check_office_open_status (intro)
Proposed fix: "Returns whether an office is open at requestedDateTime. Owns all time math." -12w.

### F-17 · Message-ban item ends with an ownership explanation
Anchor: §1.5 global_never message item
Proposed fix: delete "These actions belong only to the deterministic Leave a Message flow." -11w.

### F-18 · §1.5 intro lists the block's contents
Anchor: §1.5 Universal Base JSON Prompt (intro paragraph)
Proposed fix: "Every agent inherits this JSON block and merges its own agent-specific block with it at runtime." -11w.

### F-19 · State 2 duplicate DDO clause and rationale clause
Anchor: §2 State 2 DDO Rules > Rescheduling; Complexity Matching & Tax Pro Rating Floor > Guardrails
Proposed fix: "- **Rescheduling:** Handle a requested change as a new schedule_new DDO send in the Scheduler." and "- **Guardrails:** Never speak or relax the numeric rating (1-5)." -11w.

### F-20 · scheduler_never profile item lists pre-commit phases
Anchor: §2 State 5 scheduler_never profile item
Proposed fix: "Never create a new-customer profile before commit; only book_appointment or send_secure_link may create it. A find_customer no_match creates nothing." -10w.

### F-21 · book_appointment intro softener
Anchor: §5.2 book_appointment (intro)
Proposed fix: "Creates one new appointment." -10w.

### F-22 · Broadening intro restates the one-constraint principle
Anchor: §2 State 3 Search Broadening Ladder (intro paragraph)
Proposed fix: "Each scenario broadens in a fixed order. The caller accepting a slot or method at any step ends the sequence. Accepting Digital Drop-Off runs the DDO path (see Part 2, Digital Drop-Off (DDO) Rules)." -9w.

### F-23 · reschedule Change scope states the type/method bar twice
Anchor: §2 State 5 workflow.reschedule_existing[2]
Proposed fix: "3 Change scope. State the current date and time, use officeName only when office context is needed for disambiguation, establish exactly what changes, and preserve everything else. On a type or method change request, preserve the appointment and call transfer_to_agent with transferReason automation_blocked." -9w.

### F-24 · CDAS item takes two conditionals for one definition
Anchor: §2 State 5 scheduler_always isCDAS item
Proposed fix: "A slot is CDAS when isCDAS is true, or when taxProName is null or empty and appointmentMethod is not physical_drop_off. For a CDAS slot, speak ..." (rest unchanged). -8w.

### F-25 · re_entry restates the one-transaction limit
Anchor: §2 State 5 closure.re_entry
Proposed fix: delete "One invocation commits at most one transaction." -7w.
