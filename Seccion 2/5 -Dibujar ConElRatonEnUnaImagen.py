import cv2
import numpy as np

#Definimos la funcion para dibujar con el raton

def dibujar(event, x, y, etiquetas, parametros):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen, (x,y), 50, (255,0,0), -1)
#Conectamos la imagen con la funcion dibujar

cv2.namedWindow(winname='mi_imagen')
cv2.setMouseCallback('mi_imagen',dibujar)


# Mostramos la imagen donde vamos a pintar

imagen = np.zeros((500,500,3), np.int8)

while True:
    
    cv2.imshow('mi_imagen',imagen)

    if cv2.waitKey(10) & 0xFF ==27:
        break

cv2.destroyALLWindows()