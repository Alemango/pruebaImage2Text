import cv2
import random
from git import Repo
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

cap = cv2.VideoCapture(0)
leido, frame = cap.read()

nombreFoto = "foto" + str(random.randint(1,1000)) + ".png"

if leido == True:
	cv2.imwrite(nombreFoto, frame)
	print("Foto tomada correctamente")
else:
	print("Error al acceder a la cámara")

cap.release()

repo = Repo(r"C:\Users\aleal\OneDrive\Documentos\Prog\pruebaImage2Text")
print(repo.git.status())
repo.git.add(r"C:\Users\aleal\OneDrive\Documentos\Prog\pruebaImage2Text\{nombreFoto}".format(nombreFoto=nombreFoto))
repo.git.commit(message="test with image")
repo.git.push()

'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = "4350aed49c264b2ba424f16a51b559af"
endpoint = "https://medicinas.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
'''
END - Authenticate
'''

'''
OCR: Read File using the Read API, extract text - remote
This example will extract text in an image, then print results, line by line.
This API call can also extract handwriting style text (not shown).
'''
print("===== Read File - remote =====")
# Get an image with text
read_image_url = "https://raw.githubusercontent.com/Alemango/pruebaImage2Text/master/{nombreFoto}".format(nombreFoto=nombreFoto)

# Call API with URL and raw response (allows you to get the operation location)
read_response = computervision_client.read(read_image_url,  raw=True)

# Get the operation location (URL with an ID at the end) from the response
read_operation_location = read_response.headers["Operation-Location"]
# Grab the ID from the URL
operation_id = read_operation_location.split("/")[-1]

# Call the "GET" API and wait for it to retrieve the results 
while True:
    read_result = computervision_client.get_read_result(operation_id)
    if read_result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

# Print the detected text, line by line
if read_result.status == OperationStatusCodes.succeeded:
    for text_result in read_result.analyze_result.read_results:
        for line in text_result.lines:
            print(line.text)
            print(line.bounding_box)
print()
'''
END - Read File - remote
'''

print("End of Computer Vision quickstart.")