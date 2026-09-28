# Round 6 · Carried Human items re-check

Saved by the orchestrator from the reviewer's reply. Items L-074 to L-192 still open from rounds 1-3, checked against the current text.

| L-ID | verdict | note |
|---|---|---|
| L-074 | human | Trade-off asked at a third point (partial_acceptance) beyond the prose's "only at these two points". Carried to round 7. |
| L-075 | human | efile item applies the trade-off with no prior Tax Pro, so [Name] is empty. Carried to round 7. |
| L-077 | low | Covered by single-payload, one-transaction, and post-commit rules. Backlog. |
| L-078 | stale | Settled by D-044 (routed office is the one referent). Fixed. |
| L-079 | low | Backlog. |
| L-080 | human | Frozen §1.4 off-season line vs Part 3 address answer. Carried to round 7. |
| L-081 | human | Asked in round 6 with L-370. |
| L-084 | human | Asked in round 6 (first-party no_match in Part 4). |
| L-085 | human | Asked in round 6 with L-135. |
| L-089 | human | Five §1.4 lines have no lexicon copy. Carried to round 7. |
| L-090 | human | Asked in round 6 with L-160, L-163. |
| L-091 | low | Backlog. |
| L-111 | safe-now | Applied: State Persistence points to §1.1. |
| L-134 | low | Backlog. |
| L-135 | human | Asked in round 6 with L-085. |
| L-136 | human | Confirm Appointment requests. Carried to round 7. |
| L-140 | human | "Office associate" has two owners. Carried to round 7. |
| L-146 | human | Readiness conflict vs closed windows. Carried to round 7. |
| L-150 | human | Asked in round 6 with L-084. |
| L-160 | human | Asked in round 6. |
| L-161 | low | Backlog. |
| L-162 | human | taxProPreference.source has no enum. Carried to round 7. |
| L-163 | human | Asked in round 6. |
| L-164 | human | New customer's name readback. Carried to round 7. |
| L-192 | safe-now | Applied: §1.4 multiple_matches Path cell scoped to find_customer (the approved line is unchanged). |

## Draft options for the items carried to round 7

- L-074, L-075 · Trade-off points. A. Add partial rejection as a third point in the prose list; efile item "otherwise apply the Tax Pro trade-off" -> "otherwise follow workflow.schedule_new". B. Only the two points; partial_acceptance widens without asking.
- L-080 · Off-season line in Part 3. A. Scope the §1.4 Path to "(Scheduler)". B. Part 3 speaks the frozen line with the address; a yes hands back to appointment_scheduler.
- L-089 · Missing lexicon lines. A. Append the five §1.4 lines to global_voice_lexicon.empathy. B. Not an issue.
- L-136 · Confirm Appointment. A. A confirm request is an appointment-details question (appointment_details_provided). B. Not an issue; Head of Call confirms inline.
- L-140 · Office associate. A. Delete "or office associate" from §4 Generic. B. Replace with "tax associate".
- L-146 · Closed windows. A. A closed window returns conflict; tax_extension offers tax_prep, emerald_advance reprompts for another date. B. Add readiness result window_closed.
- L-162 · Tax Pro source values. A. prior_tax_pro, carried, existing_appointment. B. Delete source and taxProSource.
- L-164 · New customer's name. A. First-party names are never read back (§1.2). B. Read the new customer's name back once after no_match.
