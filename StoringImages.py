class Error(Exception):
   "Base class for other exceptions"
   pass
class lengthError(Error):
   "length is not 16."
   pass
class lengthError(Error):
   "length is not 16."
   pass

import cv2,os              
import numpy as np
import pandas as pd
from pandas import ExcelWriter
import base64
import io
from io import BytesIO


WHITE = [255, 255, 255]


face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')

while True:
     try:
         license_no = str(input('Enter Registered Driving Licence No.'))
         if len(license_no)<16:
             raise lengthError
         break
     except lengthError :
         print("Please Enter Valid License no.")
     except ValueError:
         print("Oops!  That was no valid number.  Try again...")
text_file = open("Licensefinal.b64", "rb")
base64_encoded = text_file.read()
text_file.close()
decrypted=base64.b64decode(base64_encoded)
toread = io.BytesIO()
toread.write(decrypted)  # pass your `decrypted` string as the argument here
toread.seek(0)  # reset the pointer
df = pd.read_excel(toread,usecols=['License_no','Name','Registered','Email-I.D'])

license_nos = df['License_no']
for i in range(len(df['License_no'])):
        if license_nos[i] == license_no :
            try:
               
               df["Registration"][i] = 'Registered'
            except Exception:
               print("copied")
            name=df["Name"][i]
bio = BytesIO()
writer = pd.ExcelWriter(bio, engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
bio.seek(0)
workbook = bio.read()
base64_encoded = base64.b64encode(workbook).decode('UTF-8')
text_file = open("Licensefinal.b64", "w")
n = text_file.write(base64_encoded)
text_file.close()

Count = 0
cap = cv2.VideoCapture(0) 
path="DriverFaces/"
#os.mkdir(path)

while Count < 4:
    ret, img = cap.read()
                                                                     
    #cv2.imwrite("images/"+name+"."+roll_no+'.'+str(Count)+".jpg", img)
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.waitKey(500)
        cv2.imwrite("DriverFaces/"+name+'.'+str(Count)+".jpg", img)
        cv2.imshow("CAPTURED PHOTO", img)                                                     
        Count = Count + 1
        cv2.imshow('Face Recognition System Capture Faces', img)
               
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print ('FACE CAPTURE FOR THE SUBJECT IS COMPLETE')

cap.release()
cv2.destroyAllWindows()
