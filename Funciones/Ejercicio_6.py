""" Realiza una función separar(lista) que tome una lista de números enteros y devuelva 
dos listas ordenadas. La primera con los números pares y la segunda con los números impares."""

list = []
number_elements = int(input("Total elementos >> "))
for lista in range(number_elements):
    elementos = int(input("Ingrese los elementos >> "))
    list.append(elementos)

list_pares = []
list_impares = []

def separar(lista):
    for recorrer in list:
        if recorrer%2 == 0:
            list_pares.append(recorrer)
        else:
            list_impares.append(recorrer)
    return list_pares, list_impares

list_pares, list_impares = separar(list)
print(list_pares)
print(list_impares)

""" Solucion:
nums = [-12, 84, 13, 20, -33, 101, 9] 
def separar(lista):
    list.sort()
    pares = []
    impares = []
    for n in lista:
        if n%2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares
pares, impares = separar(numeros)
print(pares)
print(impares)
"""