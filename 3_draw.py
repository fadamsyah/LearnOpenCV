import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') # uint8 is a basic image data type
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
# blank[200:300, 200:400] = 0,0,255 # Blue Green Red
# cv.imshow('Green', blank)
#
# # 2. Draw a Rectangle
# # cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=0)
# # cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)
# # cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=-1)
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
# cv.imshow('Rectangle', blank)
#
# # 3. Draw A circle
# # cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
# cv.imshow('Circle', blank)
#
# # 4. Draw a line
# # cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
# cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
# cv.imshow('Line', blank)

# 5. Write text
# cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
# cv.putText(blank, 'Hello, my name is Adam', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.putText(blank, 'Hello, my name is Adam', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)
