'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''
cores = {'limpa': '\033[m',
         'verde_sublinhada': '\033[4;32m',
         'verm_sublinhada': '\033[4;31m'}

lado_1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado_2 = float (input("Digite o comprimento do segundo lado do triângulo: "))
lado_3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))
#Para um triângulo ser criado, a soma de dois lado tem que ser sempre maior que o terceiro lado
if lado_1 < lado_2 + lado_3 and lado_2 < lado_1 + lado_3 and lado_3 < lado_1 + lado_2: 
    print (f"Perfeito! com essas medidas, um triângulo {cores['verde_sublinhada']}PODE{cores['limpa']} ser formado!")
else:
    print (f"Com essas medidas, é {cores['verm_sublinhada']}IMPOSSÍVEL{cores['limpa']} formar um triângulo!")
