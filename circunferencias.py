import matplotlib.pyplot as plt
import numpy as np
from skimage import draw, feature, transform

# Crear una imagen binaria con circunferencias
image = np.zeros((200, 200), dtype=np.uint8)
rr, cc = draw.circle_perimeter(60, 60, 40)
image[rr, cc] = 255
rr, cc = draw.circle_perimeter(140, 140, 30)
image[rr, cc] = 255

# Aplicar la transformada de Hough para circunferencias de radio entre 20 y 50 pixeles
hough_radii = np.arange(20, 50, 2)
# Acumulador de la Transformada de Hough en 2D (centro y radio)
hough_res = transform.hough_circle(image, hough_radii)

# Acumulador tridimensional
accumulator = np.zeros_like(hough_res)
for i in range(len(hough_radii)):
    accumulator[i] = hough_res[i]

# Graficar la imagen original y la transformada en la misma figura
fig = plt.figure(figsize=(15, 7))

# Imagen original con circunferencias
ax1 = fig.add_subplot(121)
ax1.imshow(image, cmap='gray')
ax1.set_title('Imagen Original con Circunferencias')
ax1.set_axis_off()

# Acumulador de la Transformada de Hough en 3D
ax2 = fig.add_subplot(122, projection='3d')
x, y, z = np.nonzero(accumulator)
ax2.scatter(x, y, z, c=accumulator[x, y, z], cmap='nipy_spectral_r', marker='o')
ax2.set_xlabel('Centro X')
ax2.set_ylabel('Centro Y')
ax2.set_zlabel('Radio')
ax2.set_title('Representación aproximada del acumulador de la Transformada de Hough')

plt.tight_layout()
plt.show()

# Dibujar las circunferencias detectadas en la imagen original
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.imshow(image, cmap='gray')

# Detectar los picos en el acumulador
centers = []
radii = []
for radius, h in zip(hough_radii, hough_res):
    peaks = feature.peak_local_max(h, num_peaks=2)
    for peak in peaks:
        centers.append((peak[0], peak[1]))
        radii.append(radius)

# Dibujar los círculos detectados
for center_y, center_x, radius in zip(*zip(*centers), radii):
    circ = plt.Circle((center_x, center_y), radius, color='red', fill=False)
    ax.add_patch(circ)

ax.set_axis_off()
ax.set_title('Circunferencias Detectadas')

plt.tight_layout()
plt.show()
