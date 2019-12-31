import wikipedia
import win32com.client as wc
from gtts import gTTS
from VALID import ns

wikipedia.set_lang('es')
speak=wc.Dispatch("Sapi.SpVoice")

def habla(t):
    try:
        #REPRODUCE AUDIO
        summ = wikipedia.summary(t,sentences = 2)
        speak.Speak(summ)
        #GUARDA AUDIO
        tts = gTTS(summ, lang='es')
        tts.save(t+".mp3")
    except:
        print("Va a ser que no...")
        

while True:
    tema = input("Introduce tema: ")
    habla(tema)
    conti = ns(input("¿Continuar?: "))
    if conti == "n":
        break
        
