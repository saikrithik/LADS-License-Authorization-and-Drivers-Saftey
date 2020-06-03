import dlib
import numpy as np
import os
import scipy.misc
import pickle


face_detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
face_recognition_model=dlib.face_recognition_model_v1('Face_Recognition_trainedData.dat')
TOLERANCE = 0.5

def get_face_encodings(path_to_image):
    image = scipy.misc.imread(path_to_image)
    detected_faces = face_detector(image, 1)
    shapes_faces = [shape_predictor(image, face) for face in detected_faces]
    return [np.array(face_recognition_model.compute_face_descriptor(image, face_pose, 1)) for face_pose in shapes_faces]



image_filenames = filter(lambda x: x.endswith('.jpeg') or x.endswith('.jpg') or x.endswith('.png'), os.listdir('DriverFaces/'))
image_filenames = sorted(image_filenames)
paths_to_images = ['DriverFaces/' + x for x in image_filenames]
face_encodings = []
print("Your DataSet is being processed")
for path_to_image in paths_to_images:
    print(path_to_image+" is being Trained" )
    if (path_to_image == paths_to_images[len(paths_to_images)-3]):
        print(" ")
        print("Almost Done")
    face_encodings_in_image = get_face_encodings(path_to_image)
    face_encodings.append(face_encodings_in_image[0])
    print('.  ',end='\r')
print(" ")
with open('test_encodes.dat', 'wb') as fp:
    pickle.dump(face_encodings, fp)


