total = float(input("Digite o valor total da compra: "))

parcelas = int(input("Digite a quantidade de parcelas (2, 4, 6, 8): "))

if parcelas == 2:
    juros = 0.03
elif parcelas == 4:
    juros = 0.07
elif parcelas == 6:
    juros = 0.09
elif parcelas == 8:
    juros = 0.12
else:
    print("Opção de parcelamento inválida!")
    exit()

valor_final = total * (1 + juros)
valor_parcela = valor_final / parcelas

print(f"O valor de cada parcela será: R$ {valor_parcela:.2f}")
    