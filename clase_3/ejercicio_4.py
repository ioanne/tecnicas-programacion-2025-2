"""
Problema 4:
    Queremos simular una caminata. La idea es que el programa muestre en pantalla cómo una
    persona va dando pasos, desde el paso 1 hasta el paso 10. Para lograrlo, necesitamos que
    el programa repita una acción varias veces sin escribir la misma instrucción muchas veces.
    ● Investigar qué es un bucle while en Python y cómo funciona.
    ● Documentar todo el proceso de resolución.
    ● Si se utilizó una IA como apoyo, se debe guardar y mostrar la conversación
    completa.
    ● Explicar qué debates o decisiones se tomaron para resolver el problema.
    ● Documentar el paso a paso seguido para construir la solución.
    ● Explicar qué hace cada línea del código y justificar por qué se escribió de esa forma.
    ● Asegurarse de explicar los conceptos básicos que aparecen en el código (variables,
    condiciones, incremento, etc.).
"""

pasos_a_dar = 10
contador_pasos = 0

while contador_pasos < pasos_a_dar:
    contador_pasos = contador_pasos + 1
    print(f"Avanzamos en {contador_pasos}.")

for paso in range(1, 11): # La variable paso es unicamente para el for.
    # paso es una variable temporal
    print(f"Avanzamos en {paso}.")
# Acá no podemos usar mas la variable paso

# Strings
"Hola!"

# F-string
f"Hola {pasos_a_dar}"