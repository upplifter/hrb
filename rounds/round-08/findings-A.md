# Round 8 · Lens A findings

Saved by the orchestrator from the reviewer's reply.

### A-01 · After Part 4, a request for a third named Tax Pro has no owner
Anchor: §2 State 2 Appointment Type Rules > Tax Pro Requests; After Part 4; scheduler_always routed_to_scheduler item; interruptions.intent_change
Severity: Medium
Class: Human
Issue: Tax Pro Requests hands back a named Tax Pro "neither prior nor carried" to speak_to_tax_pro, "except After Part 4". The JSON handler has the same exception ("except per the scheduler_always routed_to_scheduler item"). After D-081, After Part 4 covers only a callback request and the caller's own or Part 4-named Tax Pro. So when a caller routed from Part 4 names a different Tax Pro, the handback is switched off and nothing replaces it. The implementer has to guess whether to hand back, book, or state the D-081 line.
Fix: Options:
A. (Recommended) Narrow the exception so it covers only the cases After Part 4 lists. A different named Tax Pro still hands back to speak_to_tax_pro. Prose: "except After Part 4" becomes "except as After Part 4 lists". JSON: "except per the scheduler_always routed_to_scheduler item" becomes "except the cases the scheduler_always routed_to_scheduler item lists".
B. Treat any named Tax Pro after Part 4 like the own or Part 4-named one: one statement that this booking is with another Tax Pro, and a second request returns customer_declined_options. Edit both After Part 4 sub-bullets and the JSON item to say "any named Tax Pro".
Footprint: A is 2 edits, about +4 net words. B is 2 edits, about +2 net words, and it changes what the caller hears.

### A-02 · After Part 4, the keep-prior-Tax-Pro question conflicts with D-081
Anchor: workflow.schedule_new[1]; §2 State 2 After Part 4 second sub-bullet; scheduler_always routed_to_scheduler item
Severity: Medium
Class: Human
Issue: schedule_new[1] asks every returning client with an active prior Tax Pro "whether to keep them", and D-050 keeps that question after routed_to_scheduler. D-081 now answers any request for the caller's own Tax Pro after Part 4 with "this booking is with another Tax Pro", and a repeat returns customer_declined_options. A caller who said "another Tax Pro" in Part 4 is then asked whether to keep Sarah. If they say yes, one rule selects returning_same_tax_pro and the other refuses it.
Fix: Options:
A. (Recommended) After a Part 4 routed_to_scheduler, skip the keep-prior question and treat the prior Tax Pro as not kept, which leads to returning_tax_pro_unavailable. Add "; after a Part 4 routed_to_scheduler, skip this question" to schedule_new[1], and add the same clause to the After Part 4 prose bullet.
B. Keep the question and let a yes select returning_same_tax_pro. Scope D-081's statement to the Tax Pro named in Part 4, plus the own Tax Pro only when Part 4 found them unavailable. Edit the After Part 4 sub-bullet and the JSON item.
Footprint: A is 2 edits, about +14 net words, and it partly reverses D-050. B is 2 edits, about +16 net words, and it partly reverses D-081.

Summary: 2 findings (0 Critical, 0 High, 2 Medium, 0 Low).
