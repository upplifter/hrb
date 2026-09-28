# Reviewer brief (round 9)

You are a read-only reviewer for the spec review loop in /home/user/hrb. Read CLAUDE.md, loop/lenses.md (your lens only), loop/style.md, state/constitution.md, state/decisions.md (D-001 to D-099, binding), state/rejected.md, state/backlog.md, and the ledger state/ledger.md (skim anchors and summaries so you do not re-raise them). Then review HRB_IVA_Agents_Spec.md in full through your lens.

Focus: round 8 just applied decisions D-084 to D-099 to the spec, and no sweep has reviewed them. Check that those edits are consistent with the rest of the spec (incomplete propagation, prose/JSON mismatch, dialogues that no longer match, broken references, new contradictions). Also report any other still-valid Medium-or-higher issue for your lens.

Rules:
- Do NOT edit any file except your findings file. Write your findings to rounds/round-09/findings-<LENS>.md. If writing is blocked, put the full findings in your reply.
- Never raise anything in rejected.md, settled in decisions.md, or already open/decided in the ledger. Do not raise backlog items again.
- Anchor each finding to a heading path or JSON key path, not a line number.
- Format per finding: `### <LENS>-NN · title`, then `Anchor:`, `Severity:` (Critical/High/Medium/Low), `Class:` (Safe or Human per CLAUDE.md triage rules), `Issue:`, `Fix:` (for Safe give exact replacement text with old and new strings; for Human give 2-3 options, recommended first, with footprint in edits and net words). End with `Summary:` counts.
- Be precise and skeptical: verify each claim against the current text before reporting. Prefer few real findings over many speculative ones. Report at most 12 findings (lens F: at most 25).
- Keep the final reply short: list finding IDs, severity, class, one line each.
