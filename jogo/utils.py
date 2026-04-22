import os
import pygame
from colorama import Fore, Style

# Função para tocar sons
pygame.mixer.init()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def tocarSom(caminho, volume=0.5):
    try:
        caminho_completo = os.path.join(BASE_DIR, "..", caminho)
        som = pygame.mixer.Sound(caminho_completo)
        som.set_volume(volume)
        som.play()
    except:
        pass

# Função para limpar terminal
def limpar():
    os.system('clear')

# Funções para implementar a cor da barra
def cor_vida(vida, vida_max):
    proporcao = vida / vida_max

    if proporcao > 0.6:
        return Fore.GREEN
    elif proporcao > 0.3:
        return Fore.YELLOW
    else:
        return Fore.RED
    

# Função da barra de vida
def barra_vida(vida, vida_max, tamanho=10):
    proporcao = vida / vida_max
    preenchido = int(proporcao * tamanho)
    vazio = tamanho - preenchido

    cordabarra = cor_vida(vida, vida_max)

    barra = cordabarra + "█" * preenchido + Style.RESET_ALL
    barra += "░" * vazio

    return barra

def cor(cor, texto):
    return f"{cor}{texto}{Style.RESET_ALL}"