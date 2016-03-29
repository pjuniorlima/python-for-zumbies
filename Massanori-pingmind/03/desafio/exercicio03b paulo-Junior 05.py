#!/usr/bin/python3

numero = int(input("Digite o número a ser invertido:"))

numerousado = numero
invertido = 0

while numerousado > 0:
	invertido = invertido*10
	invertido = invertido+(numerousado%10)
	numerousado = int(numerousado/10)
	
print(invertido)
	
