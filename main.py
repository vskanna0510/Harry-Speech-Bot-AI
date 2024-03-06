import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import pywhatkit
import subprocess
import pandas
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Harry sir. Please tell me how may I help you")

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

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open("google.com")

        if 'chennai institute of technology' in query:
            a = 'Opening .'
            engine.say(a)
            engine.runAndWait()
            webbrowser.open("https://www.citchennai.edu.in")

        if 'about college' in query:
            b = 'Opening .'
            engine.say(b)
            engine.runAndWait()
            webbrowser.open("https://www.youtube.com/watch?v=_8R13swv0lQ")

        if 'admission' in query:
            c = 'Opening .'
            engine.say(c)
            engine.runAndWait()
            webbrowser.open("https://www.citchennai.edu.in/admission/")

        if 'training and placement' in query:
            d = 'Opening .'
            engine.say(d)
            engine.runAndWait()
            webbrowser.open("https://www.citchennai.edu.in/training-placement/")

        if 'about infrastructure' in query:
            e = 'Opening .'
            engine.say(e)
            engine.runAndWait()
            webbrowser.open("https://www.citchennai.edu.in/infrastructure/")

        if 'c o e' in query:
            f = 'Opening .'
            engine.say(f)
            engine.runAndWait()
            webbrowser.open("https://www.citchennai.edu.in/centre-of-excellence/")

        if 'about research' in query:
            f = 'Opening .'
            engine.say(f)
            engine.runAndWait()
            webbrowser.open("https://www.citchennai.edu.in/research/")

        if 'about campus life' in query:
            f = 'Opening .'
            engine.say(f)
            engine.runAndWait()
            webbrowser.open("https://www.citchennai.edu.in/campus-life/")



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

