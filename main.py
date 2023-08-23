import cv2 as cv
from cvzone.FaceDetectionModule import FaceDetector

cap = cv.VideoCapture(1)

Face_detector = FaceDetector(minDetectionCon=0.75)
while True:
    rec, image = cap.read()

    image, bbox = Face_detector.findFaces(image, )

    cv.imshow("Blured face", image)
    cv.waitKey(1)