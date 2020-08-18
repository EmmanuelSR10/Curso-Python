""" Realiza una función llamada area_rectangulo(base, altura) que devuelva el área
del rectangulo a partir de una base y una altura. Calcula el área de un rectángulo 
de 15 de base y 10 de altura: """

#CUANDO LOS VALORES YA LOS TIENE ASIGNADOS
def area_rectangulo(base, altura):
    return base * altura
resultado = area_rectangulo(15, 10)
print(f"El area es: {resultado}")



#PIDIENDO LA BASE Y ALTURA DEL RECTÁNGULO
base= int(input("Ingrese la base del rectángulo:"))
altura= int(input("Ingrese la altura del rectángulo:"))

def area_rectangulo(base, altura):
    return base * altura
resultado = area_rectangulo(base, altura)
print(f"El area es: {resultado}")