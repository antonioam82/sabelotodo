import wikipedia
import win32com.client as wc
from gtts import gTTS
import re
import platform
from VALID import ns, direc

wikipedia.set_lang('es')
speak=wc.Dispatch("Sapi.SpVoice")
s = platform.system()

def habla(t):
    if t!="":
        try:
            #REPRODUCE AUDIO
            if t!="":
                pagina = wikipedia.page(t)
                summ = pagina.summary
                print("\n"+summ+"\n")
                text = re.sub("\[\d+\]"," ",summ)
                #text = re.sub("km²","kilometros cuadrados",text)
                if s == "Windows":
                    speak.Speak(text)
                else:
                    print("\nSONIDO NO DISPONIBLE")
                #GUARDA AUDIO
                aud = ns(input("¿Descargar audio?: ")).lower()
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
    else:
        print("INTRODUZCA TEMA DE BÚSQUEDA")
        
while True:
    tema = input("Introduce tema: ")
    habla(tema)
    conti = ns(input("¿Continuar?: "))
    if conti == "n":
        break
