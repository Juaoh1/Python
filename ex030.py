'''Crie um programa que leia um número inteiro qualquer, e mostre se ele é par ou ímpar'''
try:
    valor = int(input("Insira um número inteiro e descubra se ele é par ou ímpar: "))
    if valor % 2 == 0:
        print (f"O número {valor} é PAR!")
    else:
        print (f"O número {valor} é ÍMPAR!")
except ValueError:
    print ("Por favor, digite apenas números inteiros!")
