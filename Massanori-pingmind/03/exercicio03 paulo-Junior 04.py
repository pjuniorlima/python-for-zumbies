#!/usr/bin/python3

n = int(input("Digite o número para calcular seu Fibonacci:"))
fibo1 = 1
fibo2 = 1
fibo3 = fibo1 + fibo2

while n > 0:
	if n == 1 or n == 2:
		fibo3 = 1
		break
	elif n == 3:
		break
	fibo1 = fibo2
	fibo2 = fibo3
	fibo3 = fibo2 + fibo1
	n -= 1
print(fibo3)
		
