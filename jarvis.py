import os
import time
from time import ctime
import random
import webbrowser
import speech_recognition as sr
import playsound
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="it")
    r = random.randint(1, 1000000)
    filename = "voce-" + str(r) + ".mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language="it")
            print(said)
        except sr.UnknownValueError:
            print("")
    return said.lower()

def respond(said):
    if "ciao" in said:
        speak("Ciao, come stai?")
        answer = get_audio()
        if "bene" in answer:
            speak("Sono felice per te!")
        elif "male" in answer:
            speak("Mi dispiace tanto, spero di poterti aiutare")
    elif "come ti chiami" in said:
        speak("Mi chiamo Jarvis")
    elif "che ore sono" in said:
        speak(ctime())
    elif "cerca" in said:
        speak("Che cosa vuoi cercare?")
        search = get_audio()
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        speak("Ecco cosa ho trovato per " + search)
    elif "esci" in said:
        speak("Arrivederci!")
        exit()

time.sleep(1)
speak("Ciao sono Jarvis, come ti chiami?")
name = get_audio()
speak("Ciao " + name + ", come posso aiutarti?")
while 1:
    wake = get_audio()
    if "jarvis" in wake:
        speak("Sono al tuo servizio")
        t_end = time.time() + 5
        while time.time() < t_end:
            said = get_audio()
            respond(said)
        print("Tempo finito")