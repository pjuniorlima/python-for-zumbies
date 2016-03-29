#!/usr/bin/python3

import urllib.request
from random import randint

def sorteia():
	return texto[randint(0, len(texto)-1)]

def desenha():
	palavra = ''
	for i in range(len(sorteada)):
		if sorteada[i] in certas:
			palavra += sorteada[i]+' '
		else:
			palavra += '_ '
	print(forca[tentativas]+'\n'+palavra)
	return palavra
	
def chute(letras):
	letra = input("Chute uma letra: ")
	while letra in letras:
		letra = input("Letra já usada antes: ")
	return letra
	
def rungame(sorteada):
	global tentativas
	tentativas = 0
	global certas
	certas  = ''
	global erradas
	erradas = ''
	palavra = desenha()
	while True:
		letra = chute(certas+erradas)
		#print("Sorteada:"+sorteada)
		if letra in sorteada:
			certas += letra
			#print("Entrou certas.")
		else:
			tentativas += 1
			erradas += letra
			#print(tentativas)
			#print(erradas)
			#print("Entrou erradas.")
		if tentativas == 8:
			palavra = desenha()
			print("PERDEU =\\")
			again()
		palavra = desenha()
		if '_' not in palavra:
			break
	again()
			
def again():
	resposta = input("Deseja jogar novamente ? [y/n]")
	if resposta in 'Yy':
		sorteada = sorteia()
		rungame(sorteada)
	else:
		print("FIM DE JOGO!!!")
		exit(0)


		
forca = [
'''
  +------+ 
  |      | 
         | 
         | 
         | 
         | 
============
''',
'''
  +------+ 
  |      | 
  O      | 
         | 
         | 
         | 
============
''',
'''
  +------+ 
  |      | 
 \O      | 
         | 
         | 
         | 
============
''',
'''
  +------+ 
  |      | 
 \O      | 
  |      | 
         | 
         | 
============
''','''
  +------+ 
  |      | 
 \O      | 
  |\     | 
         | 
         | 
============
''','''
  +------+ 
  |      | 
 \O      | 
  |\     | 
 /       | 
         | 
============
''','''
  +------+ 
  |      | 
 \O      | 
  |\     | 
 / \     | 
         | 
============
''','''
  +------+ 
  |      | 
 \O      | 
  |\     | 
_/ \     | 
         | 
============
''',
'''
  +------+ 
  |      | 
 \O      | 
  |\     | 
_/ \_    | 
         | 
============
'''
]

url = 'http://www.ime.usp.br/~pf/algoritmos/dicios/br'
texto = urllib.request.urlopen(url).read().decode('iso8859').split()
sorteada = sorteia()

rungame(sorteada)
		
	
	
	
	
	
	
	
	
	
	
	
	


