import numpy as np
import cv2

#input1 = cv2.imread(r'C:\Users\A3MAX SOFTWARE TECH\Desktop\WORK\1. KODI WORK\1. NARESH\10. WORKSHOP\7. Exploring Generative AI through computer vision\myimage.jpg')
input = cv2.imread(r"C:\Users\LIKHITH\OneDrive\Pictures\Ele.jpg")

cv2.imshow('input', input)
cv2.waitKey()
cv2.destroyWindows()

# Shape gives the dimensions of the image array
# The 2D dimensions are 830 pixels in high bv 1245 pixels wide.
# The '3L' means that there are 3 other components (RGB) that make up this image.

#print('Height of Image:', int(input1.shape[0]), 'pixels')
#print('Width of Image: ', int(input1.shape[1]), 'pixels')

# How do we save images we edit in OpenCV?
cv2.imwrite('output.jpg', input)
cv2.imwrite('output.png', input)
