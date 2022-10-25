lista = []
contador = 0
contador_par = 0
print("Dime un numero")
num1 = int(input())
print("Dime otro numero")
num2 = int(input())
for i in range(num1,num2+1):
    if i%2==0:
        contador_par+=1 
    else:
        contador +=1
print(contador_par,"numeros pares")
print(contador,"numeros impares")