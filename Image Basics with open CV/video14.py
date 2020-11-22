#Thing learned in video 14 of the course is present here 

import cv2
import numpy as np
import matplotlib.pyplot as plt

print('dssd')

blank_img = np.zeros(shape = (512,512,3), dtype =np.int16)
blank_img

"""
Draw a rectangle on above created black image
"""
cv2.rectangle(blank_img, pt1=(50,50),pt2=(100,100),color = (0,0,255),thickness = 5)

"""
Draw a circle on above created black image
"""
cv2.circle(blank_img, center = (400,400), radius = 30 , color=(255,0,0), thickness = 5)

"""
Draw a circle or rectangle on above created black image and fill it , then give thickness a negative value
"""
cv2.circle(blank_img, center = (400,400), radius = 30 , color=(255,0,0), thickness = -5)

plt.imshow(blank_img) #renders a black image of dimension 512X512X3 with all the shapes made so far