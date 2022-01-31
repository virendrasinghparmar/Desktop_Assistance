import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0) and (hour < 12):
        speak("Good Morning")
    elif (hour >= 12) and (hour < 17):
        speak("Good afternoon")
    else:
        speak("Good night")
    speak("Hello sir i am your assistance. Please tell me how i may help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("say that again please....?")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takecommand().lower()
        # Logic for executing tasks based on Query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")
        elif "open code" in query:
            codepath = "C:\\Users\\Virendra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif "open gmail" in query:
            webbrowser.open("gmail.com")
        elif "play music" in query:
            music_dir = "C:\\Users\\Virendra\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            n = random.randint(0, len(songs) - 1)
            os.startfile(os.path.join(music_dir, songs[n]))
        elif "stop" in query:
            exit()