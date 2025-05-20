anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite os meses adicionais: "))
dias = int(input("Digite os dias adicionais: "))

idade_em_dias = (anos * 365) + (meses * 30) + dias

print("Sua idade expressa em dias é:", idade_em_dias, "dias.")
