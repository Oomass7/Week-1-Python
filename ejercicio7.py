#Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo.

number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))

if number1 == number2:
    print("Los dos numero son iguales")
elif number2 > number1:
    print(f"El numero 2: {number2} es mayor que el numero 1: {number1}")
elif number1 > number2:
    print(f"El numero 1: {number1} es mayor que el numero 2: {number2}")