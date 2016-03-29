#!/usr/bin/python3

kilometros = int(input("Digite a quantidade de kilometros percorridos:"))
dias = int(input("Digite a quantidade de dias que o carro ficou alugado:"))
total = 60*dias + 0.15*kilometros
print("O valor total é {0}.".format(total))
