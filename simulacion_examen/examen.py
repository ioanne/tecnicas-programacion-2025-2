# Unit   Total
# 500    1000 -> 50 %
# 300    1000 -> 30 %
# 200    1000 -> 20 %

def analizar_lote(volumenes):
    proporciones_teoricas = (50, 30, 20) # tupla
    tolerancia = 5

    dentro_rango = 0
    fuera_rango = 0

    indice = 0 # Los recorridos
    while indice < len(volumenes):
        volumen = volumenes[indice] # Obtenemos desde el indice el primer volumen
        indice += 1
        total = 0

        for proporcion in volumen:
            total += proporcion
        
        cont = 0
        aprobado = False

        # porcentaje_proporcion
        for proporcion in volumen:
            porcentaje_proporcion = (proporcion / total) * 100
            esperado = proporciones_teoricas[cont]
            cont += 1

            minimo = esperado - tolerancia
            maximo = esperado + tolerancia
            
            if porcentaje_proporcion >= minimo and porcentaje_proporcion <= maximo:
                aprobado = True
            else:
                aprobado = False
                break     
        if aprobado:
            dentro_rango += 1
        else:
            fuera_rango += 1
    return fuera_rango == 0

volumenes = [(500, 300, 200),(500, 300, 200), (500, 300, 200), (500, 300, 200)]
print(analizar_lote(volumenes))

