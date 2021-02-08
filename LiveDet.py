import cv2
import matplotlib.pyplot as plt

from CNN_Module import *
from FaceDetection_Module import *

MODEL_NAME_INFERENCE = 'laplacian_256_model_200.pth'
DEST_PATH = 'C:/Users/User/Desktop/Video_test/'
PATH_TO_MODEL_INFERENCE = DEST_PATH+MODEL_NAME_INFERENCE

device = torch.device('cpu')
loaded_model = CNN()
loaded_model.load_state_dict(torch.load(PATH_TO_MODEL_INFERENCE, map_location=device))
loaded_model.to(device)
loaded_model.eval()



face_cascade = cv2.CascadeClassifier("C:/Users/User/Desktop/Video_test/haarcascade_frontalface_default.xml")


cap = cv2.VideoCapture("C:/Users/User/Desktop/Video_test/Mattia_test_01.mp4")

count = 1

while cap.isOpened() & count<30000:
  
    ret, frame = cap.read()
    #print(ret)
    if ret==True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detects faces of different sizes in the input image 
        faces = FaceDetection(gray).detection()#face_cascade.detectMultiScale(frame, 1.1, 6)

        # for each detected faces, find the landmark
        for (i, rect) in enumerate(faces):
            shape = 
        
        
        
        cv2.imshow('frame',gray)

        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break
    