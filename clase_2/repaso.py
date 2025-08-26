# Comentario.

"""Hola! Este es un comentario de varias líneas.
Sirve para documentar el código.
No es obligatorio pero es una buena práctica."""

# Variables
# Reglas para declarar variables
# No puede empezar con: 1 " # $ % & / ( ) = 
# Pero si se puede con _
# Ejemplos
valor = 10
_valor = 20.0 # Cuando tenemos una variable con _ delante, es "Privada". tambien con __ delante.
valor2 = 2


# Tipos de datos básicos
var1 = 10 # Entero (int)
var2 = 20.0 # Flotante (float)
var3 = "Cadena de texto" # Cadena de texto
var4 = True # Booleanos (bool)
var5 = False # Booleanos (bool)
var6 = None # Ausencia de valor (None)


# Operaciones
resultado1 = 10 + 10 # Suma
resultado2 = 20 - 10 # Resta
resultado3 = 10 / 5 # Division
resultado4 = 2 * 2 # Multiplicación

CONSTANTE = 100 # A la constante no debemos tocarla. Se escribe en mayusculas.
PI = 3.14


# uso de print
# Para imprimir algo en pantalla podemos usar print(...)
# print es una función
# Las funciones se invocan con ()
print("Hola mundo!") # invocar, llamar, ejecutar usando () y dentro de estos el argumento

# Type hint (anotaciones)
variable: int = 10
