import random
from jogo.utils import limpar, barra_vida

from personagens.herois.duelista import Duelista
from personagens.herois.paladino import Paladino
from personagens.herois.ladino import Ladino
from personagens.herois.mago import Mago

from personagens.inimigos.morcego import Morcego
from personagens.inimigos.slime import Slime
from personagens.inimigos.aranha import Aranha
from personagens.inimigos.goblim import Goblim

#Jogo: gestão do jogo
class Jogo:
    def __init__(self) -> None:
        aleatoriza = random.randint(1,4)
        #aleatoriza = 4

        if aleatoriza == 1:
            self.inimigo = Morcego(nome="Morcego", vida=80, nivel=4, tipo="Voador")

        elif aleatoriza == 2:
            self.inimigo = Slime(nome="Slime", vida=60, nivel=6, tipo="Veneno")

        elif aleatoriza == 3:
            self.inimigo = Aranha(nome="Aranha", vida=90, nivel=3, tipo="Natureza")

        elif aleatoriza == 4:
            self.inimigo = Goblim(nome="Goblin", vida=70, nivel=5, tipo="Trapaceiro")

        limpar()

        selecao = input("[1] Duelista\n[2] Paladino\n[3] Ladino\n[4] Mago\nSelecione seu herói: ")

        if selecao == 'duelista' or selecao == '1':
            self.heroi = Duelista(nome="Duelista", vida=100, nivel=5, habilidade="Super Força")

        elif selecao == 'paladino' or selecao == '2':
            self.heroi = Paladino(nome="Paladino", vida=120, nivel=4, habilidade="Recuperar Vida")
        
        elif selecao == 'ladino' or selecao == '3':
            self.heroi = Ladino(nome="Ladino", vida=70, nivel=7, habilidade="Espreita")
        
        elif selecao == 'mago' or selecao == '4':
            self.heroi = Mago(nome="Mago", vida=80, nivel=4, habilidade="Bola de fogo")


    def iniciaBatalha(self):
        print("Iniciando a Batalha")

        while self.heroi.getVida() > 0 and self.inimigo.getVida() > 0:
            limpar()
            self.heroi.processarStatus()
            self.inimigo.processarStatus()
            print("\n" + "="*36)
            print("        ⚔️  BATALHA ⚔️")
            print("="*36)

            # HERÓI
            print(f"\n{self.heroi.getEmoji()} {self.heroi.getNome().upper()}")
            print(f"Vida:{barra_vida(self.heroi.getVida(), self.heroi.getVidaMax())}")
            print(f"Nível: {self.heroi.getNivel()}")
            print(f"Buff: {self.heroi.getBuff()} | Debuff: {self.heroi.getDebuff()} | DoT: {self.heroi.getDoT()}")
            print(f"Habilidade: {self.heroi.getHabilidade()}")

            # INIMIGO
            print(f"\n{self.inimigo.getEmoji()} INIMIGO: {self.inimigo.getNome()}")
            print(f"Vida:{barra_vida(self.inimigo.getVida(), self.inimigo.getVidaMax())}")
            print(f"Nível: {self.inimigo.getNivel()}")
            print(f"Buff: {self.inimigo.getBuff()} | Debuff: {self.inimigo.getDebuff()} | DoT: {self.inimigo.getDoT()}")
            print(f"Tipo: {self.inimigo.getTipo()}")

            print("\n" + "-"*36)
            print("[1] ⚔️ Ataque Normal")
            print("[2] 💥 Ataque Especial")
            print("-"*36)
            
            if not self.heroi.podeAtacar():
                print(f"{self.heroi.getNome()} está cansado e perdeu o turno!")
                self.heroi.setPodeAtacar(True)

                if self.inimigo.getVida() > 0:
                    atk = random.randint(1,4)
                    if atk == 4:
                        self.inimigo.ataqueEspecial(self.heroi)
                    
                    else:
                        self.inimigo.ataque(self.heroi)

                input("Aperte enter...")

                continue          

            escolha = input("Escolha: ")

            if escolha == '1':
                self.heroi.ataque(self.inimigo)

            elif escolha == '2':
                self.heroi.ataqueEspecial(self.inimigo)

            else:
                print("Escolha invalida, escolha novamente")

            if self.inimigo.getVida() > 0:
                atk = random.randint(1,4)
                if atk == 4:
                    self.inimigo.ataqueEspecial(self.heroi)
                
                else:
                    self.inimigo.ataque(self.heroi)

            input("Aperte enter...")


        if self.heroi.getVida() == 0:
            print("\n" + "="*36)
            print("        💀 GOLPE FINAL 💀")
            print("="*36)

            print(f"\n⚔️ {self.inimigo.getNome()} desferiu o golpe final!")
            print(f"🧙 {self.heroi.getNome()} foi derrotado...")


            print("🪦 Derrota!")
            print("\nO inimigo ri da cara do herói, esperando a próxima batalha...\n")

        elif self.inimigo.getVida() == 0:
            print("\n" + "="*36)
            print("        💀 GOLPE FINAL 💀")
            print("="*36)

            print(f"\n⚔️ {self.heroi.getNome()} desferiu o golpe final!")
            print(f"🦇 {self.inimigo.getNome()} foi derrotado...")


            print("🏆 VITÓRIA!")
            print("\nO herói permanece de pé, pronto para a próxima batalha...\n")