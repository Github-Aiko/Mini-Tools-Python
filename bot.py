import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
import random


# obtain audio from the microphone
print("Aiko Bot Listening...")
r = sr.Recognizer()

def savefile(text):
    # save file text to file
    with open("text.txt", "w") as f:
        f.write(text)

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

with sr.Microphone() as source:
    # read the audio data from the default
    # Until not receiving the signal
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    try:
        text = r.recognize_google(audio_data, language="en-US")
    except:
        text = ""
    print(text)

    if text == "":
        aiko_bot = "Sorry, I don't hear you say anything, what do you want to say to me?"
        speak(aiko_bot)
    elif text == "hello":
        aiko_bot = "Hello, how are you?"
        speak(aiko_bot)
    elif text == "I'm fine":
        aiko_bot = "That's great, I'm fine too"
        speak(aiko_bot)
    
savefile(text)

    