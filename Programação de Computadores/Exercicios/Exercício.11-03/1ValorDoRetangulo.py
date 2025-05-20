# Informe os valores dos lados do retângulo
ladoX = float(input("Digite o valor do lado x do retângulo: "))
ladoY = float(input("Digite o valor do lado y do retângulo: "))

# Calculo do perímetro do retângulo
perimetro = 2 * (ladoX + ladoY)

# Calculo da área quadrada do retângulo
area = ladoX * ladoY

# Mostra o perímetro e a área do retângulo
print(f"O perímetro do retângulo é: {perimetro}")
print(f"A área do retângulo é: {area}")

# Comando para fechar o programa
input("Pressione Enter para sair...")