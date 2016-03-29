#!/usr/bin/python3

conta = int(input("Digite o valor da conta:"))
valor = int(input("Digite o valor da dinheiro dado:"))

troco = valor - conta
cedulas = 0

for i in [50,20,10,5,2,1]:
	if troco >= i:
		cedulas += 1
		troco = troco - i
		
print(cedulas)
