import random 
numalateorio = random.randint(1,100)
intentos = 1
num = 0
comodin = 0
print(numalateorio)
while intentos!=10 and num!=numalateorio:
    print("Dime el numero")
    num = int(input())
    if num!=numalateorio and num>numalateorio:
        intentos +=1
        print("Has fallado, has hecho",intentos,"intentos","y el numero es mayor que el introducido")
    if num!=numalateorio and num<numalateorio:
        intentos +=1
        print("Has fallado, has hecho",intentos,"intentos","y el numero es menor que el introducido")
    if intentos==10:
        print("Has fallado")
if num==numalateorio:
    print("Has adivinado","en",intentos,"intentos")