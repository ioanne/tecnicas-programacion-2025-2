# Escribimos nuestro código

"""
Reglas de las varibles:
    No pueden comenzar con un número
    No pueden comenzar con caracteres especiales como:
        ! , . # " $ % & / ( ) =
    Si pueden comenzar con _

"""

# Sintaxis
# snake case escribir_de_esta_manera
# camel case escribirDeEstaManera
# upper camel case EscribirDeEstaManera
# Guia de estilos de google https://google.github.io/styleguide/pyguide.html


_variable = 10 # Variable privada
__variable = 10 # Variable MUY privada
variable1 = 1

edad = 33 # Tipo de dato numero (int) (integer) (entero)
nombre = "Juan Ignacio" # Tipo de dato texto (str) (string) ("cadena" de texto)
apellido = "Bonini" # Texto

print(edad, nombre, apellido)

# Boolean / Booleano
verdadero = True
falso = False

# Float / Flotante
flotante = 1.10 # Decimal

# Ausencia de valor
nulo = None


variable = None
variable = "Diez"
variable = 10

# Valores que no deberían cambiar
CONSTANTE = 100

"""
Se resuelve primero lo de la derecha del igual (=)
luego se almacena dentro de la variable.
Ejemplo:
"""

suma = 10 + 5
print(suma)

"""
Operaciones aritmeticas basicas

Suma            +
Resta           -
Multiplicacion  *
Division        /

"""

suma = 1 + 1
resta = 1 - 1
multiplicar = 2 * 2
dividir = 3 / 3

print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicacion: ", multiplicar)
print("Division: ", dividir)