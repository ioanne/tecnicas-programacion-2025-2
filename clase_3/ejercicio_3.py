"""
Problema 3:
Queremos que un programa decida si una persona puede acceder a un parque de
diversiones y a qué atracciones puede subir.
● Primero, la persona debe ser mayor de 12 años para poder ingresar al parque.
● Dentro del parque, si además mide más de 1,60 metros, puede subir a la montaña
rusa.
● Si no cumple con la altura, solo podrá acceder a los juegos infantiles.
● En caso de ser menor de 12 años, no puede ingresar al parque.
● Investigar qué son los condicionales anidados en Python y cómo funcionan.
● Documentar todo el proceso de resolución.
● Si se utilizó una IA como apoyo, se debe guardar y mostrar la conversación
completa.
● Explicar qué debates o decisiones se tomaron para resolver el problema.
● Documentar el paso a paso seguido para construir la solución.
● Explicar qué hace cada línea del código y justificar por qué se escribió de esa forma.
● Asegurarse de explicar los conceptos básicos que aparecen en el código
(condicionales, operadores de comparación, anidación de estructuras).

"""

edad = 20
altura = 1.60

if edad >= 12 and altura >= 1.60:
    print("Puede ingresar y puede subir a la montaña rusa.")
elif edad >= 12:
    print("Puede ingresar al parque, pero NO subir a la montaña rusa.")
elif edad < 12:
    print("No puede entrar al parque.")
else: # Esto no se ejecuta nunca.
    print("No se comple nada de lo anterior")

# La estructura if, consta de 3 etapas.
# IF Se puede usar 1 sola vez.
# ELIF Se puede usar todas las veces que querramos, pero siempre tenemos que volver a evaluar.
# ELSE Se puede usar 1 sola vez al final.

"""
AND
Como evaluan


True and True => True
True and False => False
False and True => False
False and False => False
Multiplicacion

1 * 1 = 1
1 * 0 = 0
0 * 1 = 0
0 * 0 = 0


OR
Como evaluan


True o True => True
True o False => True
False o True => True
False o False => False
Suma

1 + 1 = 2
1 + 0 = 1
0 + 1 = 1
0 + 0 = 0


True and True or False => True
1 * 1 + 0 = 1 Verdadero

False or True and True or False => True
0 + 1 * 1 + 0 = 1


(False or True) and (False or False) => False
(0 + 1) * (0 + 0) = 0

(False or True) and (False or False) or True => True
(0 + 1) * (0 + 0) + 1 => 1
"""
