# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
    def __init__(self, file):
          self.file = file
          self.chances = 6

     
    def transform_the_file(self): #para escolher as palavras de um arquivo
          open_the_file = open(self.file, 'r', encoding='utf-8')
          file_read = open_the_file.readlines()
          #print('Este é o arquivo antes de remover os excessos', file_read)
          file_modified = []

          for line in file_read:
               file_modified.append(line.strip()) #remove the space and the \n in the beggining/end of string

          #print('Este é o arquivo após  a remoção ', file_modified)

          self.word_list = file_modified
          
          return self.word_list


    def choose_word(self):
         self.secret_word = random.choice(self.word_list).upper()
         return self.secret_word
    


    def prepare_to_play(self):
         
         print("\nWelcome to the Cowboy Carter Hangman's Game\n")
         print("GOOD LUCK! YOU MIGHT NEED IT ;-) \n")

         self.how_many_letters = ''
         self.wrong_choice = 0

         


         for letter in self.secret_word:
              
              if letter == ' ':
                   self.how_many_letters += ' '
               
              elif letter in str(range(0,10)):
                   self.how_many_letters += letter
               
              elif letter == "'":
                   self.how_many_letters += letter
               
              elif letter == '★':
                   self.how_many_letters += letter

              else:
                   self.how_many_letters += '_'

          
         self.how_many_letters = list(self.how_many_letters)

         # Running tests
     #     print(self.how_many_letters)
     #     print(len(self.secret_word))
     #     print(len(self.how_many_letters))


         print(' '.join(self.how_many_letters))

         self.word = [letter for letter in self.secret_word]

         #print(self.word)
                   
                   


         
    
 

    
     

	
	
	# Método para verificar se o jogo terminou
		
	# Método para verificar se o jogador venceu
		
	# Método para não mostrar a letra no board
		
	# Método para checar o status do game e imprimir o board na tela



game = Hangman("Cowboy_Carter_Tracklist.csv")

print(game.file)
print('____________________________')
lista_de_palavras = game.transform_the_file()
#print(lista_de_palavras)

palavra = game.choose_word()
print(palavra)

print(game.prepare_to_play())

