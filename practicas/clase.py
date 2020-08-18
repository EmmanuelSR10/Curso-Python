"""Operadores aritméticos"""
#Clase type(var)
"""
+ suma
- resta
/ division
% modulo
** potencia """
numero1= 5
numero2= 10
suma= numero1 + numero2
print(suma)

""" a=10    b=12   c=13      d=10
((a > b) or (a < c)) and ((a == c) or (a >= b))
"""
operacion= ((10 > 12) or (10 < 13)) and ((10 == 13) or (10 > 12))
print(operacion)

"""Operadores en asignación"""

a= 5
a+= 5 #Suma en asignacion
a-= 2 #Resta en asignacion
a*= 3 #Multiplicacion en asignacion
a/= 3 #Division en asignacion
print(a)


"""salida de datos"""
nombre = "Python"
version = 3.7
print(f"Curso de {nombre} de version {version}")

#SALIDA DE DATOS SIN ESPECIFICAR EL TIPO DE DATO (POR DEFECTO ES STRING "STR" )
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
print(f"Mi nombre es {nombre} y mi edad es {edad}")

#SALIDA DE DATOS ESPECIFICANDO EL TIPO DE DATO ( INT, FLOAT, ETC )

numero1 =int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un numero: "))
suma= numero1 + numero2
print( suma )


numero1 = float(input("Ingrese un numero decimal: "))
numero2= float(input ("Ingrese un numero decimal: "))
suma=numero1+numero2
print(suma)


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

"""CONDICIONALES"""
numero = int (input("Numero:"))
if numero > 0:
    print("El numero es positivo") #siempre poner " : " para identacion
elif numero== 0:
    print("El número es cero")
else:
    print("El numero es negativo")