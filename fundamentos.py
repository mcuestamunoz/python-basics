# Suma: 15
# Resta: 5
# Multiplicación: 50
# División: 2.0

try:
    a = int(input("Introduce el primer número "))
    b = int(input("Introduce el segundo número "))

    print(f"\nSuma: {a + b}")
    print(f"\nResta: {a - b}")
    print(f"\nMultiplicación: {a * b}")
    print(f"\nDivisión: {a / b:.2f}")

except ValueError:
    print("Error: Introduce números enteros.")
except ZeroDivisionError: 
    print("Error: No se puede dividir entre zero.")