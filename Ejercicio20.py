Vnum=[]
num_pri=0
i=2
print("Dime un numero")
numerodeprim=int(input())
contador = numerodeprim
def numero_primo(numero:int):
    num_primo=0
    for i in range (2,numero):
        if numero%i==0:
            num_primo+=1
    if num_primo>=1:
        return False
    else:
        return True
while contador>0:
    if numero_primo(i)==True:
        Vnum.append(i)
        contador-=1
    i+=1
print("Los numeros primos son",Vnum)    