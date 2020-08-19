try:
    a= float(input("Numero: "))
    r = 10/a
    print(r)
except TypeError:
    print("Debe ser un número, no una letra")
except ValueError:
    print("Ingreso una letra, no un número")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except Exception as x:
    print(type(x).__name__)