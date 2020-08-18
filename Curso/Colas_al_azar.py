 #programa para que atienda a un usuario al azar
import random
cola = ["Jair", "Carlos", "Emmanuel"]
cola.append("Monserrat")
comienza = random.randint(0,3)
n= cola.pop(comienza)
print(f"Atendiendo a {n}")
print (cola)
 