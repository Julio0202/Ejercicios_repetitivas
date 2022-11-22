from tkinter import *
from tkinter import ttk
from pytube import YouTube  
from pytube import Playlist

def descargaCancion(url:str):
    url = datos_entrada.get()
    youtube = YouTube(url)
    print(youtube.author)
    cancion = youtube.streams.get_audio_only()
    cancion.download
def descargarLista(url:str):
    playlist = Playlist(url)
    for cancion in playlist.videos:
        cancion.streams.get_audio_only().download("Canciones")
        print("Descargando cancion:", cancion.author)

ventana = Tk()
ventana.title("Descargar musica")
ventana.geometry("500x200")
ventana.resizable(False,False)
ventana.config(background="honeydew2")

datos_entrada  = ttk.Entry(ventana)
datos_entrada.place(x=175,y=80)
boton_descargar = ttk.Button(ventana, text="Descargar", command=descargaCancion)
boton_descargar.place(x=215,y=120)

label_titulo = ttk.Label(ventana, text="Introduce la url del video")
label_titulo.config(background="honeydew2")
label_titulo.place(x=175,y=50)













ventana.mainloop()