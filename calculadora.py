#Ejercicio Grupal

""" 
Crear un programa en Python que tendrá 3 o 4 funciones:

* Suma, 3 parámetros, devuelve la suma de los 3.
* Resta, 2 parámetros, devuelve la resta de los 2.
* Producto, 4 parámetros, devuelve el producto de los 4.
* Imprimir, 2 parámetros, texto y valor, devuelve la impresión de los valores pasados.
Usaremos Visual Studio Code, con la extensión de Python para hacer la práctica.
El equipo crea un Project en Github y agrega 2 al menos 2 issue por cada tarea a realizar.
Crear una rama por cada miembro. 

"""
# CLI GUI - Edgar G. - 2022
# ---------------------------------------------------------------------------------------------------------
# Creando un menú básico del programa usaré Input, Verdadero, Falso, Bucle While, Print, If, Else, Elif:
# Aplico contenido aprendido en Modulo 1, 2, 3, de Python Essentials 1
# ---------------------------------------------------------------------------------------------------------


cerrar = False           # Variable Booleana para salir del bucle del menú, seteada en False.

while cerrar != True :   # Mientras que la variable sea distinta de True se ejecutará el menu infinitas veces.
    print("\n-----------------------------")
    print("Bienvenido a Calculadora V0.1")  # Código del Menú desde Aquí.
    print("-----------------------------")
    
    print("Seleccione operación realizar:\n")

    print("1 - Para hacer una suma.")
    print("2 - Para hacer una resta.")
    print("3 - Para hacer una multiplicacion.")
    print("4 - Para hacer una división entera.")
    print("0 - Para salir del programa.")
    
    seleccion = int(input("\nEscriba su número de opción: "))  # Entrada de opcion numérica del menú, un numero.

    if seleccion == 0:  # Si se ingresa un cero, pasamos el booleano a True y se cerrará el programa ya que el bucle 
        cerrar = True   # While está esperando esta condición para terminar y muestra el menu infinitas veces.
                        # ponemos pass que no hace nada, temporalmente para que no de error el código.
    elif seleccion == 1:
        #codigo de la suma aqui con sus mensajes, o bien hacemos una función y la llamamos.
        num1 = input("Introduce el primer numero: ")
        num2 = input("Introduce el segundo numero: ")
        num3 = input("Introduce el tercer numero: ")

        num1  = int(num1)
        num2 = int(num2)
        num3 = int(num3)

        suma = num1+num2+num3
        
        print ("La suma de los tres números es:", suma)
        
    elif seleccion == 2:
        #codigo de la resta aqui con sus mensajes, o bien hacemos una función y la llamamos.
        num1 = input("Introduce el primer numero: ")
        num2 = input("Introduce el segundo numero: ")
        num3 = input("Introduce el tercer numero: ")

        num1  = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        
        resta = num1-num2-num3
        print ("La resta de los tres números es:", resta)


    elif seleccion == 3:
        pass #codigo de la resta aqui con sus mensajes, o bien hacemos una función y la llamamos. 
    elif seleccion == 4:
        pass #codigo de la resta aqui con sus mensajes, o bien hacemos una función y la llamamos. 
  
    else:
        print ("Ups, debe elegir una opción válida del menú entre las indicadas :)")

    

print("\nSalió del programa, que tenga buen día!")
