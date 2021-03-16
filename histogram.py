import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Viskom/kucing.jpg', 1)

cv2.imshow("Histogram Kucing", img)

r,g,b = cv2.split(img)

cv2.imshow("r",r)
cv2.imshow("g",g)
cv2.imshow("b",b)

plt.hist(r.ravel(), 256, [0,256])
plt.hist(g.ravel(), 256, [0,256])
plt.hist(b.ravel(), 256, [0,256])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()