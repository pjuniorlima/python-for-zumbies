#!/usr/bin/python3.3

anos = int(input("Digite a quantos anos o fumante fuma:"))
cigarros = int(input("Digite a quantos cigarros o fumante fuma por dia:"))
dias = anos*365
dias_perdidos = 10*cigarros*dias/(60*24)

print("O fumante perdeu {0} dias.".format(dias_perdidos))
