import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('test/haarcascades/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while(True):
    # cap frame by frame
    ret, frame = cap.read()

    # convert frame to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # detects face
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=1)
    
    # prints out regions of interest
    for (x, y, w, h) in faces:
        print(x, y, w, h)

        ## saves a face in gray
        # roi_gray = gray[y:y+h, x:x+w]
        # test_img = "test_img.jpg"
        # cv2.imwrite(test_img, roi_gray)

        color = (0, 0, 255) # (BGR) idk why it isn't (RGB)
        thickness = 2
        x1 = x + w
        y1 = y + h
        cv2.rectangle(frame, (x,y), (x1,y1), color, thickness)
    
    # display frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
