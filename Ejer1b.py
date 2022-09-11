#Pedir al usuario que ingrese un nro impar
#Mientras que el usuario no ingrese un nro impar se volverá a pedir que ingrese un nro impar
#Deberá indicar por pantalla si es impar

numero = int(input ("Ingrese un numero:")) 
if numero & 1 == 0:
    print ("Ingrese un número impar")
else:
    print ("El numero es impar")    

    