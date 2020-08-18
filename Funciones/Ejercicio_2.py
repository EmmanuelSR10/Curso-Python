""" Realiza una función llamada area_circulo(radio) que devuelva el área de un
círculo a partir de un radio. Calcula el área de un círculo de 5 de radio: """

import math
radio = float(input("Radio >> "))

def area_circulo(radio):
    return (radio ** 2) * math.pi   # ó puede ser-->  return (math.pow(rad, 2)) * math.pi
                                    # primero el radio y despues al exponente 
                                    # que elevaremos o sea el 2
                                    # .pow es para exponenciación

resultado = area_circulo(radio)
print(f"El area es {resultado:.4f}")