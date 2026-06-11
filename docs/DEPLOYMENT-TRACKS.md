# Deployment tracks — three ways to run any starter

Every project here is a plain Python agent first. But the skills are
[agentskills.io](https://agentskills.io)-spec directories, which means they
also install into assistant frameworks unchanged. Pick your track:

| Track | What you get | Best for |
|---|---|---|
| A. Bare Python (default) | `uv run python projects/<t>/<n>/agent.py "..."` | building, evals, demos |
| B. OpenClaw | your skill inside a 24/7 personal-agent gateway (channels, scheduler) | "it messages ME every morning" demos |
| C. ZeroClaw | single Rust binary, deny-by-default security, same skills idea | security-story demos, tiny footprints |

The worked example for B and C is **chief-of-stuff** — see its
[`deploy/`](../projects/chief-of-staff/chief-of-stuff/deploy/) folder.

> Frameworks move fast. Paths and flags below were verified June 2026 —
> re-verify on your machine before the demo.

## Track A — bare Python

What every README quickstart uses. The agent loop is `agentkit/loop.py`
(~100 lines); your laptop, your model, no runtime dependencies beyond uv.

## Track B — OpenClaw

[OpenClaw](https://github.com/openclaw/openclaw) (formerly Clawdbot→Moltbot)
is the open-source autonomous personal-agent gateway. It consumes
agentskills.io skills directly:

```bash
# install (docs.openclaw.ai), then drop any skill from this repo into one of:
<your-workspace>/skills/         # workspace scope
~/.agents/skills/                # personal scope
~/.openclaw/skills/              # managed scope
cp -r projects/chief-of-staff/chief-of-stuff/skills/morning-brief ~/.openclaw/skills/
```

Config lives at `~/.openclaw/openclaw.json`. The chief-of-stuff
`deploy/openclaw/README.md` sketches a scheduled 7 AM morning-brief delivery.

**Security caveat (non-optional):** OpenClaw's default posture is permissive
operator-trust, it has a documented CVE history, and 135k+ instances have
been found publicly exposed with insecure defaults. Run it local-only, scope
secrets down, and treat anything you install from a skill registry as
untrusted input (ToxicSkills found 36% of audited registry skills flawed and
76 outright malicious). The event resource guide §8 has the full story —
citing it in your demo is free rubric credit.

## Track C — ZeroClaw

[ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) is the Rust rebuild of
the same idea: a single ~3–9 MB binary, <5 MB RAM, **deny-by-default** (every
file/shell/network capability explicitly allowlisted), SQLite memory, and
any OpenAI-compatible endpoint as a provider — including your local model:

```bash
curl -fsSL https://raw.githubusercontent.com/zeroclaw-labs/zeroclaw/master/install.sh | bash
zeroclaw quickstart        # writes ~/.zeroclaw/config.toml
```

```toml
# ~/.zeroclaw/config.toml — point it at the same local model this repo uses
[providers.models.local]
kind     = "openai-compatible"
base_url = "http://localhost:11434/v1"
model    = "granite4:micro"
api_key  = "not-needed"
```

A ready-made config ships in chief-of-stuff's `deploy/zeroclaw/`. The
deny-by-default posture is a built-in security talking point for judging:
your agent *architecturally cannot* exfiltrate what it was never allowlisted
to touch.

## Which track for the demo?

Build and eval on Track A — always. Add B or C only if the "always-on
assistant" angle is your lane-merit story; budget 45+ minutes for framework
setup and keep Track A as the fallback demo. Judges grade evidence, not
infrastructure.
