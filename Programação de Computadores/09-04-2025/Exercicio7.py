n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
if media >= 9.0:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6.0:
    conceito = "C"
elif media >= 4.0:
    conceito = "D"
else:
    conceito = "E"
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")
if conceito in ["A", "B", "C"]:
    print("APROVADO")
else:
    print("REPROVADO")