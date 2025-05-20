homens = []
mulheres = []

print("Digite o sexo (M/F) e a altura de cada pessoa (digite 'fim' para encerrar):")
while True:
    entrada = input("Sexo e altura (exemplo: M 1.75): ")
    if entrada.lower() == 'fim':
        break
    try:
        sexo, valorAltura = entrada.split()
        valorAltura = float(valorAltura)
        if sexo.upper() == 'M':
            homens.append(valorAltura)
        elif sexo.upper() == 'F':
            mulheres.append(valorAltura)
        else:
            print("Use 'M' para masculino ou 'F' para feminino.")
    except ValueError:
        print("Por favor, insira o sexo e a altura no formato correto.")

if homens:
    mediaHomens = sum(homens) / len(homens)
    print(f"Altura média dos homens: {mediaHomens:.2f} m")
else:
    print("Nenhum homem foi registrado.")

if mulheres:
    mediaMulheres = sum(mulheres) / len(mulheres)
    print(f"Altura média das mulheres: {mediaMulheres:.2f} m")
else:
    print("Nenhuma mulher foi registrada.")