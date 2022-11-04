primo = 0
primito =0
print("Dime un numero")
num = int(input())
for i in range(2,num):
    if num%i==0:
        primito = primito + 1 
if primito >= 1:
    print("El numero no es primo")
else:
    print("Tu numero es primo")



