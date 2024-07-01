### Implementación de la Transformada de Hough para Identificación de Formas Geométricas

Este repositorio contiene una implementación de la transformada de Hough en Python, utilizada para identificar formas geométricas como líneas y circunferencias en imágenes, en el contexto de un caso de estudio específico.

### Autor
- Matias Sebastiao
- Email: matisebastiao@gmail.com

### Materia
- Inteligencia Artificial

### Año
- 2024

## Contenido del repositorio

### Archivos principales
1. `rectas.py`: Contiene la implementación de la transformada de Hough para la detección de líneas, incluyendo la visualización de la imagen original y el espacio de Hough, así como la detección y dibujo de las líneas.
2. `circunferencias.py`: Contiene la implementación de la transformada de Hough para la detección de circunferencias, incluyendo la visualización de la imagen original y el espacio de Hough, así como la detección y dibujo de las circunferencias.

### Ejecución
Para ejecutar los ejemplos de detección de formas geométricas utilizando la transformada de Hough, simplemente ejecute los archivos `rectas.py` y `circunferencias.py` desde la línea de comandos o desde su IDE preferido. Asegúrese de tener Python y las dependencias necesarias instaladas en su sistema.

### Dependencias
Asegúrese de tener instaladas las siguientes dependencias antes de ejecutar el código:
```bash
pip install numpy
pip install matplotlib
pip install scikit-image
```

### Cálculo de la Transformada de Hough

#### Transformada de Hough para Líneas (`rectas.py`)
El archivo `rectas.py` crea una imagen binaria con líneas y aplica la transformada de Hough para detectar estas líneas. Luego, grafica la imagen original, el espacio de Hough y las líneas detectadas sobre la imagen original.

#### Transformada de Hough para Circunferencias (`circunferencias.py`)
El archivo `circunferencias.py` crea una imagen binaria con circunferencias y aplica la transformada de Hough para detectar estas circunferencias. Luego, grafica la imagen original, el acumulador de Hough y las circunferencias detectadas sobre la imagen original.

### Resumen

Este repositorio proporciona una implementación completa de la transformada de Hough para la identificación de formas geométricas, incluyendo la detección de líneas y circunferencias en imágenes. La visualización del espacio de Hough y la detección de picos permiten una evaluación detallada de los resultados.