# ARREGLOS (ARRAYS, LISTAS)

list=[1,2,3,4,5,6,7,8,9]
print(list[2:3])

#usando for
for lista in list:
    print(lista, end= "")
    # end=" " , es para que imprima de forma horizontal
    # \t es para un tab a la derecha
    # si ponemos cualquier cosa dentro del print, nos imprime
    #el numero de veces que tenemos en el array

"""
Una lista puede contener diferentes tipos de datos:
--> Strings
--> int, double
--> otra lista
--> boooleanos
"""

#EJEMPLO

print("\n")
list2=["Python", 5,10,5, [1,True, 3.89, "Martes"], False]
for lista2 in list2:
    print(lista2, end=" ")
