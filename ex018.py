#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
import math

try:
    #Pedir o angulo
    angulo = float(input("Digite o valor do ângulo: "))
    if angulo > 0:
        angulo_radianos = math.radians(angulo)
        seno = math.sin(angulo_radianos)
        cosseno = math.cos(angulo_radianos)
        tangente = math.tan(angulo_radianos)
        print (f"O seno de {angulo} graus é: {seno:.2f} \nO cosseno de {angulo} graus é: {cosseno:.2f} \nA tangente de {angulo} graus é: {tangente:.2f}")
    else:
        print("ERRO! Digite apenas valores acima de 0 graus!")
except ValueError:
    print("ERRO! Digite apenas valores válidos!")
