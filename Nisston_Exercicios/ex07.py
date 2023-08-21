# 7. Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário

while True:
    try:
        n = int(input(f"Digite o número de termos: "))
        if n >= 0:
            break
        else:
            print("Tente novamente.")
    except ValueError:
        print("Tente novamente.")

t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> Fim.')
