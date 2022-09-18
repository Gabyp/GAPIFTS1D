#Realizar una función que se llame intermedio() que a partir de dos nros devuelva el punto intermedio.
#Ej. El punto intermedio entre 10 y 24 = 17; entre 12 y 50 = 31.

def intermedio(n1,n2):
    Intermed=int((n1+n2)/2)
    return Intermed
n1=int(input ("Ingrese un numero: "))
n2=int(input ("Ingrese un numero: "))


print(f'El punto intermedio entre {n1} y {n2} es:', intermedio(n1,n2))