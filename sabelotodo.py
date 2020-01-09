import wikipedia
import win32com.client as wc
from gtts import gTTS
import re
from VALID import ns, direc

wikipedia.set_lang('es')
speak=wc.Dispatch("Sapi.SpVoice")

def habla(t):
    try:
        #REPRODUCE AUDIO
        pagina = wikipedia.page(t)
        summ = pagina.summary
        print("\n"+summ+"\n")
        text = re.sub("\[\d+\]","",summ)
        speak.Speak(text)
        #GUARDA AUDIO
        aud = ns(input("¿Descarga audio?: ")).lower()
        if aud == "s":
            direc()
            nom = t+".mp3"
            print("Generando archivo", nom)
            tts = gTTS(text, lang='es')
            tts.save(nom)
            print("Generado archivo", nom)
    except:
        print("NO SE PUDO COMPLETAR LA ACCIÓN")
    print("\nARTÍCULOS RELACIONADOS: ",wikipedia.search(tema))
        
while True:
    tema = input("Introduce tema: ")
    habla(tema)
    conti = ns(input("¿Continuar?: "))
    if conti == "n":
        break
        
