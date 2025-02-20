#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
#preço do produto
entrada_preco = input("Por favor, insira o valor do produto: ")
#converter o preço em float e tentar aplicar o desconto
try:
    valor_prod = float(entrada_preco)
    if valor_prod > 0:
        prod_com_desconto = valor_prod - (valor_prod * 0.05)
        print (f"O produto com o desconto de 5% off aplicado ficará no valor de R$ {prod_com_desconto:.2f}.")
    else:
        print("Não é possível aplicar desconto.")
except ValueError: #caso informação armazenada na variável "entrada_preco" não seja possível converter para float
    print("Por favor, insira apenas valores válidos!")
