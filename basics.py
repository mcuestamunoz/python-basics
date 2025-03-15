# Definiendo variables
nombre = "Luis"
edad = 30
altura = 1.65
is_devoloper = False  # Booleano (Verdadero/Falso)

# Mostrando información
print(f"Hola, me llamo {nombre}, tengo {edad} años y mido {altura}m.")
print("¿Soy programador?", is_devoloper)

pi = 3.14159
print(f"Pi rounded to 2 decimals: {pi:.2f}")  # Outputs: Pi rounded to 2 decimals: 3.14


def get_age():
    return 25

print(f"My age is {get_age()}.")  # Outputs: My age is 25.

name = "Marc"
age = "twenty-five"
height = 1
is_programmer = False

print(type(name))        # <class 'str'> (String)
print(type(age))         # <class 'int'> (Integer)
print(type(height))      # <class 'float'> (Float)
print(type(is_programmer))  # <class 'bool'> (Boolean)

####

# user_name = input("What is your name? ")
# user_age = int(input("How old are you? "))  # Convert input to integer
# user_height = float(input("How is your hight?"))

# print(f"Nice to meet you, {user_name}! In 10 years, you will be {user_age + 10}. Your height {user_height} is so hight")

####

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

###

grade = int(input("Enter your grade: "))

if grade >= 90:
    print("You got an A! 🎉")
elif grade >= 80:
    print("You got a B! 👍")
elif grade >= 70:
    print("You got a C.")
elif grade >= 60:
    print("You got a D.")
else:
    print("You failed. 😢")

##

temperature = int(input("Enter the temperature: "))

if temperature > 30 and temperature < 40:
    print("It's hot! ☀️")
elif temperature <= 30 or temperature >= 40:
    print("It's either cool or extremely hot! 🌡️")

###

favorite_fruit = input("Enter your favorite fruit: ")

fruits = ["apple", "banana", "cherry"]

if favorite_fruit.lower() in fruits:
    print("That fruit is available! 🍏🍌🍒")
else:
    print("Sorry, we don’t have that fruit.")

## Exercise
# Escriba un programa que: 
# 1️. Pida al usuario un número .
# 2️. Verifique si el número es positivo, negativo o cero .
# 3️. Imprima el resultado usando if / elif / else. 

#  Aquí te explicamos cómo puedes hacerlo:
    # Un numero es parsinumber % 2 == 0
    # Un número es impar si `nunumber % 2 != 0

number = int(input("Enter a number: "))

if number > 0:
    print("It's positive ")
elif number < 0:
    print("It's negative ")
else:
    print("It's zero")

