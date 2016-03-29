#!/usr/bin/python3

import urllib.request
from time import sleep

preco = 100.0

while 1:
	pagina = urllib.request.urlopen(
	'http://beans.itcarlow.ie/prices-loyalty.html')
	texto = pagina.read().decode('utf8')
	onde = texto.find('>$')
	inicio = onde + 2
	fim = inicio + 4
	preco = float(texto[inicio:fim])
	print("Preço atual: %5.2f" %preco)
	sleep(3)
print("Comprar!! preço %5.2f" %preco)
