'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
from random import randint
from time import sleep

num_secret = randint(0, 5)
print("=-"*32)
print("Vou sortear um número aleatório entre 0 e 5, tente adivinhar...")
print("=-"*32  )

for tentativa in range(0, 6):
    palpite = int(input("Digite seu palpite: "))
    print ("PROCESSANDO...")
    sleep(2)
    if palpite > 5: #caso o número informado seja maior que os números do desafio
        print ("Por favor, o número pensado foi entre 0 e 5!")

    elif palpite == num_secret:
        print (f"PARABÉNS! O número que eu pensei foi o {num_secret}.")
        break
    else:
        print (f"VOCÊ ERROU! O número que eu pensei foi o {num_secret}.")
        break
