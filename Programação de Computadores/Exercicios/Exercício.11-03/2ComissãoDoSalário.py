# Salário atual
salarioatual = float(input("Digite o salário atual: "))

# Valor da comissão de 5% do salário
comissao = salarioatual * 0.05

# Calculo do novo salário junto com a comissão
salarionovo = salarioatual + comissao

# Mostra o novo salário com a comissão
print(f"Esse é o salário com 5% de comissão: {salarionovo:.2f}")

# Comando para fechar o programa
input("Pressione Enter para sair...")