import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Arath Valenzuela NC:0148 (10/11/26)
print("Arath Valenzuela")
print("UIII Act3 colocar puntos a una imagen en blanco y negro con VA")
Mi_imagen = cv2.imread('TBP.jpg')
plt.imshow(Mi_imagen)
plt.title('The Black Parade (Aarth Valenzuela NC:0148)')
plt.show()
print("--------+ Puntos en la imagen +--------")
plt.imshow(Mi_imagen)
x = [100,100,300,340]
y = [100,400,500,300]
plt.scatter(x, y, s=20,c='red')
plt.show()