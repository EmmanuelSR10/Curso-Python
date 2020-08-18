while True:
    print("""
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir""")

    opcion = int(input("Ingrese una opción: "))

    if opcion >= 1 and opcion <= 4:
        print("Ingrese dos numeros: ")
        num1 = float(input())
        num2 = float(input())

        if opcion == 1:
            resultado = num1 + num2
            print(f"El resultado es {resultado}")

        elif opcion ==2:
                resultado= num1 - num2
                print(f"El resultado es {resultado}")

        elif opcion==3:
                resultado = num1 * num2
                print(f"El resultado es {resultado}")

        else:
            resultado= num1 / num2
            print(f"El resultado es {resultado}")

        exit()

    else: 
        print("Si desea otra operación digite el número correspondiente") 
