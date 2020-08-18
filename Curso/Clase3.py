edad = int(input("Edad --> "))

if 0 < edad < 100:
    print("Edad es correcta")
    if edad < 18:
        print("Menor de edad")
    if edad >= 18:
        print("Es mayor de edad")
else:
    print("Edad incorrecta")