import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def greet():
    return "Hello! How can I assist you today?"

def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    return f"The current time is {current_time}"

def get_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    return f"Today is {current_date}"

def search_web(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

def main():
    engine = pyttsx3.init()
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        engine.say(greet())
        engine.runAndWait()
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")

            if "hello" in command:
                response = greet()
            elif "time" in command:
                response = get_time()
            elif "date" in command:
                response = get_date()
            elif "search" in command:
                query = command.replace("search", "").strip()
                response = f"Searching the web for {query}"
                search_web(query)
            else:
                response = "I'm sorry, I didn't understand that."

            print(response)
            engine.say(response)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Can you please repeat?")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    main()
