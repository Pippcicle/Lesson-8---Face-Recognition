import cv2, sys, numpy, os

haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'

datasets = 'datasets'

sub_data = 'pippa'

path = os.path.join(datasets, sub_data)
if not os.path.isdir(path): 
    os.makedirs(path)

(width,height) = (130,100)

face_cascade  = cv2.CascadeClassifier(haar_file)

webcam = cv2.VideoCapture(0)

count = 1
while count < 30 : 
    ret, im = webcam.read()

    if not ret: 
        continue 

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    for (x,y,w,h) in faces : 
        cv2.rectangle(im, (x,y), (x+w, y+h), (255,0,0), 2)

        face = im[y:y+h, x:x+w]

        face_resize = cv2.resize(face, (width, height))

        count1 = str(count)
        font = cv2.FONT_HERSHEY_PLAIN
        origin = (50,50)
        fontscaling = 1
        colour = (153,153,255)
        thickness = 3
        text = cv2.putText(path, "Picture : "+ count1 + "/30", origin, font, fontscaling, colour, thickness)
        cv2.imshow('text',im)

        cv2.imwrite('%s/%s.png' % (path, count), face_resize)


        count += 1
    
    cv2.imshow('OpenCV - Face Capture', im)
    
    key = cv2.waitKey(10)

    if key == 27 : 
        break

webcam.release()
cv2.destroyAllWindows()