# 8. Faça um programa que determine se um número é primo ou não.

while True:
    try:
        num = int(input(f"Digite um número inteiro positivo: "))
        if num >= 0:
            break
        else:
            print("Tente novamente.")
    except ValueError:
        print("Tente novamente.")

cont = 0
primo = False

for i in range(2, num + 1):
    if num % i == 0:
        cont += 1

primo = cont == 1

print(f"Número {num} é primo: {primo}")
