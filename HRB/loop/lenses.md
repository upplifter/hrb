# Review lenses

Each reviewer gets one lens. The audit IDs show the kind of issue each lens should catch.

## A - Scope and ownership

Compare each agent's `objective` with its tools, workflows, ladders, and outcomes. Flag any capability with no owner or with two owners. Flag routing targets that resolve to nothing. To check a handoff to a flow outside the spec, read its section in `deterministic_flows/HRB-Future-IVA-Deterministic-Flow-Spec.md`. Audit examples: F-01, F-03, F-08, F-09, F-12, F-16, F-20.

## B - Universal rules vs local overrides

Find agent rules, dialogues, examples, or tool notes that contradict or quietly narrow a Part 1 rule. Audit examples: F-06, F-07, F-10, F-14, F-28.

## C - Contracts and vocabulary

Check the terminal payload contract, outcomes, enums, `nextAction` values, and tool request and response fields. Every value used must be defined, and every defined value must be used. Check that each write has its idempotency key and consent evidence. Flag one term with two meanings, or two terms for one thing. Audit examples: F-01, F-05, F-21, F-26.

## D - Flow and termination

Walk each state machine. Check gates, loops, retries, invalidation, stop conditions, and which tools stay callable after the agent decides to hand back. Audit examples: F-02, F-11, F-24, F-25, F-27.

## E - Prose and JSON parity

Compare each prose rule with its JSON counterpart, its dialogues, and its Part 5 tool entry. Flag any pair that says different things. Partial edits cause most of these. Under constitution C-1 the prose wins, so the fix changes the JSON, and Part 5 changes to serve the agent parts. Current example: §1.2 "Abandonment" says an unanswered gate terminates, while `global_outcomes.customer_abandoned` says it transfers.

## F - Editorial

Apply `loop/style.md`. Start from `rounds/round-NN/lint-before.txt`, then read for what lint misses:

- Verbose text that fewer words can say.
- Walls of text that need splitting into bullets or a table.
- Duplicates in different wording, under the constitution's duplication policy.
- Language that breaks the style guide (hedging, vague quantities, mixed terms).

Every proposal must keep all triggers, limits, and exceptions, and be net-negative or neutral in words. Report at most 25 findings, largest word savings first.

## S - Audit seed (round 1 only, if the constitution allows)

Take each F-ID in `Sample_HRB_IVA_Boundary_Audit.md`. Check its claim against the current spec text, since some have been partly fixed. Report only what is still true, anchored to the current text, and name the F-ID.
