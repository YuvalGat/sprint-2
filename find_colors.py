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
def display_image(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def find_red_spot(img):
    blue, green, red = cv2.split(img)
    red[green > 50] = 0
    red[blue > 50] = 0
    ret, red = cv2.threshold(red, 100, 255, cv2.THRESH_BINARY)
    all_contours, h = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    copy = cv2.cvtColor(red.copy(), cv2.COLOR_GRAY2BGR)
    max = []
    for c in all_contours:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(copy, (x, y), (x + w, y + h), (255,0,0), 1)
        if len(c) > len(max):
            max = c
    M = cv2.moments(max)
    cy = int(M['m01'] / M['m00'])
    cx = int(M['m10'] / M['m00'])
    return cx - 75, cy + 40, 150, 380


# img = cv2.imread('redtop2.jpeg')
# find_red_spot(img)