"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"."""

#solicita o nome da cidade
cidade = str(input("Por favor, insira o nome da sua cidade: "))

#pesquisa se no nome informado, começa com o nome "Santo"
nome_santo = cidade.title().split()
if ("Santo" in nome_santo[0]):
    print ("Isso! o nome da sua cidade começa com 'Santo'")
else:
    print ("O nome da cidade não começa com 'Santo'!")
