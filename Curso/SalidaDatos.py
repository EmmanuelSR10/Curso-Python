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