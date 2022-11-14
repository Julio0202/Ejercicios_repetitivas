print("Dime cuantos numeros primos quieres mostrar")
numprimmostrar = int(input())
vnum = []
for i in range(1,numprimmostrar):
    vnum.append(int(range(1,numprimmostrar)%i==0))

print(vnum)