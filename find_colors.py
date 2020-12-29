import cv2 as cv
from PIL import Image

#
# def find_color_cont(img, x, y):
#     print(img[x, y])
#     if img[x, y][0] / (img[x, y][1] + img[x, y][2] + 1) > 3:
#         print("blue")
#     elif img[x, y][1] / (img[x, y][0] + img[x, y][2] + 1) > 3:
#         print("green")
#     elif img[x, y][2] / (img[x, y][0] + img[x, y][1] + 1) > 3:
#         print("red")




img = cv.imread('imgs/lit4.jpeg')
# img = Image.open('imgs/lit1.jpeg')

cv.imshow("r", img)
cv.waitKey(0)
# img = cv.imread('lit1.png')
# data = img.getdata()

# Suppress specific bands (e.g. (255, 120, 65) -> (0, 120, 0) for g)
# r = [(d[0], 0, 0) for d in data]
# g = [(0, d[1], 0) for d in data]
# b = [(0, 0, d[2]) for d in data]
# find_color_cont(img, 48, 73)
# img = img[45:50, 70:75]



blue, green, red = cv.split(img)
# for i in range(len(red)):
#     for j in range(len(red[0])):
#         if green[i][j] > 50:
#             red[i][j] = 0
#         if blue[i][j] > 50:
#             red[i][j] = 0

red[green > 100] = 0
red[blue > 100] = 0

cv.imshow("r", red)
cv.waitKey(0)
