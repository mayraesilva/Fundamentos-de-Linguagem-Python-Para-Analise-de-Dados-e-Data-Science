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





#Acessando o arquivo (file) (txt ou dic) e devolvendo uma lista de listas que contém strings
def transform_the_file(file): #para escolher as palavras de um arquivo
    open_the_file = open(file, 'r', encoding='utf-8')
    file_read = open_the_file.readlines()
    #print('Este é o arquivo antes de remover os excessos', file_read)
    file_modified = []

    for line in file_read:
        file_modified.append(line.strip()) #remove the space and the \n in the beggining/end of string

    print('Este é o arquivo após  a remoção ', file_modified)
    
    return file_modified






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

    


transform_the_file('liniker_musicas.csv')

#jogo_da_forca()