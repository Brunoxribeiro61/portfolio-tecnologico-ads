import math

numero = float(input("Digite um número: "))
if numero >= 0:
    raiz = math.sqrt(numero)
    print("A raiz quadrada de", numero, "é", raiz)
else:
    print("Em R, não há raiz quadrada de números negativos")