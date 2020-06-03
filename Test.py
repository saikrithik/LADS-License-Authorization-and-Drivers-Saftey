import numpy as np
import cv2
import face_recognition
import os
import pickle
import sys
import playsound
from threading import Thread
from imutils.video import VideoStream
import argparse


scale_factor=0.5

#ap = argparse.ArgumentParser()
#ap.add_argument("-w", "--webcam", type=int, default=0,
#	help="index of webcam on system")
#args = vars(ap.parse_args())

#video_capture = VideoStream(src=args["webcam"]).start()
video_capture = cv2.VideoCapture(0)#0
video_capture.set(cv2.CAP_PROP_FPS, 24)
scale_factor=0.5

def find_match(known_faces, names, face):
    matches = face_recognition.compare_faces(known_faces, face)
    
    face_distances = face_recognition.face_distance(known_faces, face)
    best_match_index = np.argmin(face_distances)
    #print(best_match_index)
    if matches[best_match_index]:
        if(face_distances[best_match_index]<scale_factor):
            name = names[best_match_index]
            return(name)
    return 'Not Found'


with open ('test_encodes.dat', 'rb') as fp:
    known_face_encodings = pickle.load(fp)

image_filenames = filter(lambda x: x.endswith('.jpg') or x.endswith('.png'), os.listdir('DriverFaces/'))
image_filenames = sorted(image_filenames)
known_face_names = [x[:-6] for x in image_filenames]

face_locations = []
face_encodings = []
face_names = []
decision=[]
#process_this_frame = True
i=0

process_this_frame = True       
while len(decision)<5:
    #frame = vs.read()
    ret,frame = video_capture.read()
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)#, fx=0.25, fy=0.25
    rgb_small_frame = small_frame[:, :, ::-1]
    i=i+1
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        
        face_names = []
        for face_encoding in face_encodings:
            name = find_match(known_face_encodings, known_face_names, face_encodings[0])
            face_names.append(name)

    process_this_frame = not process_this_frame
    for (x, y, w, h), name in zip(face_locations, face_names):#Rescaling
        x *= 4
        y *= 4
        w *= 4
        h *= 4

        cv2.rectangle(frame, (h, x), (y, w), (235, 206, 135), 2)
        cv2.rectangle(frame, (h, w - 35), (y, w), (235, 206, 135), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (h + 6, w - 6), font, 1.0, (0, 0, 0), 1)
        decision.append(name)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()

i=0
authorize = True
for elem in decision:
    if decision.count(elem) >=3 and decision[i]== 'Not Found':
        video_capture.release()
        cv2.destroyAllWindows()
        authorize= False
        print("The person have no regestered license")
        print("if Already have a existing license: Please regiser with the car , HERE:")
        reg=input("Enter \n'Y' For registrion ,\n'N' to continue un-authorized driving,\n'R' for recognize again,"
                  +"\n"+"'Q' For sending QR-Code to the registered email for verification.")
        if reg=='y' or reg=='Y':
            os.system('python StoringImages.py')
            os.system('python TrainingImages.py')
            print("Welcome")
            os.system('python Test.py')
        if reg=='r' or reg=='R':
            os.system('python Test.py')
        if reg=='n' or reg=='N':
            os.system('python adminlicense.py')
            playsound.playsound('alarm3.mp3',True)
        if reg=='q' or reg=='Q':
            os.system('python QR_request.py')
        sys.exit()
if authorize !=False:
    print("You Are Authorized To Drive")

# python Test.py --shape-predictor shape_predictor_68_face_landmarks.dat --alarm alarm2.mp3

