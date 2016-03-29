#!/usr/bin/python3

n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
n3 = int(input("Digite o terceiro número:"))

if n1 > n2:
	if n1 > n3:
		if n2 > n3:
			print("O maior é: {0}.".format(n1))
			print("O menor é: {0}.".format(n3))
		else:
			print("O maior é: {0}.".format(n1))
			print("O menor é: {0}.".format(n2))
	else:
		print("O maior é: {0}.".format(n3))
		print("O menor é: {0}.".format(n2))
		#08007073526
else:
	if n2 > n3:
		if n1 > n3:
			print("O maior é: {0}.".format(n2))
			print("O menor é: {0}.".format(n3))
		else:
			print("O maior é: {0}.".format(n2))
			print("O menor é: {0}.".format(n1))
	else:
		print("O maior é: {0}.".format(n3))
		print("O menor é: {0}.".format(n1))
