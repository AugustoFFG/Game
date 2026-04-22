from personagens.inimigos.inimigo import Inimigo
import random
from colorama import Fore
from jogo.utils import cor

class Morcego(Inimigo):
    def getEmoji(self):
        return "🦇"
    
    def ataqueEspecial(self, alvo):
        dano = random.randint(self.getNivel() * 6, self.getNivel() * 7)
        alvo.recebeAtaque(dano)

        print(cor(Fore.LIGHTCYAN_EX, f"🦇{self.getNome()} usou um ataque do tipo {self.getTipo()} em {alvo.getNome()} e causou {dano} de dano!"))