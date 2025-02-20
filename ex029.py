'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.'''
try:    
    velocidade = float(input("Insira a velocidade do carro: "))
    if velocidade <= 80:
        print ("Você está dentro do limite de velocidade!")
    else:
        multa = (velocidade - 80) * 7
        print (f"ATENÇÃO! Você ultrapassou o limite de velocidade e recebeu uma multa de R$ {multa:.2f}.")
except ValueError:
    print ("ERRO. Digite a valocidade em número!")
