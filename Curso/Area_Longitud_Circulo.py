"""Calcular el area y la longitud de un circulo
area= pi* radio^2
longitud = 2 * pi * radio """

import math
radio= float(input("Ingrese el radio: "))
pi= 3.1416
area= pi * radio ** 2
longitud= 2 * pi * radio
print(f"El area es {area:.2f} y la longitud {longitud:.2f} ")
#Para indicar cuantos numeros mostrar despues del punto es: {area: .2f}