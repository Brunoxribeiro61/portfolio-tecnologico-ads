def process_values():
    values = map(float, iter(lambda: input("Digite um valor real (ou 'sair' para encerrar): "), 'sair'))
    values = list(values)

    if not values:
        print("Nenhum valor foi inserido.")
        return

    print(f"Quantidade de valores positivos: {sum(v > 0 for v in values)}")
    print(f"Quantidade de valores negativos: {sum(v < 0 for v in values)}")
    print(f"Menor valor: {min(values)}")
    print(f"Maior valor: {max(values)}")
