# Round 6 decided verification (D-061 to D-072)

Verifier report saved by the orchestrator. Lint: RESULT WARN, no FAIL; round growth +0.91% after follow-ups (limit 1.0%); JSON valid. Frozen text unchanged; the only dialogue edit is the 3D System line (C-9).

L-369 | fix-needed | Part 4 objective dropped "when that one is unavailable"; §4 Fulfillment Priority step 4 names another Tax Pro and "decline every option"; tax_pro_always callback item points to "the tax_pro_always other-booking item" (C-4). Fixed.
L-081, L-370 | fix-needed | §3 Office Contact Triage restores "(with yroOfficeAddressSpoken on closed_for_season)". Fixed.
L-371 | pass
L-372 | pass
L-375 | pass
L-376 | pass
L-377 | pass
L-378 | pass
L-379 | fix-needed | §3 Lookup Failure bullet says "On either path". Fixed.
L-084, L-150 | fix-needed | Pointer changed to "(see §1.4, Approved Recovery Lines)". Fixed.
L-085, L-135 | pass
L-090, L-160, L-163 | fix-needed | §5.2 book_appointment Note adds "appointmentNotes is null except on callback." Fixed.
Offsetting trims (§1.3, closure.line_patterns handoff_unavailable, gate-correction item, outcome defaults, customer_declined_options) | pass

## New items (Human, Medium, open for round 7)
- L-383: After D-061, a Part 4 routed_to_scheduler for another Tax Pro plus a repeat request for the named Tax Pro loops to Part 4; the After Part 4 "they aren't available" line can be false.
- L-384: A Scheduler message request naming no recipient has no rule.
- L-385: Whether a Part 4 callback request booked as tax_prep phone_callback carries the appointmentNotes reason.
