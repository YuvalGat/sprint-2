import cv2
import time
import multiprocessing as mp
from sys import argv
import uuid

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
    print("Camera is alive?: " + str(cam.p.is_alive()) )

    while True:
        frame = cam.get_frame()
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
