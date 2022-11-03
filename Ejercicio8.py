from ast import NotIn
from typing import List
numinf = 0
numsup = 0
print("Dime el limite inferior")
numinf = int(input())
print("Dime el limite superior")
numsup = int(input())
vlist = []
while numinf > numsup:
    print("Dime el limite inferior")
    numinf = int(input())
    print("Dime el limite superior")
    numsup = int(input())
    if numinf < numsup:
        print("Vuelve a introducir el numero inferior e superior")
vlist = list(range(numinf,numsup))
num3=0
numerosfuera = 0
numtotal = 0
numlim = 0
comodin = 0
while comodin==0:
    print("Dime un número, y si introduces el 0 acaba el programa")
    num3 = int(input())
    if ((num3 not in vlist)):
        numerosfuera += 1 
    if ((num3 in vlist)):
        numtotal = numtotal+num3
    if num3 == numinf:
        numlim = numlim + 1 
    elif num3 == numsup:
        numlim = numlim + 1 
    if num3 == 0:
        comodin = 1
print("numeros fuera del intervalo:",numerosfuera)
print("La suma es:",numtotal)
print("Has introducido el numero del limite un total de", numlim,"veces")