# 9. Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que
# começam com a letra 'A'.

with open("Nomes.txt", encoding='utf-8') as nomes:
    lista_nomes = [nome.strip() for nome in nomes]

for nome in lista_nomes:
    a = ["A", "Á"]
    if nome[0] in a:
        print(nome)
