#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

#pedir o salário
pedir_salario = input("Por favor, informe seu salário: ")
#transformar em float e fazer aumento de 15%
try:
    salario = float(pedir_salario)
    if salario > 0:
        aumento = salario + (salario * 0.15)
        print (f"Parabéns!! Você recebeu um aumento de 15%, resultando em um novo salário no valor de R$ {aumento:.2f}!")
    else:
        print ("Não é possível realizar um aumento no seu salário.")
except ValueError:
    print ("Por favor, digite apenas valores válidos.")
