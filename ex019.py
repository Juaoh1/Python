#Um professor quer sortear um dos 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random

#pedindo os nomes separadamente
nomes = []  #lista vazia para que os nomes sejam adicionados nela

for i in range(4):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome) #adicionando cada nome na lista

print ("Os nomes dos alunos são:", nomes)

nome_sorteado = random.choice(nomes)
print (f"E o sorteado para apagar o quadro é: {nome_sorteado}!")
