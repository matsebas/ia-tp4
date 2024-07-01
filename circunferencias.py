import matplotlib.pyplot as plt  # Para graficar
import numpy as np  # Para operaciones numéricas
from skimage import draw, feature, transform  # Para dibujar, encontrar picos y la transformada de Hough

# Crea una imagen binaria con circunferencias
image = np.zeros((200, 200), dtype=np.uint8)  # Imagen de 200x200 píxeles
# Calcula las coordenadas (rr, cc) de los píxeles del perímetro de un círculo con centro (60, 60) y radio 40
rr, cc = draw.circle_perimeter(60, 60, 40)
image[rr, cc] = 255  # Establece los píxeles del perímetro del primer círculo en blanco (valor 255)
# Calcula las coordenadas (rr, cc) de los píxeles del perímetro de un círculo con centro (140, 140) y radio 30
rr, cc = draw.circle_perimeter(140, 140, 30)
image[rr, cc] = 255  # Establece los píxeles del perímetro del segundo círculo en blanco (valor 255)

# Aplica la transformada de Hough para circunferencias de radio entre 20 y 50 pixeles
hough_radii = np.arange(20, 50, 2)  # Crea un array con los posibles radios a considerar (de 20 a 48 en pasos de 2)
# Aplica la transformada de Hough para cada radio, generando un acumulador 3D donde cada capa corresponde a un radio
hough_res = transform.hough_circle(image, hough_radii)

# "Aplana" el acumulador 3D en uno 2D para visualizarlo
accumulator = np.zeros_like(hough_res)
for i in range(len(hough_radii)):
    accumulator[i] = hough_res[i]

# Grafica la imagen original y el acumulador de Hough
fig = plt.figure(figsize=(15, 7))  # Crea una figura para graficar
ax1 = fig.add_subplot(121)  # Subplot 1: para la imagen original
ax1.imshow(image, cmap='gray')
ax1.set_title('Imagen Original con Circunferencias')
ax1.set_axis_off()

# Subplot 2: para la representación aproximada del acumulador de Hough en 3D
ax2 = fig.add_subplot(122, projection='3d')
x, y, z = np.nonzero(
    accumulator)  # Obtiene los índices de los elementos no nulos del acumulador (representan posibles centros y radios)
ax2.scatter(x, y, z, c=accumulator[x, y, z], cmap='nipy_spectral_r',
            marker='o')  # Grafica los puntos no nulos, con colores según su valor (intensidad del voto)
ax2.set_xlabel('Centro X')
ax2.set_ylabel('Centro Y')
ax2.set_zlabel('Radio')
ax2.set_title('Representación aproximada del acumulador de la Transformada de Hough')

plt.tight_layout()  # Ajusta el diseño
plt.show()  # Muestra la figura

# Detecta los picos en el acumulador y dibujar las circunferencias
fig, ax = plt.subplots(1, 1, figsize=(10, 10))  # Crea una figura para la imagen con las circunferencias detectadas
ax.imshow(image, cmap='gray')

centers = []
radii = []
for radius, h in zip(hough_radii, hough_res):  # Itera sobre cada radio y su correspondiente capa en el acumulador
    # Encuentra los 2 picos más altos en la capa (máximo 2 círculos por radio)
    peaks = feature.peak_local_max(h, num_peaks=2)
    for peak in peaks:
        centers.append((peak[0], peak[1]))  # Almacena las coordenadas del centro del círculo
        radii.append(radius)  # Almacena el radio del círculo

# Dibujar los círculos detectados
for center_y, center_x, radius in zip(*zip(*centers), radii):
    circ = plt.Circle((center_x, center_y), radius, color='red', fill=False)  # Crea un objeto círculo
    ax.add_patch(circ)  # Agrega el círculo a la imagen

ax.set_axis_off()
ax.set_title('Circunferencias Detectadas')

plt.tight_layout()
plt.show()
