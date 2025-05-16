#Solicite ao usu´ario 5 nomes e armazene em uma lista. Depois, imprima cada nome em uma linha.

nomes = []

for i in range(5):
    nome = input(f'digite o {i+1}º nome: ')
    nomes.append(nome)
    
for i in range(len(nomes)):
    print(nomes[i])         