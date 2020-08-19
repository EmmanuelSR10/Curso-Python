while(True):
    try: # es donde escribimos todo lo que nos podria generar errores al momento de ejecutar
        var=float(input("Numero: "))
        a= 2
        print(f"Resultado {a*var}")
    except: # Es para que nos muestre un mensaje de que el dato ingresado no es válido
        print("No se ingresó un dato válido")
    else:
        print("Correcto")
        break
    finally:
        print("Todo salió bien")