from cmath import inf
print("Dime el numero")
num = int(input())
resultado = 1
for num in range(1,num+1):
    resultado = resultado * num 

print("El factorial de", num,"es",resultado)


