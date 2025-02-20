#Faça um programa que leia o comprimento do cateto oposto e do adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
import math
cateto_op = float(input("Digite o comprimento do cateto oposto do trângulo retângulo: "))
cateto_adj = float(input("Digite o comprimento do cateto adjacente do trângulo retângulo: "))

#hipot = math.sqrt((cateto_adj**2) + (cateto_op**2)) utilizando como raiz quadrada
hipot = math.hypot(cateto_op, cateto_adj)  #utilizando comando direto do calculo da hipotenusa
print (f"a hipotenusa do triângulo retângulo é de {hipot:.2f} centímetros.")
