"""La empresa EcoClean realiza controles de calidad automatizados sobre sus productos
líquidos. Cada lote se compone de tres sustancias: agente activo, diluyente y
conservante, cuyas proporciones teóricas deben ser 50 %, 30 % y 20 %, respectivamente.
Durante la producción, una máquina de medición informa los volúmenes reales utilizados
de cada componente (en mililitros). El objetivo del sistema es verificar si la mezcla cumple
con las especificaciones de formulación, considerando un margen de tolerancia de ±5
% para cada componente respecto de los valores teóricos.
Se solicita desarrollar un programa en Python que:
1. Solicite los volúmenes medidos de los tres componentes.
2. Calcule los porcentajes reales a partir del total.
3. Compare los resultados con los valores teóricos y determine si cada componente
está dentro del rango permitido.
4. Indique si el lote es APROBADO o RECHAZADO.
5. Permite repetir el proceso para múltiples lotes mientras el usuario lo desee.
El programa debe implementarse utilizando:
● Una función encargada de realizar el análisis y devolver el resultado.
● Un bucle while para la iteración.
● Estructuras if/elif/else para las decisiones lógicas."""