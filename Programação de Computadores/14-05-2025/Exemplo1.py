mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for i in range(12):
    salario = float(input("Digite o salário do funcionário: %s R$"%mes[i]))

media = salario  / 13
ferias = salario / 3

print("A média salarial do funcionário é: R$ %.2f" % media)
print("O valor das férias do funcionário é: R$ %.2f" % ferias)