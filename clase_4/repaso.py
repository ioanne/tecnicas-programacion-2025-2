# Variables
numero = 10
decimales = 10.5
texto = "hola!"
verdadero = True
falso = False
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)

# bucles
# Hay dos tipos de bucles: while y for
contador = 0
while contador < numero: # Se ejecuta mientras la condicion sea verdadera
    print(f"contador: {contador}")
    contador += 1 # contador = contador + 1
print("Termina el while")


# El for se recomienda para recorrer listas, es decir, cuando conocemos los elementos
for numero in lista: # lista = [1, 2, 3, 4, 5]
    print(f"numero: {numero}")







condicion_uno = True
condicion_dos = False
condicion_tres = True
mayor = 10 > 5 # ¿Cómo evalua? True
menor = 5 < 10 # True
igual = 5 == 15 # False
distinto = 10 != 11 # True

# Condicionales

# un if
if condicion_uno:
    print("Condición uno es verdadera")


# un if y un else
if condicion_uno:
    print("Condición uno es verdadera")
else:
    print("Condición uno es falsa")

# un if y un elif
if condicion_uno:
    print("Condición uno es verdadera")
elif menor:
    print("Condición menor")

# un if y mas de un elif
if condicion_uno:
    print("Condición uno es verdadera")
elif menor:
    print("Condición menor")
elif mayor:
    print("Condición mayor")
elif igual:
    print("Condicion igual")

# un if un elif y un else
if condicion_uno:
    print("Condición uno es verdadera")
elif menor:
    print("Condición menor")
else:
    print("Condición uno es falsa")


# un if muchos elif y un else
if condicion_uno:
    print("Condición uno es verdadera")
elif menor:
    print("Condición menor")
elif mayor:
    print("Condición mayor")
elif igual:
    print("Condicion igual")
else:
    print("Condición uno es falsa")

# Operador OR y AND

if menor or mayor:
    print("Es menor o mayor")

if igual is not None and igual == False:
    print("Igual no es None.")

# AND
(True and False) # False


((True and True) and False)

#NAND
not (True and False) # True


True is True
var1 = 10
var2 = 10 
var3 = None

var1 is var2 # NO

var3 is None # Para esto se usa el is.
var3 is not None # Para esto se usa el is.

# OR = +
# AND = *









