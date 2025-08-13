
from googleapiclient.discovery import build
from utils import query_ollama, speak, internet_ok

GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
GOOGLE_CX = "YOUR_CX_ID"

def google_search(query, num_results=5):
    try:
        service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
        res = service.cse().list(q=query, cx=GOOGLE_CX, num=num_results).execute()
        return [item['snippet'] for item in res.get('items', [])]
    except Exception as e:
        print(f"Google search error: {e}")
        return []

def answer_question(query: str):
    local_answer = query_ollama(query)
    if len(local_answer) > 30 and not any(x in local_answer.lower() for x in ["i'm not sure","i don't know","cannot"]):
        speak(local_answer)
        return
    if not internet_ok():
        speak("I’m not sure, and I can’t search right now.")
        return
    snippets = google_search(query, num_results=5)
    if not snippets:
        speak("I couldn’t find anything useful online.")
        return
    combined = " ".join(snippets)
    prompt = f"Answer this question using the following sources:\n{combined}\nQuestion: {query}\nAnswer concisely:"
    answer = query_ollama(prompt)
    speak(answer)
