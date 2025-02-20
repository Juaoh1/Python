#O mesmo professor quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia os nomes dos quatro e mostre a ordem sorteada.
import random

nomes = [] #armazenar os nomes

for i in range(4):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome) #adiciona os nomes na lista "nomes"

print (f"Os alunos são:", nomes)

ordem_nomes = random.shuffle(nomes)  #embaralha a ordem da lista

print(f"A ordem de apresentação dos alunos será:\n 1º {nomes[0]},\n 2º {nomes[1]},\n 3º {nomes[2]},\n 4º {nomes[3]}.")
