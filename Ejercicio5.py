caracter = str
while caracter!=" ":
    print("Dime un caracter en minusculas")
    caracter = str(input())
    if caracter==" ":
        print("Ha acabado el programa")
    if caracter=="a" or caracter=="e" or caracter=="o" or caracter=="i" or caracter=="u":
        print("Es VOCAL")
    elif caracter!="a":
        print("NO ES VOCAL")
