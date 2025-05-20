import math

def menu():
    print("Calculadora Científica")
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("7. Seno")
    print("8. Cosseno")
    print("9. Tangente")
    print("10. Logaritmo")
    print("0. Sair")

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

def potencia(x, y):
    return x ** y

def raiz_quadrada(x):
    return math.sqrt(x)

def seno(x):
    return math.sin(math.radians(x))

def cosseno(x):
    return math.cos(math.radians(x))

def tangente(x):
    return math.tan(math.radians(x))

def logaritmo(x):
    return math.log10(x)

while True:
    menu()
    escolha = input("Digite sua escolha (0-10): ")

    if escolha == '0':
        print("Saindo...")
        break

    if escolha in ['1', '2', '3', '4', '5']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"Resultado: {adicao(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {multiplicacao(num1, num2)}")
        elif escolha == '4':
            print(f"Resultado: {divisao(num1, num2)}")
        elif escolha == '5':
            print(f"Resultado: {potencia(num1, num2)}")

    elif escolha in ['6', '7', '8', '9', '10']:
        num = float(input("Digite o número: "))

        if escolha == '6':
            print(f"Resultado: {raiz_quadrada(num)}")
        elif escolha == '7':
            print(f"Resultado: {seno(num)}")
        elif escolha == '8':
            print(f"Resultado: {cosseno(num)}")
        elif escolha == '9':
            print(f"Resultado: {tangente(num)}")
        elif escolha == '10':
            print(f"Resultado: {logaritmo(num)}")

    else:
        print("Escolha inválida, tente novamente.")

    input("Pressione Enter para continuar...")
