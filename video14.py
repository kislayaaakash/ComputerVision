#Thing learned in video 14 of the course is present here 

import cv2
import numpy as np
import matplotlib.pyplot as plt

blank_img = np.zeros(shape = (512,512,3), dtype =np.int16)
plt.imshow(blank_img) #renders a black image of dimension 512X512X3