def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def es_par(numero):
    return numero % 2 == 0

def validar_edad(edad):
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero.")
    if edad < 0 or edad > 120:
        raise ValueError("Edad fuera del rango válido (0 - 120).")
    return edad >= 18
