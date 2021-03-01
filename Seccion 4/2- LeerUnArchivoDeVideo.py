import cv2

captura = cv2.VideoCapture('video.mp4') #Capturan el video

if captura.isOpened() == False: #Veirifca que el video se abrio correctamente
    print('Error al abrir el fichero de video')

while captura.isOpened(): #Bucle para mostrar el video

    resultado, video = captura.read()

    if resultado == True:

        cv2.imshow('Mivideo', video)

        if cv2.waitKey(1) & 0xFF == ord('q'): #Boton para salir
            break
    else:
        break

captura.release()
cv2.destroyAllWindows()