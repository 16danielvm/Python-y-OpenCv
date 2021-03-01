import cv2

captura = cv2.VideoCapture(0) #Hace captura

ancho = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH)) 
altura = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT))

#MAC

# codigo = cv2.VideoWriter_Fourcc(*'MJPG')
# grabador = cv2.VideoWriter('video.avi',codigo, 20, (ancho,altura))

#WINDOWS

codigo = cv2.VideoWriter_fourcc(*'DIVX') #El formato en que va a grabar
grabador = cv2.VideoWriter('video.mp4',codigo, 20, (ancho,altura)) #Creara un video.mp4


while True:
    
    resultado, video = captura.read()  #Leer capturas de pantalla continuamente y grabarlas en la variable video
    #GRABAR
    grabador.write(video) #Grabando cada uno de los fotogramas
    cv2.imshow('Nuestro Video', video) #Muestra una ventana con el video, llamada "Nuestro video"

    if cv2.waitKey(10) & 0xFF == ord('q'): #Condicion para salir del bucle, sale despues de 10 segundos o con la letra q
        break

captura.release() 
grabador.release()
cv2.destroyAllWindows() #Cierra Todo