
from sqlite3 import TimestampFromTicks
import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
rate=engine.getProperty("rate")
engine.setProperty("rate",180)
#translate = Translator()


def talk(text):
    engine.say(text)
    engine.runAndWait()

engine.say("voice assistant activation...")
engine.say("hello sir , i am jarvis " )


engine.runAndWait()
""""
with sr.Microphone() as source:
    print("listening....")
    listener.enegrgy_threshold=10000
    listener.adjust_for_ambient_noise(source,1)
    voice = listener.listen(source)
    command = listener.recognize_google(voice)
    command = command.lower() 
    print(command)"""

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            listener.enegrgy_threshold=10000
            listener.adjust_for_ambient_noise(source,1)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower() 
            print(command)
            """if "jarvis" in command:
                commamd= command.replace("jarvis"," ")
                print(command)"""
    except:
        pass
    return command

def run_jarvis():
    
    command = take_command()

    if "hi"  in command or "hello" in command:
        talk(" hi sir ,what can i do for you")

    elif "fine" in command:
        talk("ok sir what can i do for you") 
    
    elif "speeching test" in command or "audio checking " in command:
        talk("yes sir i can hear you.")
    
    elif "who create you" in command or "when do you born" in command or "how old are you" in command:
        talk("mr.ponraj create me as a prototype on 02 May 2022,7.06.40 PM ")
    
    elif "how are you"  in command  or "how was the day"  in command or "what's up buddy" in command:
        talk("i m having a good day sir ")
        talk(" what about you") 
    elif "who are you " in command :
        talk("I am jarvis , voice assistant proto type.")
    
    elif "where are you" in command:
        talk("inside your heart")

    elif "not good" in command: 
        talk("don't worry sir, better days on their ways")
        talk("what can i do for you")

    elif "that's ok" in command:
        talk("Hmm")

    elif "play" in command:
        song=command.replace("play", " ")
        talk("playing" + song)
        print("playing")
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I : %M %p')
        print(time)
        talk("current time is " + time)

    elif "who is" in command:
        person =command.replace("who is "," ")
        info =wikipedia.summary(person,2)
        print(info)
        talk(info)

    elif "are you single" in command:
        talk('no , i have a relationship with wifi')

    elif " thank you" in command :
        talk("that's my pleasure ")

    elif "tell me a joke" in command:
        talk(pyjokes.get_joke())

    else:
        talk("please say that command again")
while True:
    try:
        run_jarvis()
    except UnboundLocalError :
        talk("thank you sir")
        print(" ")
        break

    
"""
engine.say("hello sir , i am jarvis " )
engine.say("how are you sir")

with sr.Microphone() as source:
    print("listening....")
    listener.enegrgy_threshold=10000
    listener.adjust_for_ambient_noise(source,1)
    voice = listener.listen(source)
    command = listener.recognize_google(voice)
    command = command.lower() 
    print(command)

if "what about you " in command:
    talk("i having a good day sir")
engine.say("what can i do for you")
engine.runAndWait()


    elif "music" in  command:
        music=command.replace("music"," ")
        talk("playing on "+ music)
        print("playing ",+music)
        

    
"""
