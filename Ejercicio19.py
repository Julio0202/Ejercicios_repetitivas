def pintaMenu():
    comodin = 0
    while (comodin<1 or comodin>5):
        print("1-Insertar Contacto\n 2-Borrar contacto\n 3-Buscar contacto\n 4-Ver todos los contactos\n 5-Salir")
        vnomb = []
        vtelef = []
        try:
            print("Inserta el número de lo que quieres hacer")
            comodin = int(input())
        except:
            print("Las opciones son del 1 al 5") 
    return comodin
comodin = pintaMenu()
while (comodin!=5):
    print("Has seleccionado",pintaMenu())
    comodin = pintaMenu()
