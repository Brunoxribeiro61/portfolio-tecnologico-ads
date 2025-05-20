# Temperatura em graus Celsius
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Temperatura em Fahrenheit
tf = (1.8 * celsius) + 32

# Temperatura em Kelvin
tk = celsius + 273.15

# Temperaturas convertidas
print(f"Temperatura em Fahrenheit: {tf:.2f}°F")
print(f"Temperatura em Kelvin: {tk:.2f}K")

# Comando para fechar o programa
input("Pressione Enter para sair...")
