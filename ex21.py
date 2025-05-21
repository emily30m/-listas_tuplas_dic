#Solicite ao usu´ario 10 n´umeros, armazene em uma lista e remova todos os n´umeros pares usando remove.

n = [ ]
for i in range(10):
    numero = int(input(f"digite o {i}° numero"))
    n.append(numero)

numeros_sem_pares = []

for numero in n:
    if numero % 2 != 0:
        numeros_sem_pares.append(numero)

printgi