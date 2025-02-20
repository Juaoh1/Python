'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
lista = []

for i in range(3):
    numeros = int(input(f"Por favor, insira o {i+1}º número: "))
    lista.append(numeros)
print (f"Dos números {lista}, o maior é o {max(lista)}, e o menor é o {min(lista)}")
