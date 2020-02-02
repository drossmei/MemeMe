import cv2
from functions import *
from pickMeme import chooseMeme

# Initialize Camera
cam = cv2.VideoCapture(0)

# load images
glasses_img = cv2.imread('images/glasses2.png', -1)
crying_img = cv2.imread('images/cryingeyes.png', -1)
redeye_img = cv2.imread('images/redeye.png', -1)
imgGlassesGray = cv2.cvtColor(glasses_img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')

# find emotion and caption
emotion = chooseMeme()[0]
caption = chooseMeme()[1]

while True:
    ret, frame = cam.read()
    store_frame = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame)

    # width and height of image
    width  = cam.get(3)
    height = cam.get(4)

    # Apply Emotion Text
    textOverlay(frame, (f"Make a {emotion} face", "Press space to submit"), width, height)
    
    cv2.imshow("MemeMe", frame)
    
    if not ret:
        break
    k = cv2.waitKey(1)
    
    if k%256 == 32:
            # SPACE pressed
            glasses(store_frame, faces, glasses_img)
            textOverlay(store_frame, (caption,""), width, height)
            cv2.imwrite("MemeMe'd.png", store_frame)
            print("Saving Image...")
            break


cam.release()
cv2.destroyAllWindows()