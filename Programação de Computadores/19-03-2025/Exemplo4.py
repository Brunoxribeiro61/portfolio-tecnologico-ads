#Saber se a pessoa foi aprovada ou não

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")  
    
print("Fim do programa")