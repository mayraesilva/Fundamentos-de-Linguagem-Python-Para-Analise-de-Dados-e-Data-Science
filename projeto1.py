# Projeto 1 - Fundamentos de Python ára Analise de dados por Mayra Silva

import random
from os import system, name


def limpa_tela():

    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('cls')




def jogo_da_forca():

    limpa_tela()


    print('\nBem-vinda(o) ao jogo da forca!')
    print('Adivinhe a palavra abaixo:\n')

    possiveis_palavras = ['morango', 'laranja', 'uva']
    chances = 6

    palavra_escolhida = random.choice(possiveis_palavras).upper()

    qts_letras = '_ ' * len(palavra_escolhida)
    print(qts_letras)

    palavra = [letra for letra in palavra_escolhida]
    letras_erradas = []

    




jogo_da_forca()