#Pide un número al usuario. Di si está dentro del rango de 1 a 10 (inclusive).

number = float(input("Ingrese un numero: "))

if number >= 1 and number <= 10:
    print("Su numero esta dentro del rango de 1 a 10")
else:
    print("Su numero NO esta dentro del rango de 1 a 10")