#Fija un número secreto (por ejemplo, 7). Pide al usuario que lo adivine. Di si su número es mayor, menor o igual al número secreto.

secretNumber = 7


while True:
    number = int(input("Intente adivinar el numero secreto, ingresa un numero: "))
    if number < secretNumber:
        print("Tu numero es menor")
    elif number > secretNumber:
        print("Tu numero es mayor")
    else:
        number == secretNumber
        print("Haz adivinado el numero secreto")
        break


