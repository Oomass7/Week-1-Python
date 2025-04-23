#Pide un número al usuario. Di si es positivo, negativo o si es cero.

number = float(input("INgresa un numero: "))

if number > 0:
    print("El numero es positivo")
elif number < 0:
    print("El numero es negativo")
elif number == 0:
    print("El numero es cero")