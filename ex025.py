"""Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome."""

#pedir o nome
nome = str(input("Por favor, diga seu nome completo: "))
#formatar a variável 'nome'
nome_silva = nome.title()
loc_nome_silva = nome_silva.find("Silva")
#verificar se tem o "Silva" presente em qualquer lugar do nome
if (loc_nome_silva == -1):
    print ("Você não tem 'Silva' no nome!")
else:
    print ("Isso! Você tem 'Silva' no nome.")
