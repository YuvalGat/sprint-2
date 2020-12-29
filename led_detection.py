import cv2
import math
from find_colors import *
import numpy as np


# 420, 520, 200, 200
# LEFT_X = 370
# LEFT_Y = 630
# WIDTH = 220
# HEIGHT = 270


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))


def find_leds_positions(image):
    # display_image("", image)
    ret, threshed = cv2.threshold(image, 250, 255, cv2.THRESH_BINARY_INV)
    # display_image("", threshed)
    kernel = np.ones((3, 3), np.float32) / 9
    erosion = cv2.erode(threshed, kernel, iterations=1)
    dilation = cv2.dilate(erosion, kernel, iterations=1)
    dilation = cv2.dilate(dilation, kernel, iterations=1)
    # display_image("", dilation)
    all_contours, h = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    all_contours = all_contours[1:]
    # all_contour_edges = []
    all_cm_arr = []
    for c in all_contours:
        M = cv2.moments(c)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        all_cm_arr.append((cx, cy))
    sort_contours(all_contours, all_cm_arr)
    contours = []
    edges = []
    cm_arr = []
    i = 0
    for c in all_contours:
        # if len(c) > 1:  # changeble value
        contours.append(c)
        cm_arr.append(all_cm_arr[i])
        i += 1
    with_color = cv2.cvtColor(dilation, cv2.COLOR_GRAY2BGR)
    chosen_cont = []
    chosen_cm_arr = []
    for i in range(len(contours)):
        isOk = True
        for j in range(len(contours)):
            if j != i and calculate_distance(cm_arr[i][0], cm_arr[i][1], cm_arr[j][0], cm_arr[j][1]) < 5:
                if cm_arr[j][1] < cm_arr[i][1]:
                    isOk = False
            j += 1

        if isOk:
            chosen_cont.append(contours[i])
            chosen_cm_arr.append(cm_arr[i])
        i += 1
    contours = chosen_cont
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(with_color, (x, y), (x + w, y + h), (250, 50, 50), 1)
    return chosen_cm_arr


def sort_contours(contours, cm_arr):
    i = 1
    while i < len(contours):
        j = i
        while j > 0 and cm_arr[j][0] < cm_arr[j - 1][0]:
            cm_arr[j], cm_arr[j - 1] = cm_arr[j - 1], cm_arr[j]
            contours[j], contours[j - 1] = contours[j - 1], contours[j]
            j -= 1
        i += 1
    return


def find_on_leds(image, LEFT_Y, HEIGHT, LEFT_X, WIDTH):
    # display_image("", image)
    b, g, r = cv2.split(image)
    # LEFT_X, LEFT_Y, WIDTH, HEIGHT = find_red_spot(image)
    cut_image = r[LEFT_Y: LEFT_Y + HEIGHT, LEFT_X: LEFT_X + WIDTH]
    # display_image("", cut_image)
    arr = find_leds_positions(cut_image)
    return arr


# unlit = cv2.imread('./imgs/unlit4.jpeg')
# lit = cv2.imread('./imgs/lit4.jpeg')
# image = cv2.imread('redtop2.jpeg')
#
# print(find_on_leds(image))
