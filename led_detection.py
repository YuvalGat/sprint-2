import cv2

LOWER_LEFT_X = 525
LOWER_LEFT_Y = 290
WIDTH = 160
HEIGHT = 75


def display_image(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


unlit = cv2.imread('./imgs/unlit1.jpeg')
lit = cv2.imread('./imgs/lit1.jpeg')

display_image("", unlit)

cut_unlit = unlit[LOWER_LEFT_Y: LOWER_LEFT_Y + HEIGHT, LOWER_LEFT_X: LOWER_LEFT_X + WIDTH]
display_image("", cut_unlit)
cut_lit = lit[LOWER_LEFT_Y: LOWER_LEFT_Y + HEIGHT, LOWER_LEFT_X: LOWER_LEFT_X + WIDTH]
display_image("", cut_lit)
threshed_lit = cv2.threshold(cv2.cvtColor(cut_lit, cv2.COLOR_BGR2GRAY), 100, 255, 0)
display_image("", threshed_lit)
