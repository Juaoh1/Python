"""Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparecem a letra "A"
Em que posição ela aparece pela primeira vez
Em que posição ela aparece pela última vez
"""
frase = str(input("Escreva uma frase aleatória: ")).strip()
print (f"""Na frase existem {frase.lower().count("a")} letras 'a'.
O primeiro 'a' está na posição {frase.lower().find("a")+1}
O último 'a' está na posição {frase.lower().rfind("a")+1}.""")
