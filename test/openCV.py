import cv2
from functions import *

cam = cv2.VideoCapture(0)
cv2.namedWindow("Say Cheese")
glasses_img = cv2.imread('images/glasses2.png', -1)
crying_img = cv2.imread('images/cryingeyes.png', -1)
redeye_img = cv2.imread('images/redeye.png', -1)
imgGlassesGray = cv2.cvtColor(glasses_img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame)

    # width and height of image
    width  = cam.get(3)
    height = cam.get(4)

    # Apply Filter
    # crying(frame, faces, crying_img)
    # frame = invert(frame)
    glasses(frame, faces, glasses_img)

    # Apply Text
    textOverlay(frame, ("When you take a pattis final", ""), width, height)
    
    cv2.imshow("test", frame)
    
    if not ret:
        break
    k = cv2.waitKey(1)
    
    if k%256 == 32:
            # SPACE pressed
            cv2.imwrite("img.png", frame)
            print("Saving Image...")
            break


cam.release()
cv2.destroyAllWindows()