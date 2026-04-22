from personagens.herois.heroi import Heroi
import random
from colorama import Fore
from jogo.utils import cor


class Mago(Heroi):
    def getEmoji(self):
        return "🧙"

    def ataqueEspecial(self, alvo):
        fogo = self.getNivel()

        alvo.setDoT(fogo)

        print(cor(Fore.YELLOW, f"\n🔥 {self.getNome()} lançou {self.getHabilidade()}!"))
        print(cor(Fore.YELLOW, f"{alvo.getNome()} agora sofre {fogo} de dano por turno!"))