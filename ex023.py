"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
"""

#solicitar número
num = int(input("Digite um número inteiro entre 0 a 9999: "))
#Ler a unidade desse número
print (f"Unidade: {num % 10}")
print (f"Dezena: {(num // 10) % 10}")
print (f"Centena: {(num // 100) % 10}")
print (f"Milhar: {(num //1000) % 10}")
