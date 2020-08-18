"""Calculadora"""
print("Ingrese '1' para suma")
print("\nIngrese '2' para resta")
print("\nIngrese '3' para división")
print("\nIngrese '4' para multiplicación")

opcion = int(input("\nElige una opción: "))

while opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4:
    print("La opción es inválida")
    opcion= int(input("\nElige una opción:"))


num1= float(input("\nIngresa un numero: "))
num2= float(input("Ingresa otro numero: "))

if opcion == 1:
    sum= num1 + num2
    print(f"La suma es {sum}")
elif opcion== 2:
    res= num1 - num2
    print(f"\nLa resta es {res}")
elif opcion== 3:
    div= num1 / num2
    print(f"\nLa division es {div}")
elif opcion== 4:
    mult= num1 * num2
    print(f"\nLa multiplicación es {mult}")
    