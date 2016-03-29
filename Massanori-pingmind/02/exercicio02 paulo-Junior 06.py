#!/usr/bin/python3

salario = int(input("Digite quanto voce ganha por hora:"))
horas = int(input("Digite quantas horas você trabalha por mês:"))

bruto = (salario*horas)
print("O salario bruto é R$ {0}/h".format(bruto))
print("Foi pago ao INSS R$ {0}".format(bruto*0.11))
print("Foi pago ao IR R$ {0}".format(bruto*0.08))
print("Foi pago ao sindicado R$ {0}".format(bruto*0.05))
descontos = bruto*0.11+bruto*0.08+bruto*0.05
print("O salário líquido R$ {0}".format(bruto-descontos))
