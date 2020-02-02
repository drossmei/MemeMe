import cv2
import numpy as np
from typing import *
from PIL import Image

# helper method

def transparentOverlay(src, overlay, pos=(0, 0), scale=1):
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = src.shape  # Size of background Image
    y, x = pos[0], pos[1]  # Position of foreground/overlay image

    # loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][3] / 255.0)  # read the alpha channel
            src[x + i][y + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[x + i][y + j]
    return src


# source: https://www.youtube.com/watch?v=MVLuexuikv4
def invert(frame):
    return cv2.bitwise_not(frame)


# source: https://www.youtube.com/watch?v=zHNj1gAOoCY
def glasses(frame, faces,  glasses_img):
    for (x, y, w, h) in faces:
        if h > 0 and w > 0:
            glass_symin = int(y + 0.5 * h / 5)
            glass_symax = int(y + 3.6 * h / 5)
            sh_glass = glass_symax - glass_symin

            face_glass_roi_color = frame[glass_symin:glass_symax, x:x+w]

            glasses = cv2.resize(glasses_img, (w, sh_glass),interpolation=cv2.INTER_AREA)
            transparentOverlay(face_glass_roi_color,glasses)


def crying(frame, faces,  crying_img):
    for (x, y, w, h) in faces:
        if h > 0 and w > 0:
            glass_symin = int(y + 1 * h / 5)
            glass_symax = int(y + 3.6 * h / 5)
            sh_glass = glass_symax - glass_symin

            face_glass_roi_color = frame[glass_symin:glass_symax, x:x+w]

            crying = cv2.resize(crying_img, (w, sh_glass),interpolation=cv2.INTER_AREA)
            transparentOverlay(face_glass_roi_color,crying)


# source: https://www.youtube.com/watch?v=MVLuexuikv4
def red_eye(frame, redeye_img, faces, intensity=.5, red=230, green=0, blue=10):
    for (x, y, w, h) in faces:
        if h > 0 and w > 0:
            glass_symin = int(y - 1 * h / 5)
            glass_symax = int(y + 4.5 * h / 5)
            sh_glass = glass_symax - glass_symin

            face_glass_roi_color = frame[glass_symin:glass_symax, x:x+w]

            redeye = cv2.resize(redeye_img, (w, sh_glass),interpolation=cv2.INTER_AREA)
            transparentOverlay(face_glass_roi_color,redeye)
    def verify_alpha_channel(frame):
        try:
            frame.shape[3] # looking for the alpha channel
        except IndexError:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        return frame
    frame = verify_alpha_channel(frame)
    frame_h, frame_w, frame_c = frame.shape
    color_bgra = (blue, green, red, 1)
    overlay = np.full((frame_h, frame_w, 4), color_bgra, dtype='uint8')
    cv2.addWeighted(overlay, intensity, frame, 1.0, 0, frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    return frame


def blush(frame, faces,  blush_img, animeeyes_img):
    for (x, y, w, h) in faces:
        if h > 0 and w > 0:
            glass_symin = int(y + 2.2 * h / 5)
            glass_symax = int(y + 4.1 * h / 5)
            sh_glass = glass_symax - glass_symin
            face_glass_roi_color = frame[glass_symin:glass_symax, x:x+w]
            blushes = cv2.resize(blush_img, (w, sh_glass),interpolation=cv2.INTER_AREA)
            transparentOverlay(face_glass_roi_color,blushes)
    for (x, y, w, h) in faces:
        if h > 0 and w > 0:
            # smaller average = higher
            glass_symin = int(y + 1.2 * h / 5)
            glass_symax = int(y + 2.4 * h / 5)
            sh_glass = glass_symax - glass_symin
            face_glass_roi_color = frame[glass_symin:glass_symax, x:x+w]
            eyes = cv2.resize(animeeyes_img, (w, sh_glass),interpolation=cv2.INTER_AREA)
            transparentOverlay(face_glass_roi_color,eyes)



# opens MemeMe'd.png
def openImage() -> None:
    try:
        img = Image.open("MemeMe'd.png")
        img.show()
    except:
        raise "MemeMe'd.png does not exist."


def textOverlay(frame, text:tuple, width, height):
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame, text[0], (int(width//2)-(cv2.getTextSize(text[0], font, 1, 1)[0][0]//2), cv2.getTextSize(text[0], font, 1, 1)[0][1] + 20), font, 1, (200, 200, 200), 2, cv2.LINE_AA)
    cv2.putText(frame, text[1], (int(width//2)-(cv2.getTextSize(text[1], font, 1, 1)[0][0]//2), int(height)-20), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
