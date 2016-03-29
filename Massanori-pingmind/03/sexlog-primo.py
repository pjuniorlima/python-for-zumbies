#!/usr/bin/python3

posicao = 0
numero = 2

while posicao != 10001:
	contador = numero -1

	while numero%contador != 0 and contador > 1:
		contador -= 1

	if contador > 1:
		print("Número {0} não é primo.".format(numero))
		numero = numero + 1
	else:
		print("Número {0} é o primo da posição {1}.".format(numero,posicao))
		posicao = posicao + 1
		numero = numero + 1

#print("Número {0} é o primo da posição {1}.".format(numero,posicao))
#print("Número {0} é o primo da posição 10001.".format(numero))
	
