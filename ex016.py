#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua posição inteira. Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.
import math

num = float(input ("Digite um número não inteiro para que o sistema informe apenas sua parte inteira: "))
valor = math.trunc(num) #mostra apenas a parte inteira do número
print (f"A parte inteira de {num} é {valor}")
