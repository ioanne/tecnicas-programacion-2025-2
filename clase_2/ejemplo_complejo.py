puntajes = [1,2,3,4,5,4,3,4,4,5,6,3,3,4,4,5,4,9,9,9,8,7,8,10,8,7,7,8,8]

puntaje_encontrado = False
contador = 0

while not puntaje_encontrado:
    if puntajes[contador] == 10:
        print("Puntaje encontrado")
        puntaje_encontrado = True
    contador = contador + 1
print("Termina")

# if 10 == 10:
#     print("Es igual")


# """
# si <condicion>:
#     nuestro codigo
#     nuestro codigo
#     ......



# si <condicion>:
#     .....
#     .....
#     .....
# sino:
#     .....
#     .....
#     .....
# """
