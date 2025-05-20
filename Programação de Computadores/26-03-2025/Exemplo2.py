# Exemplo 2

quarto = str.upper(input("Digite o tipo de quarto (S para simples, D para duplo, T para triplo): "))
diaria = float(input("Digite a quantidade de diária: "))

s = diaria * 255.50
d = diaria * 305.50
t = diaria * 360.50

if quarto == str("S"):
    print(f"Valor do quarto simples: R$ {s:.2f}")
elif quarto == str("D"):
    print(f"Valor do quarto duplo: R$ {d:.2f}")
elif quarto == str("T"):  
    print(f"Valor do quarto triplo: R$ {t:.2f}")
else:
    print("Quarto não encontrado")
