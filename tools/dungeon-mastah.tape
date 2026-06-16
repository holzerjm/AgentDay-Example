# Render:  vhs tools/dungeon-mastah.tape   (run from the repo root; needs vhs + ffmpeg)
Output docs/media/dungeon-mastah.gif
Require uv

Set Shell zsh
Set FontSize 16
Set Width 1200
Set Height 720
Set Padding 20
Set Framerate 12
Set TypingSpeed 30ms
Set Theme "Catppuccin Mocha"

Hide
Type "cd /Users/jholzer/Documents/notes/Claude/TOA/AgentDay/AgentDay-Example" Enter
Type "export MODEL_PROVIDER=local AGENT_OFFLINE=1 PROMPT='$ '" Enter
Type "clear" Enter
Show

Sleep 600ms
Type "uv run python projects/fun/dungeon-mastah/agent.py 'I charge the ghoul with my crowbar!'"
Sleep 800ms
Enter
Sleep 13s
Sleep 2s
