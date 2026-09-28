# Constitution

Answer once, before round 1. Each answer turns a class of future questions into mechanical fixes. Write a letter, or your own text, after `Answer:`. Run `/continue` when done.

### C-1 · Precedence

When two sections conflict, which one wins?

Answer: Part 1 beats Parts 2-4. Inside a part, the prose beats the JSON prompt. Part 5 is supportive to other parts and should reconcile to offer agents the tools they need. 

### C-2 · Prose and JSON duplication

Lint finds 22 prose sentences copied verbatim into JSON. One example is the §1.4 recovery-line table, which repeats `global_voice_lexicon.empathy` line for line.

- A. Mirror. Prose and JSON may repeat each other, and the loop keeps them in sync. It removes duplicates only within prose or within JSON. (Recommended: lowest risk)
- B. JSON is canonical. Prose sections shrink to short summaries that point to the JSON key. This cuts the most length but is a large restructure.
- C. Prose is canonical. JSON keeps only what the runtime prompt needs.

Answer: A

### C-3 · Rules repeated across agent JSON blocks

Three `interruptions` rules and one `transfer_to_agent` description appear word for word in the Scheduler, Office Information, and Tax Pro JSON blocks. Each block merges with the Universal Base JSON at runtime.

- A. A rule identical in all three agent blocks moves to the Base JSON. A rule that repeats a Base JSON rule is deleted from the agent block. Both count as Safe. (Recommended)
- B. Leave agent blocks self-contained.

Answer: A

### C-4 · Pointer style

The spec has almost no cross-references today. Which style should the loop use when it replaces a duplicate?

- A. Prose points with a heading path, for example "(see §1.2, Input Exhaustion & Silence)". JSON points only to JSON key paths, for example "per global_always", and never to prose, since prose is not in the runtime prompt. (Recommended)
- B. Other: ___

Answer: A

### C-5 · Length budget

The spec is 135,118 bytes and 17,183 words today.

- A. At most +1% per round and +5% total. (Recommended)
- B. No net growth at all. Every addition must be offset.
- C. Other limits: ___

Answer: A, but I expect edits to include pruning resulting from increased brevity, chunking, cross-referencing and deduplication.

### C-6 · What blocks the exit

- A. Medium and above block the exit. Low goes to the backlog. (Recommended)
- B. High and above only.

Answer: A

### C-7 · New capabilities

May the loop ever add a capability, outcome, `nextAction`, `routingTarget`, tool, or field without asking?

- A. Never. (Recommended)
- B. Yes, when the addition only completes an enum or contract that the spec already implies.

Answer: A

### C-8 · Frozen text

Which text may change only under a decision that names it?

- A. The §1.4 approved lines, `global_voice_lexicon` (empathy, reprompt, preamble, method descriptions, and prohibited phrases), and every Agent line in the mini-dialogues. (Recommended)
- B. A, plus all Part 5 request and response schemas.
- C. Nothing is frozen.

Answer: A

### C-9 · Dialogues after a rule change

When a decided rule change makes a mini-dialogue wrong, what happens?

- A. The fixer edits the dialogue minimally to match, as part of the same decision. It never adds new dialogues. (Recommended)
- B. Each dialogue edit is a separate question.

Answer: A. Dialogues are always a reflectio nof design and rules and never a rule in their own right. They should always be analyzed and revised to reflect the rest of the rest of the spec. 

### C-10 · Use of the sample audit

The audit's line numbers are stale, and some findings are partly fixed. F-10 is one: the §1.2 prose now says "terminates" but the JSON still says "transfers".

- A. Round 1 re-verifies every F-ID against the current text and ledgers the ones still true. (Recommended: saves at least one round)
- B. Calibration only. Reviewers find everything fresh.

Answer: A

### C-11 · Deterministic flows

Head of Call, Leave a Message, Check Refund Status, Request Live Agent, VOC Survey, and the FAQ Agent are outside this spec. Their diagrams are in `deterministic_flows/` for cross-reference only. Digital Drop-Off (DDO) is not a deterministic flow and is in scope. (Corrected from chat, 2026-09-28.)

- A. The spec may name them and define its handoff to them, but never their internals. (Recommended)
- B. Other: ___

Answer: A

### C-12 · Loop limits

- A. At most 8 rounds and 12 questions per round. Extra questions carry to the next round. (Recommended)
- B. Other: ___

Answer: A

### C-13 · Style of existing text

The spec uses bold inline-header bullets throughout ("- **DOB:** Capture..."), which your writing rules ban in new prose.

- A. Leave the existing structure. Apply your writing rules only to new or rewritten wording. (Recommended)
- B. Convert the spec's bullets over time as sections are edited.

Answer: Follow `loop/style.md`. Bold-label bullets stay, since they are the spec's own style. The loop may trim, split, and rewrite existing text for brevity, and verbose text is a finding. (Recorded from chat, 2026-09-28.)
