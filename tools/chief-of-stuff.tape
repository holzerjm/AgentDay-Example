# Render:  vhs tools/chief-of-stuff.tape   (run from the repo root; needs vhs + ffmpeg)
Output docs/media/chief-of-stuff.gif
Require uv

Set Shell zsh
Set FontSize 15
Set Width 1280
Set Height 880
Set Padding 18
Set Framerate 12
Set TypingSpeed 28ms
Set Theme "Catppuccin Mocha"

Hide
Type "cd /Users/jholzer/Documents/notes/Claude/TOA/AgentDay/AgentDay-Example" Enter
Type "export MODEL_PROVIDER=local AGENT_OFFLINE=1 PROMPT='$ '" Enter
Type "clear" Enter
Show

Sleep 600ms
Type "uv run python projects/chief-of-staff/chief-of-stuff/agent.py 'Build my morning brief for Friday, June 26, 2026.'"
Sleep 800ms
Enter
Sleep 17s
Sleep 2s
