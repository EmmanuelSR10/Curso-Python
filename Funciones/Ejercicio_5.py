""" Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres parámetros. 
El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite 
superior. La función tendrá que cumplir lo siguiente:
Devolver el límite inferior si el número es menor que éste
Devolver el límite superior si el número es mayor que éste.
Devolver el número sin cambios si no se supera ningún límite. """

num_1 = int(input("Ingrese primer número: "))  # numero es el primer numero ingresado
num_2 = int(input("Ingrese segundo número: ")) # minimo es el segundo numero ingresado
num_3 = int(input("Ingrese tercer número: "))  # maximo es el tercer numero ingresado

def recortar(numero, minimo, maximo):
    if numero < minimo:
        return print(f"El limite inferior: {minimo}")
    elif numero > maximo:
         return print(f"El limite superior: {maximo}")
    return print(f"No se supera ningún límite: {numero}")
resultado = recortar(num_1, num_2, num_3)
print(resultado)