import math
area = float(input("Digite o tamanho da área a ser pintada (em m²): "))
cobertura_por_litro = 3
capacidade_lata = 18
preco_lata = 80.00
litros_necessarios = area / cobertura_por_litro
latas_necessarias = math.ceil(litros_necessarios / capacidade_lata)
preco_total = latas_necessarias * preco_lata
print(f"Quantidade de latas de tinta a serem compradas: {latas_necessarias}")
print(f"Preço total: R$ {preco_total:.2f}")