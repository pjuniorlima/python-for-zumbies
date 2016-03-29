#!/usr/bin/python3

ano = int(input("Digite o ano para saber se é bissexto:"))

if (ano%100) == 0:
	ano=ano/100
if (ano%4) == 0:
	print("o ano {0} é bissexto.".format(ano))
else:
	print("o ano {0} não é bissexto.".format(ano))
