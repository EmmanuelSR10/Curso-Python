"""Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:
>> Si el primer número es mayor que el segundo, debe devolver 1.
>> Si el primer número es menor que el segundo, debe devolver -1.
>> Si ambos números son iguales, debe devolver un 0."""

num_1 = int(input("Ingresa un número: "))
num_2 = int(input("Ingresa otro número:  "))

def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    elif a == b:
        return 0
resultado = relacion(num_1, num_2)
print(f"Devuelve {resultado}")