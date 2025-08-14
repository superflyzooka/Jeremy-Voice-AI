# JeremyAI – Snowboy Edition 🎤🤖

JeremyAI is an **offline-first voice assistant** with optional online features.  
It listens for custom wake words (“Hey Jeremy” or “Yo Jeremy”), processes your commands, and can handle music playback, general Q&A, and more.  
This edition uses **Snowboy** for wake word detection — no online accounts required.

---

## ✨ Features

### 🗣 Voice Activation
- Offline wake word detection (`Hey Jeremy` or `Yo Jeremy`) using Snowboy `.pmdl` files
- No internet needed for wake word detection
- Auto sleep mode after 10 seconds of inactivity

### 💬 AI Assistant
- Uses **LLaMA 3.2** via Ollama for responses
- Offline and private — all AI runs locally
- Falls back to online Google Search for complex questions (optional)

### 🎵 Music Controls
- Play from **YouTube Music** (requires internet)
- Pause & resume exactly where you left off
- “Play some music” → plays music you like
- Offline AI “smart music” mode when no internet

### 🌐 Optional Online Features
- Google Search for hard questions
- YouTube Music streaming
- Auto-switch between offline & online modes

---

## 📦 Requirements

JeremyAI requires **Python 3.8+** and these dependencies:

```bash
pip install -r requirements.txt
```

Main libraries:
- `snowboy` (wake word detection)
- `speechrecognition` (speech-to-text)
- `pyaudio` (microphone access)
- `requests`
- `ollama` Python API
- `ytmusicapi`

---

## 🛠 Setup

### 1️⃣ Install Python & Pip
If you don’t have Python:
- **Windows**: [Download here](https://www.python.org/downloads/)
- **Linux**:  
  ```bash
  sudo apt update && sudo apt install python3 python3-pip
  ```
- **macOS**:  
  ```bash
  brew install python
  ```

### 2️⃣ Clone or Download JeremyAI
```bash
git clone https://github.com/YOUR_USERNAME/Jeremy-Voice-AI.git
cd Jeremy-Voice-AI
```
Or download the ZIP and extract it.

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Install Ollama
[Install Ollama](https://ollama.com/download) and pull LLaMA 3.2:
```bash
ollama pull llama3.2
```
By default Ollama runs on `http://localhost:11434`.

### 5️⃣ Run JeremyAI
```bash
python3 JeremyAI.py
```

---

## 🎯 Usage

**Wake up Jeremy:**
- Say **"Hey Jeremy"** or **"Yo Jeremy"**

**Commands:**
- “What’s the weather today?” → Answers locally or via Google Search
- “Play some music” → Plays a random song you like
- “Pause music” / “Play again” → Resume from paused track
- “Search for quantum entanglement” → Uses Google Search if needed

Jeremy listens until you stop speaking.  
If there’s no response for 10 seconds, Jeremy goes to sleep until you say the wake word again.

---

## 🎤 Training Custom Wake Words

You can train your own `.pmdl` wake word model:

1. Go to [Snowboy’s Custom Wake Word Training](https://snowboy.kitt.ai/)  
   *(You may need to use an archive copy since Snowboy is discontinued)*
2. Record 3 samples of your chosen phrase
3. Download the `.pmdl` file
4. Save it to `wakewords/` and update `wakeword.py` with the new file name

---

## 📄 License

This project is licensed under the **MIT License** — see `LICENSE` for details.

---

## 🐛 Troubleshooting

- **No microphone detected**:  
  Make sure `pyaudio` is installed and your mic is connected.
- **Snowboy not working**:  
  Check that `.pmdl` files are in `wakewords/` and `wakeword.py` points to the right files.
- **Google Search not working**:  
  Make sure you have internet and `google-api-python-client` installed.

---

## 🤝 Contributing

Pull requests welcome! If you want add cool features (offline TTS, smarter music AI, etc.), we would love to have it if you added it to this repo.

---

