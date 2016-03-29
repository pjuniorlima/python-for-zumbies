#!/usr/bin/python3.3

mercadoria = int(input("Digite o preço da mercadoria:"))
desconto = int(input("Digite o percentual de desconto:"))
print("O valor do desconto é: %.2f" %((desconto/100)*mercadoria))
mercadoria_descontada = mercadoria-((desconto/100)*mercadoria)
print("O valor da mercadoria é: %.2f" %mercadoria_descontada)
