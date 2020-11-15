import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cat1.jpg')

cv.imshow('Cat', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]]) # Create the Affine Transform matrix
    dimensions = (img.shape[1], img.shape[0]) # width, height
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, scale=1.0)
    print(rotMat)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

# rotated_rotated = rotate(rotated, -45)
# cv.imshow('Rotated Rotated', rotated_rotated)

rotated2 = rotate(img, -90)
cv.imshow('Rtotated 2', rotated2)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) # use appropiate interpolation (enlarging or smalling)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, flipCode=0) # vertically
flip = cv.flip(img, flipCode=1) # horizontally
flip = cv.flip(img, flipCode=-1) # both of vertical and horizontal flip
cv.imshow('Flipped', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)
