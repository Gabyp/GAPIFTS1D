#Pedir al usuario que ingrese un email
#Verificar si el usuario ingresó una dirección de email (basta con que tenga un "@")
#Al finalizar mostrar por pantalla si es un email o no
#No utilizar in

email =str(input("Por favor ingrese un email "))

if email.count("@"):
    print ("El elemento ingresado es un email")

else:
    print("El elemento ingresado no es un email")