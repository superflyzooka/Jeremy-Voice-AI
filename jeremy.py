
from utils import speak
from music import offline_play_some_music
from google_search import answer_question

def main():
    while True:
        input("Press Enter to simulate wake word...")
        speak("Yes?")
        while True:
            user_input = input("You: ").strip().lower()
            if user_input == "":
                speak("Going to sleep.")
                break
            if any(x in user_input for x in ["play","pause","resume","stop","music"]):
                offline_play_some_music()
                continue
            answer_question(user_input)

if __name__ == "__main__":
    main()
