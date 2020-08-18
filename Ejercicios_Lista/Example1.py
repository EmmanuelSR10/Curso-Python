# Tuplas
#Caracteristicas --> Colección de datos que no podran modificarse

tupla= (4, "Hola", 10.0, True, [1,2, False], 4)
print(tupla.count(4))

#name_variable = list(name_tupla)

lista = list(tupla)
lista.append(4)
print(tupla)


lista= [4, "Hola", 10.0, True, [1,2, False]]
tupla= tuple(lista)
print(tupla)