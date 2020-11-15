import cv2 as cv

# img = cv.imread('Resources/Photos/cat1.jpg')
# cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos, and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# resized_image = rescaleFrame(img)
# cv.imshow('Image', resized_image)

def changeRes(width, height):
    # Live video
    capture.set(3,width)
    capture.set(4,height)

# Reading a video
capture = cv.VideoCapture('Resources/Videos/cat.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Resized Video', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'): # Exit when the 'd' key is pressed
        break

capture.release()
cv.destroyAllWindows()
