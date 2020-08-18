""" Conjuntos --> Lista de elementos desordenados donde NO puede haber duplicados""" 
# AL IMPRIMIR UN CONJUNTO EL PROGRAMA NOS LOS MANDARÁ DESORDENADOS
conjunto = set() # Se inicializa un conjunto vacio
conjunto= {1, 2.5, "Hola", 1} #booleanos no los acepta
conjunto.add(3) #Agregar elemento al conjunto
conjunto.discard(1) #Eliminar un elemento en especifico (en este caso no se usa el .pop()  )
conjunto.clear() # Para vaciar un conjunto, por lo tanto solo nos muestra " set() "
print(conjunto)

a= {1,2,3}
b= {3,4,5}

#Unión de conjuntos
c = a | b # EL | significa ó
print (c)

#Interseccion de conjuntos
c = a & b #El & significa intersección
print(c)

#Diferencia de conjuntos
c = a - b 
print(c)

#Diferencia simétrica
c = a ^ b #El ^ es para diferencia simetrica
print(c)


#Si un conjunto es subconjunto de otro
c= {1,2,3,4,5}
print(a.issubset(c)) #Si el conjunto "a" es subconjunto de "c"   
                    #  .issubset es para el subconjunto
                    #nos mostrará True si es subconjunto y False si no lo es