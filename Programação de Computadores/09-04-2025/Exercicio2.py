import random

alunos=[]
for i in range(500):
    alunos.append(random.randint(10, 17))
    
eleitores = [num for num in alunos if num > 16]
quantidade_de_eleitores = len(eleitores)

print("A quantidade de eleitores é", quantidade_de_eleitores)

nao_eleitores = [num for num in alunos if num <= 16]
quantidade_de_nao_eleitores = len(nao_eleitores)
idade_media = sum(nao_eleitores) / quantidade_de_nao_eleitores
print("A idade média dos não eleitores é", idade_media)