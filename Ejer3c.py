#Realizar una función que se llame relacion() que a partir de dos nros realice lo siguiente:
#Si el primer nro es mayor que el segundo, devuelva 1
#Si el primer nro es menor que el segundo, devuelva -1
#Si ambos nros son iguales, devuelva 0

def relacion(n1,n2):
   if n1>n2:
       return 1
   elif n1<n2:
       return -1
   else:
       return 0
   
n1=int(input("Ingrese un valor: "))
n2=int(input("Ingrese un segundo valor: "))

print(relacion(n1,n2))