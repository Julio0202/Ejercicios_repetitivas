from pytube import YouTube  
from pytube import Playlist
from tkinter import *
from tkinter import ttk
def descargaCancion(url:str):
    youtube = YouTube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion = youtube.streams.get_audio_only()
    cancion.download
def descargarLista(url:str):
    playlist = Playlist(url)
    for cancion in playlist.videos:
        cancion.streams.get_audio_only().download("Canciones")
        print("Descargando cancion:", cancion.author)
url = "https://www.youtube.com/watch?v=HKNz0DWQXZw&list=PLVwXkzK42QWrWyeunQ_hi4OM8iUrBWUlq"

def saludar():
    texto = campoTexto.get()
    textoLabel.set(texto)

#Generar la ventana
ventana = Tk()
ventana.title("Primer ejercicio")
ventana.geometry("500x500")
ventana.resizable(width=False,height=False)
ventana.config(background="black")
ventana.iconbitmap()

#Generar el lienzo para pintar componentes
frm = ttk.Frame(ventana, padding=20).pack()

#Componentes Label y button
textoLabel = StringVar()
textoLabel.set("Hola tkinter")
labelTexto = ttk.Label(frm, textvariable=textoLabel) 
labelTexto.config(background="red",border=5,font=("Arial",15))
labelTexto.pack()

#Componente cuadro de texto 
campoTexto = ttk.Entry(frm) 
campoTexto.pack()



ttk.Button(frm, text="Saludo", command=descargaCancion(url)).pack()
ttk.Button(frm, text="Salir", command=ventana.destroy).pack()
ventana.mainloop()