import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import json
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0) and (hour < 12):
        speak("Good Morning")
    elif (hour >= 12) and (hour < 18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am watson sir. In your service")
    speak("How can i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("Boss said :", query)
    except Exception:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to wikipedida")
            print(results)
            speak(results)

        elif 'open microsoft edge' in query:
            speak("ok . Opening Microsoft edge")
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk"
            os.startfile(path)

        elif 'open youtube' in query:
            speak("Ok . Opening youtube")
            webbrowser.open("https://www.youtube.com/?gl=IN")

        elif 'open google' in query:
            speak("Ok . Opening google")
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
            os.startfile(path)

        elif 'play music' in query:
            speak("ok . Playing music for you")
            music_dir = 'E:\\music\\'
            songs = os.listdir(music_dir)
            print(songs)
            for i in range(2):
                os.startfile(os.path.join(music_dir, songs[i]))

        elif 'open pycharm' in query:
            speak("ok . Opening pycharm")
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition " \
                   "2020.2.3.lnk "
            os.startfile(path)

        elif 'open vs code' in query:
            speak("ok . opening Visual Studio Code")
            path = "C:\\Users\\sahil\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio " \
                   "Code\\Visual Studio Code.lnk "
            os.startfile(path)

        elif 'open mc antivirus' in query:
            speak("Ok . opening MC Afee Antivirus")
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\McAfee\\McAfee AntiVirus.lnk"
            os.startfile(path)

        elif 'news about technology' in query:
            speak("ok . reading news about technology")
            url = "http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey" \
                  "=61b75da2a08c462dbf43d3307d796f5d "
            news = requests.get(url).text
            news = json.loads(news)
            print(news["articles"])
            arts = news['articles']
            for a in arts:
                speak(a['title'])
                speak("Moving to next news")
            speak("Thanks for listening")

        elif 'news about business' in query:
            speak("ok . reading news about business")
            url = "http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey" \
                  "=61b75da2a08c462dbf43d3307d796f5d "
            news = requests.get(url).text
            news = json.loads(news)
            print(news["articles"])
            arts = news['articles']
            for a in arts:
                speak(a['title'])
                speak("Moving to next news")
            speak("Thanks for listening")

        elif 'news about sports' in query:
            speak("ok . reading news about sports")
            url = "http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey" \
                  "=61b75da2a08c462dbf43d3307d796f5d "
            news = requests.get(url).text
            news = json.loads(news)
            print(news["articles"])
            arts = news['articles']
            for a in arts:
                speak(a['title'])
                speak("Moving to next news")
            speak("Thanks for listening")

        elif 'news about health' in query:
            speak("ok . reading news about health")
            url = "http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey" \
                  "=61b75da2a08c462dbf43d3307d796f5d "
            news = requests.get(url).text
            news = json.loads(news)
            print(news["articles"])
            arts = news['articles']
            for a in arts:
                speak(a['title'])
                speak("Moving to next news")
            speak("Thanks for listening")

        elif 'news about science' in query:
            speak("ok . reading news about science")
            url = "http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey" \
                  "=61b75da2a08c462dbf43d3307d796f5d "
            news = requests.get(url).text
            news = json.loads(news)
            print(news["articles"])
            arts = news['articles']
            for a in arts:
                speak(a['title'])
                speak("Moving to next news")
            speak("Thanks for listening")

        elif 'open government mail service' in query:
            speak("Ok . opening email.gov.in")
            webbrowser.open("email.gov.in")
