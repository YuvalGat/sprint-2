import cv2
from led_detection import find_on_leds
from compare_leds import compare_leds
from find_colors import find_red_spot
from coder import decoder


# unlit = cv2.imread('./imgs/unlit4.jpeg')
# lit = cv2.imread('./imgs/lit4.jpeg')
#
# unlit_leds_coords = find_on_leds(unlit)
# lit_leds_coords = find_on_leds(lit)
#
# print(unlit_leds_coords)
# print(lit_leds_coords)
#
# print(compare_leds(lit_leds_coords, unlit_leds_coords))

# cap = cv2.VideoCapture(0)
#
# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Display the resulting frame
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()

def display_image(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# empty = cv2.imread('./imgs/unlit_all9.jpg')
# display_image('', empty)
x, y, w, h = 232, 174, 30, 170
print(x, y, w, h)
on = cv2.imread('./imgs/all_on.png')
led_coords = sorted(find_on_leds(on, y, h, x, w), key=lambda x: x[1], reverse=True)
top_led_coord = led_coords[0]  # sorted(led_coords, key=lambda x: x[1])[0]
semi = cv2.imread('./imgs/some_on2.png')
semi_leds = find_on_leds(semi, y, h, x, w)
print(led_coords)
print(top_led_coord)
print(semi_leds)
char = compare_leds(led_coords, semi_leds)
print(char)
char = char[::-1][1:]
print(decoder([char]))