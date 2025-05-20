# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par
if numero % 2 == 0:  # Se o resto da divisão do número por 2 for 0, o número é par
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")