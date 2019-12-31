import wikipedia
import win32com.client as wc
from VALID import ns

wikipedia.set_lang('es')
speak=wc.Dispatch("Sapi.SpVoice")

def habla(t):
    #try:
    summ = wikipedia.summary(t,sentences = 2)
    speak.Speak(summ)
    #except:
        #print("Va a ser que no...")
        

while True:
    tema = input("Introduce tema: ")
    habla(tema)
    conti = ns(input("¿Continuar?: "))
    if conti == "n":
        break
        
