# 6. Imagine que você está desenvolvendo um navegador web simplificado. Use uma pilha para armazenar
# o histórico de páginas visitadas pelos usuários e implementar as funcionalidades de voltar e avançar
# na navegação.

class Navegacao:
    def __init__(self):
        self.historico = []
        self.pagina_atual = 0
        self.historico.append(str(f'Página {self.pagina_atual + 1}'))

    def informar_pagina(self):
        print(f'Você está na página {self.historico[-1]}.')

    def abrir_nova_pagina(self):
        self.pagina_atual += 1
        self.historico.append(str(f'Página {self.pagina_atual + 1}'))
        self.informar_pagina()

    def voltar(self):
        if self.pagina_atual == 0:
            print("Você está na primeira página.")
        else:
            print(f'Você voltou para a página {self.historico[self.pagina_atual - 1]}.')
            self.pagina_atual -= 1

    def avancar(self):
        if self.pagina_atual == len(self.historico) - 1:
            print("Você está na última página.")
        else:
            print(f'Você avançou para a página {self.historico[self.pagina_atual + 1]}.')
            self.pagina_atual += 1


nav = Navegacao()
nav.informar_pagina()
nav.abrir_nova_pagina()
nav.avancar()
nav.voltar()
nav.voltar()
nav.avancar()
nav.abrir_nova_pagina()
