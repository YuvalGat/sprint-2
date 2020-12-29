import cv2
import math

LOWER_LEFT_X = 525
LOWER_LEFT_Y = 290
WIDTH = 160
HEIGHT = 75


def display_image(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1) * (x2-x1) + (y2-y1) * (y2-y1))



unlit = cv2.imread('./imgs/unlit1.jpeg')
lit = cv2.imread('./imgs/lit1.jpeg')


def find_leds_positions(image):
    ret, threshed = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY_INV)
    display_image("", threshed)


display_image("", unlit)

cut_unlit = unlit[LOWER_LEFT_Y: LOWER_LEFT_Y + HEIGHT, LOWER_LEFT_X: LOWER_LEFT_X + WIDTH]
display_image("", cut_unlit)
cut_lit = lit[LOWER_LEFT_Y: LOWER_LEFT_Y + HEIGHT, LOWER_LEFT_X: LOWER_LEFT_X + WIDTH]
display_image("", cut_lit)
gray_cut_lit = cv2.cvtColor(cut_lit, cv2.COLOR_BGR2GRAY)

find_leds_positions(gray_cut_lit)