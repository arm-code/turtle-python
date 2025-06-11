import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
width, height = 800, 600
max_iter = 256

x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)
img = np.zeros((height, width))

for i in range(height):
    for j in range(width):
        img[i, j] = mandelbrot(x[j] + 1j*y[i], max_iter)

plt.imshow(img, cmap='hot', extent=(xmin, xmax, ymin, ymax))
plt.colorbar()
plt.title("Conjunto de Mandelbrot")
plt.show()