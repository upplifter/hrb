# Spec style guide

These rules apply to all new text and to all existing text the loop rewrites. Frozen text (constitution C-8) is excluded.

## Structure

- Structure top-down: `# PART N`, then `## N.N` sections, then `###` subsections. Within each state, rules come first, then examples.
- Write one idea per bullet. A bullet is at most 2 sentences and 35 words.
- Start a bullet with a bold label when it names a concept or trigger (e.g., **Trigger:**, **Action:**).
- Use a table for any mapping (value to rule, path to approved line, type to permitted methods). Never write a mapping as prose.
- Break any wall of text. Split a long bullet into sub-bullets, or turn a list of cases into a table.
- Write examples as short dialogues, one turn per bullet, labeled **Agent:**, **Caller:**, or **System:**. Dialogues show the rules and never add one.
- State each rule once, in the most general place. Point to it elsewhere (constitution C-4).
- Agent JSON holds only what differs from the Base JSON. Group rules into `always`, `never`, `workflow`, `tools`, and `outcomes`.

## Language

- Write in the imperative ("Call X", "Never speak Y"). Never write "should", "the agent will", or "it is recommended".
- Use "may" only to grant permission. Use "never" and "only" for hard limits.
- Start a condition with its trigger ("On slot_taken, re-search." "If officeName is null, fall back to addressLine1Spoken.").
- Quantify exactly ("exactly one", "at most three", "once"). Never write "a few", "some", or "as needed".
- Pair a prohibition with its alternative when one exists ("Never infer the type. Ask for it.").
- Use one term per concept. Rules say "Tax Pro". Caller-facing lines say "tax professional".
- Use plain verbs: call, ask, speak, state, capture, purge, hand back, stop. Never "facilitate", "leverage", or "utilize".
- Put tool names, fields, enums, and codes in backticks. Put caller-facing lines in double quotes, exactly as spoken.
- Put a short example in "(e.g., ...)" instead of a separate sentence.
- Give no rationale, hedging, or softeners. State what happens and when.
- Use hyphens, never em dashes. Use straight quotes.

## Trimming existing text

- Cut words that add no condition, number, or action.
- Keep every trigger, limit, enum value, field name, and exception. A trim that drops one is a behavior change, not an edit.
- Replace a restated rule with a pointer.
