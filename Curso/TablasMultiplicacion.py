#TABLAS DE MULTIPLICAR CON RANGE

numero=int(input("Ingrese un número: "))
for i in range(1,11):
    print(f"{numero} x {i}= {numero * i}")

#TABLAS DE MULTIPLICAR CON VARIABLE
print("\n")
numero=int(input("Ingrese un número: "))
mult=int(input("Límite a multiplicar: "))
for i in range(1, mult+1):
    print(f"{numero} x {i}= {numero * i}")

#SUMAR 10 NÚMEROS
print("\n")
suma= 0
for n in range(0,10):
    numero=int(input("Ingrese un número: "))
    suma= suma + numero
print(f"La suma es: {suma}")

#NUMEROS PARES DADO EL RANGO QUE QUERAMOS
print("\n")
num1= int(input("Dame el primer número: "))
num2= num1
while num2<=num1:
    num2= int (input("Dame otro número mayor al primer número: "))

for n in range(num1,num2+1):
    if n %2==0:
        print(n)