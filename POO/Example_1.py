""" class estudiantes:
    pass # Palabra reservada para una clase vacía
estudiantes = estudiantes() # Objeto

NombreClase """

class Auto:

    Rojo = False
    
    def __init__(self, puertas= None, color= None): 
        self.puertas = puertas
        self.color = color

        if puertas is not None and color is not None: #Si no es none, o sea lo contrario,
                                                        #nos imprime los parametros que pusimos hasta abajo
            print(f"Se creó un auto con {puertas} puertas y de color {color}")

    def Fabricar(self):
        self.Rojo = True 

    def confirmar_fabricacion(self):
        if (self.Rojo):
            print("Auto ha sido coloreado")
        else:
            print("Aún no se ha coloreado")


autos = Auto("2", "Rojo")
autos.confirmar_fabricacion()
autos.Fabricar()
autos.confirmar_fabricacion()
