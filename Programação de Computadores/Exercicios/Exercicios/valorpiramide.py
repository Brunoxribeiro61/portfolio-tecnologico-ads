h = float(input("Digite a altura do tronco da pirâmide (h): "))
Bmenor = float(input("Digite o valor da base menor (Bmenor): "))
Bmaior = float(input("Digite o valor da base maior (Bmaior): "))
volume = h / 3 * (Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)

print("O volume do tronco da pirâmide é:", volume)