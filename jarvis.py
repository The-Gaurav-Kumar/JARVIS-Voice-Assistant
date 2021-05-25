import pyttsx3#text-to-speech library
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
#speech api inbult voice intake/synthesis and recorgization
#getting details of current voice
voices = engine.getProperty('voices')

#to set voice property of engine
engine.setProperty('voice',voices[0].id)
#print(voices[0].id)
#voices[0].id for boys voice
def speak(audio):
    engine.say(audio)
    engine.runAndWait()#without this speech will not be audible to us

def wishMe():
    hour = int(datetime.datetime.now().hour)
    #0-24
    if hour>=0 and hour<12:
        speak("Good Morning Sir,")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else :
        speak("Good Evening Sir")
    speak("I am Jarvis. Please tell me how can i help you master")

def takeCommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 0.5
        #ctrl + click for details
        #seconds of non speaking audio before a phasse is considered  complete
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        #r.adjust_for_ambient_noise(source, duration=1)
        #speech recognition module
        #catch error
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        #english India
        print(f"User said: {query}\n")#fstring
    except Exception:
        #print(e)
        #exception printing
        print("Sorry Sir please Say that again")
        return "None"
        #None string is returned
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("thegauravkumar786@gmail.com","Gk@20july2001")
    server.sendmail("thegauravkumar786@gmail.com", to , content)
    server.close()

if __name__ == "__main__":
    wishMe()#function call
    while True :
        query = takeCommand().lower()
        if 'wikipedia' in query :
            speak('Searching Wikipedia...')
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/?gl=IN&tab=r1")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\sanja\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to= "sanjayamuz@gmail.com"
                sendEmail(to,content)
                speak("Emal has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am unable to send mail")
        
        elif 'quit' in query:
            speak("Have a good day sir, bye")
            exit()


