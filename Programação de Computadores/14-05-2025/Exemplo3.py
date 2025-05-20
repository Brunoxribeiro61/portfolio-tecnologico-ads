notas = [6, 7, 6.5, 4, 8, 9]
soma = 0
for i in range(6):
    soma = soma + notas[i]
    
media = soma / 6
print("A média das notas é: %.2f" % media)