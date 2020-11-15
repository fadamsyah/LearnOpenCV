import cv2 as cv

# Reading an image

# img = cv.imread('Resources/Photos/cat1.jpg')
# cv.imshow('Cat', img)

# cv.waitKey(0) # 0 --> wait until the keyboard is pressed

# Reading a video
capture = cv.VideoCapture('Resources/Videos/cat.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'): # Exit when the 'd' key is pressed
        break

capture.release()
cv.destroyAllWindows()
