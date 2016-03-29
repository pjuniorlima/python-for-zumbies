#!/usr/bin/python3.

nota = int(input("Digite uma nota entre 0 e 10:"))

while nota < 0 or nota > 10:
	nota = int(input("Nota errada, digite uma nota entre 0 e 10:"))
print("OK, nota aceita!")

