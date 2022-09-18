#Realizar una función que se llame area_circulo() que devuelva el área del círculo a partir de su radio.
#Utilizar el valor 3.14159 como pi

def area_circulo(pi,r):
    area=pi*r**2
    return area

r=int(input("Ingrese un numero "))
pi=3.14159
a=pi*r**2

print(f'El area del circulo es: {a}')


