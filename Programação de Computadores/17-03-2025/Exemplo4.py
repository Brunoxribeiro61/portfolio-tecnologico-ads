import math
raio = float(input("Digite o Raio da circunferência em cm: "))
comprimento = 2* math.pi * raio
area = math.pi * raio * raio

print("Comprimento da circunferência:", comprimento)
print("a área da circunferência é igual a %.2a cm²:" % area)

input("Pressione o enter para fechar")