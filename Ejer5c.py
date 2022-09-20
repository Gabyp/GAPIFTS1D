# Realizar una función que se llame recortar() que reciba 3 parámetros.
# 1º param => nro a recortar
# 2º param => es el límite inferior
# 3º param => es el límite superior

# La función debe cumplir lo siguiente:
# Devolver el límite inferior si el nro es menor
# Devolver el límite superior si el nro es mayor
# Devolver el nro si no supera los límites

def recortar(num,lim_inf,lim_sup):
    if num<lim_inf:
        return lim_inf
    elif num>lim_sup:
        return lim_sup
    else:
        return num

num=int(input(""" 
En caso de ingresar un mumero menor a 100 se ingresará 100
En caso de ingresar un mumero mayor a 1000 se ingresará 1000
Ingrese numero: """))

lim_inf=100
lim_sup=1000

print(f'''
El numero es:''',recortar(num,lim_inf,lim_sup))