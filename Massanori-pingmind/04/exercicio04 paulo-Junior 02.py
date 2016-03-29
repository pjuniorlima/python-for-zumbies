#!/usr/bin/python3.

import random

lista=[]
listapar=[]
listaimpar=[]
numero=0

for i in range(20):
	numero=random.randint(0,100)
	if numero%2 == 0:
		listapar.append(numero)
	else:
		listaimpar.append(numero)
	lista.append(numero)

print(lista)
print(listapar)
print(listaimpar)
