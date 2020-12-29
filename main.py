import cv2
from led_detection import find_on_leds
from compare_leds import compare_leds

unlit = cv2.imread('./imgs/unlit4.jpeg')
lit = cv2.imread('./imgs/lit4.jpeg')

unlit_leds_coords = find_on_leds(unlit)
lit_leds_coords = find_on_leds(lit)

print(unlit_leds_coords)
print(lit_leds_coords)

print(compare_leds(lit_leds_coords, unlit_leds_coords))