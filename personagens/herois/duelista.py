from personagens.herois.heroi import Heroi
import random
from colorama import Fore
from jogo.utils import cor

class Duelista(Heroi):
    def getEmoji(self):
            return "🤺"

    def ataqueEspecial(self, alvo):
        dano = random.randint(self.getNivel() * 6, self.getNivel() * 9)

        alvo.recebeAtaque(dano)
        print(cor(Fore.LIGHTRED_EX, f"\n🩸{self.getNome()} atacou {alvo.getNome()} com {self.getHabilidade()} e causou {dano} de dano!"))
        self.setPodeAtacar(False)