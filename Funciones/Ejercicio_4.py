"""Realiza una función llamada intermedio(a, b) que a partir de dos números, devuelva
su punto intermedio. Cuando lo tengas comprueba el punto intermedio entre -12 y 24: """

num_1 = int(input("Numero 1 >> "))
num_2 = int(input("Numero 2 >> "))

def intermedio(a, b):
    return (a + b) / 2
resultado = intermedio(num_1, num_2)
print(f"El numero intermedio de los numeros {num_1}, {num_2} es {resultado}")