#Definir una lista de números
#Mostrar por pantalla el valor promedio de la lista.
#No utilizar funciones sum ni len

lista   =   [36,35,1,6,89,3,12,0,14,78,90,76,56,34,100,350]

suma=0
cant_list=0
     
for numero in lista:
    suma+=numero
    
for cantidad in lista:
    cant_list+=1
                       
promedio = (suma/cant_list) 

print(f"Promedio total de lista es: {promedio}")