# Este archivo contiene la lógica principal para las operaciones básicas y avanzadas de la calculadora.

# Importamos las bibliotecas necesarias
import tkinter as tk
from tkinter import messagebox
from operaciones import calcular_seno, calcular_coseno, calcular_tangente, calcular_raiz_cuadrada, calcular_potencia, calcular_logaritmo

# Función para realizar cálculos según la operación seleccionada
def calcular(opcion, entrada1, entrada2, resultado_label):
    """
    Realiza el cálculo basado en la operación seleccionada y actualiza el resultado en la interfaz.
    Parámetros:
    - opcion: Operación seleccionada por el usuario.
    - entrada1: Primer valor ingresado por el usuario.
    - entrada2: Segundo valor ingresado por el usuario (si aplica).
    - resultado_label: Etiqueta donde se mostrará el resultado.
    """
    try:
        if opcion == "Suma":
            num1 = float(entrada1.get())
            num2 = float(entrada2.get())
            resultado = num1 + num2
        elif opcion == "Resta":
            num1 = float(entrada1.get())
            num2 = float(entrada2.get())
            resultado = num1 - num2
        elif opcion == "Multiplicación":
            num1 = float(entrada1.get())
            num2 = float(entrada2.get())
            resultado = num1 * num2
        elif opcion == "División":
            num1 = float(entrada1.get())
            num2 = float(entrada2.get())
            if num2 == 0:
                raise ValueError("No se puede dividir entre cero.")
            resultado = num1 / num2
        elif opcion == "Seno":
            angulo = float(entrada1.get())
            resultado = calcular_seno(angulo)
        elif opcion == "Coseno":
            angulo = float(entrada1.get())
            resultado = calcular_coseno(angulo)
        elif opcion == "Tangente":
            angulo = float(entrada1.get())
            resultado = calcular_tangente(angulo)
        elif opcion == "Raíz Cuadrada":
            numero = float(entrada1.get())
            resultado = calcular_raiz_cuadrada(numero)
        elif opcion == "Potencia":
            base = float(entrada1.get())
            exponente = float(entrada2.get())
            resultado = calcular_potencia(base, exponente)
        elif opcion == "Logaritmo":
            numero = float(entrada1.get())
            resultado = calcular_logaritmo(numero)
        else:
            resultado = "Operación no válida"

        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")

# Función para crear la interfaz gráfica de la calculadora
def crear_interfaz():
    """
    Crea la interfaz gráfica de la calculadora utilizando Tkinter.
    """
    ventana = tk.Tk()
    ventana.title("Calculadora Científica y Básica")

    tk.Label(ventana, text="Seleccione una operación:").pack()

    # Separar las operaciones en Básicas y Avanzadas
    opciones_basicas = ["Suma", "Resta", "Multiplicación", "División"]
    opciones_avanzadas = ["Seno", "Coseno", "Tangente", "Raíz Cuadrada", "Potencia", "Logaritmo"]

    # Crear un menú desplegable para las operaciones
    opcion_var = tk.StringVar(value="Operaciones")
    menu_operaciones = tk.OptionMenu(ventana, opcion_var, *opciones_basicas, *opciones_avanzadas)
    menu_operaciones.pack()

    tk.Label(ventana, text="Entrada 1:").pack()
    entrada1 = tk.Entry(ventana)
    entrada1.pack()

    tk.Label(ventana, text="Entrada 2 (si aplica):").pack()
    entrada2 = tk.Entry(ventana)
    entrada2.pack()

    resultado_label = tk.Label(ventana, text="Resultado: ")
    resultado_label.pack()

    tk.Button(ventana, text="Calcular", command=lambda: calcular(opcion_var.get(), entrada1, entrada2, resultado_label)).pack()
    tk.Button(ventana, text="Salir", command=ventana.quit).pack()

    ventana.mainloop()

# Punto de entrada principal del programa
if __name__ == "__main__":
    crear_interfaz()
