#!/usr/bin/python3

statement = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you'
lista = statement.split()

for i in range(len(lista)-1):
	lista[i] = lista[i].lower()
listapython = []
for i in lista:
	if i[0] in 'python' or i[len(i)-1] in 'python':
		listapython.append(i)
print(listapython)
