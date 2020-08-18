"""
Hacernun programa que simule un cajrro automatico con un sueldo inicial de $1000 y que tenga el siguiente menu:
1.- Ingresar dinero a la cuenta
2.- Retirar dinero de la cuenta
3.- Mostrar dinero disponible
4.- Salir
"""
SueldoInic=1000
print("""1.- Ingresar dinero a la cuenta.
2.- Retirar dinero de la cuenta
3.- Mostrar dinero disponible
4.- Salir. """)

var=int(input("Elija una opción: "))
while var!=1 and var!=2 and var!=3 and var!=4:
    var=int(input("Dame una opción válida a elegir: "))

if var==1:
    ingreso= float(input("Ingrese el monto a depositar: "))
    SueldoInic+= ingreso
    print(f"El sueldo actualizado es {SueldoInic}")

elif var==2:
    retiro=float(input("Ingrese la cantidad a retirar: "))
    if retiro>SueldoInic:
        print(f"Cantidad a retirar no disponible en la cuenta")
    else:
        SueldoInic-= retiro
        print(f"Cantidad retirada, el sueldo actual es: {SueldoInic}")

elif var==3:
    print(f"El sueldo disponible es: {SueldoInic}")

elif var==4:
    print("¡Gracias por su preferencia!")