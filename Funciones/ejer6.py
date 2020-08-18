""" Realiza una función separar(lista) que tome una lista de números enteros y devuelva 
dos listas ordenadas. La primera con los números pares y la segunda con los números impares."""
""" 
list=[1,2,3,4,5]


list_par=[]
list_impar=[]
def separar(lista):
    for avanzar in list:
        if avanzar %2 == 0:    #avanzar toma el valor de cada uno de los elemntos de la lista
            list_par.append(avanzar)
        else:
            list_impar.append(avanzar)
    return list_par, list_impar

list_par, list_impar = separar(list)
print(list_par)
print(list_impar) """


list=[]
n_elementos= int(input("Ingrese el número de elementos: "))
for lista in range(n_elementos):
    elementos= int(input("Ingrese el elemento: "))
    list.append(elementos)


list_par=[]
list_impar=[]
def separar(lista):
    for avanzar in list:
        if avanzar %2 == 0:    #avanzar toma el valor de cada uno de los elemntos de la lista
            list_par.append(avanzar)
        else:
            list_impar.append(avanzar)
    return list_par, list_impar

list_par, list_impar = separar(list)
print(list_par)
print(list_impar)
