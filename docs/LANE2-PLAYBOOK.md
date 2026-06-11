# Lane 2 playbook — fork BriefingClaw, prove the delta

Lane 2 ("Best Improved Agent and Skill") has one iron rule: **only in-event
deltas are scored, on the same inputs, against a baseline you tagged by
10:30 AM.** This playbook is the morning checklist.

The reference project: **BriefingClaw** —
https://github.com/holzerjm/GACEP-Spring-2026-demo — an 8-agent hub-and-spoke
executive-briefing system (Oprah-tor orchestrating; The Oddsfather predicting
meeting success on Granite 8B; Sherlock Ohms and Bloom-borg on research).
This repo's chief-of-stuff starter is its small sibling if you want to study
the architecture at readable scale first.

## 10:00–10:30 — the sacred baseline (do this first, talk later)

```bash
git clone https://github.com/holzerjm/GACEP-Spring-2026-demo briefingclaw
cd briefingclaw
# run it ONCE on the provided sample inputs, exactly as the README says
# capture whatever it produces (output files, scores, logs) as-is
git add -A && git commit -m "baseline capture" && git tag baseline   # by 10:30!
```

Don't fix anything yet. Don't even fix typos — that's a delta and it isn't
measured yet. (And never degrade the baseline; that's a DQ.)

## 10:30–12:00 — build the measuring stick

Pick the improvement-menu item that produces an unambiguous number. The two
classic plays:

**Play 1 — "The Auditor" (eval harness + calibration fix).** Target an agent
with a checkable output contract — The Oddsfather's verdict (success
probability + top-3 risks + top-3 levers) is the named example. Write 2–3
eval cases asserting what a good verdict MUST contain: a numeric probability,
≥3 risks, evidence citations. This repo's runner works on any project that
exposes `run(task, skill=None|path) -> text`:

1. Add a thin `run()` wrapper around the target agent in your fork.
2. Copy a starter's `evals/evals.json` shape (assertion types: `regex`,
   `not_regex`, `contains`, `contains_section`, `count_min`, `numeric_present`,
   `script`) and write cases against the SAMPLE inputs.
3. `uv run python -m agentkit.evals path/to/your/fork-project` (run it from
   this repo's root, or vendor `agentkit/evals.py` into the fork — it's one
   file on purpose).
4. Run on the `baseline` tag → that's your "before" `benchmark.json`.

Then make the fix (usually a SKILL.md edit: mandatory verdict template,
required evidence quotes, a gotchas section), re-run, and your demo is
literally two benchmark.json files side by side.

**Play 2 — observability (OTel spans + Langfuse/Phoenix).** Instrument the
orchestrator→spoke dispatch path, ship spans to a locally-containerized
Langfuse or Arize Phoenix, inject a fault, and measure time-to-diagnose
before/after — plus the per-agent token/cost/latency table you get for free,
which doubles as your Model Selection evidence.

## 12:00–17:00 — the loop

Eval → edit skill → eval. Every improvement either moves `benchmark.json` or
gets cut at the 3:00 PM kill-list check. Keep a `notes.md` of each
iteration — it becomes your ADLC worksheet's §4 and §7 nearly verbatim.

## The demo (5 min)

1. `git diff baseline --stat` — "everything you're about to see happened today."
2. Before/after benchmark.json on the SAME inputs — the delta is the headline.
3. One concrete output example: baseline verdict vs improved verdict.
4. The routing/cost table if you touched models (Granite vs frontier per task).
