#Importing the module to easily use it anywhere + all the libraries
import cv2
import mediapipe as mp
import time

import HTModule as htm
# dummy code from the module
def main():
    pTime=0

    cTime=0

    cap = cv2.VideoCapture(0)
    detector = htm.HandDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img,draw=False)
        # Include code if u want the landmark positions of a certain node (21), [8] is index finger tip
        #if len(lmList) != 0:
        #    print(lmList[8])
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime



        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),2)
        cv2.imshow('Video', img)
        cv2.waitKey(1)
