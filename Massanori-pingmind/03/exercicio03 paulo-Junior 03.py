#!/usr/bin/python3

a = 80000
b = 200000
ataxa = 0.03
btaxa = 0.015
anos = 0

while a < b:
	a = a + a*ataxa
	b = b + b*btaxa
	anos += 1
	
print(anos)
