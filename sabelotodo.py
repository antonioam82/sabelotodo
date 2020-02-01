import wikipedia
from gtts import gTTS
import re
import platform
from locale import getdefaultlocale
from VALID import ns, direc, OKI

s = platform.system()

i,s = getdefaultlocale()
idioma_local = (i.split("_"))[0]

def busca_idioma(i):
    try:
        while not i in wikipedia.languages():
            i = input("Input no válido: ")
            
        return i
    except:
        print("MALA CONEXIÓN.")

def crea_audio(ti,te):
    direc()
    nom = ti+".mp3"
    print("Generando archivo", nom)
    tts = gTTS(te, lang='es')
    tts.save(nom)
    print("Generado archivo", nom)

def desamb(tem):
    posibles_temas = wikipedia.search(tem)
    if len(posibles_temas)>1:
        print("********DESAMBIGUACIÓN********")
        print(tem,"puede referirse a:")
        for i,posible_tema in enumerate(posibles_temas):
            print(i,posible_tema)
        eleccion = OKI(input("Introduzca número correspondiente a su opción: "))
        if eleccion <= (len(posibles_temas)-1):
            assert eleccion in range(len(posibles_temas))
            habla(posibles_temas[eleccion])
        else:
            print("VALOR DE ENTRADA INCORRECTO")
    
def habla(t):
    if t!="":
        try:
            #REPRODUCE AUDIO
            if t!="":
                print("ACCEDIENDO...")
                pagina = wikipedia.page(t)
                summ = pagina.summary
                print("\n"+(pagina.title).upper()+"\n")
                print("\n"+summ+"\n")
                text = re.sub("\[\d+\]","",summ)
                #text = re.sub("km²","kilometros cuadrados",text)\[cita requerida\]
                text = re.sub("\[cita requerida\]","",text)
                if audio == "s":
                    try:
                        speak.Speak(text)
                    except:
                        print("SONIDO NO DISPONIBLE")
                #GUARDA AUDIO
                aud = ns(input("¿Descargar un audio?: ")).lower()
                if aud == "s":
                    crea_audio(t,text)
                print("\nARTÍCULOS RELACIONADOS: ",wikipedia.search(tema))
        except:
            print("NO SE PUDO COMPLETAR LA ACCIÓN")
            #ERROR DE DESAMBIGUACION
            desamb(t)
    else:
        print("INTRODUZCA TEMA DE BÚSQUEDA")

idioma = busca_idioma(input("Seleccione idioma: "))
wikipedia.set_lang(idioma)

if s == "cp1252" and idioma == idioma_local:
    audio = ns(input("¿Activar audio?: ").lower())
    if audio == "s":
        import win32com.client as wc
        speak=wc.Dispatch("Sapi.SpVoice")

while True:
    tema = input("Introduce tema: ")
    if tema == ".":
        break
    habla(tema)
    #conti = ns(input("¿Continuar?: "))
    #if conti == "n":
        #break
        
        
