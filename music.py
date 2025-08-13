
import os, random, subprocess
from utils import speak, current_mood, mood_history, save_memory

LOCAL_MUSIC_DIR = os.path.expanduser("~/Music")
MPV_SOCKET = "/tmp/mpvsocket"
mpv_process = None
is_paused = False
last_local_path = None
last_song_id = None
current_mode = "offline"

AUDIO_EXTS = {".mp3",".flac",".wav",".m4a",".ogg"}

def detect_mood_from_text(title: str) -> str:
    t = (title or "").lower()
    if any(k in t for k in ["lofi", "chill", "ambient"]): return "chill"
    if any(k in t for k in ["rock", "metal", "punk"]): return "rock"
    if any(k in t for k in ["pop", "dance", "edm"]): return "upbeat"
    if any(k in t for k in ["piano", "classical", "strings"]): return "calm"
    return "mixed"

def update_mood(mood: str):
    global current_mood
    mood_history.append(mood)
    if len(mood_history) >= 3 and len(set(mood_history[-3:])) == 1:
        current_mood = mood
        save_memory()

def scan_local_library():
    paths = []
    for root, _, files in os.walk(LOCAL_MUSIC_DIR):
        for f in files:
            if os.path.splitext(f)[1].lower() in AUDIO_EXTS:
                paths.append(os.path.join(root, f))
    return paths
LOCAL_TRACKS = scan_local_library()

def spawn_mpv(url: str, no_video=True):
    global mpv_process
    if mpv_process and mpv_process.poll() is None:
        try: mpv_process.terminate()
        except: pass
    args = ["mpv", url, f"--input-ipc-server={MPV_SOCKET}"]
    if no_video: args.insert(1, "--no-video")
    mpv_process = subprocess.Popen(args)

def offline_play_some_music():
    global last_local_path, is_paused, current_mode
    if not LOCAL_TRACKS:
        speak("I couldn't find local music to play.")
        return
    current_mode = "offline"
    pick = random.choice(LOCAL_TRACKS)
    last_local_path = pick
    title = os.path.splitext(os.path.basename(pick))[0]
    update_mood(detect_mood_from_text(title))
    speak(f"Playing {title} from your library")
    spawn_mpv(pick, no_video=True)
    is_paused = False
