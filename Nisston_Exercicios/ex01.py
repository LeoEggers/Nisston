# 1. Faça um programa que calcule a média de três números inseridos pelo usuário.

numeros = []
for c in range(3):
    while True:
        try:
            n = float(input(f"Digite o {c + 1}º número: "))
            break
        except ValueError:
            print("Tente novamente.")

    numeros.append(n)

media = sum(numeros) / len(numeros)
print(f"A média entre {numeros[0]}, {numeros[1]} e {numeros[2]} é {media:.2f}.")
