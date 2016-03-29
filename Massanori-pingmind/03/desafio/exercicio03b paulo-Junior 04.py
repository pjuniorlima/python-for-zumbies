#!/usr/bin/python3

numero = int(input("Digite número para ser decomposto:"))
decompositor = 2
decompositores = []
multiplicidade = 1

while numero != 1:
	if numero%decompositor == 0:
		decompositores.append(decompositor)
		numero = numero/decompositor
	else:
		decompositor += 1

for i in range(len(decompositores)):
	if len(decompositores) > i+1 and decompositores[i] == decompositores[i+1]:
		multiplicidade += 1
	else:
		print("Multiplicidade de {0} é {1}".format(decompositores[i], multiplicidade))
		multiplicidade = 1
	
print(decompositores)
