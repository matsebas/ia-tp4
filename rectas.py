import matplotlib.pyplot as plt  # Para graficar
import numpy as np  # Para operaciones numéricas
from skimage import transform  # Importa funciones para leer, convertir imágenes y para la transformada

# Crea una imagen binaria con líneas
image = np.zeros((100, 100), dtype=np.uint8)  # Imagen de 100x100 píxeles
image[10, :] = 255  # Línea horizontal en y=10 (blanco)
image[:, 20] = 255  # Línea vertical en x=20
image[30, :] = 255  # Línea horizontal en y=30
image[:, 50] = 255  # Línea vertical en x=50

# Aplica la transformada de Hough
hough_result, angles, dists = transform.hough_line(image)
# hough_result: Matriz del espacio de Hough (acumulador)
# angles: Ángulos en radianes
# dists: Distancias desde el origen

# Grafica la imagen original y el espacio de Hough
fig, axes = plt.subplots(1, 2, figsize=(15, 5))  # Crea una figura con dos subplots
ax = axes.ravel()  # Aplana el arreglo de axes para acceder individualmente

ax[0].imshow(image, cmap='gray')  # Muestra la imagen original en escala de grises
ax[0].set_title('Imagen Original')
ax[0].set_axis_off()  # Oculta los ejes

# Grafica el espacio de Hough (en escala logarítmica para visualizar mejor los picos)
ax[1].imshow(np.log(1 + hough_result), extent=[np.rad2deg(angles[-1]), np.rad2deg(angles[0]), dists[-1], dists[0]],
             aspect=1, cmap='gray')
ax[1].set_title('Transformada de Hough')
ax[1].set_xlabel('Ángulo (grados)')
ax[1].set_ylabel('Distancia (pixeles)')

# Ajusta las marcas de los ejes (opcional, para mayor claridad)
ax[1].set_xticks(np.arange(-90, 90, 30))  # Marca cada 30 grados
ax[1].set_yticks(np.arange(-150, 150, 10))  # Marca cada 10 píxeles

plt.tight_layout()  # Ajusta el diseño para evitar superposiciones
plt.show()  # Muestra la figura

# Detecta picos en el espacio de Hough y dibuja las líneas
fig, ax = plt.subplots(1, 1, figsize=(10, 10))  # Crea una nueva figura
ax.imshow(image, cmap='gray')  # Muestra la imagen original

# Encuentra los picos más prominentes en el espacio de Hough
for _, angle, dist in zip(*transform.hough_line_peaks(hough_result, angles, dists)):
    y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)  # Calcula el punto inicial de la línea
    y1 = (dist - image.shape[1] * np.cos(angle)) / np.sin(angle)  # Calcula el punto final de la línea
    ax.plot((0, image.shape[1]), (y0, y1), '-r')  # Dibuja la línea en rojo

ax.set_xlim((0, image.shape[1]))  # Establece los límites del eje x
ax.set_ylim((image.shape[0], 0))  # Establece los límites del eje y (invertido para que el origen esté arriba)
ax.set_axis_off()  # Ocultar los ejes
ax.set_title('Líneas Detectadas')

plt.tight_layout()
plt.show()  # Muestra la figura
