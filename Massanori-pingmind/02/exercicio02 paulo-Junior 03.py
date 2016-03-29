#!/usr/bin/python3

peso = int(input("Digite o peso de peixes:"))

if peso > 50:
	excesso = peso-50
	multa = excesso*4
	print("Há excesso.")
	print("Peso: {0} Kg".format(peso))
	print("Excesso: {0} Kg".format(excesso))
	print("Multa: R$ {0}".format(multa))
else:
	print("Não há excesso.")
	print("Peso: {0}".format(peso))
	print("Excesso: {0}".format(excesso))
	print("Multa: {0}".format(multa))
