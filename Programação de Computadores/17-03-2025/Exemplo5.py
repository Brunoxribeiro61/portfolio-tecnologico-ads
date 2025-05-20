import math
sombra = float(input("Digite o comprimento da sombra em metros:"))
angulo = math.radians(float(input("Digite o angulo em graus:")))
altura = math.tan(angulo)* sombra

print("Altura do prédio é :", altura)

input("Pressione enter para sair")
