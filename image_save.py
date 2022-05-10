import cv2
import numpy as np

def image(road, N, M):
    img = np.zeros((6*M+1, 6*N+1, 3), np.uint8)

    for y, ro in enumerate(road):
        for x, pos in enumerate(ro):
            if pos == 0 :
                #img = white_rectangle(x, y, img)
                img = cv2.rectangle(img, (6*int(x), 6*int(y)), (6*int(x)+6, 6*int(y)+6), (255,255,255), cv2.FILLED)
            elif pos == 1:
                #img = red_circle(x, y, img)
                img = cv2.circle(img, (3 + 6*int(x), 3 + 6*int(y)), 3, (0,0,255), cv2.FILLED)
            elif pos == 2:
                img = cv2.circle(img, (3 + 6*int(x), 3 + 6*int(y)), 3, (255,0,0), cv2.FILLED)
                #img = blue_circle(x, y, img)
            elif pos == 3:
                pass
            
    return img

'''
def red_circle(x, y, img):
    
    img = cv2.circle(img, (1.5 + 3*x, 1.5 + 3*y), 1.5, (0,0,255), -1)

    # cv2.circle(img, center, radian, color, thickness)

def blue_circle(x, y, img):
    
    img = cv2.circle(img, (1.5 + 3*x, 1.5 + 3*y), 1.5, (255,0,0), -1)

def white_rectangle(x, y, img):
    
    img = cv2.rectangle(img, (3*x, 3*y), (3*x+3, 3*y+3), (255,255,255), -1)

    # cv2.rectangle(img, start, end, color, thickness)
'''