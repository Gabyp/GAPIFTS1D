#Definir una lista de números
#Encontrar el valor máximo de la lista
#Imprimir el valor
#No utilizar max


lista   =   [1,6,89,3,12,0,14,78,690,76,56,34,100,350,1000,20000]

maximo=0
     
for numero in lista:
    if numero > maximo:
       maximo=numero
    
print(f"El número maximo de la lista es: {maximo}")