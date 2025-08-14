# JeremyAI - Snowboy Edition

JeremyAI is an offline-first, modular voice assistant that uses **Snowboy** for wake word detection,
**Ollama** for local LLM responses, and can optionally use Google Search and YouTube Music.

## Features
- Multiple wake words (default: "Hey Jeremy", "Yo Jeremy")
- Local speech-to-text with Vosk
- Local Ollama integration for responses
- Music playback (offline and online via YouTube Music)
- Pause / Resume music support
- Google Search fallback for complex questions
- Silence detection to stop listening automatically
- Fully offline operation supported

## Installation
```bash
git clone <your-repo-url>
cd JeremyAI_Snowboy
pip install -r requirements.txt
```

## Running Jeremy
```bash
python JeremyAI.py
```

## Training a Custom Wake Word
1. Go to the Snowboy backup repo: https://github.com/Kitt-AI/snowboy  
2. Follow the "Training models" section to record **3 samples** of your wake phrase.
3. Download the `.pmdl` file.
4. Place it in the `wake_words/` folder.
5. Edit `wake.py`:
```python
WAKE_WORD_MODEL = "wake_words/my_custom.pmdl"
```
6. Run Jeremy and say your wake phrase.

## License
MIT License
