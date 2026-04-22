from personagens.inimigos.inimigo import Inimigo
import random
from colorama import Fore
from jogo.utils import cor

class Goblim(Inimigo):
    def getEmoji(self):
        return "👺"

    def ataqueEspecial(self, alvo):
        alvo.setDebuff(2)

        print(cor(Fore.LIGHTMAGENTA_EX, f"👺{self.getNome()} usou um ataque do tipo {self.getTipo()} em {alvo.getNome()}, {alvo.getNome()} teve o ataque reduzido!"))