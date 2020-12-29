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


def find_red_spot(img):
    # cv.imshow("r", img)
    # cv.waitKey(0)

    blue, green, red = cv.split(img)
    red[green > 50] = 0
    red[blue > 50] = 0

    ret, red = cv.threshold(red, 100, 255, cv.THRESH_BINARY)
    all_contours, h = cv.findContours(red, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    max = []
    for c in all_contours:
        if len(c) > len(max):
            max = c
    x, y, w, h = cv.boundingRect(c)
    M = cv.moments(c)
    cy = int(M['m01'] / M['m00'])
    cx = int(M['m10'] / M['m00'])
    print((x + w / 2, y + h / 2))
    return (cx, cy)
    # cv.imshow("r", red)
    # cv.waitKey(0)

img = cv.imread('redtop2.jpeg')
find_red_spot(img)