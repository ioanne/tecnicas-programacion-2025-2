"""
variables
donde vamos a almacenar diferentes datos
"""

texto = "Hola, soy una variable de tipo texto"
numero = 42 # variable de tipo entero

listas_textos = ["manzana", "banana", "cereza"] # variable de tipo lista
listas_numeros = [1, 2, 3, 4, 5] # variable de tipo lista
listas_mixtas = ["texto", 100, 3.14, True] # variable de tipo lista

diccionarios_texto = {"nombre": "Juan", "apellido": "Pérez"} # variable de tipo diccionario
diccionarios_numeros = {"edad": 30, "año": 2024} # variable de tipo diccionario
diccionarios_mixtos = {
    "nombre": "Ana",
    "edad": 25,
    "sexo": "Femenino",
    "es_estudiante": True
} # variable de tipo diccionario

alumno = {
    "nombre": "Luis",
    "edad": 20,
    "cursos": ["Matemáticas", "Física", "Química"],
    "promedio": 8.5,
    "activo": True
}

alumnos = [
    {
        "nombre": "Luis",
        "edad": 20,
        "cursos": ["Matemáticas", "Física", "Química"],
        "promedio": 8.5,
        "activo": True
    },
    {
        "nombre": "María",
        "edad": 22,
        "cursos": ["Biología", "Historia"],
        "promedio": 9.0,
        "activo": False
    }
]
alumno = alumnos[0]
lista_sencilla = [1, 2, 3, 4, 5]
lista_sencilla[0] # 1
lista_sencilla[4] # 5

for valor in lista_sencilla:
    print(valor)

indice = 0
while indice < len(lista_sencilla):
    print(lista_sencilla[indice])
    indice += 1


diccionario_sencillo = {"clave1": "valor1", "clave2": "valor2"}
diccionario_sencillo["clave1"] # "valor1"
diccionario_sencillo["clave2"] # "valor2"

"""
si {condición} :
    {bloques de código}
    ...
    ...
    ...
    ...
si no se da lo anterior es {nueva_condición} :
    {bloques de código}
    ...
    ...
sino:
    {bloques de código}
    ...
    ...
    ...
"""

"""
if (1 == 2):
    pass
elif (2 == 3): # tantos como se quieran
    pass
elif (3 == 5): # tantos como se quieran
    pass
else:
    pass
"""

"""
else if en español es "si no"

else en español es "de lo contrario"
"""

if diccionario_sencillo["clave1"] == "valor":
    print("La clave1 tiene el valor 'valor1'")
else:
    print("La clave1 no tiene el valor 'valor1'")

""" operadores de comparación
== igual a
!= diferente de
> mayor que
< menor que
>= mayor o igual que
<= menor o igual que

operadores aritméticos
+ suma
- resta
* multiplicación
/ división
// división entera
% módulo
** potencia


operadores lógicos
and y
or o
not no

"""

10 > 5 # True
5 < 10 # True

v1 = 10
v2 = 5

v1 >= v2 # True
v2 <= v1 # True

10 // 4 # 2

a = 10
b = 0

b != 0 and a / b

True and False and 10 / 0
True or False

(True or False) or (True and True or False)
True or True


True or False or True and True or False # 1 + 0 + 1 * 1 + 0 = 

1 + 1 = 1

10
0


# and es multiplicación
# or es suma

1 * 0 # True and False | False
1 * 1 # True and True | True
0 * 0 # False and False | False
0 * 1 # False and True | False

1 + 0 # True or False | True
1 + 1 # True or True | True
0 + 0 # False or False | False
0 + 1 # False or True | True



def foo(a, b):
    if a == b:
        return a
    return 0

def foo(a, b):
    if a == b:
        return a

def suma(a,b):
    if a > 0:
        resultado = a + b
        return resultado
    
suma(10, 5)
suma(5, 3)
suma(-5, 3)

def suma(a,b):
    return a + b

def suma1(a,b):
    return a + b

def _suma(a,b):
    return a + b

def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
"""explicame con ejemplo la busqueda de burbuja paso a paso para un lista conocida
[5, 2, 9, 1, 5, 6]

"""

def buscar_en_texto(texto, subtexto):
    """sin usar in"""
    for i in range(len(texto) - len(subtexto) + 1):
        encontrado = True
        for j in range(len(subtexto)):
            if texto[i + j] != subtexto[j]:
                encontrado = False
                break
        if encontrado:
            return True
    return False

def buscar_en_texto(texto, subtexto):
    if subtexto in texto:
        return True
    return False

for numero in range(10, 0, -1):
    print(numero)

# range
# len
# sum


# Promedio de las notas
notas = [1,2,3,4]
cont = 0
suma_notas = 0
while cont < len(notas):
    suma_notas += notas[cont]
    cont += 1
suma_notas / len(notas)

sum(notas) / len(notas)