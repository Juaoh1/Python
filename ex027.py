"""Faça um programa que leia um nome de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex:Ana Maria de Souza
Primeiro:Ana
último: Souza"""
nome = str(input("Informe seu nome completo: "))

format_nome = nome.title().split()

print (f"""O seu primeiro nome é '{format_nome[0]}'.
O seu último nome é '{format_nome[-1]}'.""")
