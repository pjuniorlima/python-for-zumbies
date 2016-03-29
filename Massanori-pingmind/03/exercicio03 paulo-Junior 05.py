#!/usr/bin/python3

n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))


if n1 > n2:
	dividendo = n1
	divisor = n2
else:
	dividendo = n2
	divisor = n1

while dividendo%divisor != 0:
	resto = dividendo%divisor
	dividendo = divisor
	divisor = resto
mdc = divisor
print("O MDC entre {0} e {1} é {2}".format(n1, n2, mdc))
