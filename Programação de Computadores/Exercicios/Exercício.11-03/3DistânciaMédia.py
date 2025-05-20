# Distância entre duas cidades
distancia = float(input("Qual a distância entre as duas cidades em km: "))

# Tempo de viagem aproximada
tempo = float(input("Digite o tempo de viagem aproximada em horas: "))

# Calculo da velocidade média usando - velocidade = distância / tempo
velocidade_media = distancia / tempo

# Mostrar a velocidade média
print(f"A velocidade média do veiculo é: {velocidade_media:.2f} km/h")

# Comando para fechar o programa
input("Pressione Enter para sair...")