"""Generate docs/cheat-sheet.pdf — one printable landscape page for the room.

Run:  uv run --with reportlab python tools/make_cheatsheet.py
"""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    BaseDocTemplate, Frame, FrameBreak, PageTemplate, Paragraph, Spacer, Table, TableStyle,
)

OUT = Path(__file__).resolve().parent.parent / "docs" / "cheat-sheet.pdf"
INK = colors.HexColor("#1A1A2E")
ACCENT = colors.HexColor("#CC0000")  # Boston red
SUB = colors.HexColor("#6B7280")
BG = colors.HexColor("#F3F4F6")

styles = getSampleStyleSheet()
H = ParagraphStyle("H", parent=styles["Heading2"], textColor=ACCENT, fontSize=10,
                   spaceAfter=3, spaceBefore=2, fontName="Helvetica-Bold")
body = ParagraphStyle("body", parent=styles["BodyText"], fontSize=7.6, leading=10, textColor=INK)
mono = ParagraphStyle("mono", parent=body, fontName="Courier", fontSize=7.4, leading=10.5)
cell = ParagraphStyle("cell", parent=body, fontSize=7.2, leading=8.6)
cellb = ParagraphStyle("cellb", parent=cell, fontName="Helvetica-Bold")
cellh = ParagraphStyle("cellh", parent=cellb, textColor=colors.white, fontSize=7.4)


def picker_table():
    head = ["Project", "Theme", "Lane", "Diff", "Offline", "You'll learn"]
    rows = [
        ("fridge-whisperer", "everyday", "L1", "1", "fully", "the agent loop + skill templating"),
        ("dungeon-mastah", "fun", "L1", "1", "fully", "tested scripts (real dice), memory"),
        ("wicked-smaht-bahtendah", "fun", "L1", "1", "fixtures", "defaults-not-menus, API fallback"),
        ("qrious-citizen", "social good", "L1", "2", "fixtures", "multi-tool loops, real open data"),
        ("storm-ready", "social good", "L1", "2", "fixtures", "two-step APIs, degrade gracefully"),
        ("paypah-trail", "everyday", "L1", "2", "fully", "deterministic scripts > willpower"),
        ("skill-forge", "wildcard", "L1", "2", "fully", "the spec, by building a skill-maker"),
        ("model-matchmakah", "wildcard", "L1", "2", "partial", "cascade routing with cost receipts"),
        ("chief-of-stuff", "chief of staff", "L3", "3", "yes", "multi-agent delegation + routing"),
    ]
    data = [[Paragraph(h, cellh) for h in head]]
    for r in rows:
        data.append([Paragraph(r[0], cellb)] + [Paragraph(c, cell) for c in r[1:]])
    t = Table(data, colWidths=[150, 92, 36, 26, 64, 364])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), INK),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 7.4),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, BG]),
        ("BACKGROUND", (0, 9), (-1, 9), colors.HexColor("#FFF3CD")),  # flagship row highlight
        ("LINEBELOW", (0, 0), (-1, 0), 0.7, INK),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 2.4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def kv_block(title, lines):
    out = [Paragraph(title, H)]
    out += [Paragraph(l, body) for l in lines]
    return out


def build():
    doc = BaseDocTemplate(str(OUT), pagesize=landscape(letter),
                          leftMargin=26, rightMargin=26, topMargin=22, bottomMargin=18)
    W, Hpt = landscape(letter)
    # full-width header band, full-width picker table, then two columns below
    M, GAP = 26, 18
    full_w = W - 2 * M
    col_w = (full_w - GAP) / 2
    head_h, band_h = 50, 196
    head_y = Hpt - 22 - head_h
    band_y = head_y - 6 - band_h
    col_h = band_y - 18 - 4
    doc.addPageTemplates([PageTemplate(id="cs", frames=[
        Frame(M, head_y, full_w, head_h, id="head", topPadding=0, bottomPadding=0),
        Frame(M, band_y, full_w, band_h, id="band", topPadding=2, bottomPadding=0),
        Frame(M, 18, col_w, col_h, id="L", topPadding=4),
        Frame(M + col_w + GAP, 18, col_w, col_h, id="R", topPadding=4),
    ])])

    title = ParagraphStyle("title", parent=styles["Title"], fontSize=19, textColor=INK,
                           spaceAfter=0, leading=21)
    tag = ParagraphStyle("tag", parent=body, fontSize=9.2, textColor=ACCENT, spaceBefore=1)

    story = [
        Paragraph("TOA Agent Build Day &mdash; Cheat Sheet", title),
        Paragraph("Wicked Smart Agents: pick a lane, pick your models, ship a skill. "
                  "&middot; Sat June 27, 2026 &middot; Fort Point &middot; "
                  "<b>github.com/holzerjm/AgentDay-Example</b>", tag),
        FrameBreak(),
    ]
    # FULL-WIDTH band: the picker table
    story += [Paragraph("Pick your project", H), picker_table(), FrameBreak()]
    # LEFT column
    story += kv_block("Five commands (zero keys, local model)", [
        '<font face="Courier">git clone …/AgentDay-Example &amp;&amp; cd AgentDay-Example</font>',
        '<font face="Courier">uv sync</font>',
        '<font face="Courier">ollama pull granite4:micro</font>',
        '<font face="Courier">uv run python tests/manual_loop_smoke.py</font> &rarr; SMOKE PASS',
        '<font face="Courier">uv run python projects/&lt;theme&gt;/&lt;name&gt;/agent.py "your task"</font>',
        '<font face="Courier">uv run python -m agentkit.evals projects/&lt;theme&gt;/&lt;name&gt;</font>',
    ])
    story += [Spacer(1, 8)]
    story += kv_block("Five failure modes to dodge", [
        "Vague instructions &middot; menus instead of one default &middot; "
        "SKILL.md that blows the context budget &middot; skipping evaluation &middot; "
        "no model-selection rationale.",
    ])
    story.append(FrameBreak())
    # RIGHT column
    story.append(Paragraph("Day-of timeline", H))
    for t_, what in [
        ("9:30", "Setup check &mdash; model service up, <font face='Courier'>skills-ref</font> installed"),
        ("10:30", "<b>Lane 2: tag your baseline</b> (sacred &mdash; before any change)"),
        ("by lunch", "Write 2&ndash;3 evals; flip to eval-driven iteration"),
        ("3:00", "Kill list &mdash; cut anything not serving demo + rubric"),
        ("5:00", "Commit freeze &mdash; <font face='Courier'>skills-ref validate</font>, README, push"),
    ]:
        story.append(Paragraph(f"<b><font color='#CC0000'>{t_}</font></b> &nbsp; {what}", body))
    story += [Spacer(1, 6)]
    story.append(Paragraph("Rubric (100 pts) &mdash; read it backwards", H))
    for pts, crit in [
        ("25", "Shippability &mdash; runs from README, <font face='Courier'>validate</font> passes, public + OSI license"),
        ("20", "ADLC &mdash; worksheet + &ge;1 evaluate/observe loop (benchmark.json)"),
        ("20", "Model Selection &mdash; written rationale + measured cost/latency/quality"),
        ("20", "Lane Merit &mdash; L1 end-to-end / L2 same-input delta / L3 delegation"),
        ("15", "Skill Quality &mdash; triggers, defaults, gotchas, template, eval delta"),
    ]:
        story.append(Paragraph(f"<b>{pts}</b> &nbsp; {crit}", body))

    doc.build(story)
    print(f"wrote {OUT}  ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    build()
