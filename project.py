import numpy as np
import cv2

img = cv2.imread("assets2/solar-system.jpg")

cv2.putText(img,
            "sun",
            (20,220),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            1.5,
            (255,255,255))

cv2.putText(img,
            "Mercury",
            (120,180),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Venus",
            (200,260),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))            

cv2.putText(img,
            "Earth",
            (290,170),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))            

cv2.putText(img,
            "Mars",
            (390,260),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))            

cv2.putText(img,
            "Jupiter",
            (520,220),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            1.5,
            (255,255,255))            

cv2.putText(img,
            "Saturn",
            (760,300),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))            

cv2.putText(img,
            "Uranus",
            (970,130),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))            

cv2.putText(img,
            "Neptune",
            (1120,290),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))            
cv2.imshow('output', img)
cv2.waitKey(0)