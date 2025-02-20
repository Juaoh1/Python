#Crie um programa que leia o quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$ 1,00 = R$ 3,27
#Conversor de moedas
def converter_numero (valor):
    try:
        return float(valor), "float"
    except ValueError:
        return str(valor), "str"
        
saldo_reais = input("Digite seu Saldo disponível em reais para ser convertido em dólares: ")

val, moeda_real = converter_numero(saldo_reais)

if moeda_real in ["int", "float"]:
    vlr_moeda_dol = val / 3.27
    
    if vlr_moeda_dol == 0:
        print ("Você não tem saldo suficiente para ser convertido em dólares!")
    else:
        print (f"Seu saldo em dólares será de: US$ {vlr_moeda_dol:.2f}")
else:
    print ("Digite apenas valores válidos para a conversão!")
