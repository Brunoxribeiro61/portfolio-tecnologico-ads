valorPrestacao = float(input("Digite o valor da prestação: "))
multa = float(input("Digite a porcentagem de multa pelo atraso: "))
qtdeDias = int(input("Digite a quantidade de dias de atraso: "))

prestacao = valorPrestacao + (valorPrestacao * (multa / 100) * qtdeDias)

print("O valor da prestação em atraso é: R$", prestacao)