#!/usr/bin/python3.

lado1 = int(input("Digite o primeiro lado do triangulo:"))
lado2 = int(input("Digite o segundo lado do triangulo:"))
lado3 = int(input("Digite o terceiro lado do triangulo:"))

if abs(lado1-lado2) < lado3 and lado3 < lado1+lado2:
	if lado1 == lado2 and lado2 == lado3:
		print("Triangulo equilatero.")
	elif lado1 == lado2 or lado2 == lado3:
		print("Triangulo isósceles.")
	elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
		print("Triangulo escaleno.")
else:
	print("Triangulo invalido.")
