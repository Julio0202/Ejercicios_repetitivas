print("Dime la cantidad de numeros")
cantidad = int(input())
numfin=0
menor = 0
mayor = 0
iguales_cero = 0
while numfin!=cantidad:
    print("Dime los numeros")
    num = int(input())
    numfin +=1
    if num<0:
        menor=menor+1
    if num>0:
        mayor=mayor+1
    if num==0:
        iguales_cero=iguales_cero+1
print("Hay un total de",mayor,"numeros mayores que 0,",menor,"numeros menores que el 0, y",iguales_cero,"numeros iguales a cero")
