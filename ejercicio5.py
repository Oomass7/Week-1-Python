#Pide al usuario el total de una cuenta. Luego pregunta qué porcentaje de propina quiere dejar (10, 15 o 20). Calcula y muestra el valor de la propina.

account = float(input("Ingrese el valor de la cuenta: "))

while True:
    tip = int(input("""1. 10%
2. 15%
3. 20% 
Elija el porcentaje de propina: """))
    if tip == 1:
        valueTip = account * 0.1
        print(f"El valor de la propina es: ${valueTip}")
        break
    elif tip == 2:
        valueTip = account * 0.15
        print(f"El valor de la propina es: ${valueTip}")
        break
    elif tip == 3:
        valueTip = account * 0.2
        print(f"El valor de la propina es: ${valueTip}")
        break
    else:
        print("Valor no valido")


