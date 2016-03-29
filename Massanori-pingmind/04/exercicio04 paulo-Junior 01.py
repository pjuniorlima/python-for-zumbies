#!/usr/bin/python3.

import random

lista=[]

for i in range(10):
	lista.append(random.randint(0,100))

lista.sort()	
print("Max: {0} Min: {1}".format(lista[0], lista[len(lista)-1]))

