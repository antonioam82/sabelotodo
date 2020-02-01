# /usr/bin/env python
# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-
import wikipedia
from gtts import gTTS
import re
from VALID import ns, direc, OKI

lista_exren = ["RESUMEN","TEXTO COMPLETO"]

def busca_idioma(i):
    try:
        while not i in wikipedia.languages():
            i = input("Input no válido: ")
        return i
    except:
        print("MALA CONEXIÓN.")

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
    contenido = ""
    if t!="":
        try:
            #REPRODUCE AUDIO
            if t!="":
                pagina = wikipedia.page(t)
                print("ESCOJA OPCIÓN DE CONTENIDO.")
                ele_con = enum(lista_exren)
                print("ACCEDIENDO...")
                if ele_con == "RESUMEN":
                    summ = pagina.summary
                    for i in summ:
                        contenido = contenido+i
                else:
                    summ = pagina.content
                print("\n"+(pagina.title).upper()+"\n")
                print("\n"+summ+"\n")
                #GUARDA AUDIO
                fil = ns(input("¿Descargar artículo?: ")).lower()
                if fil == "s":
                    text = re.sub("\[\d+\]","",summ)
                    text = re.sub("\[cita requerida\]","",text)
                    text = re.sub("\[==\]","",text)
                    print("TIPO DE ARCHIVO")
                    tip = enum(["ARCHIVO DE TEXTO","ARCHIVO DE AUDIO"])
                    if tip == "ARCHIVO DE TEXTO":
                        print("ACCIÓN AUN NO DISPONIBLE")
                    else:
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

while True:
    tema = input("Introduce tema: ")
    if tema == ".":
        break

    habla(tema)
