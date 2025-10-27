"""
Una fábrica produce botellas de jugo.
Cada botella debe pesar exactamente 500 gramos, con una tolerancia de ±5 %.
El sistema recibe una lista con los pesos medidos de varias botellas.
Tu tarea es crear una función control_calidad(pesos)
que recorra la lista usando un bucle while,
y cuente cuántas botellas cumplen con la tolerancia y cuántas no.
La función debe devolver ambos valores.
"""

# Buscamos el dato de entrada
# El peso de cada botella



def control_calidad(pesos):
    TOLERANCIA = 0.05 # 5%

    cumplen = 0
    no_cumplen = 0
    indice = 0 # es nombre mas representativo
    limite_inferior = 500 - (500 * TOLERANCIA) # 475 
    limite_superior = 500 + (500 * TOLERANCIA) # 525

    # Para usar un while necesitamos un contador
    while indice < len(pesos): # estructura de repeticón
        peso = pesos[indice]
        if peso <= limite_superior and peso >= limite_inferior: # estructura de control
            # aumentamos a cumplen
            cumplen = cumplen + 1
        else:
            # aumentamos no cumplen
            no_cumplen = no_cumplen + 1

        indice += 1 # agarrar el próximo
    return cumplen, no_cumplen


# cumplen 3
# no cumplen 2
pesos = [500, 501, 529, 468, 498]

resultado = control_calidad(pesos)
print(resultado)



"""
2) Promedio de notas
Escribí una función promedio_notas() que pida notas por pantalla hasta ingresar -1.
Usá un while para acumularlas y calcular el promedio final. Si no se ingresó ninguna nota
válida, devolvé None.


2) Promedio de notas
Escribí una función promedio_notas()
Usá un while para acumularlas y calcular el promedio final. Si no se ingresó ninguna nota válida,
devolvé None.
"""
notas = []
while True:
    nota = input("Ingresar nota: ")
    if nota == -1:
        break
    notas.append(nota)
    

notas2 = [9,8,7,8,9,6]

def promedio_notas(notas):
    indice = 0
    notas_totales = 0
    while indice < len(notas):
        nota = notas[indice]
        if not (nota <= 10 and nota >= 0):
            return None
        notas_totales = notas_totales + nota
        indice += 1
    return notas_totales / len(notas)

