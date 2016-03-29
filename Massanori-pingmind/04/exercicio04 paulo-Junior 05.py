#!/usr/bin/python3

statement = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you'
lista = statement.split()
palavras = 0

for i in range(len(lista)-1):
	lista[i] = lista[i].lower()
listapython = []
contador = 0
for i in lista:
	if len(i) >= 4:
		for a in 'python':
			if a in i:
				palavras += 1
				listapython.append(i)
				break

print(palavras)
print(listapython)
print(lista)
