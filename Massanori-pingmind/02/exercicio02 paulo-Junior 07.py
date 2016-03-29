#!/usr/bin/python3

metros = int(input("Digite a quantidade em metros quadrados:"))


litros = metros/3

if litros < 18:
	latas = 1
else:
	if (litros%18) == 0:
		latas = litros/18
	else:
		latas = litros/18
		latas = round(latas+0.5)

print("O quantidade de latas é {0}".format(latas))
print("O preço total é R$ {0}".format(latas*80))
