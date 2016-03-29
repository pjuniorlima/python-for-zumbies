#!/usr/bin/python3

fibo1 = 0
fibo2 = 1
fibo3 = fibo2 + fibo1
soma = fibo3 + fibo2
n = 3
print("Número {0} é o fibonacci da posição {1}.".format(fibo1,n-2))
print("Número {0} é o fibonacci da posição {1}.".format(fibo2,n-1))
print("Número {0} é o fibonacci da posição {1}. Soma {2}".format(fibo3,n,soma))

while n <= 50:
	fibo1 = fibo2
	fibo2 = fibo3
	fibo3 = fibo2 + fibo1
	soma = soma + fibo3
	n += 1
	print("Número {0} é o fibonacci da posição {1}. Soma {2}".format(fibo3,n,soma))
		
