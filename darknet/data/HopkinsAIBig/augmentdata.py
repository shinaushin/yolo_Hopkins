import numpy as np
import os
import cv2
import shutil
import matplotlib.image as mpimg

directory = "."
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        img = mpimg.imread("/home/shinaushin/darknet/data/HopkinsAIBig/"+filename)[:,:,:3]
        img = np.array(img, dtype=np.float32)

        row, col, _ = img.shape
        mean = 0
        var = 0.1
        sigma = var ** 0.5

        gaussian = np.random.random((row, col, 1)).astype(np.float32)
        gaussian = np.concatenate((gaussian, gaussian, gaussian), axis = 2)
        gaussian_img = cv2.addWeighted(img, 0.75, 0.25 * gaussian, 0.25, 0)
        # save gaussian img
        name, ext = filename.split(".")
        cv2.imwrite("/home/shinaushin/darknet/data/HopkinsAIBig/"+name+"_1.jpg", gaussian_img);

    if filename.endswith(".txt"):
        name, ext = filename.split(".")
        shutil.copy("/home/shinaushin/darknet/data/HopkinsAIBig/"+filename, "/home/shinaushin/darknet/data/HopkinsAIBig/"+name+"_1.txt")
