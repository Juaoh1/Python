"""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras ao todo (sem considerar os espaços)
quantas letras tem o primeiro nome
""" 

#Solicitar o nome
nome = str(input("Por favor, informe seu nome completo: "))

#nome com todas as letras maiúsculas
print(nome.upper())
#nome com todas as letras minúsculas
print(nome.lower())
#total de letras sem considerar os espaços
print (len(nome.replace(" ", "")))
#total de letras do primeiro nome
print (len(nome.split()[0]))
