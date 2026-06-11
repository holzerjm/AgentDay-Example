# Ideas appendix — ten more seeds, one paragraph each

Starters too good to leave unmentioned, too many to build. Each names the
existing project to fork as a base. Difficulty in 🦞.

1. **roast-mastah** (fun, L1, 🦞 — fork dungeon-mastah, drop the dice).
   Point it at a git repo; it reads `git log --stat` through one tool and
   lovingly roasts the commit history ("14 commits named 'fix', a Friday
   17:58 force-push — bold"). The skill is a `kind-comedy` contract: punch at
   patterns, never people; end with one sincere compliment and one actually
   useful suggestion. Fully offline, very demoable.

2. **curb-your-enthusiasm** (social good, L1, 🦞🦞 — fork qrious-citizen).
   The same Analyze Boston loop pointed at sidewalk/curb-ramp and
   accessibility-related 311 categories: "which blocks got wheelchair-access
   complaints and how long did closures take?" The civic-brief skill gains an
   equity lens section (response-time by neighborhood, with caveats).

3. **storm-ready + FEMA layer** (social good, L1→L3, 🦞🦞 — extend storm-ready).
   OpenFEMA's keyless API (`DisasterDeclarationsSummaries` with `$filter`)
   adds "has this county been declared before, how often, for what" — turning
   the brief from weather into risk history. Natural second agent + skill if
   you want the Lane 3 bar.

4. **inbox-zero-coach** (everyday, L1, 🦞🦞🦞). Triage an mbox/email export
   into reply-now / delegate / archive with drafted one-line replies. Do NOT
   wire live email send on day one — that's the lethal trifecta (private
   data + untrusted content + outbound channel) on a silver platter; the
   skill's Gotchas section IS the security slide.

5. **plant-doctah** (everyday/fun, L1, 🦞🦞). Photo of the sad houseplant →
   vision-capable model (LLaVA-class local, or frontier) → diagnosis card
   skill: symptom, suspect, treatment this week, "am I overwatering" verdict
   (yes). Good first vision-tool project.

6. **bouncer-at-the-claw-b** (wildcard/security, L3, 🦞🦞🦞 — the event doc's
   §3.2 seed). Two agents, capabilities split: one executes code only inside
   `podman run --network=none --read-only --cap-drop=ALL`, the other has
   search but no execution. A `sandbox-discipline` skill makes the separation
   procedural; the demo beat is a prompt-injected "exfiltrate the workspace"
   instruction failing architecturally. Cite ToxicSkills + OWASP ASTop10.

7. **chief-of-stuff + traces** (chief-of-staff, L3, 🦞🦞 — extend the flagship).
   Wrap each specialist dispatch in OpenTelemetry GenAI spans, ship to a
   containerized Arize Phoenix next to your models, and demo the live trace
   waterfall — the hub-and-spoke fan-out is genuinely pretty in spans, and
   the per-agent cost table doubles as Model Selection evidence.

8. **commute-whisperah** (everyday, L1, 🦞🦞). MBTA's v3 API (free key,
   generous limits) + the NWS tool from storm-ready → "leave at 8:12, Orange
   Line is degraded, here's the bike-vs-train call given the radar." The
   skill encodes the decision rules; the agent just fetches.

9. **skill-librarian** (wildcard/security, L1, 🦞🦞 — fork skill-forge).
   Inverts the forge: scans a directory of installed skills and red-flags
   ToxicSkills patterns — scripts with network calls, base64 blobs, curl-pipe
   installs, descriptions that don't match bodies. Output: a graded inventory
   per the source-grading idea. The room full of freshly-installed registry
   skills is the live demo.

10. **translate-the-town** (social good, L1→L3, 🦞🦞 — fork any brief-emitting
    starter). A `plain-language-translation` skill that re-renders civic/storm
    briefs at a 6th-grade reading level and in a second language, preserving
    every number and caveat (the gotcha: translation must not soften
    warnings). Composes as a second agent pass — instant Lane 3 shape.
