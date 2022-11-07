print("Dime la base")
base = int(input())
basetotal = base
print("Dime el exponente")
exponente = int(input())
for i in range(exponente-1):
    basetotal *= base
    print(basetotal)