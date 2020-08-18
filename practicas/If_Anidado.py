edad = int(input("Edad -->"))

if edad > 0 and edad < 100: # ó tambien podemos ponerlo if 0 > edad < 100:
    print("La edad es correcta")
    if edad < 18:
        print("Menor de edad")
    if edad >= 18:
        print("Es mayor de edad")
else:
    print("La edad es incorrecta")