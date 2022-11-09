pagadototal = 10
vmes = []
for i in range(1,21):
    pagadototal = pagadototal*2
    vmes.append(pagadototal)
print("En total pagastes", pagadototal)
print("Dime en que mes")
x = int(input())
print("En ese mes pagastes", vmes[x-1])