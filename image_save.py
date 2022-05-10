import cv2
import numpy as np

def image(road, N, M):
    img = np.zeros((3*N, 3*M, 3), np.uint8)

    for y, ro in enumerate(road):
        for x, pos in enumerate(ro):
            if pos == 0 :
                img = white_rectangle(x, y, img)
            elif pos == 1:
                img = red_circle(x, y, img)
            elif pos == 2:
                img = blue_circle(x, y, img)
            elif pos == 3:
                pass
            
    return img


def red_circle(x, y, img):
    
    img = cv2.circle(img, (1.5 + 3*x, 1.5 + 3*y), 1.5, (0,0,255), -1)
    return img
    # cv2.circle(img, center, radian, color, thickness)

def blue_circle(x, y, img):
    
    img = cv2.circle(img, (1.5 + 3*x, 1.5 + 3*y), 1.5, (255,0,0), -1)
    return img

def white_rectangle(x, y, img):
    
    img = cv2.rectangle(img, (3*x, 3*y), (3*x+3, 3*y+3), (255,255,255), -1)
    return img
    # cv2.rectangle(img, start, end, color, thickness)