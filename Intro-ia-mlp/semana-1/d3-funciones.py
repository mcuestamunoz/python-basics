## Funciones
# Crear una función calcular_area_circulo(radio) que reciba el radio y devuelva el área del círculo.
# Usar la fórmula: Area = Pi * radio ** 2

import math

def calcular_area_circulo(r):
    area = math.pi * (r ** 2)
    return area

r = float(input(f"Introduce el radio: "))

area = calcular_area_circulo(r)
print(f"El área del circulo és {area:.2f}.")

# print(es_par(4))  # Salida esperada: True
# print(es_par(7))  # Salida esperada: False

def es_par(num):
    return num % 2 == 0

num = int(input("introduce el número: "))
print(f"El número es par: {es_par(num)}")

#  Escribe una función operaciones(a, b) que reciba dos números y retorne la suma, resta, multiplicación y división como una tupla.

def operaciones(a, b):
    suma = a + b
    resta = a - b
    multi = a * b
    div = a / b
    return suma, resta, multi, div

a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))


suma, resta, multi, div = operaciones(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multi}, División: {div}.")


