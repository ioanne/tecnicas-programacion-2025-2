"""
Problema 1:
    Necesitamos organizar información sencilla dentro de un programa. Para ello, vamos a
    declarar distintas variables que representen datos de la vida cotidiana: un nombre, una
    edad, una altura, si una persona es estudiante o no, y una lista de materias que cursa. El
    objetivo es aprender a crear variables y entender qué tipo de dato representa cada una.
    ● Investigar qué son las variables en Python y cuáles son los tipos de datos básicos
    más comunes (str, int, float, bool, list).
    ● Documentar todo el proceso de resolución.
    ● Si se utilizó una IA como apoyo, se debe guardar y mostrar la conversación
    completa.
    ● Explicar qué debates o decisiones se tomaron para resolver el problema.
    ● Documentar el paso a paso seguido para construir la solución.
    ● Explicar qué hace cada línea del código y justificar por qué se escribió de esa forma.
    ● Explicar con ejemplos qué significa cada tipo de dato y por qué es útil.
"""
# Declaramos una variable de tipo string
alumno = "Juan" # Se declara una variable de tipo texto
edad = 20 # Se declara una variable de tipo entero
altura = 175.5
es_estudiante = True
materias = ["Matematica", "Fisica"]

# ¿Que son las variables en python?
# Un lugar donde podemos almacenar datos
# Es una posicion en la memyoria RAM de la PC donde se encuentra lo que almacenamos.
# Es una etiqueta que contiene el dato con el que nosotros trabajamos
# Para declararla, hay que asignarle un valor.
# Si no uso = no declaro una variable.
variable: str # Esto no es declarar una variable.

# Para documentar, podemos armar un doc hecho por chatgpt para obtener toda la informacion
# respecto a las variables.

""" Prompt:
Documentar todo el proceso de resolución.

Hacemos un prompt
Hablame acerca de las variables en pyhon

En Python, una variable es un nombre que se utiliza para guardar un valor en memoria.
Funciona como una "etiqueta" que apunta a un objeto (dato) que el programa puede usar y manipular.

Características principales de las variables en Python
    No es necesario declararlas antes de usarlas
    Basta con asignarles un valor y Python crea la variable dinámicamente.
    x = 10
    nombre = "Juan"
    activo = True


    Tipado dinámico (La variable no es dinamica)
    El tipo de dato se asigna automáticamente según el valor. Una misma variable puede cambiar de tipo:

    dato = 42        # entero
    dato = "texto"   # ahora es cadena

    Case-sensitive
    Python distingue entre mayúsculas y minúsculas:

    mi_dato = 10 Se usa de esta manera en python (snake case)

    MiDato = 20 Upper CamelCase

    No necesitan tipo explícito
    A diferencia de otros lenguajes (Java, C++), no se escribe int, string, etc. al declarar.
    Reglas para nombres de variables
    Pueden contener letras, números y guiones bajos (_), pero no pueden empezar con un número.
    No se permiten espacios ni símbolos como @, -, $.
    No deben coincidir con palabras reservadas de Python (ej.: for, if, class, etc.).

    Ejemplos válidos:
    .....


    Ejemplos inválidos:
    .....

    Tipos de datos comunes que se almacenan en variables
        int → enteros (10, -5)
        float → decimales (3.14, -0.1)
        str → cadenas de texto ("hola", 'Python')
        bool → valores lógicos (True, False)
        list → listas ([1, 2, 3])
        tuple → tuplas ((1, 2, 3))
        dict → diccionarios ({"clave": "valor"})

        https://chatgpt.com/share/68bf4a2a-b6d0-8013-b5ee-1bdb05dcaa1b
"""