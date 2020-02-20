# -*- coding: utf-8 -*-
import wikipedia
from gtts import gTTS
import re
import platform
from locale import getdefaultlocale
#from VALID import ns, direc, OKI

fin = False
alter = "INTRODUCIR NUEVO TÉRMINO DE BÚSQUEDA"
audio = "n"
s = platform.system()
desam = False
i,s = getdefaultlocale()
idioma_local = (i.split("_"))[0]

expre = ["\[cita requerida\]","\[\d+\]","===","=="]
opcion_cont = ["NO GUARDAR","GUARDAR UN AUDIO","GUARDAR ARCHIVO DE TEXTO"]

def titulo():
    print("***********************************")
    print("*                                 *")
    print("*           SABELOTODO            *")
    print("*                                 *")
    print("***********************************")

def OKI(n):
    try:
        n=int(n)
    except:
        n=OKI(input("Caracter no válido: "))
    return n

def direc():
    import os
    while True:
        nueva_ruta=input("Introduzca ruta: ")
        if os.path.isdir(nueva_ruta):
            os.chdir(nueva_ruta)
            break
        else:
            print("RUTA NO VALIDA")

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)

def busca_idioma(i):
    try:
        while not i in wikipedia.languages():
            i = input("Input no válido: ")
        return i
    except:
        print("FALLO AL ESTABLECER EL IDIOMA")

def enum(opcions):
    global fail
    for i,opcion in enumerate(opcions):
        print(i,opcion)
    eleccion = OKI(input("Introduzca número correspondiente a su opción: "))
    while eleccion > (len(opcions)-1):
        eleccion = OKI(input("Introduzca indice válido correspondiente a su opción: "))
    assert eleccion in range(len(opcions))
    tex_elec = opcions[eleccion]
    fail = False
    return tex_elec
    
def crea_audio(ti,te):
    direc()
    nom = ti+".mp3"
    print("Generando archivo",nom)
    try:
        if idioma == None:
            tts = gTTS(te, lang=idioma_local)
        else:
            tts = gTTS(te, lang=idioma)
        tts.save(nom)
        print("Generado archivo", nom)
    except:
        print("IDIOMA NO SOPORTADO")

def genera_archivo(ti,te,op):
    if op == "GUARDAR UN AUDIO":
        crea_audio(ti,te)
    else:
        crea_documento(ti,te)

def finaliza():
    global fin
    fin = True

def crea_documento(tit,te):
    direc()
    nom = tit+".txt"
    documento=open(nom,"w",encoding="utf-8")
    linea=""
    for c in te:
        linea=linea+c
        if len(linea)==90:
            documento.write(linea+"\n")
            linea=""
    documento.write(linea)#FINAL
    documento.close()
    print("Generado archivo",nom)

def desamb(tem):
    global fail, desam
    posibles_temas = wikipedia.search(tem)
    if len(posibles_temas)>0:
        desam = True
        if not alter in posibles_temas:
            posibles_temas.append(alter)
        print("********DESAMBIGUACIÓN********")
        print("'\'"+tem+"'\' puede referirse a:")
        ele_tema = enum(posibles_temas)
        if ele_tema!="INTRODUCIR NUEVO TÉRMINO DE BÚSQUEDA":
            habla(ele_tema)
        else:
            fail=True
            main_func()

def habla(t):
    if t!="" and t!=".":
        try:
            print("ACCEDIENDO...")
            pagina = wikipedia.page(t)
            print("ESCOJA OPCIÓN DE CONTENIDO.")
            ele_con = enum(["RESUMEN","TEXTO COMPLETO"])
            if ele_con == "RESUMEN":
                summ = pagina.summary
            else:
                summ = pagina.content
            global titulo
            global text
            global fail
            titulo = pagina.title.upper()
            print("\n"+titulo+"\n")
            print("\n"+summ+"\n")
            text = summ
            for i in expre:
                text = re.sub(i,"",text)
            if audio == "s":
                #REPRODUCE AUDIO
                speak.Speak(text)
        except:
            print("NO SE PUDO COMPLETAR LA ACCIÓN")
            fail = True
            #ERROR DE DESAMBIGUACION
            desamb(t)
    else:
        print("INTRODUZCA TEMA DE BÚSQUEDA")

titulo()
idioma = busca_idioma(input("Seleccione idioma: "))
if idioma == None:
    wikipedia.set_lang(idioma_local)
else:
    wikipedia.set_lang(idioma)

if s == "cp1252" and idioma == idioma_local:
    audio = ns(input("¿Activar audio?(n/s): ").lower())
    if audio == "s":
        import win32com.client as wc
        speak=wc.Dispatch("Sapi.SpVoice")

def main_func():
    global desam
    while fin == False:
        tema = input("\nIntroducir término de busqueda: ")
        habla(tema)
        if fail == False and tema != "" and fin == False:
            print("****OPCIONES DE GUARDADO****")
            aud = enum(opcion_cont)#ns(input("¿Descargar un audio?: ")).lower()
            if aud != "NO GUARDAR":
                try:
                    genera_archivo(titulo,text,aud)
                except:
                    print("NO SE PUDO COMPLETAR LA OPERACIÓN")
            if desam == True:
                #print("A")
                 print("\nARTÍCULOS RELACIONADOS: ",(wikipedia.search(tema))[:-1])
            else:
                #print("B")
                print("\nARTÍCULOS RELACIONADOS: ",wikipedia.search(tema))
           
        desam = False
        if fin == False:
            conti = ns(input("\n¿Desea continuar?(n/s): "))
            if conti == "n":
                finaliza()
            
main_func()

