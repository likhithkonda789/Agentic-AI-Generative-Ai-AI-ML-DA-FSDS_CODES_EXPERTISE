import cv2
from tracker import *  # Assuming you need this for later tracking, even though it's not used here
from itertools import zip_longest

# Load the video
cap = cv2.VideoCapture(r"C:\Users\LIKHITH\OneDrive\Desktop\Data science\NIT\FEB\img frame,object_tracking from video\highway.mp4")

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Create background subtractor
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Reached end of video or failed to read frame.")
        break

    # Apply background subtraction
    mask = object_detector.apply(frame)

    # Display the original frame and mask
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)

    # Exit on pressing ESC key
    key = cv2.waitKey(30)
    if key == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
