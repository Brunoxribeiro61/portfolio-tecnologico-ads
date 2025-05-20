# numero binario para decimal

binario = input("Digite um número binário: ")
n = len(binario) - 1
decimal = 0
for d in binario:
    decimal = decimal + int(d) * 2**n
    n = n - 1
print("O número binario ", binario, "em decimal é", decimal)