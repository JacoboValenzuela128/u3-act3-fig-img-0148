import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Arath Valenzuela NC:0148 (10/11/26)
print("Arath Valenzuela")
print("UIII Act3 colocar puntos a una imagen en blanco y negro con VA")
Mi_imagen = cv2.imread('TBP.jpg')
plt.imshow(Mi_imagen)
plt.title('The Black Parade (Arath Valenzuela NC:0148)')
plt.show()
print("--------+ Puntos en la imagen +--------")
plt.imshow(Mi_imagen)
x = [100,100,300,340]
y = [100,400,500,300]
plt.scatter(x, y, s=20,c='red')
plt.show()
print("--------+ Cuadro en la imagen +--------")
img_tpb = cv2.imread('TBP.jpg')
plt.imshow(img_tpb)
x = [330, 330, 710, 710, 330]
y = [670, 370, 370, 670, 670]
plt.plot(x, y, c='blue')
plt.show()

print("----------+ Circulo verde en la imagen +----------")
I = cv2.imread('TBP.jpg')
plt.imshow(I)
N = 30
x = np.zeros((N+1,))
y = np.zeros((N+1,))
(xc, yc) = (510, 490)
r = 75

for i in range(N+1):
    t = 2*np.pi/N*i
    x[i] = xc + r*np.cos(t)
    y[i] = yc + r*np.sin(t)

plt.plot(x, y, c='green')
plt.show()
