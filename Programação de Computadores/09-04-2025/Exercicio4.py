segundos = float(input("Digite o tempo em segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
print("Em horas: ", horas)
print("Em segundos: ", segundos)
print("Em minutos: ", minutos)