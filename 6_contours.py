import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/bananas.jpg')
# img = cv.imread('Resources/Photos/fruits.jpg')
cv.imshow('Bananas', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

 canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)
#
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f'{len(contours)} contour(s) found!')

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # binarizing the value (0 or 1)
cv.imshow('Thres', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), thickness=1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
