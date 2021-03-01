import cv2
import numpy as np

#Variables globales
dibujando = False
valorx = 0
valory = 0

#Definir funcion para dibujar

def dibujar(event,x,y,etiquetas,parametros):
    
    global dibujando,valorx,valory #Variables globales por que estan definidas fuera de la funcion

    if event == cv2.EVENT_LBUTTONDOWN:
        dibujando = True
        valorx = x
        valory = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if dibujando == True:
            cv2.rectangle(imagen, (valorx,valory), (x,y), (255,0,0), -1) #Crea un rectangulo desde donde se hizo click hasta donde esta el raton en la imagen
    elif event == cv2.EVENT_LBUTTONUP:
        dibujando = False
        cv2.rectangle(imagen, (valorx,valory), (x,y) (255,0,0), -1)

#Conectar funcion dibujar con la imagen

cv2.namedWindow(winname='mi_imagen')
cv2.setMouseCallback('mi_imagen', dibujar)

#Mosrtar la imagen donde vamos a dibujar

imagen = np.zeros((500,500,3), np.int8) #Creacion de imagen negra

while True: #Bucle para mantener la imagen activa
    cv2.imshow('mi_imagen',imagen) #Abre ventana con titulo 'mi_imagen' con la imagen

    if cv2.waitKey(10) & 0xFF == 27: #Si pulsa la tecla imagen cierra la aplicaccion
        break
cv2.destroyALLWindows()