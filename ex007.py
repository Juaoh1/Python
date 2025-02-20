#conversor de medida
def converter_para_numero (valor):
    try:
        return int(valor), "Int"
    except ValueError:
        try:
            return float(valor), "Float"
        except ValueError:
            return valor, "Str"

#solicitar a medida
medida = input("por favor, informe uma medida a ser convertida: ")

val1, medida1 = converter_para_numero(medida)

if medida1 in ["Int", "Float"]:
    medida_cm = val1 * 100
    medida_mm = val1 * 1000
    print (f"{val1} metros é igual a {medida_cm} centímetros, ou {medida_mm} milímetros.")
else:
    print ("Por favor, insira uma medida válida.")
