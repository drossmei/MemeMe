import cv2
from functions import *
from pickMeme import chooseMeme, data, random_caption_string

    
def main(emotion="random"):
    # Initialize Camera
    cam = cv2.VideoCapture(0)

    # load images
    glasses_img = cv2.imread('test/images/glasses2.png', -1)
    crying_img = cv2.imread('test/images/cryingeyes.png', -1)
    redeye_img = cv2.imread('test/images/redeye.png', -1)
    imgGlassesGray = cv2.cvtColor(glasses_img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('test/data/haarcascade_frontalface_alt2.xml')

    # find emotion and caption and image filter

    caption = ""
    if (emotion == "random"): # randomize caption and emotion
        temp = chooseMeme()
        emotion = temp[0]
        caption = temp[1]
    else:
        caption = random_caption_string(emotion)

    def applyFilter(store_frame, faces, emotion):
        if (emotion == "happy"):
            pass
        if (emotion == "sad"):
            crying(store_frame, faces, crying_img)
        elif (emotion == "surpised"):
            pass
        elif (emotion == "badass"):
            glasses(store_frame, faces, glasses_img)


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
            applyFilter(store_frame, faces, emotion)
            textOverlay(store_frame, (caption,""), width, height)
            cv2.imwrite("MemeMe'd.png", store_frame)
            print("Saving Image...")
            break


    cam.release()
    cv2.destroyAllWindows()
    openImage()
