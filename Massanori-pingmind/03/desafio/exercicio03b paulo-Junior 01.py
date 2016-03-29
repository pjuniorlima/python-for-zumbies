#!/usr/bin/python3

numero = int(input("Digite número para verificar se é triangular:"))
contador = 1

while numero/2 > contador:
	if ((contador**3)-contador) == numero:
		print(contador-1)
		print(contador)
		print(contador+1)
		break
	else:
		contador += 1
