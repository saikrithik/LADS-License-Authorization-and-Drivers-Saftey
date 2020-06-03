import numpy as np
import pyzbar.pyzbar as pyzbar
import qrcode
import base64
import os
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import cv2
import io
from io import BytesIO
from pandas import ExcelWriter
import pandas as pd
import time
import sys



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
df = pd.read_excel(toread)
license_nos = df['License_no']
for i in range(len(df['License_no'])):
        if license_nos[i] == license_no :
            email_send=df["Email-I.D"][i]
            print(df["Email-I.D"][i])

email_user='iamnullnull007@gmail.com'
qr = qrcode.make(license_no)
qr.save('myQR.png')
def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'QR CODE FOR AUORTHIZE DRIVER'
    msg['From'] = 'iamnullnull007@gmail.com'
    msg['To'] = 'pvsaikrithik@gmail.com'
    text = MIMEText("QR CODE ")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s=smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(email_user, 'jeebu123')
    s.sendmail(email_user,email_send, msg.as_string())
    s.quit()
SendMail('myQR.png')

print("Please check the gmail registered with the license and scan the QR")
time.sleep(2)
cap = cv2.VideoCapture(0)
font=cv2.FONT_HERSHEY_PLAIN
decodeObjects=[]
while len(decodeObjects)<1:
    ret , frame = cap.read()
    decodeObjects=pyzbar.decode(frame)
    for obj in decodeObjects:
        cv2.putText(frame, str(obj.data),(50,50), font,2,
                    (255,0,0),3)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
data=str(obj.data)
data=data[2:18]
print(data)
for i in range(len(df['License_no'])):
    print(license_nos[i])
    if data == license_nos[i] :
        print("You are Authorized")
        os.system('python Sleepyness_detection.py')
        sys.exit()
print("Register your Details in the database")
os.system('python Final.py')
            
