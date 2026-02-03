import cv2, sys, numpy, os

haar_file = 'haarcascade_frontalface_default.xml'

datasets = 'datasets'

sub_data = 'pippa'

path = os.path.join(datasets, sub_data)
if not os.path.isdir(path): 
    os.makedirs(path)

(width,height) = (130,100)

face_cascade  = cv2.CascadeClassifier(haar_file)

webcam = cv2.VideoCapture(0)
