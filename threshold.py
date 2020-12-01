import sys
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Converts a RGB image to grayscale, 0,333 is the average percentage
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.333, 0.333, 0.333])

# This function compares each pixel's intesity with given threshold value
# After each comparison, sets current intesity to black or white
# Finaly, saves the output image 
def threshold(input_threshold, B, output_filename):
    row, col = B.shape
    for i in range(0,row):
        for j in range(0,col):
            if B[i][j] > input_threshold:
                B[i][j] = 255
            else:
                B[i][j] = 0
    plt.imsave(output_filename, B, cmap='gray')

# File parameters given by the user
input_filename = sys.argv[1]
output_filename = sys.argv[2]

# Threshold parameter given by the user, casting to integer
k = int (sys.argv[3])

# Try-except block that opens input image or prints fail message
try:
    img = Image.open(input_filename)
except IOError:
  print ("Unable to open file. Please try another format.")

# Converting input image to np array
B = np.array(img)

# Checking for 3rd dimension, if so input image is RGB that needs conversion to grayscale
if B.ndim == 3:
    B = rgb2gray(B)

# Parsing input parameters and execute
threshold(k, B, output_filename)