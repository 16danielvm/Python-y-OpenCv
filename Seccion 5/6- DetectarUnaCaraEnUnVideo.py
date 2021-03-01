import numpy as np
import matplotlib.pyplot as plt
import cv2

cascada_cara = cv2.CascadeClassifier('D:/Universidad/Vision por Computador/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml')

def detectar_cara(imagen):
    imagen1 = imagen.copy()
    rectangulos = cascada_cara.detectMultiScale(imagen1) #Detecta mediante donde esta la cara y la devuelve en la variable rectangulos
    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen1,(x,y),(x+w,y+h),(255,0,0),10)
    return imagen1

captura = cv2.VideoCapture(0)

while True:
    res,video = captura.read(0)
    video = detectar_cara(video)
    cv2.imshow('Deteccion Cara',video)
    tecla = cv2.waitKey(1)
    if tecla == 27:
        break

captura.release()
cv2.destroyAllWindows()

