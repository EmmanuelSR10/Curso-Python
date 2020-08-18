pila = [1,2,3]
pila.append(4) # .append es para agregar elementos 
pila.append(5)
print(pila)

#Eliminando elemento por el final
n = pila.pop() #pop elimina el elemento que está al final
               # o el último agregado, en este caso el 5
print(f"Eliminando {n} por el final")
print(pila) #nos imprime la pila sin el elemento eliminado
