import numpy as np
import cv2
import math


def display_image(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


imgname = "imgs\\blackboard.jpeg"
img = cv2.imread(imgname)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
display_image("name", gray)
## Split the H channel in HSV, and get the red range
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
h[h < 20] = 0
h[h > 50] = 255

## normalize, do the open-morp-op
normed = cv2.normalize(h, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
kernel = cv2.getStructuringElement(shape=cv2.MORPH_ELLIPSE, ksize=(3, 3))
opened = cv2.morphologyEx(normed, cv2.MORPH_OPEN, kernel)
display_image("", opened)
res = np.hstack((h, normed, opened))
cv2.imwrite("tmp1.png", res)
