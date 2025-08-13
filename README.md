# Jeremy AI Voice Assistant

Jeremy is an offline-first AI voice assistant that can:

- Respond to general questions using a local LLaMA 3.2 model (via Ollama)
- Fallback to Google Search for complex questions if internet is available
- Listen to wake words: "Yo Jeremy" or "Hey Jeremy"
- Play music:
  - Online from YouTube Music if connected
  - Offline from your local music library
- Resume music after pause
- Auto-sleep after 10 seconds of inactivity
- Remember music mood

## Setup Instructions

1. Install Python 3.10+  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place your wake word `.ppn` files in `wake_words/`  
   (use Porcupine keyword tool to generate custom ones if needed)  
4. Ensure Ollama is running locally on port 11434  
5. (Optional) Setup YouTube Music headers (`headers_auth.json`) for online music  
6. Get a Google API Key & CSE ID for online search fallback  

## Run

```bash
python jeremy.py
```

Say **"Yo Jeremy"** or **"Hey Jeremy"** to wake him up, then ask questions or control music.

## Notes

- Jeremy works fully offline for chat and music, but will use online features if available.  
- Default music directory is `~/Music` for local tracks.  
- Auto-sleep occurs after 10 seconds of silence.
