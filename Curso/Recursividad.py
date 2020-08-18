time= int(input("Ingrese el tiempo: "))
def atras(segundos):
    segundos -= 1
    if segundos > 0:
        print(segundos)
        atras(segundos)
    else:
        print("Tiempo terminado")
atras(time)