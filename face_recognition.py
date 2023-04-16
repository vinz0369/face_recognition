
import cv2
import numpy as np
import os
import csv
from datetime import datetime



recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#khoi tao id
id = 0

# ten gan voi id
names = ['None', 'Vinh', 'musk','ronaldo','mixi do']
students = names.copy()

#khoi tao va quay video realtime
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

#kich thuoc toi thieu de nhan dang
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
#tao file csv
now = datetime.now()
current_date = now.strftime("%d-%m-%Y")
f = open(current_date+'.csv','w+',newline = '')
lnwriter = csv.writer(f)

while True:

    ret, img =cam.read()
    # img = cv2.flip(img, -1) # Flip vertically

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
       
        #kiem tra do chinh xac cua khuon mat
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        if id in students:
            students.remove(id)
            print(students)
            current_time = now.strftime("%H:%M:%S")
            lnwriter.writerow([id,current_time])
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        
        
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # ESC de thoat
    if k == 27:
        break

#end
print("\n Thoat chuong trinh")
cam.release()
cv2.destroyAllWindows()
