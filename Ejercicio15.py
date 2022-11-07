pagadototal = 0
vmes = []
for i in range(1,21):
    print("Dime cuanto has pagado ese mes")
    pagadomes = int(input())
    vmes.append(pagadomes)
    pagadototal = pagadomes + pagadototal
print("Has pagado un total de", pagadototal)
print("Dime el mes que quieres saber cuanto has pagado")
xx = int(input())
print(vmes[xx])