import cv2
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
    img = cv2.imread('imgs/redtop.jpeg')

    # cv.imshow("r", img)
    # cv.waitKey(0)

    blue, green, red = cv2.split(img)
    red[green > 50] = 0
    red[blue > 50] = 0

    ret, red = cv2.threshold(red, 100, 255, cv2.THRESH_BINARY)
    all_contours, h = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    max = []
    for c in all_contours:
        if len(c) > len(max):
            max = c
    x, y, w, h = cv2.boundingRect(c)
    M = cv2.moments(c)
    cy = int(M['m01'] / M['m00'])
    cx = int(M['m10'] / M['m00'])
    # print((x + w / 2, y + h / 2))
    # print(cx, cy)
    # cv2.rectangle(red, (x, y), (x + w, y + h), (250, 50, 50), 1)
    return cx - 75, cy - 50, 150, 300
