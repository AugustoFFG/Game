from personagens.inimigos.inimigo import Inimigo
import random
from colorama import Fore
from jogo.utils import cor


class Slime(Inimigo):
    def getEmoji(self):
        return "🟢"

    def ataqueEspecial(self, alvo):
        veneno = self.getNivel()

        alvo.setDoT(veneno)

        print(cor(Fore.LIGHTGREEN_EX, f"🟢{self.getNome()} usou um ataque do tipo {self.getTipo()} em {alvo.getNome()} e causou {veneno} de dano, agora todo turno o {alvo.getNome()} receberá um dano de envenenamento!"))