#!/usr/bin/python3

usuario = input("Digite o usuario:")
senha = input("Digite a senha:")

while usuario == senha:
	print("Senha igual ao usuário, digite a senha novamente")
	senha = input("Digite a senha:")
