import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

def Qreader():
    while True:
        _, frame = cap.read()
        listJson=[]
        read = {}
        decodedObjects = pyzbar.decode(frame)

        for obj in decodedObjects:
            lista.append(str(obj.data))


        for i in lista:
            i[1:]
        
        cv2.imshow("Frame", frame)
        print(lista)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break