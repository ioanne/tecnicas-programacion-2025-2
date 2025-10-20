"""
Para crear una función usa la palabra def
luego, el nombre que le queremos dar a nuestra función
!"#!"$&%())&/
no puede empezar con número

pero sin con _

"""

def nombre_funcion(): # La función es una especie de caja negra.
    return

def suma(valor_a, valor_b): # Se declaran las variables valor_a, valor_b
    return valor_a + valor_b # acá las podemos usar

suma(5, 8) # por posición
suma(valor_a=5, valor_b=8) # por nombre
suma(5, valor_b=8) # mixto

"""
5. Buscar elemento
Implementá buscar_elemento(lista, objetivo) que use un while para devolver
True si el valor está en la lista y False si no.
"""

def buscar_elemento(lista, objetivo): # doble return
    indice = 0
    while indice < len(lista):
        if lista[indice] == objetivo:
            return True
        indice += 1
    return False

def buscar_elemento1(lista, objetivo):
    objetivo_encontrado = False # Variable de estado
    indice = 0
    while indice < len(lista):
        if lista[indice] == objetivo:
            objetivo_encontrado = True
        indice += 1
    return objetivo_encontrado

def buscar_elemento2(lista, objetivo): # Sin usar while
    return objetivo in lista

def buscar_elemento3(lista, objetivo): # Mismo funcionamiento
    for elemento in lista:
        if elemento == objetivo:
            return True
    return False

lista = [1,2,3,4,5,6]
resultado = buscar_elemento(lista, 51)
print(resultado)

lista = [1,2,3,4,5,6]
resultado = buscar_elemento1(lista, 51)
print(resultado)

lista = [1,2,3,4,5,6]
resultado = buscar_elemento2(lista, 51)
print(resultado)


lista = [1,2,3,4,5,6]
resultado = buscar_elemento(lista, 1)
print(resultado)

lista = [1,2,3,4,5,6]
resultado = buscar_elemento1(lista, 1)
print(resultado)

lista = [1,2,3,4,5,6]
resultado = buscar_elemento2(lista, 1)
print(resultado)