# Loop procedure

The main session is the orchestrator. It runs the steps below, spawns the `reviewer`, `fixer`, and `verifier` subagents, and keeps all state in files. It never relies on memory from an earlier session.

## Start

1. If the folder is not a git repository, run `git init` and commit every file as "baseline".
2. If `state/baseline.json` is missing, run `python tools/lint.py snapshot baseline`.
3. If any `Answer:` line in `state/constitution.md` is blank, tell the user to answer it and run `/continue`. Stop.
4. Otherwise apply the constitution (see "Apply the constitution"), then run a round.

## Continue

1. If the constitution has not been applied yet, apply it and run a round.
2. Otherwise open the newest `rounds/round-NN/questions.md` and read every `Answer:` line.
3. If an answer is blank or ambiguous, write `Clarify:` with a short follow-up under that question. List those questions in chat and stop.
4. Record each answer:
   - A decision goes to `state/decisions.md` as `D-NNN | rule in one sentence | Q-ID | ledger IDs`.
   - "not an issue" goes to `state/rejected.md` with the ledger IDs.
   - "defer" goes to `state/backlog.md`.
5. Update the ledger status for every item the answers cover.
6. Send the decided items to the fixer, then the verifier (steps 5 and 6 of the round).
7. Run a new round.

## Apply the constitution

Copy each constitution answer into `state/lint_config.json` where it sets a threshold. Commit as "constitution".

## Round

1. Create `rounds/round-NN/`. Run `python tools/lint.py snapshot round_start` and save `python tools/lint.py check --all` output to `lint-before.txt`.
2. **Review.** Spawn one `reviewer` per lens in `loop/lenses.md`, in parallel. Pass the lens letter and the round folder. Each writes `findings-<lens>.md`. If the constitution says to seed from the audit, round 1 also spawns one reviewer on lens `S` to re-verify every F-ID against the current text.
3. **Triage.** Read all findings files. Drop anything already in the ledger, `rejected.md`, or settled in `decisions.md`. Merge findings that share an anchor. Classify each as Safe or Human under the CLAUDE.md triage rules. Low findings go to `backlog.md` unless they are Safe editorial fixes. Give each kept item a ledger ID `L-NNN` and add it to `state/ledger.md`.
4. **Oscillation guard.** If an anchor has been edited in 3 earlier rounds, reclassify any new item on it as Human.
5. **Fix.** Spawn the `fixer` with the Safe items (IDs and rows). It writes `changes.md`.
6. **Verify.** Spawn the `verifier`. It writes `verify.md`. For each item marked `fix-needed`, send it to the fixer once more. For each item marked `revert`, or still failing, have the fixer revert it and reclassify it as Human.
7. **Questions.** Group Human items by the decision that would settle them. Write `questions.md` in the format below, with at most `max_questions_per_round` questions (constitution). Carry the rest to the next round.
8. **Status.** Update `state/status.md`: round number, findings by severity, Safe fixed, questions asked, words and bytes versus baseline, and the clean-sweep counter.
9. Commit as "round NN".
10. **Exit check.**
    - A sweep is clean when it produced no new Medium-or-higher finding and no question.
    - After a clean sweep, add 1 to the counter. Otherwise reset it to 0.
    - If the counter reaches 2 and lint shows no FAIL, write `rounds/FINAL.md` with the summary from `status.md` and stop. The loop is done.
    - If `questions.md` has questions, send a notification if available, tell the user where the file is, and stop.
    - If the round cap is reached, write `rounds/FINAL.md` with what is still open and stop.
    - Otherwise start the next round at once.

## Question format

```
### Q-07 · Callback ownership (resolves L-003, L-004, L-011)
Conflict: one or two sentences, with the anchors.
Options:
  A. ... (Recommended: smallest edit)
  B. ...
  C. Other: ___
Footprint: A ≈ 6 edits, net -40 words. B ≈ 9 edits, net +25 words.
Answer:
```

The user may also answer "defer" or "not an issue".
