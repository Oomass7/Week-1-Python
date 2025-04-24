#Pide al usuario su peso (kg) y altura (m). Calcula su IMC (peso / altura²) y muestra:
#
#"Bajo peso" si es menor a 18.5
#"Normal" si está entre 18.5 y 24.9
#"Sobrepeso" si está entre 25 y 29.9
#"Obesidad" si es mayor o igual a 30


while True: 
    weigth = float(input("Ingrese su peso en kg: "))
    if weigth <= 0:
        print("Por favor ingrese un peso valido")
    else:
        break
    
while True:
    height = float(input("Ingrese su altura en metros: "))
    if weigth <= 0:
        print("Por favor ingrese un peso valido")
    else:
        break
    
imc = weigth / (height ** 2)

if imc > 0 and imc < 18.5:
    print("Bajo peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Normal")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso") 
elif imc >= 30:
    print("Obesidad")

