# ALEX 🎙️
> An AI that controls your PC with just your voice. Free. Local. No keyboard needed.

---

## What is this?
ALEX is a voice controlled PC assistant built with Python.
Press CTRL+SPACE, say a command, and your PC does it.
Opening apps, searching google, typing — all hands free.

---

## How it works
1. You press CTRL+SPACE
2. Mic records your voice
3. Whisper converts voice to text
4. Ollama AI thinks and writes Python code
5. PyAutoGUI executes it on your PC

---

## Tools used
- Whisper by OpenAI — voice to text
- Ollama + LLaMA3 — free local AI brain
- PyAutoGUI — controls the PC
- SoundDevice — records mic audio
- FFmpeg — audio converter
- Python — ties everything together

---

## Requirements
- Windows PC
- Python 3.13+
- VS Code
- Ollama installed and running

---

## Setup

**Step 1 — Install FFmpeg**
winget install ffmpeg
Add the bin folder to your system PATH.

**Step 2 — Install libraries**
pip install keyboard sounddevice numpy openai-whisper pyautogui ollama

**Step 3 — Install Ollama**
Go to ollama.com, download and install it.
Then run:
ollama run llama3

**Step 4 — Run ALEX**
python jarvis.py
Wait for ✅ Ready! then press CTRL+SPACE and speak.

---

## Example commands
- "open google"
- "open notepad"
- "search for weather today"
- "type hello world"
- "press enter"

---

## What's next
- [ ] Switch to Gemini API for smarter responses
- [ ] Add BFF memory mode
- [ ] Auto start on PC boot
- [ ] Better error handling
- [ ] Support for more complex multi step commands

---

## Built by
just a lazy girl figuring things out 🔥
follow the journey → https://www.youtube.com/@figuringz_out
