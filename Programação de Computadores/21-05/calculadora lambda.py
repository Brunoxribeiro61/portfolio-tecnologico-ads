#Calculadora

#Soma
soma = lambda a, b: a + b
#Subtração
subtracao = lambda a, b: a - b
#Multiplicação
multiplicacao = lambda a, b: a * b
#Divisão
divisao = lambda a, b: a / b

print("Calculadora Lambda")
print(" [1] Soma\n [2] Subtração\n [3] Multiplicação\n [4] Divisão")
while True:
    numero = int(input("Escolha uma opção: "))
    if numero == 0:
        print("Obrigado por usar nosso programa!")
        print("Até logo!")
        break
    elif str(numero) not in ['1', '2', '3', '4']:
        print("Opção inválida! Tente novamente.")
    else:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        if numero == 1: print("Soma:", soma(a, b))
        elif numero == 2: print("Subtração:", subtracao(a, b))
        elif numero == 3: print("Multiplicação:", multiplicacao(a, b))
        elif numero == 4: print("Divisão:", divisao(a, b))