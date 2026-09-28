# Round 9 questions

Per your instruction, the orchestrator settled the Human items with educated guesses (D-100 to D-113, applied). Only the items below need you. Blank `Answer:` means keep the guess. Write a letter or text to change it.

### Q-96 · Cross-Office Restriction (resolves L-438)
Conflict: §3 Office Contact Triage > Cross-Office Restriction and the `office_never` phone item allow a phone number "only for the routed office". After D-044 and D-094, any office the caller names becomes the routed office, so the rule cannot fire. Not edited.
Options:
  A. Delete the restriction and the `office_never` item (Recommended if D-044 is intended: about -45 words).
  B. Keep D-044 for hours and status only; the phone number stays limited to the dialed routedOfficeRef office (about +15 words).
  C. Leave both (dead rule).
Footprint: A ≈ 2 edits, -45 words. B ≈ 2 edits, +15 words.
Answer: A

## Guesses to check (applied, provisional)

Least certain first:
- **D-101 (L-431)** Callback handoff officeRef: the Tax Pro's `primaryOfficeId`, or `priorOfficeRef` for the prior Tax Pro. Alternative: `routedOfficeRef`, or no officeRef on a callback.
  Answer: 
- **D-111 (L-443)** `taxProPreference` and `taxProRef` are sent whenever a Tax Pro is bound, with source mapped: caller_stated (caller asks for one), prior_tax_pro (keeps the prior), carried, existing_appointment. Alternative: drop `caller_stated`.
  Answer:
- **D-100 (L-426)** On reschedule, emerald_advance, tax_notice_service, callback, and physical_drop_off keep their fixed floor; the raised baseline applies to the other types. Alternative: the raised baseline on every type except physical_drop_off.
  Answer:
- **D-104 (L-434)** Keep-prior-Tax-Pro question only on tax_prep. Same-day requests still waste one answer (scenario_selection item 6 wins over item 8).
  Answer:
- **D-113 (L-445)** Transfer paths with no §1.4 row speak the agent_available line. Alternative: speak nothing.
  Answer:
- **D-108 (L-440)** Free empathy lines are "the first three" lexicon lines by position.
  Answer:
- Also applied, low risk: D-102, D-103, D-105, D-106, D-107, D-109, D-110, D-112 (see `rounds/round-09/changes.md`).
