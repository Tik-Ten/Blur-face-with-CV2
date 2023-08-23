import cv2 as cv

cap = cv.VideoCapture(1)

while True:
    rec, image = cap.read()

    cv.imshow(image)
    cv.waitKey(1)