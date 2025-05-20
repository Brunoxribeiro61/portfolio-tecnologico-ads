contador = 0
soma = 0
resp = 's'

while resp == 's':
    num = float(input("Digite quantos carneirinhos contou: "))
    soma = soma + num
    contador = contador + 1
    resp = input("Você ainda não dormiu, continuar contando? (s/n): ")
if resp	== 's':
    print("Você finalmente dormiu!", "contou um total de", soma, "carneirinhos.")
elif resp == 'n':
    num = float(input("Digite quantos carneirinhos contou: "))
    soma = soma + num
    contador = contador + 1
    resp = input("Você ainda não dormiu, continuar contando? (s/n): ")

    print("Você finalmente dormiu!", "contou um total de", soma, "carneirinhos.")