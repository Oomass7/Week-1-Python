#Pide un año al usuario. Determina si es bisiesto (es divisible entre 4 y no entre 100, excepto si también es divisible entre 400).

año = int(input("Ingrese un año: "))

leap = año % 4
leap2 = año % 100


if leap == 0 and leap2 != 0:
    print("El año es bisiesto")
else:
    print("El año no es biciesto")