#!/usr/bin/python3

import random

lista1=[]
lista2=[]

for i in range(10):
	lista1.append(random.randint(1,100))
	lista2.append(random.randint(1,100))

lista=[]
for i in range(len(lista1)):
	lista.append(lista1[i])
	lista.append(lista2[i])
	
	


print(lista1)
print(lista2)
print(lista)

	
