import cv2
#from tracker import *

#https://pyimagesearch.com/2018/07/30/opencv-object-tracking/

cap = cv2.VideoCapture(r"C:\Users\LIKHITH\OneDrive\Desktop\Data science\NIT\FEB\img frame,object_tracking from video\highway.mp4")

while True:
    ret, frame = cap.read()
    
    cv2.imshow('Frame', frame)
    
    key = cv2.waitKey(30)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()

