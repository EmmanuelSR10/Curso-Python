def estudiantes():
    print("Hola estudiantes")

estudiantes() 



#Funcion que muestra la tabla elegida
num = int(input("Número a multiplicar: ")) 

def tabla_multiplicar(n):                  
    for x in range(1, 11):                 
        print(f"{num} x {x} = {num * x}") 
tabla_multiplicar(num)                     


#Alcance global es cuando el " num "
#está fuera de la funcion
#y funciona para todas las funciones
#por lo que no es necesario ponerlo en todas las func.


#Alcance local es cuando el " num " 
# está dentro de una funcion en especif.
#y solo funcionará para esa función en donde lo pusimos