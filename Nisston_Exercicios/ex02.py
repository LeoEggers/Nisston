# 2. Crie um programa que determine se um número inserido pelo usuário é par ou ímpar

while True:
    try:
        n = float(input(f"Digite um número: "))
        break
    except ValueError:
        print("Tente novamente.")

if n % 2 == 0:
    print("O número escolhido é par.")
else:
    print("O número escolhido é ímpar.")
    