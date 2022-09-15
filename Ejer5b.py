#Definir una lista de números
#Sumar todos sus valores de esa lista
#Al finalizar mostrar por pantalla el total de la suma.
#No utilizar función sum

   
    #Suma un grupo de valores en una lista
    
lista   =   [36,35,1,6,89,3,12,0,14,78,90,76,56,34,100,350]

suma=0
      
for numero in lista:
    suma+=numero
                        
print(f"suma total de lista es:{suma}")