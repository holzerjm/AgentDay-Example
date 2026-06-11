# Setup — one client, four providers, zero required keys

Every starter in this repo talks to its model through one switch:

```
MODEL_PROVIDER = local | anthropic | openai | gemini     (default: local)
```

All four speak the OpenAI chat-completions dialect (Anthropic and Gemini via
their compatibility endpoints, local via Ollama / Podman AI Lab / llama.cpp /
vLLM), so the same code path serves every option — that's `agentkit/llm.py`,
~90 readable lines.

**You can complete the entire event with zero API keys** on a local model.
Four of the nine starters never even touch the network.

## The 30-second check

```bash
uv sync                                   # once
uv run python tests/manual_loop_smoke.py  # agent loop + tool call on YOUR model
```

`SMOKE PASS` means your setup works for every project in the repo.

## Path A — Ollama (simplest)

```bash
brew install ollama          # or https://ollama.com/download
ollama pull granite4:micro   # ~2 GB; the event's Granite, tool-capable, fast
ollama serve                 # usually already running as a service
```

Done — the repo's defaults (`http://localhost:11434/v1`, `granite4:micro`)
already point here. Alternatives: `granite3.3:8b` (closer to the event's
"Granite 8B", needs ~8 GB RAM), `qwen3:4b`, `llama3.1` (tool-calling is
shakier — see docs note in MODEL_SELECTION files).

## Path B — Podman AI Lab (the event's house path)

1. Install Podman Desktop → Extensions → **Podman AI Lab**.
2. Resource the machine: `podman machine set --memory 16384 --cpus 8` (stopped machine first).
3. Catalog → pull **granite-4.0-micro** (8 GB laptops) or **granite-3.3-8b-instruct** (16 GB+).
4. Services → New Model Service → start it → **copy the port** (it's random per service).
5. Point the repo at it:

```bash
export LOCAL_BASE_URL=http://localhost:<YOUR-PORT>/v1
export LOCAL_MODEL=granite        # the service's model name (check its page)
curl $LOCAL_BASE_URL/models       # sanity check
```

## Path C — frontier keys (optional, enables "strong" tier + routing demos)

| Provider | Env var | Get a key | Default / strong models used |
|---|---|---|---|
| Anthropic | `ANTHROPIC_API_KEY` | console.anthropic.com | claude-sonnet-4-6 / claude-opus-4-8 |
| OpenAI | `OPENAI_API_KEY` | platform.openai.com | gpt-5.4-mini / gpt-5.5 |
| Google | `GEMINI_API_KEY` | aistudio.google.com (free tier) | gemini-2.5-flash / gemini-3.5-flash |

```bash
cp .env.example .env    # then uncomment what you have — agentkit auto-loads .env
MODEL_PROVIDER=anthropic uv run python projects/everyday/fridge-whisperer/agent.py "..."
```

Override any tier's model with `AGENTKIT_MODEL` / `AGENTKIT_STRONG_MODEL` /
`AGENTKIT_CHEAP_MODEL`.

## Offline mode

`AGENT_OFFLINE=1` (or `--offline` on any agent) forces every networked tool
onto its committed `fixtures/` — same demo, no wifi. **Evals always run
offline** so benchmark numbers are reproducible; live APIs are for demos.

## Troubleshooting

- **"Could not reach your local model"** — the error message itself prints
  the fix (start Ollama, or copy the AI Lab port into `LOCAL_BASE_URL`).
- **First local call is slow** — that's the model loading into memory once;
  subsequent calls are seconds.
- **`ModuleNotFoundError: agentkit`** — run from the repo root with
  `uv run …`. (Rare macOS case: on iCloud-synced folders the hidden flag can
  land on the venv's `.pth` files and Python skips them silently —
  `chflags nohidden .venv/lib/python*/site-packages/*.pth`, or keep the repo
  outside Documents/Desktop. Every `agent.py` self-locates the repo root, so
  the starters keep working regardless.)
- **Validator** — the spec validator installs from PyPI as `skills-ref` but
  the executable is `agentskills`: `uv run agentskills validate <skill-dir>`.
