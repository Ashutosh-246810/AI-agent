import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis, your desktop assistant.")
    speak("I can search the web, play music, tell you the time, open applications, and more.")
    speak("Tell me how can I help you today.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please...")
        return "None"
    return query.lower()

def main():
    wishMe()
    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")
            speak("Opening Stack Overflow")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\YourUsername\\Music'
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
                speak("Playing music now")
            else:
                speak("No music found in your directory.")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ashut\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening Visual Studio Code")

        elif 'search' in query:
            speak("What should I search for?")
            search_query = takeCommand()
            pywhatkit.search(search_query)
            speak(f"Here are the search results for {search_query}")

        elif 'stop' in query or 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("I didn't understand that. Please try again.")

if __name__ == "__main__":
    main()
