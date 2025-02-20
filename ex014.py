#escreva um programa que pergunte a quantidade de KM rodados por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por KM rodado.

dias_alugados = int(input("Por quantos dias o carro foi alugado? "))
km_rodados = float(input("Quantos KM o carro rodou? "))

aluguel = (60 *dias_alugados) + (0.15 * km_rodados)

print (f"O aluguel do carro ficou em R${aluguel:.2f}")
