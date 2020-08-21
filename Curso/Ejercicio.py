
# EJERCICIO INCOMPLETO

""" Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. 
La función debe añadir el elemento al final de la lista con la condición de no repetir ningún 
elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo 
ValueError que debes capturar y mostrar este mensaje en su lugar:

Error: Imposible añadir elementos duplicados => [elemento].
Cuando tengas la función intenta añadir los siguiente valores a la lista 10, -2, "Hola" y luego 
muestra su contenido. """



"""list=[]
total_elementos = int(input("Ingrese el numero de elementos que tendrá la lista: "))
for lista in range(total_elementos):
    elemento = int(input("Ingrese elemento:"))
    list.append(elemento)

print(list)"""


list=[]
total_elementos = int(input("Ingrese el numero de elementos que tendrá la lista: "))
for lista in range(total_elementos):
    elemento = int(input("Ingrese elemento:"))
    list.append(elemento)

def agregar_una_vez(lista, el):
    try:
        total_elementos = int(input("Ingrese el numero de elementos que tendrá la lista: "))
        for lista in range(total_elementos):
            elemento = int(input("Ingrese elemento:"))
            list.append(elemento)
    except ValueError:
        print("Error: Elemento duplicado")




