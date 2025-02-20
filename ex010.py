#Faça um programa que leia a largura e a altura de uma parede em metros, e calcule sua área e a quantidade necessária de tinta para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

#pedir largura da parede (metros)
largura_parede = input("Informe a largura da parede: ")
#pedir altura da parede (metros)
altura_parede = input("informe a altura da parede: ")
#calcular área da parede (m²)
try:
    valor_largura = float(largura_parede) # tenta converter para float
    valor_altura = float(altura_parede)
    if valor_largura == valor_altura: #parede será quadrada: A = lado²
        area_parede = valor_largura**2
        print (f"A área da parede é de {area_parede} m².")
    else: #parede será retangular: A = base(largura) x altura
        area_parede = valor_largura * valor_altura
        print (f"A área da parede é de {area_parede} m².")
    #calcular quantidade de tinta para pintar (1L = 2m²)
    qtd_tinta = area_parede / 2
    print (f"A quantidade necessária de tinta para pintar a parede será de {qtd_tinta} litros.")
except ValueError:
    print ("Por favor, insira apenas valores válidos!")
