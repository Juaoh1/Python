#calcular o dobro, triplo e raiz quadrada do número informado
num = input ("Informe um número inteiro: ")
try:
    valor = int(num)
    num_dobro = valor * 2
    num_triplo = valor * 3
    num_raiz = valor **(1/2)
    print (f"O dobro do número {valor} é {num_dobro}\nO triplo é {num_triplo}\nE a sua raiz quadrada é {num_raiz:.2f}.")
except ValueError:
    print ("Por favor, digite apenas números inteiros!")
