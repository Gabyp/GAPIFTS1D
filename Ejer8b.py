#Definir una lista de números
#Encontrar el valor mínimo de la lista
#Imprimir el valor
#No utilizar min

lista   =   [6,89,12,14,78,690,76,56,34,100,350,1000,20000,5]

minimo=10000000
     
for numero in lista:
    if numero < minimo:
       minimo=numero
    
print(f"El número minimo de la lista es: {minimo}")