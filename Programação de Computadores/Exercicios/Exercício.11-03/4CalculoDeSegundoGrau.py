import math

# Qual o coeficientes da equação
a = float(input("Digite o valor do coeficiente a: "))
b = float(input("Digite o valor do coeficiente b: "))
c = float(input("Digite o valor do coeficiente c: "))

# Calcula o discriminante (delta)
delta = b**2 - 4*a*c

# Verifica se as raízes são reais
if delta < 0:
    print("As raízes não são reais.")
else:
    # Calculo das duas raízes usando a fórmula de Bhaskara
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    
    # Exibir as raizes
    print(f"As raízes da equação são: {raiz1:.2f} e {raiz2:.2f}")

# Comando para fechar o programa
input("Pressione Enter para sair...")