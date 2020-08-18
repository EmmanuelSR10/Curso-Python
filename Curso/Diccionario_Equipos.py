equipo = {10: "Messi", 7: "Cristiano", 11: "Neymar"}
#print(equipo.get(15, "No existe")) #Para mostrar un mensaje que no existe

#print (10 in equipo) # nos muestra "True" si el elemento existe y "False" si no existe

#print(equipo.keys()) #Nos muestra las claves que existen en el diccionario, en este caso los numeros

#print(equipo.values()) #Nos muestra los valores del diccionario, en este caso los nombres de jugadores

print(len(equipo)) #El len nos dice cuantos elementos posee el diciconario
equipo.clear() #Limpia todo lo del diccionario
print(equipo)