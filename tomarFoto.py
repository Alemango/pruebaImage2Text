import cv2
import random

cap = cv2.VideoCapture(0)
leido, frame = cap.read()

nombreFoto = "foto" + str(random.randint(1,1000)) + ".png"

if leido == True:
	cv2.imwrite(nombreFoto, frame)
	print("Foto tomada correctamente")
else:
	print("Error al acceder a la cámara")

cap.release()