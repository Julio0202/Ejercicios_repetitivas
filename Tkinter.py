from tkinter import *
from tkinter import ttk

#Generar la ventana
ventana = Tk()
ventana.title("Primer ejercicio")
ventana.geometry("300x100")
ventana.resizable(width=False,height=False)
ventana.config(background="cum")
#Generar el lienzo para pintar componentes
frm = ttk.Frame(ventana, padding=10).pack()
#Componentes Label y button
labelTexto = ttk.Label(frm, text = "Hola Tkinter") 
labelTexto.config(background="red",border=5,font=("Arial",15))
labelTexto.pack()
ttk.Button(frm, text="Salir", command=ventana.destroy).pack()
#
ventana.mainloop()