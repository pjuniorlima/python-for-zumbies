#!/usr/bin/python3.3

distancia = int(input("Digite a distância da viagem em kilometros:"))
velocidade_media = int(input("Digite a velocidade em km/h:"))
tempo = distancia/velocidade_media
horas = tempo-(tempo%1)
minutos = (tempo%1)*60
print("O tempo de viagem será: %dh:%dm" %(horas,minutos))
