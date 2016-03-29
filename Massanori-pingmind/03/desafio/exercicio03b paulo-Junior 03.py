#!/usr/bin/python3

numero = int(input("Digite o número:"))
contador = numero -1

while numero%contador != 0 and contador > 1:
	contador -= 1

if contador > 1:
	print("Número {0} não é primo.".format(numero))
else:
	print("Número {0} é primo.".format(numero))
	
