'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários acima de R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''
salario = float(input("Qual o seu salário atual? "))
if salario > 1250:
    novo_salario = salario + (salario * 0.1)
    print (f"Com o aumento de 10%, seu novo salário será no valor de R$ {novo_salario:.2f}")
else:
    novo_salario = salario + (salario * 0.15)
    print (f"Com o aumento de 15%, seu novo salário será no valor de R$ {novo_salario:.2f}")
