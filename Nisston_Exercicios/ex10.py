# 10. Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. O
# programa deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do
# computador e determinar o vencedor.

from random import choice

cont_vitorias = cont_derrotas = cont_empates = 0

while True:

    lista_opcoes = ["P", "A", "T"]
    pc = choice(lista_opcoes)

    while True:
        jogador = input(f"Escolha Pedra[P], Papel [A] ou Tesoura[T]: ").strip().upper()
        if jogador not in lista_opcoes:
            print("Comando inválido. Tente novamente.")
        else:
            break

    if jogador == pc:
        print("\033[1;30;47mEMPATE!\033[m")
        cont_empates += 1
    elif jogador == "P" and pc == "T" \
            or jogador == "A" and pc == "P" \
            or jogador == "T" and pc == "A":
        print("\033[1;30;42mVOCÊ VENCEU!\033[m")
        cont_vitorias += 1
    else:
        print("\033[1;30;41mVOCÊ PERDEU!\033[m")
        cont_derrotas += 1

    print(f'Vitórias: {cont_vitorias}\n'
          f'Derrotas: {cont_derrotas}\n'
          f'Empates: {cont_empates}\n')

    if pc == "P":
        string_pc = "Pedra"
    elif pc == "A":
        string_pc = "Papel"
    else:
        string_pc = "Tesoura"

    if jogador == "P":
        string_jogador = "Pedra"
    elif jogador == "A":
        string_jogador = "Papel"
    else:
        string_jogador = "Tesoura"

    print(f"Eu joguei: {string_pc}\n"
          f"Você jogou: {string_jogador}\n")

    denovo = ["S", "N"]
    while True:
        dnv = input("Deseja jogar novamente? [S/N]: ").strip().upper()
        if dnv in denovo:
            break
        else:
            print("Tente novamente")

    if dnv == "N":
        print("Finalizando...")
        break
