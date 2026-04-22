from personagens.herois.heroi import Heroi
import random
from colorama import Fore
from jogo.utils import cor


class Paladino(Heroi):
    def getEmoji(self):
        return "🛡️"

    def ataqueEspecial(self, alvo):
        cura = random.randint(self.getNivel() * 5, self.getNivel() * 6)

        self.curar(cura)
        print(cor(Fore.GREEN, f"\n✨ {self.getNome()} se curou em {cura} de vida!"))