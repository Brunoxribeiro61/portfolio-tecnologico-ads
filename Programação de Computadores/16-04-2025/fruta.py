fruta = "banana"
vegetal = "alface"
letra = fruta[1]
print(letra + " e " + vegetal)
print(len(fruta))


num = int(input("Digite um número: "))
qt = len(str(num))
print(qt)

string = input("Digite uma texto: ")
inversa = " "
for x in string:
    inversa = x + inversa
print(inversa)

resp = 'n'
carneirinho = 0

while resp =='n' or resp =='N':
    resp = input("Deseja continuar? ")
    carneirinho +=1
    
print(carneirinho)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

resp = 'n'
carneirinho = 0

while resp in 'nN':
    resp = input("Deseja continuar? ")
    carneirinho +=1
    
print(carneirinho)