# Este archivo contiene funciones matemáticas utilizadas por la calculadora.

# Importamos las bibliotecas necesarias
import math

# Función para calcular el seno de un ángulo en grados
def calcular_seno(angulo):
    """Devuelve el seno de un ángulo dado en grados."""
    return math.sin(math.radians(angulo))

# Función para calcular el coseno de un ángulo en grados
def calcular_coseno(angulo):
    """Devuelve el coseno de un ángulo dado en grados."""
    return math.cos(math.radians(angulo))

# Función para calcular la tangente de un ángulo en grados
def calcular_tangente(angulo):
    """Devuelve la tangente de un ángulo dado en grados."""
    return math.tan(math.radians(angulo))

# Función para calcular la raíz cuadrada de un número
def calcular_raiz_cuadrada(numero):
    """Devuelve la raíz cuadrada de un número. Lanza un error si el número es negativo."""
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(numero)

# Función para calcular la potencia de una base elevada a un exponente
def calcular_potencia(base, exponente):
    """Calcula la potencia de una base elevada a un exponente."""
    return math.pow(base, exponente)

# Función para calcular el logaritmo natural de un número positivo
def calcular_logaritmo(numero):
    """Calcula el logaritmo natural de un número positivo."""
    if numero <= 0:
        raise ValueError("El logaritmo solo está definido para números positivos.")
    return math.log(numero)
