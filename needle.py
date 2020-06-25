import cv2
import numpy as np

d_im = cv2.imread("3.jpg")
d_im = d_im.astype("float64")

normals = np.array(d_im, dtype="float32")
h,w,d = d_im.shape
for i in range(1,w-1):
  for j in range(1,h-1):
    t = np.array([i,j-1,d_im[j-1,i,0]],dtype="float64")
    f = np.array([i-1,j,d_im[j,i-1,0]],dtype="float64")
    c = np.array([i,j,d_im[j,i,0]] , dtype = "float64")
    d = np.cross(f-c,t-c)
    n = d / np.sqrt((np.sum(d**2)))
    normals[j,i,:] = n

cv2.imshow("0",normals)
cv2.waitKey()
cv2.imwrite("normal.jpg",normals*255)