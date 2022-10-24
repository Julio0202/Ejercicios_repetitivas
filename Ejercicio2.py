import random 
numalateorio = random.randint(1,100)
intentos = 0
num = 0
comodin = 0
print(numalateorio)
while intentos!=10 or num!=numalateorio or comodin==2:
    print("Dime el numero")
    num = int(input())
    if num!=numalateorio and num>numalateorio:
        intentos +=1
        print("Has fallado tienes",intentos,"intentos","y el numero es mayor que el introducido")
    if num!=numalateorio and num<numalateorio:
        intentos +=1
        print("Has fallado tienes",intentos,"intentos","y el numero es menor que el introducido")
    if num==numalateorio:
        comodin = 2

print("Has adivinado","en",intentos,"intentos")