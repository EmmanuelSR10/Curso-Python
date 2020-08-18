# RECIBIR POR POSICIÓN
""" def argu(*tu):  # el * es cuando no se sabe cuantos parametros le pasaremos
    for tus in tu: # cuando se manda a llamar
        print(tus)
argu("Python", "Hi", 10) """

# Por nombre

def ejemplo(*tu, **lo):
    b = 0
    for tus in tu:
        b += tus
    print(b)
    for x in lo:
        print(x, " ", lo[x])

ejemplo(1,2,3,4, Python = "language", calificacion = [9, 8 , 7])
