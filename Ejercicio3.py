introducido = 0
comodin = 1
sumatotal = 0
media = 0
while comodin!=0:
    print("Dime un numero")
    introducido = int(input())
    sumatotal = introducido + sumatotal
    media +=1
    if introducido==0:
        comodin=0
print("La suma es", sumatotal)
print("La media es", sumatotal/(media-1))
