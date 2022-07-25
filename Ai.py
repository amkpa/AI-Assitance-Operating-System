import cv2
import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice into text
def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('hckjamki89@gmail.com','BaB7@123')
    server.sendmail('hckjamki89@gmail.com', to, content)
    server.close()

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis sir. please tell me how can i help you")


if __name__ == "__main__":
    wish()
    #while True:
    if 1:

        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\Windows\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\Users\\amitk\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                  os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip} ")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            #print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open flipkart" in query:
            webbrowser.open("www.flipkart.com")

        elif "open amazon" in query:
            webbrowser.open("www.amazon.com")

        elif "open linkedin" in query:
            webbrowser.open("www.linkedin.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+918249424236", "pela",13,42)


        elif "play songs on youtube" in query:
            kit.playonyt("dura akash mu uda chadae")

        elif "email to amit" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "amitkumarpalai3@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to amit")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this mail to amit")
