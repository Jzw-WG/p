import cv2
import numpy as np
from matplotlib import pyplot as plt
import grip as gp

img = cv2.imread('0.jpg',0)
# f = np.fft.fft2(img)
# ff = np.fft.fftshift(f)
# res = (20*np.log(np.abs(ff))).astype(np.uint8)
a = gp.GripPipeline()
a.process(img)
a.cv_threshold_output
cv2.imshow('1',a.cv_laplacian_output)
cv2.waitKey()
# plt.subplot(121), plt.imshow(img, 'gray'), plt.title('Original Image')
# plt.axis('off')
# plt.subplot(122), plt.imshow(res, 'gray'), plt.title('Fourier Image')
# plt.axis('off')
# plt.show()
