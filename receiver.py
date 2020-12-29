import cv2
import time
import multiprocessing as mp
from sys import argv
import uuid
import numpy as np
from led_detection import find_on_leds
from compare_leds import compare_leds
from coder import *


class Camera:
    def __init__(self, rtsp_url):
        # load pipe for data transmission to the process
        self.parent_conn, child_conn = mp.Pipe()
        # load process
        self.p = mp.Process(target=self.update, args=(child_conn, rtsp_url))
        # start process
        self.p.daemon = True
        self.p.start()

    def end(self):
        # send closure request to process
        self.parent_conn.send(2)

    def update(self, conn, rtsp_url):
        # load cam into separate process
        print("Cam Loading...")
        cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)
        print("Cam Loaded...")
        run = True
        while run:
            cap.grab()  # grab frames from the buffer
            rec_dat = conn.recv()  # receive input data
            if rec_dat == 1:
                ret, frame = cap.read()  # if frame requested
                conn.send(frame)
            elif rec_dat == 2:
                cap.release()  # if close requested
                run = False
        print("Camera Connection Closed")
        conn.close()

    def get_frame(self, resize=None):
        # used to grab frames from the cam connection process
        # [resize] param : % of size reduction or increase i.e 0.65 for 35% reduction  or 1.5 for a 50% increase
        self.parent_conn.send(1)  # send request
        frame = self.parent_conn.recv()
        self.parent_conn.send(0)  # reset request
        if resize is None:  # resize if needed
            return frame
        else:
            return self.rescale_frame(frame, resize)

    def rescale_frame(self, frame, percent=65):
        return cv2.resize(frame, None, fx=percent, fy=percent)


def main():
    cam = Camera("http://" + argv[1] + ":5000/video_feed")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    file_name = uuid.uuid4()
    out = cv2.VideoWriter(f'{file_name}.mp4', fourcc, 20.0, (640, 480))
    led_coords = find_on_leds(cv2.imread("constant_leds.jpeg"))
    top_led_coord = led_coords[0]  # sorted(led_coords, key=lambda x: x[1])[0]
    print("Camera is alive?: " + str(cam.p.is_alive()))
    charbit_arr = []
    top_led_on = True
    while True:
        frame = cam.get_frame()
        top_led = frame[top_led_coord[0] - 10: top_led_coord[0] + 10, top_led_coord[1] - 10: top_led_coord[1] + 10]
        b, g, r = cv2.split(top_led)
        # cv2.imshow("", b)
        # cv2.imshow("", g)
        # cv2.imshow("", r)
        top_led_before = top_led_on
        top_led_on = (np.average(r) > 200 and np.average(g) + np.average(b) < 80)
        if top_led_before != top_led_on:
            leds_current = find_on_leds(frame)
            character = compare_leds(led_coords, leds_current)
            if character == "0000000":
                print(decoder(charbit_arr))
                break
            charbit_arr.append(character)
        out.write(frame)
        cv2.imshow("Feed", frame)
        key = cv2.waitKey(1)
        if key == 13:  # 13 is the Enter Key
            break

    cv2.destroyAllWindows()
    cam.end()
    out.release()


if __name__ == '__main__':
    main()
