import cv2 as cv

img = cv.imread('Resources/Photos/cat1.jpg')
cv.imshow('Cat', img)
# img = cv.imread('Resources/Photos/fruits.jpg')
# cv.imshow('Fruits', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
# blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
# canny = cv.Canny(img, 125, 175)
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the Image
# dilated = cv.dilate(canny, (3,3), iterations=1)
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
# eroded = cv.erode(dilated, (3,3), iterations=1)
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
# resized = cv.resize(img, (500,500))
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA) # Bagus untuk ngekicil dimensi
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) # Bagus untuk memperbesar dimensi
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
