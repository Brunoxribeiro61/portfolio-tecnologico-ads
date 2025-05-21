def imc( peso, altura):
    ideal = peso / altura**2
    return (ideal)

def despedida():
    print("Obrigado por usar nosso programa!")
    print("Até logo!")
    
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
print("Seu IMC é:", imc(peso, altura), "kg/m²")
if imc(peso, altura) < 18.5:
    print("Abaixo do peso")
elif imc(peso, altura) >= 18.5 and imc(peso, altura) < 24.9:
    print("Peso normal")
elif imc(peso, altura) >= 25 and imc(peso, altura) < 29.9:
    print("Sobrepeso")
despedida()
despedida()
