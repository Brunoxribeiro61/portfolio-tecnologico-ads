contador = 0
soma = 0
resp = 's'

while resp == 's':
    num = float(input("Digite um número: "))
    soma = soma + num
    contador = contador + 1
    resp = input("Deseja continuar? (s/n): ")
print("A média dos números digitados é", soma/contador)