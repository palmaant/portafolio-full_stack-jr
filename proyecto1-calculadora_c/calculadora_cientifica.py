# Este archivo contiene la lógica para las operaciones avanzadas de la calculadora científica.

# Importamos las bibliotecas necesarias
import math

# Función para mostrar el menú de opciones de la calculadora
def mostrar_menu():
    """Muestra el menú de opciones disponibles en la calculadora científica."""
    print("\nCalculadora Científica")
    print("1. Seno")
    print("2. Coseno")
    print("3. Tangente")
    print("4. Raíz Cuadrada")
    print("5. Potencia")
    print("6. Logaritmo")
    print("7. Salir")

# Función para calcular el seno de un ángulo en grados
def calcular_seno():
    """Solicita un ángulo en grados y muestra su seno."""
    try:
        angulo = float(input("Ingrese el ángulo en grados: "))
        resultado = math.sin(math.radians(angulo))
        print(f"El seno de {angulo}° es {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

# Función para calcular el coseno de un ángulo en grados
def calcular_coseno():
    """Solicita un ángulo en grados y muestra su coseno."""
    try:
        angulo = float(input("Ingrese el ángulo en grados: "))
        resultado = math.cos(math.radians(angulo))
        print(f"El coseno de {angulo}° es {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

# Función para calcular la tangente de un ángulo en grados
def calcular_tangente():
    """Solicita un ángulo en grados y muestra su tangente."""
    try:
        angulo = float(input("Ingrese el ángulo en grados: "))
        resultado = math.tan(math.radians(angulo))
        print(f"La tangente de {angulo}° es {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

# Función para calcular la raíz cuadrada de un número
def calcular_raiz_cuadrada():
    """Solicita un número y muestra su raíz cuadrada. Maneja errores si el número es negativo."""
    try:
        numero = float(input("Ingrese el número: "))
        if numero < 0:
            print("No se puede calcular la raíz cuadrada de un número negativo.")
        else:
            resultado = math.sqrt(numero)
            print(f"La raíz cuadrada de {numero} es {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

# Función para calcular la potencia de un número
def calcular_potencia():
    """Solicita una base y un exponente, y muestra el resultado de elevar la base al exponente."""
    try:
        base = float(input("Ingrese la base: "))
        exponente = float(input("Ingrese el exponente: "))
        resultado = math.pow(base, exponente)
        print(f"{base} elevado a la {exponente} es {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

# Función para calcular el logaritmo natural de un número
def calcular_logaritmo():
    """Solicita un número y muestra su logaritmo natural. Maneja errores si el número es no positivo."""
    try:
        numero = float(input("Ingrese el número: "))
        if numero <= 0:
            print("El logaritmo solo está definido para números positivos.")
        else:
            resultado = math.log(numero)
            print(f"El logaritmo natural de {numero} es {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

# Función para manejar el menú de la calculadora
def menu_calculadora():
    """Muestra el menú de la calculadora y ejecuta la opción seleccionada por el usuario."""
    while True:
        print("\n--- Menú Calculadora Científica ---")
        print("1. Seno")
        print("2. Coseno")
        print("3. Tangente")
        print("4. Raíz Cuadrada")
        print("5. Potencia")
        print("6. Logaritmo")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            calcular_seno()
        elif opcion == "2":
            calcular_coseno()
        elif opcion == "3":
            calcular_tangente()
        elif opcion == "4":
            calcular_raiz_cuadrada()
        elif opcion == "5":
            calcular_potencia()
        elif opcion == "6":
            calcular_logaritmo()
        elif opcion == "7":
            print("Saliendo de la calculadora científica. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Función principal de la calculadora científica
def calculadora_cientifica():
    """Inicia la calculadora científica mostrando la bienvenida y el menú."""
    print("\nBienvenido a la Calculadora Científica")
    menu_calculadora()

# Punto de entrada del programa
if __name__ == "__main__":
    calculadora_cientifica()
