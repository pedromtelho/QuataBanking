import requests
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import urllib.request
from os import system, name
from time import sleep
import json  
import requests

#Funções
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


counter = 0
counter_frame = 5
def decode(im) :
    global counter
    
    # Find barcodes and QR codes
    try:
        decodedObjects = pyzbar.decode(im)
    
        # Print results
        for obj in decodedObjects:
            #print('Type : ', obj.type)
            #print('Data : ', obj.data,'\n')
            if obj.type == "QRCODE":
                counter +=1

        return decodedObjects
    except ValueError:
        return decodedObjects

     
def check_frame(decodedObjects):
  global counter_frame
  global counter
  global Filme
  if counter_frame <= 0 and counter >= 5:
    counter = 0
    counter_frame = 0
    Filme = False
    for obj in decodedObjects:
      if obj.type == "QRCODE":
        return obj.data

  if counter_frame <= 0:
    counter_frame = 5
    counter = 0

 
 
# Display barcode and QR code location  
def display(im, decodedObjects):
 
  # Loop over all decoded objects
  for decodedObject in decodedObjects: 
    points = decodedObject.polygon
 
    # If the points do not form a quad, find convex hull
    if len(points) > 4 : 
      hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
      hull = list(map(tuple, np.squeeze(hull)))
    else : 
      hull = points;
     
    # Number of points in the convex hull
    n = len(hull)
 
    # Draw the convext hull
    for j in range(0,n):
      cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)
 
  # Display results 
  cv2.imshow("Results", im)
  
 
   
# Main 
def QR_READER():
    global counter
    global counter_frame
    global Filme
    

    Filme = True


    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    lower = 0
    upper = 1
    
    # Read image
    #im = cvframe
    

    while Filme:
        #print("Escaneie o QR code com a camera, para sair clique na janela e precione 'q'")
        counter_frame -= 1
        ret, frame = cap.read()
        decodedObjects = decode(frame)
        display(frame, decodedObjects)
        dado = str(check_frame(decodedObjects))[2:-1]
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    if Filme == False:
        return dado

def pagaBoleto():

    lista_bancos = ["banco1","banco2","banco3"]
    for banco in lista_bancos:
        url = "https://www.btgpactual.com/btgcode/api/"+banco+"/money-movement/pay"
        payload = json.loads(QR_READER)
        headers = {
        'Content-Type': "application/json",
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        if (response.json()) != "Saldo insuficiente!":
            return True
        
        else:
            return False
