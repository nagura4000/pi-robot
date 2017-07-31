# -*- coding: utf-8 -*-

import cv2
import time
import threading
import os


def saveimg(cam):
    while os.path.isfile("stop.txt") == False:
        print("save")
        ret, frame = cam.read()
        cv2.imwrite("output.png", frame)
        time.sleep(1)
    

def hello():
    print("Hello")

if __name__ == '__main__':

    print("start")

    cam = cv2.VideoCapture(0)
    t = threading.Timer(2, saveimg, args = [cam])
    t.start()
    
    #while(True):
    while os.path.isfile("stop.txt") == False:
        ret, frame = cam.read()
        cv2.imshow("Show FLAME Image", frame)
        
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    t.cancel()

    cam.release()
    cv2.destroyAllWindows()

    print("end")
