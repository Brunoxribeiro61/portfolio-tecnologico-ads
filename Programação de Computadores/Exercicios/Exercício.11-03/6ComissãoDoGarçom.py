# Valor do que gastou no restaurante
valorcomida = float(input("Digite o valor que gastou no restaurante: "))

# 10% de gorjeta para o garçom
gorjeta = valorcomida * 0.10

# Calcula o valor total a ser pago
valor_total = valorcomida + gorjeta

# Formata o valor total com separadores de milhares e decimais
valor_comissao = f"{valor_total:,.2f}"

# Valor total a ser pago
print(f"Valor que será pago incluindo 10% de gorjeta do garçom será de: R$ {valor_comissao}")

# Comando para fechar o programa
input("Pressione Enter para sair...")