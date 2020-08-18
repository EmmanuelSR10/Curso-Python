""" Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una
lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> 
es cada una de las asignaturas de la lista."""

materias = []
num_materias = int(input("Numero de materias >> "))

for num in range(num_materias):
    name_materia = input("Materia >> ")
    materias.append(name_materia)

print(f"""Yo estudio {materias}, donde {materias} 
      es cada una de las asignaturas de la lista""")