# 9. Crie uma estrutura que possa ler uma expressão matemática do tipo "(2+3)*(8-9)/(7^3) "e apresente
# todos os operadores matemáticos existente nessa expressão, utilize a pilha para responder a questão.

expressao = "(2+3)*(8-9)/(7^3)"
operadores = ["+", "-", "*", "/", "^"]

operadores_expressao = []
for char in expressao:
    if char in operadores:
        operadores_expressao.append(char)

if len(operadores_expressao) != 0:
    set_operadores = set(operadores_expressao)
    print('Estes foram os operadores matemáticos utilizados na expressão escolhida:')
    for operador in set_operadores:
        print(operador)
