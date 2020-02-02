import wikipedia
from gtts import gTTS
import re
import platform
from locale import getdefaultlocale
from VALID import ns, direc, OKI

audio = "n"
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

#wikipedia.set_lang('es')

def enum(opcions):
    for i,opcion in enumerate(opcions):
        print(i,opcion)
    eleccion = OKI(input("Introduzca número correspondiente a su opción: "))
    while eleccion > (len(opcions)-1):
        eleccion = OKI(input("Introduzca indice válido correspondiente a su opción: "))
    assert eleccion in range(len(opcions))
    tex_elec = opcions[eleccion]
    return tex_elec
    


def crea_audio(ti,te):
    direc()
    nom = ti+".mp3"
    print("Generando archivo", nom)
    tts = gTTS(te, lang=idioma)
    tts.save(nom)
    print("Generado archivo", nom)

def desamb(tem):
    posibles_temas = wikipedia.search(tem)
    if len(posibles_temas)>0:
        print("********DESAMBIGUACIÓN********")
        print(tem,"puede referirse a:")
        ele_tema = enum(posibles_temas)
        habla(ele_tema)

def habla(t):
    if t!="":
        try:
            #REPRODUCE AUDIO
            if t!="":
                print("ACCEDIENDO...")
                pagina = wikipedia.page(t)
                print("ESCOJA OPCIÓN DE CONTENIDO.")
                ele_con = enum(["RESUMEN","TEXTO COMPLETO"])
                if ele_con == "RESUMEN":
                    summ = pagina.summary
                else:
                    summ = pagina.content
                titulo = pagina.title.upper()
                print("\n"+titulo+"\n")
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
                    crea_audio(titulo,text)
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
        

        
        
