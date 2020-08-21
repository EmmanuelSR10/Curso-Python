"""Métodos especiales y objetos embebidos"""

class Fabrica:
    def __init__(self, tiempo, nombre, ruedas): #def __init__ nos ayuda como método constructor
        self.tiempo = tiempo
        self.nombre = nombre
        self.ruedas = ruedas

        print("Se creó el auto", self.nombre)

    def __del__(self): # __del__(self) es el método destructor, "delete"
        print("Se eliminó el auto", self.nombre)

    def __str__(self): # __str__(self) nos ayuda con los strings (caracteres)
        return "{} ({})".format(self.nombre, self.tiempo) #las llaves nos sirve para imprimir usando format
                                                        # en este caso el nombre y tiempo

class listado:
    autos = []

    def __init__(self, autos = []):
        self.autos = autos

    def fabricar(self, x):
        self.autos.append(x)

    def visualizar(self):
        for x in self.autos:
            print(x)

ob = Fabrica(10, "Yo", 4) # cuando se pone  =  es para crear el objeto

li= listado([ob])

li.visualizar() # cuando se usa el  .  es para llamar a una funcion
li.fabricar(Fabrica(15, "Otro yo", 2))
li.visualizar()