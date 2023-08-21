# 5. Faça um programa que leia uma lista de números e retorne a média dos números pares.

from random import randint

lista = []
for c in range(10):
    n = randint(1, 100)
    lista.append(n)

lista_par = []

for c in range(len(lista)):
    if lista[c] % 2 == 0:
        lista_par.append(lista[c])
        
try:     
    media_pares = sum(lista_par) / len(lista_par)
except ZeroDivisionError:
    media_pares = "Não foram gerados números pares."

print(f'Lista completa: {lista}\n'
      f'Lista dos Pares: {lista_par}\n'
      f'Média dos números pares: {media_pares}')

