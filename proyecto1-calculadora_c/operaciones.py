# Este archivo contiene funciones auxiliares para realizar operaciones matemáticas.

# Importamos las bibliotecas necesarias
import math

# Función para calcular el seno de un ángulo
def calcular_seno(angulo):
    """Devuelve el seno de un ángulo dado en grados."""
    return math.sin(math.radians(angulo))

# Función para calcular el coseno de un ángulo
def calcular_coseno(angulo):
    """Devuelve el coseno de un ángulo dado en grados."""
    return math.cos(math.radians(angulo))

# Función para calcular la tangente de un ángulo
def calcular_tangente(angulo):
    """Devuelve la tangente de un ángulo dado en grados."""
    return math.tan(math.radians(angulo))

# Función para calcular la raíz cuadrada de un número
def calcular_raiz_cuadrada(numero):
    """Devuelve la raíz cuadrada de un número. Lanza una excepción si el número es negativo."""
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(numero)

# Función para calcular la potencia de un número
def calcular_potencia(base, exponente):
    """Devuelve la base elevada al exponente."""
    return math.pow(base, exponente)

# Función para calcular el logaritmo de un número
def calcular_logaritmo(numero):
    """Devuelve el logaritmo natural de un número. Lanza una excepción si el número es menor o igual a cero."""
    if numero <= 0:
        raise ValueError("El logaritmo solo está definido para números positivos.")
    return math.log(numero)
