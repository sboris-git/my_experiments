import cv2 as cv
import numpy as np
from imageio import imread

# https://stackoverflow.com/questions/43111029/how-to-find-the-average-colour-of-an-image-in-python-with-opencv
# pip install opencv-python
image = imread('https://i.stack.imgur.com/DNM65.png')
img = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
rows, cols, _ = img.shape

color_B = 0
color_G = 0
color_R = 0
color_N = 0 # neutral/gray color

for i in range(rows):
    for j in range(cols):
        k = img[i,j]
        if k[0] > k[1] and k[0] > k[2]:
            color_B = color_B + 1
            continue
        if k[1] > k[0] and k[1] > k[2]:
            color_G = color_G + 1
            continue
        if k[2] > k[0] and k[2] > k[1]:
            color_R = color_R + 1
            continue
        color_N = color_N + 1

pix_total = rows * cols
print('Blue:', color_B/pix_total, 'Green:', color_G/pix_total, 'Red:',  color_R/pix_total, 'Gray:',  color_N/pix_total)