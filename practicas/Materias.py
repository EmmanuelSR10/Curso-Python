materias = []
total_materias=int(input("Total materias >>"))
for materia in range(total_materias):
    name_materia = input("Materia >>")
    materias.append(name_materia)

    n=0
    suma_calificaciones = 0
    for calificacion in materias:
        calificacion_materia = int(input(f"Ingrese la calificación de la materia: {materias[n]}"))
        suma_calificaciones+= calificacion_materia
        n += 1

        promedio= suma_calificaciones / total_materias
        print(f"El promedio es {promedio}")

        """for materia in materias:
        print(materia, end =",") """