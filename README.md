Fundamentos

¿Qué es programar?
R/ Programar es la accion de escribir una serie de instrucciones ordenadas para dar solucion a una necesidad

¿Qué es Python y para qué sirve?
R/ Python es un lenguaje de programación y sirve para la creacion de software

¿Qué es un programa y cómo se ejecuta?
R/ Un programa es una serie de instrucciones que se ejecutan a traves de una consola o terminal de una computadora

¿Qué es una variable?
R/ Una variable es un dato que puede variar dependiendo de su tipo, y se le puede asignar un valor inicial

Tipos de datos básicos: texto (str), número entero (int), número decimal (float), verdadero/falso (bool).
R/ name = "Tomas Loaiza"
age = 20
heigth = 1.73
developer = True

Operaciones básicas con números (+, -, *, /).
R/ 2 + 3
10 - 4
2 * 7
50 / 5

Mostrar información en pantalla: print().
R/ print("Hola mundo")

Pedir información al usuario: input().
R/ input("Digite su edad")

Convertir tipos de datos: int(), float(), str().
R/ newInt = int(heigth)
newFloat = float(heigth)
newString = str(developer)

¿Qué es un error? Errores comunes para principiantes.
R/ Un error es una situacion o problema en el codigo que resulta en un comportamineto no deseado para el programa. Uno de los errores mas comunes dentro de los desarrolladores principiantes es la falta de los dos puntos(:) luego de un if, elif, else, etc.

Comparar datos: (==, !=, <, >, <=, >=).
R/ name == age
height == developer
age <= height 
age >= height



Tomar decisiones: if, else, elif.
R/ 
if age > height:
    print("Hola mundo")
elif age < height:
    print("Adios mundo")
else:
    print("Hello World")

Combinar condiciones: and, or, not.
R/ logicOper = (age or height) and (not developer)

Cómo escribir comentarios en el código (# comentario).
R/ #En esta linea estamos aprendiendo herramientas y conicimineto sobre python

Qué es la indentación y por qué es tan importante en Python.
R/ La identacion se refiere a la sangria (tabulacion entre desarrolladores) que hay dentro de una linea de codigo y es muy importante ya que esta marca la jerarquia del codigo dentro de un bloque

Buenas prácticas al nombrar variables (nombres claros, sin espacios).
R/ lastName = "Rodriguez"

¿Qué hacer cuando algo no funciona? (buscar, leer errores, no frustrarse).
R/Cuando algo no funciona lo mejor es leer el error (si lo hay) para entenderlo, luego investigar y aprender a solucionar el error, en caso de que no se encuentre lo deseado, pedir ayuda a alguien que tenga concimineto

Repetir acciones con bucles: for y while.
R/ 
while age == 20:
    print(f"Usted tiene {age} años")

Salir de un bucle antes de tiempo: break y continue.
R/
while age == 20:
    print(f"Usted tiene {age} años")
    break 

Manejo básico de errores: try-except.
R/
while True:
    try:
        number = int(input("Ingrese un numero: "))
        print (number)
        break
    except:
        print("Intentas escribir una letra/palabra")


