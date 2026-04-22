import time
from colorama import Fore
import pygame
import random
from jogo.utils import tocarSom, cor

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
            print(cor(Fore.LIGHTRED_EX, f"💢{self.getNome()} sofre {self.__DoT} de dano contínuo!"))
    
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
            tocarSom("sons/miss.wav",0.13)
            print(cor(Fore.LIGHTBLUE_EX, f"💨 {self.getNome()} errou o ataque!"))
        
        elif sorte == 15:
            dano = self.getNivel() * 10
            alvo.recebeAtaque(dano)
            tocarSom("sons/crit.wav",0.13)
            print(cor(Fore.RED, f"💥 CRÍTICO! {self.getNome()} causou {dano} de dano em {alvo.getNome()}!"))

        else:
            dano = random.randint(self.getNivel() * 2, self.getNivel() * 3)

            dano += self.getBuff() * 3
            dano -= self.getDebuff() * 2

            alvo.recebeAtaque(dano)
            tocarSom("sons/damage.aiff",0.13)
            print(cor(Fore.LIGHTYELLOW_EX, f"⚔️ {self.getNome()} atacou {alvo.getNome()} causando {dano} de dano!"))
    
    def exibirDetalhes(self):
        return f"Nome: {self.getNome()}\nVidda: {self.getVida()}\nNível: {self.getNivel()}"