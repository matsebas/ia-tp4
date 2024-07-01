import matplotlib.pyplot as plt
import numpy as np
from skimage import transform

# Crear una imagen binaria con líneas
image = np.zeros((100, 100), dtype=np.uint8)
image[10, :] = 255  # Línea horizontal en y=10
image[:, 20] = 255  # Línea vertical en x=20
image[30, :] = 255  # Línea horizontal en y=30
image[:, 50] = 255  # Línea vertical en x=50

# Aplicar la transformada de Hesse-Hough
hough_result, angles, dists = transform.hough_line(image)

# Graficar la imagen original y la imagen de bordes
fig, axes = plt.subplots(1, 2, figsize=(15, 5))
ax = axes.ravel()

ax[0].imshow(image, cmap='gray')
ax[0].set_title('Imagen Original')
ax[0].set_axis_off()

# Graficar el resultado de la transformada de Hough
ax[1].imshow(np.log(1 + hough_result), extent=[np.rad2deg(angles[-1]), np.rad2deg(angles[0]), dists[-1], dists[0]],
             aspect=1, cmap='gray')
ax[1].set_title('Transformada de Hough')
ax[1].set_xlabel('Ángulo (grados)')
ax[1].set_ylabel('Distancia (pixeles)')

ax[1].set_xticks(np.arange(-90, 90, 30))  # Marcas cada 10 grados
ax[1].set_yticks(np.arange(-150, 150, 10))  # Marcas cada 10 píxeles

plt.tight_layout()
plt.show()

# Dibujar las líneas detectadas en la imagen original
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.imshow(image, cmap='gray')

for _, angle, dist in zip(*transform.hough_line_peaks(hough_result, angles, dists)):
    y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
    y1 = (dist - image.shape[1] * np.cos(angle)) / np.sin(angle)
    ax.plot((0, image.shape[1]), (y0, y1), '-r')

ax.set_xlim((0, image.shape[1]))
ax.set_ylim((image.shape[0], 0))
ax.set_axis_off()
ax.set_title('Líneas Detectadas')

plt.tight_layout()
plt.show()
