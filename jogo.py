import random
import os
import time
from colorama import Fore, Style, init
import pygame

pygame.mixer.init()
init(autoreset=True)

#Perssonagem
class Perssonagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
        self.__vidaMax = vida
        self.__buff = 0
        self.__debuff = 0
        self.__DoT = 0

    def getNome(self):
        return self.__nome
    
    def getVida(self):
        return self.__vida
    
    def getVidaMax(self):
        return self.__vidaMax

    def getNivel(self):
        return self.__nivel
    
    def getEmoji(self):
        return "❓"
    
    def getBuff(self):
        return self.__buff
    
    def getDebuff(self):
        return self.__debuff
    
    def getDoT(self):
        return self.__DoT

    def setNivel(self, valor):
        self.__nivel = valor

    def setDoT(self, valor):
        self.__DoT += valor

    def setBuff(self, valor):
        self.__buff += valor
        if self.__debuff > 10:
            self.__debuff = 10

    def setDebuff(self, valor):
        self.__debuff += valor
        if self.__debuff > 10:
            self.__debuff = 10   

    def processarStatus(self):
        if self.__DoT > 0:
            self.recebeAtaque(self.__DoT)
            print(Fore.LIGHTRED_EX + f"💢{self.getNome()} sofre {self.__DoT} de dano contínuo!")
    
    def curar(self, valor):
        self.__vida += valor
        if self.__vida > self.__vidaMax:
            self.__vida = self.__vidaMax

    def recebeAtaque(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0

    def ataque(self, alvo):
        sorte = random.randint(1,15)
        if sorte == 1:  
            tocar_som("sons/miss.wav",0.13)
            print(Fore.LIGHTBLUE_EX + f"💨 {self.getNome()} errou o ataque!")
        
        elif sorte == 15:
            dano = self.getNivel() * 10
            alvo.recebeAtaque(dano)
            tocar_som("sons/crit.wav",0.13)
            print(Fore.RED + f"💥 CRÍTICO! {self.getNome()} causou {dano} de dano em {alvo.getNome()}!")

        else:
            dano = random.randint(self.getNivel() * 2, self.getNivel() * 3)

            dano += self.getBuff() * 3
            dano -= self.getDebuff() * 2

            alvo.recebeAtaque(dano)
            tocar_som("sons/damage.aiff",0.13)
            print(Fore.LIGHTYELLOW_EX + f"⚔️ {self.getNome()} atacou {alvo.getNome()} causando {dano} de dano!")
    
    def exibirDetalhes(self):
        return f"Nome: {self.getNome()}\nVidda: {self.getVida()}\nNível: {self.getNivel()}"

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

class Duelista(Heroi):
    def getEmoji(self):
            return "🤺"

    def ataqueEspecial(self, alvo):
        dano = random.randint(self.getNivel() * 6, self.getNivel() * 9)

        alvo.recebeAtaque(dano)
        print(Fore.LIGHTRED_EX + f"\n🩸{self.getNome()} atacou {alvo.getNome()} com {self.getHabilidade()} e causou {dano} de dano!")
        self.setPodeAtacar(False)
    
class Paladino(Heroi):
    def getEmoji(self):
        return "🛡️"

    def ataqueEspecial(self, alvo):
        cura = random.randint(self.getNivel() * 5, self.getNivel() * 6)

        self.curar(cura)
        print(Fore.GREEN + f"\n✨ {self.getNome()} se curou em {cura} de vida!")

class Ladino(Heroi):
    def getEmoji(self):
        return "🗡️"

    def ataqueEspecial(self, alvo):
        self.setBuff(3)
        print(Fore.WHITE + f"\n🌑{self.getNome()} entrou em modo furtivo e buffou seu ataque!")

class Mago(Heroi):
    def getEmoji(self):
        return "🧙"

    def ataqueEspecial(self, alvo):
        fogo = self.getNivel()

        alvo.setDoT(fogo)

        print(Fore.YELLOW + f"\n🔥 {self.getNome()} lançou {self.getHabilidade()}!")
        print(Fore.YELLOW +f"{alvo.getNome()} agora sofre {fogo} de dano por turno!")


#inimigo: adversário
class Inimigo(Perssonagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def getTipo(self):
        return self.__tipo

    def exibirDetalhes(self):
        return f"{super().exibirDetalhes()}\nTipo: {self.getTipo()}\n"
    
class Morcego(Inimigo):
    def getEmoji(self):
        return "🦇"
    
    def ataqueEspecial(self, alvo):
        dano = random.randint(self.getNivel() * 6, self.getNivel() * 7)
        alvo.recebeAtaque(dano)

        print(Fore.LIGHTCYAN_EX + f"🦇{self.getNome()} usou um ataque do tipo {self.getTipo()} em {alvo.getNome()} e causou {dano} de dano!")

class Slime(Inimigo):
    def getEmoji(self):
        return "🟢"

    def ataqueEspecial(self, alvo):
        veneno = self.getNivel()

        alvo.setDoT(veneno)

        print(Fore.LIGHTGREEN_EX + f"🟢{self.getNome()} usou um ataque do tipo {self.getTipo()} em {alvo.getNome()} e causou {veneno} de dano, agora todo turno o {alvo.getNome()} receberá um dano de envenenamento!")

class Aranha(Inimigo):
    def getEmoji(self):
        return "🕷️"

    def ataqueEspecial(self, alvo):
        alvo.setPodeAtacar(False)
        
        print(Fore.LIGHTWHITE_EX + f"🕷️{self.getNome()} usou um ataque do tipo {self.getTipo()} em {alvo.getNome()}, {alvo.getNome()} ficará um turno sem jogar!")

class Goblin(Inimigo):
    def getEmoji(self):
        return "👺"

    def ataqueEspecial(self, alvo):
        self.ataque(alvo)
        alvo.setDebuff(2)

        print(Fore.LIGHTMAGENTA_EX + f"👺{self.getNome()} usou um ataque do tipo {self.getTipo()} em {alvo.getNome()}, {alvo.getNome()} teve o ataque reduzido!")

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
            self.inimigo = Goblin(nome="Goblin", vida=70, nivel=5, tipo="Trapaceiro")

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

# Função da barra de vida
def barra_vida(vida, vida_max, tamanho=10):
    proporcao = vida / vida_max
    preenchido = int(proporcao * tamanho)
    vazio = tamanho - preenchido

    cor = cor_vida(vida, vida_max)

    barra = cor + "█" * preenchido + Style.RESET_ALL
    barra += "░" * vazio

    return barra

# Funções para implementar a cor da barra
def cor_vida(vida, vida_max):
    proporcao = vida / vida_max

    if proporcao > 0.6:
        return Fore.GREEN
    elif proporcao > 0.3:
        return Fore.YELLOW
    else:
        return Fore.RED

#Função de Som
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def tocar_som(caminho, volume=0.5):
    try:
        caminho_completo = os.path.join(BASE_DIR, caminho)
        som = pygame.mixer.Sound(caminho_completo)
        som.set_volume(volume)
        som.play()
    except:
        pass

# Função para limpar terminal
def limpar():
    os.system('clear')

# Instância do jogo
jogo = Jogo()
jogo.iniciaBatalha()