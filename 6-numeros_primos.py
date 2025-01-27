


""""
# En este ejercicio nos pedían generar un Script de Python que imprimiese los numeros primeros entre 1 y 251
    Después nos pedían que el resultado del print se guardase en una variable llamada 'results.txt'
        Para después ejecutar el script sería python3 results.py
"""

# Script de Python 


def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def numeros_primos():
    for numero in range(1, 251):
        if es_primo(numero):
            print(numero)

numeros_primos()


# Comando para ejecutar el script y guardarlo en otra variable 


# ""python3 results.py >> results.txt""