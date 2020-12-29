import cv2
import numpy as np

LED_SIDE_LENGTH = 20  # Needs to be even


def find_lit_leds(x, y, img):
    half_lsl = LED_SIDE_LENGTH / 2
    led = img[y - half_lsl: y + half_lsl, x - half_lsl: x + half_lsl]
    avg_color = np.average(np.average(led, axis=0), axis=0)
    does_have_led = np.norm(avg_color) > 0
    return does_have_led
