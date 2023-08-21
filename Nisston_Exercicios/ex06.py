# 6. Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse
# número.

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)


while True:
    try:
        num = int(input(f"Digite um número inteiro positivo: "))
        if num >= 0:
            break
        else:
            print("Tente novamente.")
    except ValueError:
        print("Tente novamente.")

fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')

# outras formas:
# # Fatorial (For)
# n = int(input("Fatorial de: "))
# c = n
# fat = 1
# print('{}! = '.format(n), end='')
# for c in range(n, 0, -1):
#     print('{}'.format(c), end='')
#     print(' * ' if c > 1 else ' = ', end='')
#     fat *= c
# print(fat, end='')

# # Fatorial (While)
# n = int(input("Fatorial de: "))
# c = n
# fat = 1
# print('{}! = '.format(n), end='')
# while c > 0:
#     print('{}'.format(c), end='')
#     print(' * ' if c > 1 else ' = ', end='')
#     fat *= c
#     c -= 1
# print(fat, end='')
