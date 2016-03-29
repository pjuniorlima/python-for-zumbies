#!/usr/bin/python3.3

dias = int(input("Digite o número de dias:"))
horas = int(input("Digite o número de horas:"))
minutos = int(input("Digite o número de minutos:"))
segundos = int(input("Digite o número de segundos:"))

total = dias*86400 + horas*3600 + minutos*60 + segundos

print("O total de segundos é: %d" %total)
