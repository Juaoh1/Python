num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

soma = num1 + num2
subtrac = num1 - num2
multiplic = num1 * num2
divi = num1 / num2
divi_inteira = num1 // num2
rest_divi = num1 % num2
potencia_num1 = num1 ** num2
potencia_num2 = num2 ** num1
raiz_quadrada_num1 = num1 ** (1/2)
raiz_quadrada_num2 = num2 ** (1/2)

print (f"O antecessor de {num1} é {num1-1}.\nO sucessor de {num1} é {num1+1}.\nJá o antecessor de {num2} é {num2-1}, e o seu sucessor é o {num2+1}.")
print (f"A soma de {num1} + {num2} é igual a {soma}")
print (f"A subtração de {num1} - {num2} é igual a {subtrac}")
print (f"A multiplicação de {num1} x {num2} é igual a {multiplic}")
print (f"A divisão de {num1} / {num2} é igual a {divi}")
print (f"A divisão inteira de {num1} / {num2} é igual a {divi_inteira}")
print (f"O resto da divisão inteira de {num1} / {num2} é igual a {rest_divi}")
print (f"A potência de {num1} elevado a {num2} é igual a {potencia_num1}")
print (f"A potência de {num2} elevado a {num1} é igual a {potencia_num2}")
print (f"A raiz quadrada de {num1} é {raiz_quadrada_num1}")
print (f"A raiz quadrada de {num2} é {raiz_quadrada_num2}")

"""
Ordem de precedência:
1: ()
2: **
3: *, /, //, %
4: +, -
Ex: 
(3*5+4**2) = 31
(3*(5+4)**2) = 243
"""
