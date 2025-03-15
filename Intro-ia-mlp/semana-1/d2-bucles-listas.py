# Baicos If, elif, else

num = int(input("Introduce un número: "))

if num > 0:
    print("El número es positivo")
elif num < 0: 
    print("El número es negativo")
else:
    print("El número es cero") 

# Numero par o impar

num = int(input("Introduce un número: "))

if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar") 

# bucles For

suma = 0

for i in range(1,11):
    suma += i
print("La suma de los número del 1 al 10 es: ", suma)

## Retos adicional 1:

a = int(input("Introduce el número inicial del rango "))
b = int(input("Introduce el número final del rango "))

if a > b:
    a, b = b, a

#Posible mejora para hacer mas compacto el código
# suma = sum(range(a, b + 1))
# print(f"La suma de {a} al {b} es: {suma}")
suma = 0

for i in range(a, b + 1):
    suma += i 
print(f"La suma de {a} al {b} es: {suma}")

## Retos adicional 2:

try: 
    a = int(input("Introduce el número inicial del rango "))
    b = int(input("Introduce el número final del rango "))

    if a > b:
        a, b = b, a

        suma = 0

        i = a
        while i <= b:
            suma += i
            i += 1

    print(f"La suma de {a} al {b} es: {suma}")
except ValueError:
    print("Error, introduce solo números enteros")


## Diccionarios y listas

# Ejercicio 1: lista de 5 números, busca el número mas grande

lista = [int(input("Introduce un número: ")) for _ in range(5)]

print(f"La lista és: {lista}")
print(f"El número más grande és: {max(lista)}")

# Ejercicio 2:
# Crear un diccionario con nombre, edad y ciudad.
# Agregar un nuevo dato, como "profesión" o "correo electrónico".
# Mostrar el diccionario actualizado.

persona = {
    "nombre": "Marc",
    "edad": 25,
    "ciudad": "Parets del Valles"
}

persona["profesión"] = "Analista"
persona["correo electrónico"] = "marc.parets@gmail.com"

for clave, valor in persona.items():
    print(f"{clave.capitalize()}: {valor}")

