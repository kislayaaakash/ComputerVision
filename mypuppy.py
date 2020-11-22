# This piece of code is to read an image using opencv and render it and close it using ESC button
import cv2
img = cv2.imread('C:/Users/kisaakas/Downloads/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/00-puppy.jpg')

while True:
    cv2.imshow('puppy',img)
    if cv2.waitKey(1) & 0xFF == 27: # use 0xFF == 27 for execution of esc key to close the picture
            break
            
cv2.destroyAllWindows()            
