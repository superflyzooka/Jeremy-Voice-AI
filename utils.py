
import requests, json, os
import pyttsx3

MEMORY_FILE = "jeremy_music_memory.json"
engine = pyttsx3.init()

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2"

current_mood = None
mood_history = []

def save_memory():
    global current_mood, mood_history
    data = {"current_mood": current_mood, "mood_history": mood_history[-20:]}
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f)

def load_memory():
    global current_mood, mood_history
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as f:
                d = json.load(f)
                current_mood = d.get("current_mood")
                mood_history[:] = d.get("mood_history", [])
        except:
            pass
load_memory()

def speak(text: str):
    print(f"Jeremy: {text}")
    engine.say(text)
    engine.runAndWait()

def query_ollama(prompt: str) -> str:
    try:
        r = requests.post(OLLAMA_URL, json={"model": OLLAMA_MODEL, "prompt": prompt}, timeout=30)
        r.raise_for_status()
        return r.json().get("response", "").strip()
    except Exception as e:
        return f"(LLM error) {e}"

def internet_ok() -> bool:
    try:
        requests.get("https://www.google.com", timeout=1.5)
        return True
    except:
        return False
