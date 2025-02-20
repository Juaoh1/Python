#inserir os números
try:
    num1 = int(input("Informe um número: "))
    num2 = int(input("Informe um segundo número: "))
    num3 = int(input("Informe um terceiro número: "))

    #calcular a média aritmética dos 3 números
    soma = num1 + num2 + num3
    media = soma / 3

    #informar resultado
    result = (f"a média de {num1}, {num2}, {num3} é: {media:.2f}")
    print (result)
except ValueError:
    print("Por favor, insira valores númericos válidos.")