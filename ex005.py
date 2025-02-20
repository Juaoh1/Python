msg = input("Digite algo: ")

print(type(msg))
print ("É um número? ", msg.isnumeric())
print ("É alfabético? ", msg.isalpha())
print ("Éstá em maiúsculo? ", msg.isupper())
print ("É um espaço? ", msg.isspace())
print ("Está capitalizada? ", msg.istitle())
