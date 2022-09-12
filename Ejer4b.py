#Definir una lista
#Contar los elementos de esa lista
#Al finalizar mostrar por pantalla la cantidad de elementos de la lista
#No utilizar función len


lista = ["Paleta", "pelota", "gato"]

def elementos(lista):
    count = 0
    for element in(lista):
        count += 1
    return count

print("Cantidad de elementos en la lista : ", elementos(lista))