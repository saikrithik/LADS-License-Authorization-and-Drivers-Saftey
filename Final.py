
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import playsound
import argparse
import imutils
import time
import dlib
import cv2
import os

os.system('python Test.py')

faceCascade = cv2.CascadeClassifier('Haar/haarcascade_frontalface_default.xml')


def sound_alarm(path):
        playsound.playsound(path)

def eye_aspect_ratio(eye):

        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])
        C = dist.euclidean(eye[0], eye[3])
        ear = (A + B) / (2.0 * C)

        return ear
 

ap = argparse.ArgumentParser()
ap.add_argument("-w", "--webcam", type=int, default=0,
        help="index of webcam on system")
args = vars(ap.parse_args())
 

EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 48


COUNTER = 0
ALARM_ON = False


print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]


print("[INFO] starting video stream thread...")
vs = cv2.VideoCapture(0)
#time.sleep(1.0)
i=0
loop=[]
person=True


while True:

        ret,frame = vs.read()
        frame = imutils.resize(frame, width=450)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray)
        loop.append(faces)
        print(person)
        # detect faces in the grayscale frame
        rects = detector(gray, 0)
        i=i+1
        if i>40:
                for j in range(i-40,i):
                        if len(loop[j]) == 0:
                                person=False
                                
                                cv2.destroyAllWindows()
                                vs.release()
                                os.system('python Final.py')
                                
                        else:
                                person=True


        rects = detector(gray, 0)


        for rect in rects:

                shape = predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)


                leftEye = shape[lStart:lEnd]
                rightEye = shape[rStart:rEnd]
                leftEAR = eye_aspect_ratio(leftEye)
                rightEAR = eye_aspect_ratio(rightEye)


                ear = (leftEAR + rightEAR) / 2.0


                leftEyeHull = cv2.convexHull(leftEye)
                rightEyeHull = cv2.convexHull(rightEye)
                cv2.drawContours(frame, [leftEyeHull], -1, (255, 255, 255), 1)
                cv2.drawContours(frame, [rightEyeHull], -1, (255, 255, 255), 1)

                if ear < EYE_AR_THRESH:
                        COUNTER += 1


                        if COUNTER >= EYE_AR_CONSEC_FRAMES:
                                if not ALARM_ON:
                                        ALARM_ON = True
                                        os.system('python adminsleepy.py')


                                        if 'alarm2.mp3' != "":
                                                t = Thread(target=sound_alarm,
                                                        args=('alarm2.mp3',))
                                                t.deamon = True
                                                t.start()

                                cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


                else:
                        COUNTER = 0
                        ALARM_ON = False
                cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
 
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
 
        if key == ord("q"):
                break


cv2.destroyAllWindows()
vs.release()

