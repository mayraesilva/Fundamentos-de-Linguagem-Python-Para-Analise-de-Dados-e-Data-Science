# Projeto 1 - Desenvolvimento de Game em Linguagem Python -  Versão 2 por Mayra SIlva

import random
from os import system, name

#Função para limpar a tela a cada execução

def limpa_tela():
    # Windows
    if name =='nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')


def jogo_da_forca():
    limpa_tela()

    print('\n Bem-vinda(o) ao jogo da forca!')
    print('Adivinhe a palavra abaixo:\n')

    palavras_possiveis = ['banana', 'uva', 'morango', 'manga', 'pera', 'tangerina' ]