from personagens.inimigos.inimigo import Inimigo
import random
from colorama import Fore
from jogo.utils import cor


class Aranha(Inimigo):
    def getEmoji(self):
        return "🕷️"

    def ataqueEspecial(self, alvo):
        alvo.setPodeAtacar(False)
        
        print(cor(Fore.LIGHTWHITE_EX, f"🕷️{self.getNome()} usou um ataque do tipo {self.getTipo()} em {alvo.getNome()}, {alvo.getNome()} ficará um turno sem jogar!"))