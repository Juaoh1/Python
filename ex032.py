'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.'''
import calendar
from time import sleep
ano = int(input("Por favor, Digite o ano para eu verificar se é bissexto ou não: "))
print ("PENSANDO...")
sleep(2)
if (calendar.isleap(ano)):
    print (f"O ano de {ano} é um ano bissexto!")
else:
    print (f'O ano de {ano} não é um ano bissexto!')
print ("O número de anos bissexto entre 1950 e 2021 é de:",end=" ")
print (calendar.leapdays(1950, ano))
