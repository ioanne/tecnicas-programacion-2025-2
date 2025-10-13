# Esperamos a que se sume gente xD!

"""
El bucle while

"""
condicion = True
while condicion:
    condicion = False

while True:
    print("While....")
    break

contador = 0
while contador < 2:
    #
    #
    #
    #
    contador += 1
# print(contador)


texto = "Este es un texto"
contador = 0
while contador < len(texto):
    contador += 1


for letra in texto:
    pass

"""
Contar palabras Creá contar_palabras(texto)
que recorra un texto y cuente cuántas palabras hay
(una palabra se separa por espacios).
No uses .split()
implementá el conteo con un while y
verificá los espacios manualmente.
"""


texto = "Este es un texto de prueba para ver si anda bien."
def contar_palabras(texto):
    # El algoritmo empieza acá
    indice = 0
    cantidad_palabras = 0
    while indice < len(texto):
        if texto[indice] == " " and texto[indice + 1] != " ":
            cantidad_palabras += 1
        indice += 1

    if cantidad_palabras > 0:
        cantidad_palabras += 1
    return cantidad_palabras
    # El algoritmo termina acá.

cantidad_palabras = contar_palabras(texto)
print(cantidad_palabras)

palabras = "Uno dos"
palabras = "Uno dos tres"

texto = "Este es un texto de prueba para ver si anda bien."
print(len(texto.split(" ")))
