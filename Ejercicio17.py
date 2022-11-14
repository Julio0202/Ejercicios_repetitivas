horastrabajadas = 0
horastrabajadastotales = 0
print("Dime cuanto cobras por hora")
euroshora = int(input())
print("Dime cuantos trabajadores tienes")
trabajadores = int(input())
print("Dime cuantas dias has trabajado")
diastrabaj = int(input())
for i in range(1,diastrabaj):
    print("Dime cuantas horas has trabajado, en ese dia")
    horastrabajadas = int(input())
    horastrabajadastotales = horastrabajadastotales + horastrabajadas
print("El sueldo semanal de los trabajadores es", euroshora*horastrabajadastotales*diastrabaj)
print("La empresa pagó por",euroshora*horastrabajadastotales*diastrabaj*trabajadores)