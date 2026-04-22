from personagens.personagem import Perssonagem

#inimigo: adversário
class Inimigo(Perssonagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def getTipo(self):
        return self.__tipo

    def exibirDetalhes(self):
        return f"{super().exibirDetalhes()}\nTipo: {self.getTipo()}\n"