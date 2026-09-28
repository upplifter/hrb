# Spec review loop

This folder runs a review-and-fix loop on `HRB_IVA_Agents_Spec.md`. The round procedure is in `loop/procedure.md`. The review lenses are in `loop/lenses.md`. The rules below bind the orchestrator and every subagent.

## Files

- `HRB_IVA_Agents_Spec.md` is the only file the loop edits for content.
- `Sample_HRB_IVA_Boundary_Audit.md` is calibration material. Its line numbers are stale. Never copy its text into the spec.
- `deterministic_flows/HRB-Future-IVA-Deterministic-Flow-Spec.md` documents the flows outside this spec (Head of Call, Check Refund Status, Request Live Agent, Leave a Message, VOC Survey). Read it only to check the spec's handoff to a flow. Never write a flow's internals into the spec (constitution C-11).
- `loop/style.md` is the writing style for every edit.
- `state/constitution.md` holds standing policy. `state/decisions.md` holds answered questions as binding rules. Both outrank reviewer opinion.
- `state/rejected.md` lists issues the user ruled "not an issue". Never raise them again.
- `state/ledger.md` has one row per finding. `state/backlog.md` holds Low findings and deferred items.
- `rounds/round-NN/` holds each round's findings, changes, verification, lint output, and questions.

## Editorial rules for the spec

1. A bullet is at most 2 sentences and 35 words. A paragraph is at most 3 sentences. A JSON string item is at most 60 words.
2. Each rule lives in one place. Other places point to it. The pointer style is set in the constitution.
3. Change existing text before adding new text. Pair each addition with a deletion where possible.
4. Add no new section, table, example, dialogue, or JSON key without a decision that approves it.
5. Never explain why inside the spec. Reasons go in `changes.md`.
6. Anchor every finding and change to a heading path or JSON key path, for example `§1.5 global_outcomes.customer_abandoned`. Line numbers are hints only.
7. Frozen text (constitution C-8) is never trimmed or restyled. It changes only to follow a rule change (C-9) or under a decision that names it.
8. Keep every JSON block valid. Run `python tools/lint.py check` after every edit batch.
9. Write and rewrite in the style of `loop/style.md`. Trimming verbose existing text is in scope and is a finding in its own right.
10. Digital Drop-Off (DDO) is not a deterministic flow. It is handled inside the spec.

## Triage rules

An issue is **Safe** only when the spec, the constitution, and the decisions log together allow exactly one correct fix. Typical Safe cases:

- A broken reference or key path.
- A duplicate where one copy is canonical under the constitution.
- A contradiction the precedence order settles (constitution C-1). The losing text changes to match the winner.
- An incomplete propagation of a rule that a decision or the spec already settled.
- A dialogue that no longer matches the rules (constitution C-9).
- A trim, split, or rewrite for brevity that keeps every trigger, limit, and exception.

An issue is **Human** when the fix would do any of these:

- Assign or move ownership of a capability between agents or flows.
- Change what the caller hears or experiences.
- Touch PII, IRS 7216, consent, or other compliance behavior.
- Add or remove a capability, outcome, `nextAction`, `routingTarget`, tool, or field.
- Reverse a business choice written into the spec.
- Pick between two readings that are both plausible.

A Human trigger outranks a Safe case. When in doubt, the issue is Human.

## Severity

- **Critical:** a wrong write, a compliance breach, or a caller dead end.
- **High:** two sections require behaviors that cannot both be built, or a contract cannot validate.
- **Medium:** an implementer must guess.
- **Low:** clarity, length, or duplication with no behavior effect.
