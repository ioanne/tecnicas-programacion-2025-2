# Tipos de datos básicos
var1 = 10 # Entero (int)
var2 = 20.0 # Flotante (float)
var3 = "Cadena de texto" # Cadena de texto
var4 = True # Booleanos (bool)
var5 = False # Booleanos (bool)
var6 = None # Ausencia de valor (None)


# Tipos de datos estructurales
# Lista
lista_vacia = []
lista_numeros = [1,2,3,4]
lista_nombres = ["Juan", "Pedro", "Julian", "Maria"]
lista_mediciones = [1.232, 3.4534, 23.12312]
lista_validaciones = [True, False, False, True]

# Las listas no tienen limitaciones de tipos de datos.
# Podemos meter lo que se nos ocurra, siempre y cuando, nos alcance la memoria RAM de la PC.
lista = [
    1,2,3,4,
    "Juan",
    "Pedro",
    "Julian",
    "Maria",
    1.232,
    3.4534,
    23.12312,
    True,
    False,
    False,
    True,
    None,
    [1,2,3],
    ["Juan", "Pedro", "Julian", "Maria"],
    [[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]],
    (1,2,3),
    {"clave":"valor"}
]
# Las listas nos permiten almacenar cualquier tipo de dato.
# Las listas son mutables.
# Las listas son estructuras que mantienen la posición de los elementos
# A las listas podemos agregarle o quitarles datos.
# Para averiguar el tamaño de una lista, podemos usar la funcion len

# Pseudo código
# estructura.accion()

dict_basico = {"clave": "valor"}

nombres = {
    "varon": ["Lucas", "Juan"],
    "mujer": ["Jorgelina", "Maria"],
    "unisex": ["sasha"]
}

# tupla
tupla = (1,2,3,4)

# conjuntos
conjunto = {}


# Bucles repetitivos
# Estructuras de repeticion / recorrer

"""
El bucle while mientras la condición es verdadera, va a recorrer.

Pseudo código
mientras<condicion>:
    Se ejecuta el código.

"""
# while True: # Iterador infinito
#     # Mientras es verdadero, hacemos algo.
#     pass

# El while se utiliza cuando no conocemos lo que estamos iterando.

valores = [1,2,3,4]
for valor in valores:
    print(valor)

# Es un sistema de puntajes que va creciendo
puntajes = [1,2,3,4,5,4,3,4,4,5,6,3,3,4,4,5,4,9,9,9,8,7,8,10,8,7,7,8,8]

puntaje_encontrado = False # Flag
contador = 0 # Contador que inicializa en 0.

while not puntaje_encontrado: # Condicion "de corte"
    if puntajes[contador] == 10: # Estructura de control que nos va permitir hacer chequeos 
        print("Puntaje encontrado")
        puntaje_encontrado = True
    contador = contador + 1

# Estructura de control (la mas basica)
"""Pseudo código:

si se cumple la <condicion>
    se hace algo

los operadores de comparación:
== 
>= 
<=
!=


<condicion>
si 10 == 10 (Es verdadero)
si 11 == 5  (Es falso)
si 10 > 5   (Es verdadero)
si 10 > 10  (Es falso)
si 10 >= 10 (Es verdadero)
si 10 != 5  (Es verdadero)
"""
if 10 == 10:
    print("Es igual")

if 11 == 5:
    print("Es igual")
else:
    print("Es distinto")