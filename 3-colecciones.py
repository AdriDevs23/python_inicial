"""
--------------------------- COLECCIONES ---------------------------
En este taller aprenderás a manipular coleccciones de datos: Listas, diccionarios, tuplas y sets.
"""
"""
    --- LISTAS ---
Las listas son ordenadas y mutables.
Pueden contener elementos duplicados.
Puedes modificar, añadir y eliminar elementos.
"""



"""
--- Ejercicio 1 Listas ---
Crea una variable "mascotas" que almacene una lista con los siguientes elementos: 'perro', 'gato', 'loro'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""
# Escribe tu código aquí
mascotas = ["perro", "gato", "loro"]

# Escribe el código para saber la cantidad de elementos que tiene la lista, imprimir por consola
print(f"La lista {mascotas} contiene {len(mascotas)} elementos.")

# Escribe el código para acceder al valor de la posición 2, imprimir por consola
print(f"La posicion numero 2 contiene al animal {mascotas[1]}")

# Escribe el código para agregar una elemento a la lista, imprimir por consola la lista
mascotas.insert(1, "pajaros")
print(f"A la lista de {mascotas} le hemos añadido un animal en la segunda posicion")

# Escribe el código para modificar un elemento de la lista, imprimir por consola la lista
mascotas[1] = "gaviota"
print(mascotas)

# Escribe el código para eliminar un elemento de la lista, imprimir por consola la lista
mascotas.remove("perro")
print(mascotas)



"""
    --- TUPLAS ---
Las tuplas son ordenadas e inmutables.
Pueden contener elementos duplicados.
No puedes modificar, añadir o eliminar elementos después de la creación.
"""

tuple = (1, 2, 3, 4)

"""
--- Ejercicio 2 Tuplas ---
Crea una variable "plantas" que almacene una tupla con los siguientes elementos: 'cactus', 'orquidea', 'rosas'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""
# Escribe tu código aquí
plantas = ("Cactus", "Orquidea", "Rosas")

# Escribe el código para saber la cantidad de elementos que tiene la tupla, imprimir por consola
print(f"La tupla {plantas} contiene {len(plantas)} elementos")

# Escribe el código para acceder al valor de la posición 2, imprimir por consola
print(f"El valor 2 de la tupla de plantas es {plantas[2]}")

# Intentar modificar una tupla

# plantas[1] = "Margaritas"
# plantas[1] = 'hoja rota'  # Descomenta esta línea para ver qué sucede
# Escribe tu análisís acá acerca de qué sucede

# Las tuplas, al ser inmutables, no es posible modificar nada sobre la misma 


"""
    --- SETS ---
Los sets son desordenados y mutables.
No pueden contener elementos duplicados.
Puedes añadir y eliminar elementos, pero no puedes modificar los elementos existentes.
"""


"""
--- Ejercicio 3 Sets ---
Crea una variable "nombres" que almacene un set con los siguientes elementos: 'María', 'Cris', 'Cris', 'Alex'
Imprime por la terminal dicha variable
Haz los pasos pedidos
"""
# Escribe el código aqui
nombres = {"Maria", "Cris", "Cris", "Alex"}

# Explica qué sucede cuándo imprimes el valor que almacena "nombres"

print(nombres) # Al estar duplicados en el Set dos veces el mismo nombre, cuando imprimimos solo nos aparece uno de los elementos.


# Escribe el código para saber la cantidad de elementos que tiene el set, imprimir por consola
print(f"El set de nombres contiene {len(nombres)} elementos")

# Escribe el código para acceder al valor de la posición 3, imprimir por consola
nombres_lista = list(nombres)

print(f"Al ser un set, tenemos que convertirlo en una lista para que nos diga que la posicion 3 es {nombres_lista[2]}")



# Escribe el código para agregar una elemento al set, imprimir por consola el set
nombres.add("Patricia")
print(nombres)

# Escribe el código para eliminar un elemento del set, imprimir por consola el set
nombres.remove("Alex")
print(nombres)

"""



--- DICCIONARIOS ---
Los diccionarios son desordenados y mutables.
Contienen pares clave-valor.
Puedes añadir, modificar y eliminar pares clave-valor.
"""


"""
--- Ejercicio 4 Diccionarios ---
Crea un diccionario llamado "ciudad" con las claves 'nombre' y 'pais' y los valores 'Barcelona' y 'España' respectivamente.
Imprime el diccionario
"""
# Escribe el código aqui para acceder y ver por consola el valor de 'nombre'

ciudad = {"Nombre": "Barcelona", "Pais": "España"}

print(ciudad["Nombre"])

# Escribe el código aqui para añadir un nuevo par clave-valor y ver por consola el valor de 'ciudad'

ciudad = {"Nombre": "Vallecas", "Pais": "Vallekas"}

print(ciudad["Pais"])

# Escribe el código aqui para modificar el valor de un par clave-valor de 'ciudad' y verlo por consola

ciudad["Nombre"] = "Madrid"

print(ciudad["Nombre"])

# Escribe el código aqui para eliminar un par clave-valor de 'ciudad' y verlo por consola

del ciudad["Pais"]

print(ciudad)