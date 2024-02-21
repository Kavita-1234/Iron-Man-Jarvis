import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install SpeechRecognition
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
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

    speak("I am Jarvis maam. Please tell me how may I help you")

def takeCommand():
    #It take microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        #print(e)
        print("say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp_gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kumawatkavita1772@gmail.com', 'Kavita_123@1772')
    server.sendmail('kumawatkavita1772@gmail.com', to, content)
    server.close()

if __name__ =="__main__":
    speak("kavita is a good girl")
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()
    # logic for excuting tasks based on query
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stack overflow.com")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\HP\\OneDrive\\Desktop\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Ma'am, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open game' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Games\\Jewel Quest.lnk"
            os.startfile(codePath)
        
        
        
    