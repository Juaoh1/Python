def converter_para_numero(valor):
    try:
        return int(valor), "Int"
    except ValueError:
        try:
            return float(valor), "Float"
        except ValueError:
            return valor, "Str"

# Solicita os números
num1 = input("Informe um número: ")
num2 = input("Informe outro número: ")

# Converte os números e identifica seus tipos
val1, tipo1 = converter_para_numero(num1)
val2, tipo2 = converter_para_numero(num2)

# Exibe os tipos identificados
print(f"O primeiro valor é do tipo: {tipo1}")
print(f"O segundo valor é do tipo: {tipo2}")

# Verifica se ambos são números para realizar a soma
if tipo1 in ["Int", "Float"] and tipo2 in ["Int", "Float"]:
    soma = val1 + val2
    print(f"A soma de {val1} + {val2} é igual a {soma}.")
else:
    print("Não é possível somar os valores, pois pelo menos um deles não é um número.")
