import cv2 as cv
from cvzone.FaceDetectionModule import FaceDetector

cap = cv.VideoCapture(1)

Face_detector = FaceDetector(minDetectionCon=0.75)
while True:
    rec, image = cap.read()

    image, bboxs = Face_detector.findFaces(image)

    if bboxs:
        for i, bbox in enumerate(bboxs):
            x, y, w, h = bbox["bbox"]
            if x < 0: x = 0
            if y < 0: y = 0
            imageCrop = image[y:y + h, x:x + w]
            imageBlur = cv.blur(imageCrop, (500, 500))
            image[y:y + h, x:x + w] = imageBlur

    cv.imshow("Blured face", image)
    cv.waitKey(1)