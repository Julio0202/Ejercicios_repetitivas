horastotales = 0
print("Cuantos trabajadores tienes")
trabajadores = int(input())
print("Cuanto cobras por hora")
dinero = int(input())
for x in range(1,7):
    print("Cuántas horas has trabajado")
    horas = int(input())
    horastotales = horas + horastotales
print("El sueldo de los", trabajadores,"son de",horastotales*dinero,"en total")
print("La empresa pago en total de", trabajadores*horastotales*dinero)