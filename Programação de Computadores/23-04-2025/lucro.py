faturamento= float(input("Digite o faturamento"))
custo = float(input("Custo de Produção"))

lucro = faturamento - custo

print("Lucro da empresa é R$: {:,.2f}".format(lucro).replace('.', ',').replace(',', '.').replace('.', ',', 1))