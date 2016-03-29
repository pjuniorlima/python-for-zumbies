#!/usr/bin/python3

sortudos=0
for i in range(18644, 33088):
	convertido = str(i)
	if '2' in convertido and not '7' in convertido:
		sortudos+=1
print(sortudos)

