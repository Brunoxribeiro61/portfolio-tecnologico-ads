n = int(input("Digite um valor inteiro e positivo para n: "))
if n <= 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    soma = 0
    for i in range(1, n + 1):
        soma += 1 / i

    print(f"A soma S é: {soma}")