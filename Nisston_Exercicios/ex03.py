# 3. Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até
# esse número.

while True:
    try:
        n = int(input(f"Digite um número inteiro: "))
        break
    except ValueError:
        print("Tente novamente.")

for c in range(0, n+1 if n > 0 else n-1, -1 if n < 0 else 1):
    if c % 2 == 0:
        print(f'{c}', end='.' if (c == n or c == n-1 or c == n+1) else ', ')
