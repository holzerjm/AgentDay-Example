# tools/ — optional build helpers

These regenerate the repo's media and handouts. None are needed to run the
projects; they're here so the artifacts are reproducible, not hand-made.

| File | Makes | Run |
|---|---|---|
| `make_cheatsheet.py` | `docs/cheat-sheet.pdf` (one printable page) | `uv run --with reportlab python tools/make_cheatsheet.py` |
| `social_card.html` | `docs/media/social-preview.png` (1280×640) | Chrome headless — see the comment at the top of the file |
| `dungeon-mastah.tape` | `docs/media/dungeon-mastah.gif` | `vhs tools/dungeon-mastah.tape` (needs `vhs` + `ffmpeg`) |
| `chief-of-stuff.tape` | `docs/media/chief-of-stuff.gif` | `vhs tools/chief-of-stuff.tape` |

The `.tape` files run the **real** agent on the local model (offline fixtures),
so re-recording shows live output — the dice and the routing-table numbers
will differ run to run. Warm the model first (`ollama run granite4:micro ""`)
for snappier captures.

**Social preview** is committed as a PNG but must be set once by hand —
GitHub has no API for it: repo **Settings → General → Social preview →
Upload**, pick `docs/media/social-preview.png`.
