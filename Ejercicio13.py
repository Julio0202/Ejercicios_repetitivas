horastotales = 0
for x in range(1,7):
    print("Dime las horas que has trabajado en este día")
    horas = int(input())
    horastotales = horastotales + horas
cobrahorastotales = 0
print("Dime lo que cobras a la hora")
cobrahoratotales = int(input())
for x in range(1,7):
    print("Dime las horas que trabajastes en cada día")
    cobrahora = int(input())
    cobrahorastotales = cobrahorastotales + cobrahora
print("Has trabajado un total de", horastotales,"horas")
print("El sueldo que recibira es de", cobrahorastotales)
