# Este archivo contiene la configuración principal de la aplicación Flask y las rutas para las operaciones de la calculadora.

# Importamos las bibliotecas necesarias
from flask import Flask, request, jsonify, render_template
import logging
from waitress import serve
from utils.operaciones import calcular_seno, calcular_coseno, calcular_tangente, calcular_raiz_cuadrada, calcular_potencia, calcular_logaritmo

# Configuración del sistema de logging para registrar información de las solicitudes y respuestas
logging.basicConfig(level=logging.INFO)

# Creamos la instancia de la aplicación Flask
app = Flask(__name__, static_folder='static', template_folder='templates')

# Middleware para registrar información de cada solicitud antes de procesarla
@app.before_request
def log_request_info():
    logging.info(f"Request: {request.method} {request.url}")
    logging.info(f"Headers: {request.headers}")
    if request.method in ['POST', 'PUT', 'PATCH']:
        logging.info(f"Request Content-Type: {request.content_type}")
        logging.info(f"Request Body: {request.get_data(as_text=True)}")

# Middleware para registrar información de cada respuesta después de procesarla
@app.after_request
def log_response_info(response):
    logging.info(f"Response status: {response.status_code}")
    return response

# Ruta principal que renderiza la página de inicio
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para realizar la suma de dos números
@app.route('/api/suma', methods=['POST'])
def suma():
    # Obtenemos los datos enviados en formato JSON
    data = request.get_json()
    # Realizamos la operación de suma
    resultado = data['num1'] + data['num2']
    # Devolvemos el resultado en formato JSON
    return jsonify({'resultado': resultado}), 200

# Ruta para realizar la resta de dos números
@app.route('/api/resta', methods=['POST'])
def resta():
    data = request.get_json()
    resultado = data['num1'] - data['num2']
    return jsonify({'resultado': resultado}), 200

# Ruta para realizar la multiplicación de dos números
@app.route('/api/multiplicacion', methods=['POST'])
def multiplicacion():
    data = request.get_json()
    resultado = data['num1'] * data['num2']
    return jsonify({'resultado': resultado}), 200

# Ruta para realizar la división de dos números
@app.route('/api/division', methods=['POST'])
def division():
    data = request.get_json()
    # Validamos que el divisor no sea cero
    if data['num2'] == 0:
        return jsonify({'error': 'No se puede dividir entre cero'}), 400
    resultado = data['num1'] / data['num2']
    return jsonify({'resultado': resultado}), 200

# Ruta para calcular el seno de un ángulo
@app.route('/api/seno', methods=['POST'])
def seno():
    """Calcula el seno de un ángulo proporcionado en grados."""
    try:
        data = request.get_json()
        angulo = data.get('num1')
        if angulo is None:
            raise ValueError("Falta el parámetro 'num1' para el cálculo del seno.")
        resultado = calcular_seno(angulo)
        return jsonify({'resultado': resultado}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Ruta para calcular el coseno de un ángulo
@app.route('/api/coseno', methods=['POST'])
def coseno():
    """Calcula el coseno de un ángulo proporcionado en grados."""
    try:
        data = request.get_json()
        angulo = data.get('num1')
        if angulo is None:
            raise ValueError("Falta el parámetro 'num1' para el cálculo del coseno.")
        resultado = calcular_coseno(angulo)
        return jsonify({'resultado': resultado}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Ruta para calcular la tangente de un ángulo
@app.route('/api/tangente', methods=['POST'])
def tangente():
    """Calcula la tangente de un ángulo proporcionado en grados."""
    try:
        data = request.get_json()
        angulo = data.get('num1')
        if angulo is None:
            raise ValueError("Falta el parámetro 'num1' para el cálculo de la tangente.")
        resultado = calcular_tangente(angulo)
        return jsonify({'resultado': resultado}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Ruta para calcular la raíz cuadrada de un número
@app.route('/api/raiz', methods=['POST'])
def raiz():
    """Calcula la raíz cuadrada de un número proporcionado."""
    try:
        data = request.get_json()
        numero = data.get('num1')
        if numero is None:
            raise ValueError("Falta el parámetro 'num1' para el cálculo de la raíz cuadrada.")
        resultado = calcular_raiz_cuadrada(numero)
        return jsonify({'resultado': resultado}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Ruta para calcular la potencia de una base elevada a un exponente
@app.route('/api/potencia', methods=['POST'])
def potencia():
    """Calcula la potencia de una base elevada a un exponente."""
    try:
        data = request.get_json()
        base = data.get('num1')
        exponente = data.get('num2')
        if base is None or exponente is None:
            raise ValueError("Faltan los parámetros 'num1' y/o 'num2' para el cálculo de la potencia.")
        resultado = calcular_potencia(base, exponente)
        return jsonify({'resultado': resultado}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Ruta para calcular el logaritmo natural de un número
@app.route('/api/logaritmo', methods=['POST'])
def logaritmo():
    """Calcula el logaritmo natural de un número proporcionado."""
    try:
        data = request.get_json()
        numero = data.get('num1')
        if numero is None:
            raise ValueError("Falta el parámetro 'num1' para el cálculo del logaritmo.")
        resultado = calcular_logaritmo(numero)
        return jsonify({'resultado': resultado}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Ruta para renderizar la página del cálculo del seno
@app.route('/seno')
def seno_page():
    return render_template('seno.html')

# Ruta para renderizar la página del cálculo del coseno
@app.route('/coseno')
def coseno_page():
    return render_template('coseno.html')

# Ruta para renderizar la página del cálculo de la tangente
@app.route('/tangente')
def tangente_page():
    return render_template('tangente.html')

# Ruta para renderizar la página del cálculo de la raíz cuadrada
@app.route('/raiz')
def raiz_page():
    return render_template('raiz.html')

# Ruta para renderizar la página del cálculo de la potencia
@app.route('/potencia')
def potencia_page():
    return render_template('potencia.html')

# Ruta para renderizar la página del cálculo del logaritmo
@app.route('/logaritmo')
def logaritmo_page():
    return render_template('logaritmo.html')

# Ruta para calcular el seno desde el formulario
@app.route('/calcular_seno', methods=['POST'])
def calcular_seno_route():
    try:
        angulo = float(request.form.get('valor'))
        resultado = calcular_seno(angulo)
        return render_template('seno.html', resultado=resultado)
    except Exception as e:
        return render_template('seno.html', error=str(e))

# Ruta para calcular el coseno desde el formulario
@app.route('/calcular_coseno', methods=['POST'])
def calcular_coseno_route():
    try:
        angulo = float(request.form.get('valor'))
        resultado = calcular_coseno(angulo)
        return render_template('coseno.html', resultado=resultado)
    except Exception as e:
        return render_template('coseno.html', error=str(e))

# Ruta para calcular la tangente desde el formulario
@app.route('/calcular_tangente', methods=['POST'])
def calcular_tangente_route():
    try:
        angulo = float(request.form.get('valor'))
        resultado = calcular_tangente(angulo)
        return render_template('tangente.html', resultado=resultado)
    except Exception as e:
        return render_template('tangente.html', error=str(e))

# Ruta para calcular la raíz cuadrada desde el formulario
@app.route('/calcular_raiz', methods=['POST'])
def calcular_raiz_route():
    try:
        numero = float(request.form.get('valor'))
        resultado = calcular_raiz_cuadrada(numero)
        return render_template('raiz.html', resultado=resultado)
    except Exception as e:
        return render_template('raiz.html', error=str(e))

# Ruta para calcular la potencia desde el formulario
@app.route('/calcular_potencia', methods=['POST'])
def calcular_potencia_route():
    try:
        base = float(request.form.get('base'))
        exponente = float(request.form.get('exponente'))
        resultado = calcular_potencia(base, exponente)
        return render_template('potencia.html', resultado=resultado)
    except Exception as e:
        return render_template('potencia.html', error=str(e))

# Ruta para calcular el logaritmo desde el formulario
@app.route('/calcular_logaritmo', methods=['POST'])
def calcular_logaritmo_route():
    try:
        numero = float(request.form.get('valor'))
        resultado = calcular_logaritmo(numero)
        return render_template('logaritmo.html', resultado=resultado)
    except Exception as e:
        return render_template('logaritmo.html', error=str(e))

# Ruta para renderizar la página del cálculo de la suma
@app.route('/suma')
def suma_page():
    return render_template('suma.html')

# Ruta para renderizar la página del cálculo de la resta
@app.route('/resta')
def resta_page():
    return render_template('resta.html')

# Ruta para renderizar la página del cálculo de la multiplicación
@app.route('/multiplicacion')
def multiplicacion_page():
    return render_template('multiplicacion.html')

# Ruta para renderizar la página del cálculo de la división
@app.route('/division')
def division_page():
    return render_template('division.html')

# Ruta para calcular la suma desde el formulario
@app.route('/calcular_suma', methods=['POST'])
def calcular_suma():
    try:
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        resultado = num1 + num2
        return render_template('suma.html', resultado=resultado)
    except Exception as e:
        return render_template('suma.html', error=str(e))

# Ruta para calcular la resta desde el formulario
@app.route('/calcular_resta', methods=['POST'])
def calcular_resta():
    try:
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        resultado = num1 - num2
        return render_template('resta.html', resultado=resultado)
    except Exception as e:
        return render_template('resta.html', error=str(e))

# Ruta para calcular la multiplicación desde el formulario
@app.route('/calcular_multiplicacion', methods=['POST'])
def calcular_multiplicacion():
    try:
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        resultado = num1 * num2
        return render_template('multiplicacion.html', resultado=resultado)
    except Exception as e:
        return render_template('multiplicacion.html', error=str(e))

# Ruta para calcular la división desde el formulario
@app.route('/calcular_division', methods=['POST'])
def calcular_division():
    try:
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        if num2 == 0:
            raise ValueError("No se puede dividir entre cero.")
        resultado = num1 / num2
        return render_template('division.html', resultado=resultado)
    except Exception as e:
        return render_template('division.html', error=str(e))

# Punto de entrada de la aplicación
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
