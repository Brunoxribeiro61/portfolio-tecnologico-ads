import math

graus = float(input("Digite o valor do ângulo em graus: "))

radianos = math.radians(graus)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print("Seno:", seno)
print("Cosseno:", cosseno)
print("Tangente:", tangente)
