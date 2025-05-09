# Proyecto Calculadora Científica

## Descripción
Este proyecto es una calculadora científica interactiva desarrollada con Python y Flask. Permite realizar operaciones básicas como suma, resta, multiplicación y división, así como operaciones avanzadas como seno, coseno, tangente, raíz cuadrada, potencia y logaritmo.

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/palmaant/portafolio-full_stack-jr
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd proyecto1-calculadora_c
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
1. Inicia el servidor:
   ```bash
   python api.py
   ```
2. Abre tu navegador y ve a `http://127.0.0.1:5000`.

## Estructura del Proyecto
```
proyecto1-calculadora_c/
├── api.py                # Contiene las rutas principales de la aplicación.
├── calculadora.py        # Lógica para operaciones básicas.
├── calculadora_cientifica.py # Lógica para operaciones avanzadas.
├── operaciones.py        # Funciones matemáticas.
├── requirements.txt      # Dependencias del proyecto.
├── static/               # Archivos estáticos (CSS, imágenes, etc.).
│   ├── favicon.ico
│   └── styles.css
├── templates/            # Plantillas HTML para la interfaz.
│   ├── index.html
│   ├── suma.html
│   ├── resta.html
│   ├── multiplicacion.html
│   ├── division.html
│   ├── seno.html
│   ├── coseno.html
│   ├── tangente.html
│   ├── raiz.html
│   ├── potencia.html
│   └── logaritmo.html
└── utils/                # Módulos utilitarios.
    ├── __init__.py
    └── operaciones.py
```

## Funcionalidades
### Operaciones Básicas
- Suma
- Resta
- Multiplicación
- División

### Operaciones Avanzadas
- Seno
- Coseno
- Tangente
- Raíz Cuadrada
- Potencia
- Logaritmo

## Requisitos
- Python 3.8 o superior
- Flask

## Licencia
Este proyecto está bajo la Licencia MIT.
