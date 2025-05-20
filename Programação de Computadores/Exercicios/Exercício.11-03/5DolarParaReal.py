# Cotação do dólar hoje
cotacao_dolar = float(input("Digite a cotação do dólar: "))

# Valor que será convertido para dólares
valor = float(input("Digite o valor em dólares: "))

# Conversão do valor de dólares para Reais
real = valor * cotacao_dolar

# Mostra o valor equivalente em Reais
print(f"O valor em Reais é: R$ {real:.2f}")

# Comando para fechar o programa
input("Pressione Enter para sair...")