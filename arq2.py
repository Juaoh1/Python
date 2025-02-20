import random

#gerar número aleatório
numero_secret = random.randint(1, 50)
print("Jogo da adivinhação")
print("Tente adivinhar o número que estou pensando (entre 1 e 50). Você tem 5 tentativas.")

#controlar as tentativas feitas
for tentativa in range(1, 6):
    palpite = int(input(f"Digite seu palpite {tentativa}: "))

    if palpite == numero_secret:
        print("Parabéns, você acertou!!")
        break
    elif palpite < numero_secret:
        print("O número é maior!")
    else:
        print("O número é menor!")

#caso não acerte em nenhuma tentativa
if palpite != numero_secret:
    print(f"Você não conseguiu adivinhar. O número era {numero_secret}.")