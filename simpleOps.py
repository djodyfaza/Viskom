import cv2
import numpy as np


img = cv2.imread('Viskom/kucing.jpg', 1)
img = cv2.resize(img, (400,400))

cv2.imshow("Resize Kucing", img)
cv2.waitKey(0)
cv2.destroyAllWindows()