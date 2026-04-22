from personagens.personagem import Perssonagem

#Herói: usuário
class Heroi(Perssonagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
        self.__podeAtacar = True

    def podeAtacar(self):
        return self.__podeAtacar

    def setPodeAtacar(self, valor):
        self.__podeAtacar = valor

    def getHabilidade(self):
        return self.__habilidade

    def exibirDetalhes(self):
        return f"{super().exibirDetalhes()}\nHabilidade: {self.getHabilidade()}\n"