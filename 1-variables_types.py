"""
--------------------------- VARIABLES / TIPOS DE DATOS ---------------------------
En este taller aprenderás cómo crear variables, trabajar con diferentes tipos de datos.
"""

"""
--- Ejercicio 1 Variables---
Crea una variable llamada "mensaje". 
Asígnale el valor "¡Hola, Mundo!". 
Imprime el valor de la variable en la consola.
"""
mensaje = "¡Hola, Mundo!"
print(mensaje)

"""
--- Ejercicio 2 Variables---
Invoca la variable anterior llamada "mensaje". 
Reasígnale el valor "Hello world!". 
Imprime el valor de la variable en la consola.
Escribe en un comentario de línea lo que sucede.
"""
mensaje = "Hello world!"
print(mensaje) # Se imprime el nuevo valor de la variable mensaje

"""
--- Ejercicio 3 Tipos de datos---
Crea variables para cada uno de los siguientes tipos de datos y colecciones: string, int, float, 
bool, list, tuple, dicctionary and set. 
Imprime cada variable y el tipo de dato o colección que almacena en la consola.
"""
string = "Este es un string"
print("La variable", string, "pertenece a", type(string))

int = 10
print("La variable", int, "pertenece a", type(int))

float = 10.5
print("La variable", float, "pertenece a", type(float))

bool = True
print("La variable", bool, "pertenece a", type(bool))

list = [1, 2, 3, 4]
print("La variable", list, "pertenece a", type(list))

tuple = (1, 2, 3, 4)
print("La variable", tuple, "pertenece a", type(tuple))

dicctionary = {"nombre": "Juan", "apellido": "Perez"}
print("La variable", dicctionary, "pertenece a", type(dicctionary))

set = {1, 2, 3, 4}
print("La variable", set, "pertenece a", type(set))
