L-036 | fix-needed | send_secure_link now takes newCustomer "as in book_appointment", but scheduler_never still says only book_appointment may create the new-customer profile; whether the DDO send creates a profile is undecided and needs a question. The key format interactionId-ddo-1/-ddo-2 is a necessary completion of D-001 and is acceptable
L-037 | pass
L-038 | pass
L-039 | pass
L-040 | pass
L-041 | pass
L-042 | pass
L-043 | fix-needed | context_envelope gains only appointmentType, so the taxProRef and officeRef carried on route_intent have no entry field in §1.1 or context_envelope; the callback ladder's "carried Tax Pro" has no source, and D-004 does not settle this, so it needs a question
L-044 | pass
L-045 | pass
L-046 | pass
L-047 | fix-needed | New contract default "intent is the current agent's intent" is ambiguous in Part 3, which has two intents (office_info, office_contact), for global outcomes such as system_failure or clarification_exhausted. Fill those values or name the rule for Part 3
L-048 | pass
L-049 | pass
L-050 | pass
L-051 | pass
L-052 | pass
L-053 | pass
L-054 | pass
L-055 | pass
L-056 | fix-needed | "Named Office" requires a ZIP for any caller-named office with no exception for the routed office, while dialogues 3A and 3B answer a caller-named office with no ZIP turn (C-9). Either scope the rule to an office other than the routed office or fix the dialogues
L-057 | pass
L-058 | pass
L-059 | fix-needed | The tax_prep follow-up now returns route_intent after committing the extension, but no finalOutcome is named. intent_changed no longer fits because the follow-up is inside the agent's scope, and new_appointment_scheduled fixes nextAction offer_additional_help; needs a question
L-060 | pass
L-061 | pass
L-062 | pass
L-063 | fix-needed | Agents may now send only appointments_and_logistics or tax_prep_and_records, but scheduler_never ("Answer from search_knowledge_base" for loan, fee, penalty questions) and §1.2 Tax/Financial Boundary still send financial_products-type questions to search_knowledge_base with no handback target
L-064 | pass
L-065 | pass
L-066 | pass
L-067 | pass
L-068 | pass
L-033 | pass
lint | RESULT WARN (new: dup_mirror L437/L731 callback ladder prose-JSON mirror, allowed under C-2 A; L494 and L809 are line-shift artifacts of untouched text; length transfer_unavailable 96w grew but was already in backlog L-034; objective 68w, down from 69; web_deflection L955/L987 "Online Message Center" allowed by D-006)
L-047 (re-check) | pass | Default is now "the intent the agent is serving", which is office_info or office_contact per the path in progress in Part 3; there is no longer a two-intent ambiguity and the other defaults are unchanged
L-056 (re-check) | pass | Prose and JSON both scope the ZIP match to an office other than the routedOfficeRef office, so dialogues 3A and 3B read as routed-office calls with no ZIP turn; triggers and tool steps are unchanged
lint (re-check) | RESULT WARN (same new warnings as before; none from the follow-ups)
