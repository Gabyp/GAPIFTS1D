#Realizar una función que se llame area_rectangulo() que devuelva el área del cuadrado a partir de su base y altura.


def area_rectangulo(b,h):
    area=b*h
    return area
b= int (input("Ingrese el valor de la base "))
h= int (input("Ingrese el valor de la altura "))


print (f'Resultado del area es:', area_rectangulo(b,h))