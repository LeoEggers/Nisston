# 10. Palíndromos são palavras, frases ou sequências que mantêm a sua mesma forma quando invertidos. Por
# exemplo, a palavra "radar" é um palíndromo, pois se você a ler de trás para frente, ela ainda será
# "radar". Construa um programa que possa ler uma palavra ou frase e dizer se ela é um Palíndromo,
# use a estrutura de pilha para responder essa questão.

def is_palindromo(palavra):
    letras = list(palavra)
    palavra_invertida = letras[::-1]

    print(f'Palavra: {palavra}')
    print('Palavra Invertida: ', end="")
    for letra in palavra_invertida:
        print(letra, end="")
    print(f'\nÉ palíndromo: {palavra == "".join(palavra_invertida)}\n')


is_palindromo("arara")
is_palindromo("abelha")
