import wikipedia
import win32com.client as wc
from gtts import gTTS
from VALID import ns, direc

wikipedia.set_lang('es')
speak=wc.Dispatch("Sapi.SpVoice")

def habla(t):
    try:
        #REPRODUCE AUDIO
        summ = wikipedia.summary(t,sentences = 2)
        speak.Speak(summ)
        #GUARDA AUDIO
        aud = ns(input("¿Descarga audio?: ")).lower()
        if aud == "s":
            direc()
            nom = t+".mp3"
            print("Generando archivo", nom)
            tts = gTTS(summ, lang='es')
            tts.save(nom)
    except:
        print("NO SE PUDO COMPLETAR LA ACCIÓN")
        

while True:
    tema = input("Introduce tema: ")
    print("RELACIONADOS: ",wikipedia.search(tema))
    habla(tema)
    conti = ns(input("¿Continuar?: "))
    if conti == "n":
        break
        
