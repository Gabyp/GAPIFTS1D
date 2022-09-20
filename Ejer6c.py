# Realizar una función que se llame separar() que reciba una lista de nros y devuelva dos listas ordenadas.
# La primera con nros pares.
# La segunda con nros impares.

num = [-12,84,13,20,-33, 101,9,90,4,21,1,7,60]

def separar(args):
    lista = sorted(args)
    pares = []
    impares = []
    
    for arg in lista:
        if arg % 2 == 0:
            pares.append(arg)
        else:
            impares.append(arg)
        
    return pares, impares

pares, impares = separar(num)

print(f'Los numeros pares son: {pares}\nLos numeros impares son: {impares}')
