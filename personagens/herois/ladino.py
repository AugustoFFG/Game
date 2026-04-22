from personagens.herois.heroi import Heroi
import random
from colorama import Fore
from jogo.utils import cor


class Ladino(Heroi):
    def getEmoji(self):
        return "🗡️"

    def ataqueEspecial(self, alvo):
        self.setBuff(3)
        print(cor(Fore.WHITE, f"\n🌑{self.getNome()} entrou em modo furtivo e buffou seu ataque!"))
