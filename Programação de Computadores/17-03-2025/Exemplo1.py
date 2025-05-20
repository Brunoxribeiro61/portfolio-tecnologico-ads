num = int(input("Digite o número com três digitos "))
centena = num // 100
dezena = num % 100 // 10
unidade = num % 10
inverso = unidade * 100 + dezena * 10 + centena
print(f"O inverso de {num} é {inverso}")
input("Pressione Enter para fechar...")