import cv2
import numpy as np


img = cv2.imread('Viskom/kucing.jpg', 1)

cv2.imshow('Kucing',img)
height = img.shape[0]
width = img.shape[1]
print("Resolusi gambar:", height, "x", width)
cv2.waitKey(0)
cv2.destroyAllWindows()