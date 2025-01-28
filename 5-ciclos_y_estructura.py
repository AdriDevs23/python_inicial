
"""
--------------------------- CICLOS Y ESTRUCTURAS DE CONTROL ---------------------------
En este taller aprenderás usar los métodos más típicos para dirigir el flujo de ejecuón y la lógica de un algoritmo
"""


"""
--- Ejercicio 1 condicionales  ---
Escribe un programa que pida al usuario una letra y luego imprima un mensaje indicando si es una vocal o una consonante.
"""

def identificar_letra():
    letra = input("Introduce una letra y te diré si es vocal o consonante: ").lower()
    
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, introduce una única letra.")
        return
    
    if letra in "aeiou":
        print(f"La letra {letra.upper()} es una vocal.")
    else:
        print(f"La letra {letra.upper()} es una consonante")
identificar_letra()


"""
--- Ejercicio 2  condicionales anidados  ---
Escribe un programa que pida al usuario una nota (entre 0 y 100) y determine si
es una calificación de "A", "B", "C", "D" o "F".
"""
def identificador_nota():
    nota = int(input("Introduce un numero y te diré tu calificación: "))
    
    if nota < 0 or nota > 100:
        print("No es un valor posible, pro favor introduce un valor numérico entre 0 y 100")
        return
    
    if 90 <= nota <= 100:
        print(f"Tu nota {nota} entra dentro de la calificación A. ¡Enhorabuena! Eres de los primeros de la clase.")
    elif 80 <= nota <= 89:
        print(f"Tu nota {nota} entra dentro de la calificación B. Un pasito más para la excelencia.")
    elif 70 <= nota <= 79:
        print(f"Tu nota {nota} entra dentro de la calificación C. Aprobado, pero esperaba más de ti.")
    elif 60 <= nota <= 69:
        print(f"Tu nota {nota} entra dentro de la calificación D. Necesitas mejorar.")
    else:
        print(f"Tu nota {nota} entra dentro de la calificación F. Necesitas mejorar... ¡aún más!")

identificador_nota()


"""
--- Ejercicio 3  bucle while  ---
Escribe un programa que pida al usuario un número entero positivo y
luego imprima la cuenta regresiva desde ese número hasta 1.
"""
def cuenta_atras():
    numero = int(input("Introduce un número que sea positivo"))
    
    if numero <= 0:
        print("Por favor, introduce un número positivo")
        return

    while numero >= 1:
        print(f"El contador actualmente está en {numero}")
        numero -= 1
    print("Cuenta atrás finalizada")   

cuenta_atras()


"""
--- Ejercicio 4  bucle for  ---
Escribe un programa que imprima todos los caracteres de una cadena de texto ingresada por el usuario.
"""
# Escribe tu código aquí


"""
--- Ejercicio 5  bucle for con range ---
Escribe un programa que imprima la tabla de multiplicar del 5 (del 1 al 10).
"""
# Escribe tu código aquí


"""
--- Ejercicio 6  bucle for con listas ---
Escribe un programa que pida al usuario 5 palabras, las guarde en una lista y
luego en una nueva lista guarde todas las palabras en mayúsculas.
"""
# Escribe tu código aquí


"""
--- Ejercicio 7  break and continue ---
Escribe un programa que le pida al usuario una mascota y
si es un perro, que imprima en la consola "Tengo un perro",
si es un gato, que imprima en la consola "Tengo un gato",
si es un pájaro, que imprima en la consola "Tengo un pájaro" y
si no es ninguno de los 3 que imprima "No tengo una mascota convencional"
"""
# Escribe tu código aquí


