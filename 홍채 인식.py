
import cv2 
import cv
import numpy as np
import os
directory = os.listdir("iris1.jpg")
numero_file = len(directory)
for file in directory:
    print(file)
file_iride = raw_input("File(riportare anche estensione): ")
path = "iris1.jpg" %(file_iride)
image_iride = cv2.imread(path)
output = image_iride.copy()
image_test = cv2.imread(path, cv2.CV_LOAD_IMAGE_GRAYSCALE)
image_test = cv2.Canny(image_test,5,70,apertureSize=3)
image_test = cv2.GaussianBlur(image_test, (7,7), 1)
cerchi = cv2.HoughCircles(image_test, cv2.cv.CV_HOUGH_GRADIENT,50, 100, 50,300)
if cerchi is not None:
    cerchi = np.round(cerchi[0,:]).astype("int")
for (x,y,raggio) in cerchi:
    cv2.circle(output, (x,y),raggio,(255,0,0),4)
cv2.imshow("Image test", np.hstack([image_iride,output]))
cv2.waitKey() 
