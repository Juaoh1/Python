#tabuada
try:
    num = int(input("Digite um número inteiro: "))
    print ("="*20)
    print (f"Tabuada do {num}")
    print ("="*20)
    for i in range (1, 11): #de 1 a 10
        tabuada = num * i
        print (f"{num} x {i:2} = {tabuada:2}")
    print ("="*20)
except ValueError:
    print ("ERRO! Informe apenas números!")
