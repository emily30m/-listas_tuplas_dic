#Solicite 5 n´umeros ao usu´ario e armazene em uma lista. Em seguida, imprima o maior e o menor n´umero
numeros = [ ]

for i in range(5):
    numero = input(f'digite o {i + 1}º numero:')
    numeros.append(numero)
    
print(max(numeros))
print(min(numeros))