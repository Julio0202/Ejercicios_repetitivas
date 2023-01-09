from cmath import inf
print("Dime el numero")
num = int(input())
resultado = 1
for i in range(1,num+1):
    resultado = resultado * i 

print("El factorial de", num,"es",resultado)


