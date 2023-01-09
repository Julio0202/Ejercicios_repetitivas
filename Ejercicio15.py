pagadototal = 0
vmes = []
pagadomes = 0
for i in range(1,21):
    vmes.append(pagadomes)
    pagadototal = pagadomes + pagadototal
print("Has pagado un total de", pagadototal)
print("Dime el mes que quieres saber cuanto has pagado")
xx = int(input())
print(vmes[xx])