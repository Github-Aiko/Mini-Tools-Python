import speech_recognition as sr
from gtts import gTTS
import webbrowser
import os
import time
import playsound
import random


# obtain audio from the microphone
print("Aiko Bot Listening...")
r = sr.Recognizer()

def write(text):
    with open("log.txt", "a") as f:
        f.write(text)

def speak(text):
    tts = gTTS(text=text, lang="vi")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

while True:
    with sr.Microphone() as source:
    # read the audio data from the default
    # Until not receiving the signal
        audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    try:
        text = r.recognize_google(audio_data, language="vi-VN")
    except:
        text = ""
    print(text)

    if text in "":
        continue
    if "chào" in text:
        speak("Chào bạn")
    elif text in "Mở Google":
        aiko_bot = "Bạn muốn tìm kiếm gì ở google ?"
        speak(aiko_bot)
        with sr.Microphone() as source:
            audio_data = r.record(source, duration=5)
            print("Recognizing...")
            try:
                text = r.recognize_google(audio_data, language="vi-VN")
            except:
                text = ""
            print(text)
            aiko_bot = "Đang tìm kiếm " + text + " trên google"
            speak(aiko_bot)
            webbrowser.open("https://www.google.com/search?q=" + text)
            time.sleep(2)
    elif text in "Mở YouTube":
        aiko_bot = "Bạn muốn tìm kiếm gì ở youtube ?"
        speak(aiko_bot)
        with sr.Microphone() as source:
            audio_data = r.record(source, duration=5)
            print("Recognizing...")
            try:
                text = r.recognize_google(audio_data, language="vi-VN" or "en-US" or "jp-JP")
            except:
                text = ""
            print(text)
            aiko_bot = "Đang tìm kiếm " + text + " trên youtube"
            speak(aiko_bot)
            webbrowser.open("https://www.youtube.com/results?search_query=" + text)
            time.sleep(2)
    elif text in "Mở Facebook":
        aiko_bot = "Đang mở facebook cho bạn"
        speak(aiko_bot)
        # mở trình duyệt safari và tìm kiếm text
        webbrowser.open("https://www.facebook.com/")
        time.sleep(2)
    elif text in "Mở Zalo":
        aiko_bot = "Đang mở zalo cho bạn"
        speak(aiko_bot)
        webbrowser.open("start safari https://zalo.me/")
        time.sleep(2)
    elif text in ["tạm biệt", "bye", "goodbye", "Xéo", "Đi chỗ khác chơi"]:
        speak("Bye Bạn")
        break
    else:
        aiko_bot = "Xin lỗi, tôi không hiểu"
        speak(aiko_bot)
        time.sleep(5)

write(text)