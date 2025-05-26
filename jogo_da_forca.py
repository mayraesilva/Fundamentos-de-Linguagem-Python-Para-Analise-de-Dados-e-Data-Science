# Projeto 1 - Desenvolvimento de Game em Linguagem Python -  Versão 2 por Mayra SIlva

import random
from os import system, name

#Função para limpar a tela a cada execução

def limpa_tela():
    #windows
    if name =='nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')
        