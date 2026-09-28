# Round 8 · Lens C findings

Saved by the orchestrator from the reviewer's reply.

### C-01 · book_appointment existing-customer example still sends a phone_callback with no reason
Anchor: §5.2 book_appointment > Request JSON (Existing Customer) `appointmentMethod`; book_appointment Note
Severity: Medium
Class: Safe
Issue: D-083 requires the one-phrase reason on any phone_callback, and the Note now says "appointmentNotes is null except on a phone_callback". The existing-customer example is a tax_prep phone_callback with `appointmentNotes` null, so the example breaks the contract it illustrates. D-072 fixes the example's `appointmentNotes` as null, so the method is the only value that can change. An in-person method also matches the `transfer_to_agent` example for the same slot (`slt-0091`, `meetingMethodChosen` in_person) and the address in the booked `confirmedSummary`.
Fix: Old: "\"appointmentMethod\": \"phone_callback\"," New: "\"appointmentMethod\": \"in_person\","

### C-02 · "empathy" now means both a free acknowledgment and path-bound recovery lines
Anchor: §1.5 global_always (empathy acknowledgment item); global_voice_lexicon.empathy
Severity: Medium
Class: Human
Issue: global_always lets the agent use any `global_voice_lexicon.empathy` line "when the moment calls for it" as a one-clause acknowledgment that adds no facts. After D-076, that list also holds the agent_available, agent_unavailable, Unregistered ANI, and other recovery lines, which promise a person or state facts. An implementer must guess which lines are free acknowledgments. The item as written allows speaking a "let me get you to someone" line before `transfer_to_agent`, which D-014 forbids.
Fix: Options:
A. (Recommended) Edit only the global_always item: "Acknowledge the caller's position in one clause with global_voice_lexicon.empathy items 0 to 2 when the moment calls for it, and add no facts. Speak every other empathy item only on its own path." Footprint: 1 edit, about +14 words, no frozen text touched.
B. Move the path-bound lines out of `empathy` into a new `recovery_lines` lexicon key and repoint the references (the same_day rung, check_search_readiness). Footprint: 1 new JSON key plus frozen-lexicon edits under a decision, about 5 edits, about +5 words net.
C. Leave as is. The path tags inside the strings are the only guard. Footprint: 0.

### C-03 · check_search_readiness points to "the appointment-type item", which is a different item
Anchor: §2 State 5 agent_specific_tools.check_search_readiness
Severity: Low
Class: Safe
Issue: "Follow the appointment-type item" matches the scheduler_always item that begins "Establish the appointment type before the method…", which says nothing about closed windows. D-078 means the emerald_advance and tax_extension items, which hold the closed-window rules.
Fix: Old: "for a closed window, follow the appointment-type item." New: "for a closed window, follow the emerald_advance or tax_extension item."

### C-04 · check_search_readiness reschedule example uses source caller_stated for the bound Tax Pro
Anchor: §5.2 check_search_readiness Request JSON `taxProPreference.source`; Response JSON `resolvedConstraints.taxProSource`
Severity: Low
Class: Safe
Issue: The example is a reschedule_existing request whose time comes from the bound appointment (`requestedTimeSource` existing_appointment). Its Tax Pro `tp-496951` is the bound appointment's Tax Pro, but it is labeled caller_stated. D-079 added existing_appointment for this case, and taxProSource must echo the same value.
Fix: Old: "\"source\": \"caller_stated\"" New: "\"source\": \"existing_appointment\"" ; Old: "\"taxProSource\": \"caller_stated\"," New: "\"taxProSource\": \"existing_appointment\","

Summary: 4 findings (2 Medium, 2 Low).
