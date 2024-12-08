import speech_recognition as sr 
import pyttsx3
import logging
import os
import datetime
import webbrowser
import wikipedia

# this is logger
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR,exist_ok = True)
log_path = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path ,
    format = "[%(asctime)s ] %(name)s - %(levelname)s - %(message)s ",
    level = logging.INFO
)

# taking male voice 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()as source :
        print("Lisening.......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try :
       print("Recognizing......")
       query = r.recognize_google(audio,lanugaue = "en-in")
       print(f"user said : {query}\n")
    except Exception as e:
        logging.info(e)
        print("Say that Again Please")
        return "None"
    return query


# this function will greet you
def wish_me():
    hour = (datetime.datetime.now().hour)

    if hour >=  0 and hour<=12 :
        speak("Good Morning  sir!,How are you doing")
    elif hour >= 12 and hour<=18 :
        speak("Good Afternoon sir!,How are you doing")   
    else :
        speak("Good evening sir!,How are you doing") 
    speak("I am JARVIS,Tell me sir How can i help you?")



wish_me()
while True:
    query = takecommand()
    if "time" in query:
        speak(f"hi sir the time is {datetime}")


