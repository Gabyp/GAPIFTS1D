#Ejercicio 2b-Guia 2

#Pedir al usuario que ingrese dos nros
#Luego imprimir 3 opciones (1. sumar, 2. restar y 3. multiplicar)
#Pedir al usuario que ingrese una opción
#Verificar la opción del usuario
#Mientras que el usuario no ingrese una opción correcta se volverá a pedir que
#Ingrese una opción
#Ejecutar la operación
#Mostrar por pantalla el resultado

n1 = int(input("Ingresar primer número "))
n2 = int(input("Ingresar segundo número "))
print ("""Operación disponibles.
               1) Suma
               2) Resta
               3) Multipliación 
               """)

op = int(input("Seleccione una operación "))
print ("")

while (op >= 0):
        if  op==1:
            print(f"La suma es {n1+n2}")
            break

        elif op==2:
            print(f"La resta es {n1-n2}")
            break
        elif op==3:
            print(f"La multiplicación es {n1*n2}")
            break
        else:
            print ("""La operación ingresada no es válida, seleccione una operación disponible.
               1) Suma
               2) Resta
               3) Multipliación 
               """)
            op = int(input("Seleccione una operación "))
            