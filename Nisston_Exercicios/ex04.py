# 4. Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.
from random import randint

lista = []
for c in range(5):
    n = randint(1, 100)
    lista.append(n)

lista = sorted(lista)
menor = lista[0]
maior = lista[-1]

print(f'Valores: {lista}\n')
print(f'Maior valor: {maior}\n'
      f'Menor valor: {menor}\n')

# outra possibilidade:
maior_n = float("-inf")
menor_n = float("inf")

for c in range(len(lista)):
    if maior_n < lista[c]:
        maior_n = lista[c]
    if menor_n > lista[c]:
        menor_n = lista[c]

print(f'maior_n = {maior_n}\n'
      f'menor_n = {menor_n}')
