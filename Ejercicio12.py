vahorros = []
ahorros_total = 0
for i in range(1,13):
    print("Cuanto has ahorrado este mes?")
    vahorros = int(input())
    ahorros_total = vahorros + ahorros_total
print("Has ahorrado en total", ahorros_total)
print("Dime un mes, en forma de numero, del 0 al 11")
nummes = int(input())
print("En ese mes", vahorros[nummes])
acumulado = 0
for x in range(nummes+1):
    acumulado += vahorros[x]
print("En ese mes ahorraste acumulados", acumulado)
