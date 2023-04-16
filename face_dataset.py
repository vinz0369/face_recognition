
import cv2
import os
import numpy as np
from PIL import Image
#set kich thuoc cam
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480) 

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# nhap id tuong ung voi nguoi 
face_id = input('\n nhap id nguoi dung  ')

print("\n Dang mo tinh nang chup, nhin vao may quay")
#khoi tao so luong
count = 0

while(True):

    ret, img = cam.read()
    img = cv2.flip(img, 1) # flip= lat hinh anh theo chieu doc
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Luu hinh anh vao dataset
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # ESC de thoat
    if k == 27:
        break
    elif count >= 100: #lay 100 mau anh, cang nhieu do chinh xac khi nhan dien cang cao
         break

# duong dan data
path = 'dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

# function: lay hinh anh va du lieu
def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L') #chuyen sang mau xam
        img_numpy = np.array(PIL_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

# Luu mo hinh vao trainer/trainer.yml
recognizer.write('trainer/trainer.yml') # cong cu nhan dang

# in ra so cac khuon mat duoc nhan dien
print("\n  {0} faces trained".format(len(np.unique(ids))))


cam.release()
cv2.destroyAllWindows()
